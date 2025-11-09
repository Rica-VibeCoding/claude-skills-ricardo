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

### Step 1: Parse with Python

Run the parser to do the heavy lifting:

```python
from promob_parser import PromobParser

parser = PromobParser()
data = parser.parse(input_text)
```

The parser automatically:
- Removes unwanted fields (Fita de Borda, Tipo de Fundo, etc.)
- Cleans material names (Duratex Cor>Itapuã → MDF Duratex Itapuã)
- Consolidates related sections
- Categorizes items into proper sections

### Step 2: Ask Hardware Decisions

**ALWAYS ask about Dobradiças and Corrediças** using multiSelect:

```javascript
// Dobradiças
{
  question: "Quais tipos de dobradiças utilizar?",
  header: "Dobradiças",
  multiSelect: true,
  options: [
    { label: "Blum Clip Top Blumotion", description: "Premium com amortecedor" },
    { label: "Blum (genérica)", description: "Sem especificação" },
    { label: "Hettich Sensys", description: "Hettich com amortecedor" },
    { label: "Hafele c/amortecedor", description: "Hafele premium" },
    { label: "Hafele s/amortecedor", description: "Hafele básica" },
    { label: "Dobradiça c/amortecedor (generic)", description: "Genérica premium" },
    { label: "Dobradiça s/amortecedor (generic)", description: "Genérica básica" }
  ]
}

// Corrediças
{
  question: "Quais tipos de corrediças utilizar?",
  header: "Corrediças",
  multiSelect: true,
  options: [
    { label: "Quadro/Invisível", description: "Corrediça quadro" },
    { label: "Telescópica", description: "Corrediça telescópica" },
    { label: "Nenhuma", description: "Sem corrediças" }
  ]
}
```

### Step 3: Handle Unknown Items

If `data.unknown_items` has entries, ask user to classify:

**First Level** (common categories):
```javascript
{
  question: `Encontrei "${item}". Em qual categoria incluir?`,
  options: [
    { label: "COMPONENTES", description: "Organizadores, lixeiras, etc" },
    { label: "FERRAGENS", description: "Hardware, mecanismos" },
    { label: "ACESSÓRIOS", description: "Cabideiros, ponteiras" },
    { label: "Nenhuma das anteriores", description: "Ver todas as categorias" },
    { label: "Ignorar", description: "Não incluir no texto final" }
  ]
}
```

**Second Level** (if "Nenhuma das anteriores"):
Show all categories: CAIXA, PORTAS / FRENTES, PUXADORES, PORTA DE VIDRO, FERRAGENS, PAINÉIS / TAMPOS / TAMPONAMENTOS, VIDROS, COMPONENTES, ESTRUTURA, SERRALHERIA, ILUMINAÇÃO, ACESSÓRIOS, PORTAS DE PASSAGEM, Criar nova categoria, Ignorar.

### Step 4: Generate Output

```python
output = parser.format_output(
    include_dobradica=user_dobradica_choices,
    include_corredica=user_corredica_choices
)
```

The output is plain text, ready to paste into Promob.

### Step 5: Present Result

Show the cleaned text with processing report:

```
──────────────────────────────────
RELATÓRIO DE PROCESSAMENTO

Processado automaticamente:
✓ Removidas fitas de borda (X linhas)
✓ Removidos tipos de fundo (X linhas)
✓ Convertidos formatos MDF (X itens)
✓ Consolidadas seções relacionadas

Decisões do usuário:
✓ Dobradiça: [selections]
✓ Corrediça: [selections]
✓ [Unknown item classifications if any]

Tempo de processamento: ~0.1s (parser) + decisões do usuário
```

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
