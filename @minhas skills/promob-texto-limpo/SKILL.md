---
name: promob-texto-limpo
description: Transform messy Promob specification text into clean, organized documentation ready to paste into Promob's text box. Use when user provides furniture specification text from Promob that needs cleaning and organization.
version: 1.0.0
---

# Promob Texto Limpo

## Overview

This skill transforms messy, unstructured text output from Promob furniture design software into clean, well-organized documentation ready for pasting into Promob's text box or client documentation.

The skill processes furniture specifications including materials, finishes, hardware, handles, glass doors, and passage doors - organizing them into logical sections with proper formatting for Promob's limited text box.

## When to Use This Skill

Use this skill when:
- User provides messy text from Promob software
- Text contains furniture specifications that need organizing
- User asks to "clean up Promob text" or "organize furniture specs"
- Text includes sections like: Caixas, Portas/Frentes, Ferragens, Puxadores, Painéis, etc.

## Workflow

### Step 1: Receive and Parse Input

Accept the messy Promob text from the user. The text typically contains:
- Multiple disorganized sections
- Redundant information
- Unnecessary details (edge banding, specific fund types)
- Scattered color/material specifications
- Mixed hardware information

### Step 2: Process and Clean Text

Apply the following cleaning rules systematically:

#### Items to ALWAYS Remove:
- Entire "Decore" section
- All "Fita de Borda" (edge banding) lines
- All "Tipo de Fundo" lines and variations (Tipo de Fundo Superiores, Tipo de Fundo Despenseiro, etc.)
- "COMPONENTES AVULSOS" section
- Environment titles (Cozinha, Dormitório, Sala, etc.) - multiple environments may exist in same space
- "Capa Suporte L: Branco"

#### Material/Color Formatting:
When listing materials or colors in any section, use this format:
```
MDF Marca Linha Cor
```

Examples:
- MDF Arauco Verde Jade
- MDF Duratex Madeirado Itapuã
- MDF Guararapes Terrino

Remove prefixes like:
- "Caixas:"
- "Painéis:"
- "Acabamento:"
- "Acab. Portas/Frentes:"

Apply this to ALL sections: Caixa, Painéis/Tampos/Tamponamentos, Puxadores, Portas/Frentes.

#### Automatic Item Classification:

**Known Items to Specific Categories:**
- **COMPONENTES:** Tip-On, organizadores, lixeiras, cestos aramados
- **ESTRUTURA:** Base Estrutural, estrado, base cama, pés
- **SERRALHERIA:** Metalon, perfis metálicos, cantoneiras
- **ILUMINAÇÃO:** LED, spots, fitas LED, transformadores
- **ACESSÓRIOS:** Cabideiros, porta-panos, suportes

