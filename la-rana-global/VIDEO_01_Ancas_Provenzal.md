# VÍDEO 01 — Ancas de rana a la provenzal · Chef Fabien
## Instrucciones completas de producción · FREE (TEST, no publicable)

> Receta: `FR-001` · Mercado: España (audio ES) · Avatar: Fabien (sin tatuaje)
> Salida: 1 largo (≈3 min) + 1 corto (≈1 min) + micro-reels. Subtítulos quemados.
> Referencia de cara: `ref_fabien_v1.png` (versión sin tatuaje) en TODO prompt de cara.

---

## A. FICHA DE RECETA (plantilla rellena)

| Campo | Valor |
|---|---|
| receta_id | FR-001 |
| Nombre | Ancas de rana a la provenzal |
| País / Cocina | Francia / Provenzal tradicional |
| Avatar | Fabien |
| Dificultad | 1 (fácil) |
| Tiempo | 20 min |
| Comensales | 2 |
| Temporada | Todo el año (óptima oct-feb) |
| Momento ideal | Tapeo / cena con amigos / aperitivo |
| kcal/ración | ~150 kcal |
| Proteína | ~16 g · Grasa ~9 g · Sodio bajo |
| Perfil | Alto en proteína, bajo en grasa, bajo en sodio |
| Score nutricional | **A** |
| Apto para | Deportistas, dieta proteica, hipertensos |
| Alérgenos | Lácteos (mantequilla). Sin gluten si no se enharina; ver truco. |
| Origen ancas | Pelophylax perezi · GRENOUCERIE |
| CTA | ancasderana.com?utm_source=youtube&utm_medium=video&utm_campaign=FR-001 |

**Ingredientes (2 pers.):** 500 g ancas de rana, 3 dientes de ajo, perejil fresco,
30 g mantequilla, 2 cucharadas aceite de oliva, sal, pimienta, 1 limón. (Opcional: harina.)

---

## B. GUION — 10 micro-escenas (locución Fabien, ES + acento francés suave)

> Tono: cercano, enérgico, de sobremesa. ~2,5 palabras/seg. Muletilla "¡voilà!" al emplatar.

| # | Escena | Dur | Locución | Plano | Motor sugerido |
|---|---|---|---|---|---|
| 1 | Hook | 5s | "Esto son ancas de rana a la provenzal. Y huelen a Francia." | Plato final humeante, primerísimo plano | Seedance |
| 2 | Identidad | 5s | "Soy Fabien, y en mi cocina, en la Provenza, esto se hace así." | Fabien a cámara, sonríe, cocina al fondo | Veo/Kling |
| 3 | Las ancas | 8s | "Las ancas de rana son carne tierna, suave, alta en proteína. Frescas, las tienes en ancasderana.com." | Manos sostienen ancas crudas; cierre con web | Seedance |
| 4 | Ingredientes | 6s | "Ajo, perejil, mantequilla, aceite, limón. Nada más." | Cenital del mise en place | Seedance |
| 5 | Técnica | 8s | "Sartén bien caliente, mantequilla y aceite. Las ancas, dos minutos por lado. Que se doren." | Ancas en sartén, chisporroteo | Seedance/Veo |
| 6 | El truco | 5s | "El truco: el ajo y el perejil al final, fuera del fuego. Así no amarga." | Fabien echa ajo/perejil, guiño | Veo/Kling |
| 7 | Guarnición | 6s | "Un poco de pan tostado para mojar. Nada más necesita." | Emplatado con pan | Seedance |
| 8 | Maridaje | 5s | "¿Con qué? Un blanco seco de Provenza. Frío." | Copa de vino blanco junto al plato | Seedance |
| 9 | Tip saludable | 5s | "150 calorías, alto en proteína, bajo en grasa. Hasta para deportistas." | Plato + overlay ficha | overlay |
| 10 | Cierre+CTA | 6s | "Ancas de rana a la provenzal. ¡Voilà! Compra las tuyas en ancasderana.com." | Fabien levanta plato, abre manos | Veo/Kling |

Total ≈59s base. Largo 3 min: extender técnica (cámara lenta dorado), emplatado, plano
de la ventana provenzal, historia corta de la receta.

---

## C. PROMPTS DE PRODUCCIÓN

### C.1 — Imagen de anclaje (Nano Banana 2) — ya tienes la base
Reusar `ref_fabien_v1.png` **sin tatuaje**. Si el render actual lo tiene, regenerar con el
prompt maestro de la biblia añadiendo al final: `forearms clean, no tattoos`.
**Generar también versión vertical 9:16** del mismo Fabien (misma cara, encuadre retrato)
para Reels → guardar como `ref_fabien_v1_vertical.png`.

### C.2 — Prompts de vídeo (uno por escena)

**Estructura común a todos:** anclar `ref_fabien_v1.png` en planos de cara · capas de realismo
(luz cálida lateral, sombras suaves, reflejos en cobre, profundidad de campo, ventana a campo
de lavanda) · 9:16 para corto/micro, 16:9 para largo.

