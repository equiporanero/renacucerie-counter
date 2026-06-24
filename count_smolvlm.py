#!/usr/bin/env python3.12
import torch, os, json, datetime, re
from PIL import Image
from transformers import AutoProcessor, AutoModelForImageTextToText

print("Loading SmolVLM model...")
model_id = "HuggingFaceTB/SmolVLM-Instruct"
processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForImageTextToText.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto"
)
print("Model loaded! Device:", model.device)

image_dir = "/root/renacuja-counter/public/images"
results = {}

for i in range(1, 10):
    img_path = os.path.join(image_dir, f"bandeja_{i}.jpg")
    if not os.path.exists(img_path):
        print(f"MISSING: {img_path}")
        results[str(i)] = "MISSING"
        continue

    print(f"Processing bandeja_{i}.jpg...")
    image = Image.open(img_path).convert("RGB")

    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image"},
                {"type": "text", "text": "Count the tadpoles in this image. Reply ONLY with a single number, nothing else."}
            ]
        }
    ]

    prompt = processor.apply_chat_template(messages, add_generation_prompt=True)
    inputs = processor(images=[image], text=prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=50, do_sample=False)

    # Decode only the new tokens
    generated = output[0][inputs["input_ids"].shape[1]:]
    response = processor.decode(generated, skip_special_tokens=True).strip()
    
    # Extract number
    nums = re.findall(r'\d+', response)
    num = int(nums[0]) if nums else 0
    print(f"  Result: {num} (raw: '{response}')")
    results[str(i)] = num

print("\n--- RESULTS ---")
print(json.dumps(results, indent=2))

total = sum(v for v in results.values() if isinstance(v, int))
print(f"Total: {total}")

output_data = {
    "bandejas": results,
    "total": total,
    "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
}

os.makedirs("/root/renacuja-counter/public/data", exist_ok=True)
with open("/root/renacuja-counter/public/data/counts.json", "w") as f:
    json.dump(output_data, f, indent=2)

print(f"\nSaved to counts.json")
print(json.dumps(output_data, indent=2))
