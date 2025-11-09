---
name: promob-texto-limpo-web
description: Transform messy Promob furniture specification text into clean, organized documentation using Python parser. Handles materials, hardware, and categorization with interactive questions.
metadata:
  version: 2.0.0
---

# Promob Texto Limpo (Web Version)

## Overview

This Skill transforms messy Promob furniture specification text into clean, organized documentation ready to paste into Promob's text box.

**Performance**: 90% code (Python), 10% AI (questions) = Fast and efficient.

## When to Use

Use when the user provides messy Promob text containing furniture specifications that need cleaning and organization.

## Workflow

### Step 1: Receive Input

Accept the messy Promob text from the user.

### Step 2: Process with Python Parser

Run the parser to analyze the text:

```python
from parser import PromobParser

parser = PromobParser()
data = parser.parse(user_input_text)
questions_data = parser.get_questions_data()
```

The parser automatically:
- Removes unwanted fields (Fita de Borda, Tipo de Fundo, etc.)
- Cleans material names (Duratex Cor>Itapuã → MDF Duratex Itapuã)
- Consolidates related sections
- Detects hardware and unknown items

### Step 3: Ask User Questions

Based on `questions_data`, ALWAYS ask the user:

**Question 1 - Dobradiças (allow multiple selections):**
Present options:
- Blum Clip Top Blumotion (Premium com amortecedor)
- Hettich Sensys (Hettich com amortecedor)
- Hafele c/amortecedor (Hafele premium)
- Dobradiça genérica (Sem especificação)

User can select one or more.

**Question 2 - Corrediças (allow multiple selections):**
Present options:
- Quadro/Invisível (Corrediça quadro)
- Telescópica (Corrediça telescópica)
- Nenhuma (Sem corrediças)

User can select one or more.

**Question 3 - Unknown Items (if any):**
For each unknown item, ask where to include it:
- CAIXA (Cores, estruturas, gavetas)
- PORTAS / FRENTES (Tipos, acabamentos)
- PUXADORES (Handles)
- FERRAGENS (Hardware)
- COMPONENTES (Organizadores, lixeiras)
- ACESSÓRIOS (Cabideiros, ponteiras)
- Ignorar (Don't include)

### Step 4: Generate Output

With user's answers, generate the final clean text:

```python
output = parser.format_output(
    include_dobradica=user_dobradica_choices,  # e.g., ['Blum Clip Top Blumotion', 'Hettich Sensys']
    include_corredica=user_corredica_choices   # e.g., ['Quadro/Invisível']
)
```

### Step 5: Present Result

Show the clean text to the user in plain format (no markdown code blocks).

The text is ready to paste directly into Promob.

## Technical Details

### What the Parser Does

**Automatic Removal:**
- Entire "Decore" section
- All "Fita de Borda" fields
- All "Tipo de Fundo" fields
- Environment titles (Cozinhas, Dormitórios, etc.)
- Modelo Interno fields
- Empty fields

**Smart Conversion:**
- `MDF Cores>Branco TX` → `MDF Branco TX`
- `Duratex Cor>Itapuã` → `MDF Duratex Itapuã`
- `Arauco Madeirado>Sertanejo` → `MDF Arauco Sertanejo`

**Section Consolidation:**
- Rometal + Vidraçaria → PORTA DE VIDRO
- All Puxador fields → PUXADORES
- Frentes de Gaveta → PORTAS / FRENTES
- Links Rometal model to handles (e.g., "Cielo - Rometal 150mm")

**Special Formatting:**
- PORTAS DE PASSAGEM: Groups handles as "Modelo do Puxador: Externo/Interno"
- Tracks origin section for unknown items (e.g., "Porta-Pano (FGVTN)")

### Output Structure

```
CAIXA
  Cores, Base Estrutural, Corpo de Gavetas

PORTAS / FRENTES
  Tipos, Acabamentos, Frentes Internas, Frente Gaveta Interna, Miolo Porta

PUXADORES
  Main items, Acabamento Puxador, Obispa

PORTA DE VIDRO
  Porta Perfil, Perfil Rometal, Puxador, Vidros

FERRAGENS
  Dobradiça, Corrediça, Fechadura

PAINÉIS / TAMPOS / TAMPONAMENTOS
  Main items, Ripas

ACESSÓRIOS
  Cabideiro, Alternativa

SERRALHERIA
  Metalon

PORTAS DE PASSAGEM
  Acabamento Interno/Externo, Acabamento Puxador, Modelo do Puxador
```

## Important Notes

- Always ask about dobradiças and corrediças, even if none were found in text
- Present results WITHOUT markdown code blocks (plain text only)
- Process unknown items interactively with user
- Link Rometal model (Cielo) to handle sizes automatically
- Track section origin for all unknown items