**When Unknown Item Found:**
- Ask user how to classify with options:
  - Ignore (don't include)
  - Include as "Não Identificado"
  - Assign to specific category
  - Always ignore this item (remember for session)

#### Section Consolidation:

**Combine "Painéis" + "Tampos/Tamponamentos":**
```
PAINÉIS / TAMPOS / TAMPONAMENTOS

MDF Duratex Madeirado Itapuã
MDF Arauco Verde Jade
MDF Arauco Cinza Cristal
```

**Combine all "Puxadores" (Handles):**
```
PUXADORES

Cava Central 200mm
Meia Cava 100mm
Meia Cava Vertical
Acabamento: MDF Duratex Madeirado Itapuã
```

**Combine all "Porta de Vidro" (Glass Door) items:**
```
PORTA DE VIDRO

Porta Perfil: Aba Zero RM-377
Perfil Rometal: Champagne Claro
Puxador: Luna Embutido Luna 100mm
Vidros: Incolor
```

**Group all hardware intuitively in "Ferragens":**
```
FERRAGENS

Dobradiça: Blum Clip Top Blumotion
Corrediça: Quadro Invisível
Fechadura: Trinco Rolete (porta passagem)
Ou Lixeira Izy: Branco
Blum Tip-On: Cinza
```

**Organize colors in "Caixa":**
```
CAIXA

Cores:
  MDF Branco TX
  MDF Duratex Madeirado Itapuã
  MDF Arauco Verde Jade
  MDF Arauco Cinza Cristal
```

### Step 3: Identify Missing Common Items

Check for common items that may be missing from the specification:

**ALWAYS Ask About Corrediças (Drawer Slides):**
- Always ask user which slide type to use (even if none mentioned):
  - Quadro/Invisível
  - Telescópica
  - Nenhuma (no slides needed)

**ALWAYS Ask About Dobradiças (Hinges):**
- Always ask user which hinge type to use, even if specified:
  - Blum Clip Top Blumotion
  - Hafele c/amortecedor
  - Dobradiça c/amortecedor (generic/China)
  - Dobradiça s/amortecedor (generic/China)
  - Keep original (if different from options above)

**Multiple Types Present?**
- If text shows multiple types of the same hardware, confirm with user which to use

Use the AskUserQuestion tool to gather this information interactively.

### Step 4: Generate Clean Output

Format the final output with these rules:

**Formatting Rules (Vertical Simple Format):**
1. **Titles:** ALL CAPS, with 2 blank lines before and 1 blank line after
2. **No special symbols:** No `*`, `-`, `>` or markdown formatting
3. **Vertical lists:** Each item on its own line, no bullets or prefixes
4. **Sub-items:** When there's a category (like "Cores:", "Tipos:"), add it on its own line followed by the items
5. **Clean spacing:** Single line break between sub-categories within a section
6. **Plain text only:** Ready to paste directly into Promob text box
7. **One item per line:** Never use commas or slashes to separate items on same line

**Section Order:**
1. CAIXA
2. PORTAS / FRENTES
3. PUXADORES
4. PORTA DE VIDRO
5. FERRAGENS
6. PAINÉIS / TAMPOS / TAMPONAMENTOS
7. VIDROS
8. COMPONENTES (Tip-On, organizadores, lixeiras)
9. ESTRUTURA (Base Estrutural, estrados)
10. SERRALHERIA (Metalon, perfis metálicos)
11. ILUMINAÇÃO (LED, spots, fitas) - if applicable
12. PORTAS DE PASSAGEM - if applicable

**Example Clean Output (Vertical Simple Format):**
```
CAIXA

Cores:
MDF Branco TX
MDF Duratex Madeirado Itapuã
MDF Arauco Verde Jade


PORTAS / FRENTES

Tipos:
Meia Cava Vertical
Reta
Perfil Borda

Acabamentos:
MDF Guararapes Terrino
MDF Duratex Gianduia Trama

Frentes Internas:
MDF Branco TX

Vidros:
Reflecta Prata


PUXADORES

Meia Cava Vertical
Meia Cava 100mm

Acabamento:
MDF Duratex Madeirado Itapuã


FERRAGENS

Dobradiça:
Blum Clip Top Blumotion

Corrediça:
Quadro/Invisível

Fechadura:
Fecho Rolete


PAINÉIS / TAMPOS / TAMPONAMENTOS

MDF Guararapes Terrino
MDF Duratex Gianduia Trama
MDF Arauco Madeirado Sertanejo


PORTA DE VIDRO

Porta Perfil:
Aba Zero RM-377

Perfil Rometal:
Preto

Puxador:
Luna Embutido Luna 100mm

Vidros:
Incolor
```

### Step 5: Deliver Result

Present the cleaned text to the user with:
- Clear indication it's ready to paste into Promob
- Any clarifications made during processing
- Confirmation of any user selections (hardware choices)

## Important Notes

- This skill is used 10+ times per day in production workflow
- Output must be plain text with NO formatting characters
- Promob's text box is limited - compact formatting is essential
- Text serves as technical documentation for clients
- Never lose information - use common sense to place unclear items logically
- When in doubt about categorization, ask the user
- **Format standard:** Vertical Simple (Variation 5) - one item per line, with sub-categories
- **Key principle:** Vertical readability for easy text placement in Promob project

## Interactive Behavior

**ALWAYS ASK:**
- Dobradiças type (even if specified in text)
- Corrediças type (even if mentioned or not)
- Multiple hardware conflicts (which to use)

**AUTO-CLASSIFY:**
- Known items go to their designated categories
- Unknown items trigger user decision
- Learn classifications during session (not permanently)

## Resources

### references/
Contains example messy texts from Promob for reference and testing purposes.
