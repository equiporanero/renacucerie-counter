# PLANTILLA MAESTRA DE RECETA — Sistema "La Rana Global"
## Fuente única de verdad. De aquí beben: guion (A1), ficha en pantalla, cola pre-rankeada.

> Toda receta del canal rellena esta plantilla ANTES de entrar a producción.
> Si un campo obligatorio falta o está sin verificar, el sistema escala a Fabi y no produce.

---

## BLOQUE 1 — IDENTIFICACIÓN (metadatos / cola)

| Campo | Valor | Oblig. |
|---|---|---|
| `receta_id` | _(ej. FR-001)_ | ✅ |
| Nombre receta | | ✅ |
| País | | ✅ |
| Cocina | _(provenzal / tradicional / fusión / contemporánea...)_ | ✅ |
| Avatar asignado | _(debe coincidir con avatar activo, ej. Fabien)_ | ✅ |
| Dificultad | 1-3 _(1 fácil · 2 media · 3 alta)_ | ✅ |
| Tiempo total | _(min)_ | ✅ |
| Nº comensales | | ✅ |
| Temporada | _(óptima oct-feb / todo el año / verano...)_ | ✅ |
| Momento ideal | _(tapeo · con amigos · celebración · día de campo · barbacoa · post-gym · cena pareja · aperitivo)_ | ✅ |

---

## BLOQUE 2 — LOS 10 BLOQUES DE GUION (orden de retención → los locuta A1)

| # | Bloque | Dur. | Contenido a rellenar |
|---|---|---|---|
| 1 | Hook / plato final + país | 5s | |
| 2 | Identidad de cocina + avatar | 5s | |
| 3 | Las ancas: qué son + cómo comprarlas | 8s | _(incluir CTA web)_ |
| 4 | Ingredientes (mise en place) | 6s | |
| 5 | Técnica y modo de cocción | 8s | |
| 6 | El truco | 5s | |
| 7 | Guarnición / acompañamiento | 6s | |
| 8 | Maridaje | 5s | |
| 9 | Tip saludable | 5s | |
| 10 | Cierre + plato final + CTA | 6s | |

---

## BLOQUE 3 — INGREDIENTES Y TÉCNICA

- **Ingredientes** _(lista con cantidades para el nº de comensales)_:
- **Técnica principal** _(salteado / fritura / guiso / horno / pochado...)_:
- **El truco** _(el detalle que lo hace especial — momento compartible del vídeo)_:
- **Guarnición / acompañamiento**:
- **Maridaje** _(vino o bebida de la región)_:

---

## BLOQUE 4 — SALUD Y NUTRICIÓN (datos verificados — si dudoso → `[VERIFICAR]`)

| Campo | Valor |
|---|---|
| kcal / ración | |
| Proteína (g) | |
| Grasa (g) | |
| Sodio | _(alto / medio / bajo)_ |
| Perfil saludable | _(alto en proteína · bajo en grasa · bajo en sodio · apto hipertensos...)_ |
| **Score nutricional** | **A–E** _(escala tipo Nutri-Score: A verde = más saludable, E rojo)_ |
| Apto para | _(deportistas · dieta proteica · hipertensos · bajo en sodio...)_ |

> **Nota de seguridad:** los datos nutricionales no se inventan. Sin fuente fiable → `[VERIFICAR]` y escalar.

---

## BLOQUE 5 — ALÉRGENOS

Marcar presentes _(según receta y guarnición)_:
☐ Gluten ☐ Lácteos ☐ Huevo ☐ Pescado ☐ Crustáceos ☐ Moluscos
☐ Frutos secos ☐ Cacahuete ☐ Soja ☐ Apio ☐ Mostaza ☐ Sésamo ☐ Sulfitos
- Las ancas de rana **no** son alérgeno declarado por sí mismas; vigilar rebozados (gluten/huevo) y salsas.

---

## BLOQUE 6 — PRODUCTO Y CTA

| Campo | Valor |
|---|---|
| Origen ancas | Pelophylax perezi · GRENOUCERIE (granja intensiva europea) |
| Cómo comprarlas | _(formato: frescas/congeladas, cantidad recomendada)_ |
| Mercado / CTA | España → ancasderana.com · Francia → grenoucerie.fr |

---

## BLOQUE 7 — FICHA TÉCNICA EN PANTALLA (overlay del vídeo)

> Subconjunto visual de los datos de arriba. Aparece sobreimpreso en el vídeo.
> Diseño compacto, legible en vertical (9:16). Lo genera la skill de ficha.

```
┌─────────────────────────────┐
│  [NOMBRE RECETA]            │
│  🇫🇷 [País] · [Cocina]       │
│  ⏱ [Tiempo] · 👥 [Comensales]│
│  🔥 Dificultad [1-3]         │
│  🥗 Score nutricional [A-E]  │
│  💪 [Perfil: alto proteína…] │
│  🍷 Marida con [maridaje]    │
│  📍 Ideal para [momento]     │
│  ⚠ Alérgenos: [iconos]      │
│  👉 [web del mercado]        │
└─────────────────────────────┘
```

---

*Plantilla v1.0 — toda receta la rellena antes de producción. Campos ✅ obligatorios.*
*Sin campo obligatorio o con `[VERIFICAR]` sin resolver → el sistema escala y no produce.*
