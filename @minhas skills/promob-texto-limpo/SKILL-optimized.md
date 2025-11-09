---
name: promob-texto-limpo-v2
description: Transform messy Promob specification text into clean documentation using efficient Python parsing (90% code, 10% AI).
---

# Promob Texto Limpo v2 (Optimized)

## Overview

High-performance skill that transforms messy Promob furniture specifications into clean, organized text using hybrid approach:
- **Code handles 90%**: Parsing, filtering, consolidation, formatting
- **AI handles 10%**: User decisions (hardware choices, unknown items)

**Performance**: 70-80% faster than pure AI approach.

## When to Use

Use when user provides messy Promob text that needs cleaning.

## Workflow

### Step 1: Save Input to File

Write user's text to temporary file:
```bash
# Use Write tool to save to /tmp/promob_input.txt
```

### Step 2: Get Questions Data

Run parser in questions mode to identify what needs to be asked:
```bash
python3 "@minhas skills/promob-texto-limpo/promob_parser.py" /tmp/promob_input.txt --questions
```

This returns JSON with:
- `dobradicas_found`: Hinges found in text (e.g., ["Blum Clip Top Blumotion", "Hettich Sensys"])
- `corredicas_found`: Drawer slides found (usually empty)
- `unknown_items`: Items needing classification
- `needs_dobradica_question`: true (always ask)
- `needs_corredica_question`: true (always ask)

### Step 3: Ask User Questions

**ALWAYS use AskUserQuestion tool for hardware:**

**Question 1 - Dobradiças (multiSelect: TRUE):**
```
question: "Quais tipos de dobradiças utilizar?"
header: "Dobradiças"
multiSelect: true
options:
  - Blum Clip Top Blumotion (Premium com amortecedor)
  - Blum (genérica) (Sem especificação)
  - Hettich Sensys (Hettich com amortecedor)
  - Hafele c/amortecedor (Hafele premium)
  - Hafele s/amortecedor (Hafele básica)
  - Dobradiça c/amortecedor (generic) (Genérica premium)
  - Dobradiça s/amortecedor (generic) (Genérica básica)
```

**Question 2 - Corrediças (multiSelect: TRUE):**
```
question: "Quais tipos de corrediças utilizar?"
header: "Corrediças"
multiSelect: true
options:
  - Quadro/Invisível (Corrediça quadro)
  - Telescópica (Corrediça telescópica)
  - Nenhuma (Sem corrediças)
```

**Question 3 - Unknown Items (if any):**
For each unknown item, ask classification:
```
question: "Encontrei 'Módulo s/ Rodapé'. Em qual categoria incluir?"
header: "Item"
multiSelect: false
options:
  - COMPONENTES (Organizadores, lixeiras, etc)
  - FERRAGENS (Hardware, mecanismos)
  - ACESSÓRIOS (Cabideiros, ponteiras)
  - CAIXA (Cores, estruturas, gavetas)
  - Ignorar (Não incluir no texto final)
```

### Step 4: Generate Final Output

Run parser with user's choices:
```bash
python3 "@minhas skills/promob-texto-limpo/promob_parser.py" /tmp/promob_input.txt \
  --dobradicas "Blum Clip Top Blumotion,Hettich Sensys" \
  --corredicas "Quadro/Invisível"
```

Note: Join multiple selections with commas (no spaces around commas).

### Step 5: Present Clean Text

Copy the parser output and present to user WITHOUT markdown code blocks.
The text is ready to paste directly into Promob's text box.

## Technical Details

### What the Parser Does

**Automatic Removal:**
- Entire "Decore" section
- All "Fita de Borda" fields
- All "Tipo de Fundo" fields
- Environment titles (Cozinhas, Dormitórios, etc.)
- Empty fields

**Smart Conversion:**
- `MDF Cores>Branco TX` → `MDF Branco TX`
- `Duratex Cor>Itapuã` → `MDF Duratex Itapuã`
- `Arauco Madeirado>Sertanejo` → `MDF Arauco Sertanejo`

**Section Consolidation:**
- Rometal + Vidraçaria → PORTA DE VIDRO
- Cava 45 + Basculantes → PORTAS / FRENTES
- All Puxador fields → PUXADORES

**Output Format:**
```
SECTION TITLE

Subsection:
Item 1
Item 2

Another Subsection:
Item A
```

### Performance Comparison

| Metric | Original (Pure AI) | Optimized (Hybrid) |
|--------|-------------------|-------------------|
| Prompt size | ~455 lines | ~80 lines |
| Processing | Full LLM parsing | Instant parsing + minimal LLM |
| Speed | ~10-15s | ~2-4s |
| Token usage | ~15-20k tokens | ~3-5k tokens |

## Code Location

Parser: `promob_parser.py`
- Class: `PromobParser`
- Main method: `parse(text: str) -> PromobData`
- Format method: `format_output(include_dobradica, include_corredica) -> str`
