---
name: promob-texto-limpo
description: Transform messy Promob specification text into clean, organized documentation ready to paste into Promob's text box. Use when user provides furniture specification text from Promob that needs cleaning and organization.
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

Apply INCLUSIVE approach - process EVERYTHING except specific exclusions:

#### Items to ALWAYS Remove (ONLY THESE):
- Entire "Decore" section
- All "Fita de Borda" (edge banding) lines - any line containing "Fita"
- All "Tipo de Fundo" lines and variations
- Environment titles (Cozinha, Dormitório, Sala, Banheiros, etc.)
- Empty fields (lines ending with ": " with no content)
- "COMPONENTES AVULSOS" section (integrate items elsewhere)

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

**Comprehensive Mapping (INCLUSIVE approach):**

**CAIXA - Include subsections:**
- Base Estrutural → subsection
- Corpo de Gavetas → subsection
- Frente Gaveta Interna → subsection
- Cores → main content

**PORTAS / FRENTES - Consolidate all door types:**
- All from Portas/Frentes section
- Cava 45 items → integrate here
- Cava Tech items → integrate here
- Basculantes → subsection

**PUXADORES - All handle types:**
- Puxador Perfil (any brand)
- Puxador Concha
- Meia Cava / Cava Central
- Luna items from Rometal

**PORTA DE VIDRO - Consolidate from multiple sources:**
- Rometal section (Porta Perfil, Perfil, Puxador Luna, Vidros)
- Vidraçaria section (Vidros)
- Miolo Porta: Vidro (from Portas/Frentes)

**FERRAGENS - All hardware:**
- Dobradiça (all types)
- Corrediça (all types)
- Fechadura / Fecho Rolete
- Vão Eletro

**PAINÉIS / TAMPOS / TAMPONAMENTOS:**
- All Painéis items
- Ripas → important subsection
- Tampo Composto

**ACESSÓRIOS - Comprehensive list:**
- Cabideiro (all types)
- Ponteiras (Cava Y, Gola)
- Puxador Concha (if not in PUXADORES)
- Alternativas/Acabamentos
- Tucano models
- Capa Suporte (if needed)

**COMPONENTES:**
- Tip-On
- Porta-Pano
- Organizadores
- Lixeiras

**ESTRUTURA:**
- Base Estrutural (if standalone)
- Estrado
- Pés

**SERRALHERIA:**
- Metalon
- Perfis metálicos

**When Unknown Item Found - Two-Level Decision:**

