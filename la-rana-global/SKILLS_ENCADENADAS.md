# SKILLS ENCADENADAS — Sistema "La Rana Global" (empaquetado final)
## Manual operativo para Cowork. Cómo todo corre "en continuo".

> Cinco skills que se llaman en cadena, orquestadas por el sistema maestro.
> Una ejecución del webhook = receta → paquete de vídeo listo para revisión de Fabi.

---

## MAPA DE SKILLS

```
WEBHOOK {receta_id}
   │
   ▼
[SKILL 0] ORQUESTADOR ──── carga biblia + plantilla + techo de clips
   │
   ├─► [SKILL 1] RECETA      → rellena plantilla, escribe guion (A1)
   ├─► [SKILL 2] AVATAR+ESCENA→ escaleta visual + prompts img/vídeo (A2+A3)
   ├─► [SKILL 3] FICHA        → overlay en pantalla desde datos de receta
   ├─► [SKILL 4] TEXTOS       → títulos, descripción, hashtags, CTA+UTM
   └─► [SKILL 5] QC+ENSAMBLE  → 3 cortes + control coherencia/marca (A4+A5)
   │
   ▼
PAQUETE → carpeta de revisión de Fabi → aprobar/corregir
```

---

## SKILL 0 — ORQUESTADOR
- **Dispara:** webhook con `receta_id`.
- **Hace:** carga biblia Chef Fabien, plantilla, techo de clips. Llama skills 1→5 en orden.
- **Para y escala** si: falta campo obligatorio, hay `[VERIFICAR]`, se excede presupuesto,
  avatar de receta ≠ avatar activo, o el paquete está listo (aprobación).
- **Nunca publica.**

## SKILL 1 — RECETA (ghostwriter A1)
- **Input:** `receta_id` + ficha de cola. **Output:** `PLANTILLA_RECETA` rellena + `guion_receta.md`.
- 10 bloques locutados, español/acento francés, tono Fabien cercano. Datos nutricionales
  verificados o `[VERIFICAR]`.

## SKILL 2 — AVATAR + ESCENA (A2 + A3)
- **Input:** guion + biblia + librería de realismo. **Output:** `escaleta_visual.md` + `prompts_produccion.md`.
- Avatar = Fabien anclado a `ref_fabien_v1.png`. Motor de vídeo agnóstico (mejor por plano).
- Aplica capas de realismo (luz/humo/salpicadura/reflejo/textura/ventana).

## SKILL 3 — FICHA EN PANTALLA
- **Input:** plantilla rellena. **Output:** overlay 9:16 con nombre, país, tiempo, comensales,
  dificultad, score nutricional, perfil, maridaje, momento, alérgenos, CTA.

## SKILL 4 — TEXTOS DEL CANAL
- **Input:** plantilla + mercado. **Output:** título, descripción, caption, hashtags, CTA+UTM
  por `receta_id`. Versión ES; FR cuando se active grenoucerie.fr.

## SKILL 5 — QC + ENSAMBLE (A4 + A5)
- **Input:** assets + escaleta. **Output:** `montaje_3min` + `montaje_1min` + `microreels` + `qc_report`.
- Reutiliza clips (no genera dos veces). Verifica coherencia, realismo, producto, CTA, subtítulos,
  marca de agua (free=TEST). NO APTO → reintento (máx 2) → escala.

---

## SKILLS DE SOPORTE (transversales)

- **BANCO DE ASSETS:** registra clips reutilizables (ancas crudas/emplatadas, planos genéricos).
  Antes de generar, comprueba si ya existe → baja coste por vídeo con el tiempo.
- **TRADUCCIÓN ES→FR:** subtitula/readapta textos y voz para grenoucerie.fr sin rehacer vídeo.
- **TRACKING CTA:** genera UTM por vídeo/mercado y registra qué receta lleva tráfico.

---

## REGLAS INVIOLABLES DEL SISTEMA

1. **Seguridad alimentaria:** datos nutricionales y manipulación de producto crudo NO se inventan.
   Sin fuente fiable → `[VERIFICAR]` y escalar. Nunca afirmar propiedades de salud sin base.
2. **Coherencia de avatar:** Fabien es inmutable. Deriva irresoluble → escala.
3. **Presupuesto:** techo de clips por vídeo. Excederlo → para y escala.
4. **Aprobación humana:** el sistema entrega, Fabi aprueba. Nunca publica solo.
5. **Free = TEST:** lo producido con marca de agua no se publica.
6. **CTA siempre:** todo vídeo lleva la web del mercado correcto con UTM.

---

## CHECKLIST DE ACTIVACIÓN (Cowork)

- [ ] Biblia Chef Fabien + `ref_fabien_v1.png` generada y validada.
- [ ] voice_id ElevenLabs elegido (acento francés suave/español).
- [ ] Cola ≥6 recetas francesas con plantilla completa.
- [ ] Cuentas free creadas: Nano Banana 2, Veo 3.1, Seedance 2.0, Kling 3.0, ElevenLabs.
- [ ] Techo de clips por vídeo fijado.
- [ ] Carpeta de revisión de Fabi definida en Cowork.
- [ ] UTMs configurados para ancasderana.com.

---

## DOCUMENTOS DEL SISTEMA (mapa de entregables)

1. `SISTEMA_CANAL_ANCAS_v2.md` — sistema maestro (arquitectura, agentes, stack, flujos).
2. `PLANTILLA_RECETA.md` — fuente única de datos de cada receta.
3. `TEXTOS_CANAL.md` — copys por pieza y mercado.
4. `SKILLS_ENCADENADAS.md` — este documento (empaquetado operativo).

---

*Empaquetado v1.0 — Sistema "La Rana Global" / GRENOUCERIE.*
*Arranca en free con Chef Fabien para validar pipeline. Escala a pago (3-10€/vídeo) y a más*
*avatares cuando coherencia y coste estén probados.*