- **E1 (Seedance):** `Extreme close-up of cooked frog legs à la provençale on a rustic ceramic plate, glistening with butter, garlic and parsley, light steam rising, warm side light, copper reflections, shallow depth of field, photorealistic, 5s.`
- **E2 (Veo/Kling, cara):** `[ref_fabien] French chef Fabien, early 30s, white double-breasted jacket, lavender apron, smiling warmly at camera in a rustic Provençal kitchen, hanging copper pots, lavender field through the window, warm light, speaking, 5s.`
- **E3 (Seedance):** `Close-up of hands holding fresh raw frog legs over a stone countertop, Provençal kitchen background, natural light, photorealistic, 8s.`
- **E4 (Seedance):** `Top-down shot of mise en place: garlic cloves, fresh parsley, butter, olive oil, lemon on a wooden board, stone counter, warm light, 6s.`
- **E5 (Seedance/Veo):** `Frog legs searing in a hot pan with bubbling butter and olive oil, sizzling, light smoke, golden browning, close-up, dynamic, photorealistic, 8s.`
- **E6 (Veo/Kling, cara):** `[ref_fabien] Chef Fabien off the heat, sprinkling chopped garlic and parsley over the pan, playful wink, Provençal kitchen, warm light, 5s.`
- **E7 (Seedance):** `Plating frog legs à la provençale with toasted bread on a ceramic plate, garnish, warm light, copper reflections, 6s.`
- **E8 (Seedance):** `A glass of chilled dry white wine beside the finished plate, condensation on the glass, Provençal window light, shallow depth of field, 5s.`
- **E9:** plato final + overlay de ficha técnica (sección D).
- **E10 (Veo/Kling, cara):** `[ref_fabien] Chef Fabien lifting the finished plate towards camera, opening his hands, saying voilà, big warm smile, rustic Provençal kitchen, 6s.`

### C.3 — Voz (ElevenLabs)
Voz masculina ~30s, **español con acento francés suave**, cálida y enérgica. Generar las 10
locuciones por separado (archivos `voz_E1`…`voz_E10`). Fijar voice_id elegido en la biblia.

---

## D. FICHA TÉCNICA EN PANTALLA (overlay 9:16, escena 9)

```
ANCAS A LA PROVENZAL
🇫🇷 Francia · Provenzal
⏱ 20 min · 👥 2 · 🔥 Fácil
🥗 Score nutricional: A
💪 Alto proteína · bajo grasa · bajo sodio
🍷 Vino blanco seco de Provenza
📍 Ideal para tapeo y amigos
⚠ Alérgenos: lácteos
👉 ancasderana.com
```

---

## E. ENSAMBLE (3 cortes)

- **Largo 3 min (16:9, YouTube):** E1→E10 completas + extensiones (dorado cámara lenta,
  emplatado detallado, ventana provenzal, historia de la receta). Música suave provenzal.
- **Corto 1 min (9:16):** E1 + E3 + E5 + E6 + E9 + E10 (las de mayor retención).
- **Micro-reels (9:16):** "El truco" (E6) · "Cómo comprar ancas" (E3) · "El emplatado" (E7),
  cada uno con mini-hook + CTA. Reutilizan clips del largo (no se regenera nada).
- Subtítulos quemados en los tres. Marca de agua presente → **TEST, no publicar**.

---

## F. TEXTOS DEL CANAL (ES)

- **Título YouTube:** "Ancas de rana a la provenzal — el secreto francés en 20 min"
- **Título corto:** "El truco francés para las ancas perfectas 🐸"
- **Descripción:** gancho + ficha (país, score A, maridaje, momento) + CTA con UTM FR-001 +
  timestamps + `#ancasderana #recetafrancesa #provenzal #tapeo #grenoucerie`
- **Caption Reel:** "Ancas de rana como en la Provenza 🐸 El truco: ajo y perejil fuera del
  fuego. 👉 ancasderana.com (link en bio) #ancasderana #provenzal"
- **Miniatura:** plato + Fabien, texto "ANCAS A LA PROVENZAL", color lavanda.

---

## G. QC ANTES DE ENTREGAR (checklist A5)

- [ ] ¿Fabien idéntico en E2, E6, E10 (planos de cara)? Sin tatuaje en ningún plano.
- [ ] ¿Escenario provenzal coherente (cobre, lavanda, piedra, ventana)?
- [ ] ¿Capas de realismo presentes (vapor E1/E5, salpicadura/dorado E5, reflejos)?
- [ ] ¿Ancas centrales y apetecibles?
- [ ] ¿CTA ancasderana.com con UTM FR-001 en E3, E10, descripción y caption?
- [ ] ¿Datos nutricionales coherentes? (score A, ~150 kcal — verificar antes de publicar real)
- [ ] ¿Subtítulos en los 3 formatos? ¿9:16 corto/micro, 16:9 largo?
- [ ] ¿Marca de agua → marcado TEST?
- Si algún ítem falla → reintento dirigido (máx 2) → escalar a Fabi.

---

## H. PASOS DE EJECUCIÓN (orden operativo)

1. Regenerar `ref_fabien_v1.png` sin tatuaje + versión vertical 9:16.
2. Validar voice_id en ElevenLabs (acento francés suave/español).
3. Generar imágenes de arranque de cada escena (Nano Banana 2).
4. Generar los 10 clips de vídeo (motor según tabla B), anclando la referencia en planos de cara.
5. Generar las 10 locuciones (ElevenLabs).
6. Montar overlay de ficha (escena 9).
7. Ensamblar los 3 cortes + subtítulos quemados.
8. Pasar QC (sección G).
9. Entregar paquete a Fabi para revisión. **No publicar** (es TEST free).

---

*Nota seguridad alimentaria: los datos nutricionales (~150 kcal, score A) deben verificarse*
*con fuente fiable antes de cualquier publicación real. En FREE/TEST sirven para validar pipeline.*