*First Level - Common Categories:*
- Ask user to classify in main categories:
  - COMPONENTES
  - FERRAGENS
  - ACESSÓRIOS
  - Nenhuma das anteriores (show all categories)
  - Ignorar (don't include in final text)

*Second Level - All Categories (if "Nenhuma" selected):*
- Show complete list:
  - CAIXA
  - PORTAS / FRENTES
  - PUXADORES
  - PORTA DE VIDRO
  - FERRAGENS
  - PAINÉIS / TAMPOS / TAMPONAMENTOS
  - VIDROS
  - COMPONENTES
  - ESTRUTURA
  - SERRALHERIA
  - ILUMINAÇÃO
  - ACESSÓRIOS
  - PORTAS DE PASSAGEM
  - Criar nova categoria
  - Ignorar definitivamente

#### Critical Processing Rules:

**ALWAYS KEEP - Never Remove:**
- Puxadores (all types and brands)
- Ripas (under PAINÉIS)
- Base Estrutural / Corpo de Gavetas (under CAIXA)
- Vidros/Vidraçaria info (consolidate to PORTA DE VIDRO)
- Fechadura (to FERRAGENS)
- All Acessórios items

#### Section Consolidation:

**Smart Consolidations:**
1. **Rometal + Vidraçaria + "Miolo Porta: Vidro"** → PORTA DE VIDRO section
2. **Cava 45 + Cava Tech + Basculantes** → PORTAS / FRENTES types
3. **All Puxador mentions** → PUXADORES (from any section)
4. **Base Estrutural + Corpo de Gavetas** → CAIXA subsections

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

**ALWAYS Ask About Dobradiças (Hinges) - USE MULTISELECT:**
- Always use multiSelect: true to allow multiple selections
- User can check one or more options:
  - Blum Clip Top Blumotion
  - Blum (genérica)
  - Hettich Sensys
  - Hafele c/amortecedor
  - Hafele s/amortecedor
  - Dobradiça c/amortecedor (generic)
  - Dobradiça s/amortecedor (generic)

**ALWAYS Ask About Corrediças (Drawer Slides) - USE MULTISELECT:**
- Always use multiSelect: true to allow multiple selections
- User can check one or more options:
  - Quadro/Invisível
  - Telescópica
  - Nenhuma

**Multiple Types Present?**
- If text shows multiple types of the same hardware, confirm with user which to use

Use the AskUserQuestion tool to gather this information interactively.

**Implementation for Hardware Questions:**
When asking about dobradiças and corrediças:
```javascript
{
  question: "Quais tipos de dobradiças utilizar?",
  header: "Dobradiças",
  multiSelect: true,  // CRITICAL - always true
  options: [
    { label: "Blum Clip Top Blumotion", description: "..." },
    { label: "Hettich Sensys", description: "..." },
    // etc
  ]
}
```

**Implementation for Unknown Items:**
When encountering unknown item (e.g., "Suporte Microondas", "Fecho Toque"):
1. First question: "Encontrei [item]. Em qual categoria incluir?"
   - Options: COMPONENTES, FERRAGENS, ACESSÓRIOS, Nenhuma das anteriores, Ignorar
2. If "Nenhuma das anteriores" selected, second question shows ALL categories
3. Remember classification for entire session (not permanently)

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

**Example Clean Output (Vertical Simple Format - INCLUSIVE):**
```
CAIXA

Cores:
MDF Branco TX
MDF Duratex Madeirado Itapuã
MDF Arauco Verde Jade

Base Estrutural:
MDF Cru

Corpo de Gavetas:
MDF Branco TX


PORTAS / FRENTES

Tipos:
Meia Cava Vertical
Reta
Perfil Borda
Cava 45
Basculante

Acabamentos:
MDF Guararapes Terrino
MDF Duratex Gianduia Trama

Frentes Internas:
MDF Branco TX


PUXADORES

Meia Cava Vertical
Meia Cava 100mm
Puxador Perfil Rometal 200mm
Puxador Concha Cromado
Luna Embutido Luna 100mm

Acabamento:
MDF Duratex Madeirado Itapuã


FERRAGENS

Dobradiça:
Blum Clip Top Blumotion
Hafele c/amortecedor

Corrediça:
Quadro/Invisível

Fechadura:
Fecho Rolete


PAINÉIS / TAMPOS / TAMPONAMENTOS

MDF Guararapes Terrino
MDF Duratex Gianduia Trama

Ripas:
MDF Branco TX


PORTA DE VIDRO

Porta Perfil:
Aba Zero RM-377

Perfil Rometal:
Preto
Natural

Puxador:
Luna Embutido Luna 100mm

Vidros:
Incolor
Reflecta Prata


ACESSÓRIOS

Cabideiro:
Oblongo Genérico
Rometal Vesto

Ponteiras:
Cava Y Abertas
Gola Abertas

Tucano:
SP-180
```

### Step 5: Deliver Result

Present the cleaned text to the user with:
- Clear indication it's ready to paste into Promob
- Any clarifications made during processing
- Confirmation of any user selections (hardware choices)

**Include Processing Report:**
```
──────────────────────────────────
RELATÓRIO DE PROCESSAMENTO

Removido:
✗ Seção Decore completa
✗ Todas as fitas de borda (X linhas)
✗ Tipos de fundo (X linhas)
✗ Campos vazios (X linhas)

Decisões do usuário:
✓ Dobradiça: [user selection]
✓ Corrediça: [user selection]
✓ [Other decisions]

Classificações automáticas:
→ Item X → Category Y
→ Consolidado: Rometal + Vidraçaria → PORTA DE VIDRO

Observações:
• [Any important notes]
```

## Important Notes

- This skill is used 10+ times per day in production workflow
- Output must be plain text with NO formatting characters
- Promob's text box is limited - compact formatting is essential
- Text serves as technical documentation for clients
- **INCLUSIVE APPROACH:** Process everything except explicit exclusions
- **NEVER LOSE INFORMATION** - when in doubt, include it and ask user
- **Smart consolidation:** Combine related sections (Rometal→Porta de Vidro)
- **Format standard:** Vertical Simple - one item per line, with sub-categories
- **Key principle:** Completeness over minimalism - client needs ALL details

## Interactive Behavior

**ALWAYS ASK:**
- Dobradiças: multiSelect: true (checkboxes - can select multiple)
- Corrediças: multiSelect: true (checkboxes - can select multiple)
- Better UX: checkboxes allow flexible selection without "Ambas" option

**AUTO-CLASSIFY:**
- Known items go to their designated categories
- Unknown items trigger user decision
- Learn classifications during session (not permanently)

## Resources

### references/
Contains example messy texts from Promob for reference and testing purposes.
