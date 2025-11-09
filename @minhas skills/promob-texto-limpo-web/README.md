# Promob Texto Limpo - Web Version

Versão otimizada da skill para uso no Claude.ai (web interface).

## 📦 Como Empacotar

Para usar no Claude.ai, você precisa criar um arquivo ZIP com esta estrutura:

```
promob-texto-limpo-web.zip
└── promob-texto-limpo-web/
    ├── Skill.md
    ├── parser.py
    └── README.md
```

### Criar o ZIP (Windows):

1. **Via PowerShell:**
```powershell
cd "C:\Users\ricar\Projetos\claude-skills-master\@minhas skills"
Compress-Archive -Path "promob-texto-limpo-web" -DestinationPath "promob-texto-limpo-web.zip"
```

2. **Via Explorador de Arquivos:**
- Clique com botão direito na pasta `promob-texto-limpo-web`
- Selecione "Enviar para > Pasta compactada (zipada)"
- Renomeie para `promob-texto-limpo-web.zip`

### Criar o ZIP (WSL/Linux):

```bash
cd "/mnt/c/Users/ricar/Projetos/claude-skills-master/@minhas skills"
zip -r promob-texto-limpo-web.zip promob-texto-limpo-web/
```

## 🚀 Como Instalar no Claude.ai

1. Acesse [Claude.ai](https://claude.ai)
2. Vá em **Settings** > **Capabilities** > **Skills**
3. Clique em **Upload Skill**
4. Selecione o arquivo `promob-texto-limpo-web.zip`
5. Ative a skill

## 🎯 Como Usar

Simplesmente cole um texto bagunçado do Promob na conversa:

```
Tampos/Tamponamentos
- Painéis: Duratex Cor>Gianduia Trama
- Fita de Borda: Duratex Cor>Gianduia Trama
...
```

O Claude vai:
1. Detectar que é texto Promob
2. Processar automaticamente com Python
3. Fazer perguntas sobre dobradiças/corrediças
4. Retornar texto limpo e organizado

## 🔧 Diferenças vs Versão CLI

| Aspecto | CLI | Web |
|---------|-----|-----|
| **Ambiente** | Claude Code terminal | Claude.ai browser |
| **Parser** | Chamado via Bash | Executado internamente |
| **Perguntas** | AskUserQuestion tool | Perguntas normais da conversa |
| **Performance** | ~2-4s | ~1-3s (ainda mais rápido) |

## 📊 Performance

- **Tempo:** 1-3 segundos
- **Tokens:** ~3,000-5,000
- **Trabalho IA:** 10%
- **Trabalho Código:** 90%

## 🛠️ Desenvolvimento

Para testar localmente:

```python
from parser import process_promob_text

# Primeira passagem - detectar perguntas
texto_input = "..."
output, questions = process_promob_text(texto_input)

# Segunda passagem - com respostas do usuário
output, _ = process_promob_text(
    texto_input,
    dobradicas=['Blum Clip Top Blumotion', 'Hettich Sensys'],
    corredicas=['Quadro/Invisível']
)

print(output)
```

## 📝 Versão

**v2.0.0** - Web-optimized version with Python integration
