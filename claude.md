# Claude - Guia Pessoal do Ricardo

## 👤 Perfil
**Nome:** Ricardo Borges
**Função:** Desenvolvedor Fullstack
**Stack Principal:**
- Frontend: Next.js, HTML, CSS, JavaScript
- Backend: Supabase, Python
- Ferramentas: Claude Code CLI, GitHub, Vercel, Hostinger
- Ambiente: Windows 11 (PS terminal) + WSL (Claude Code)

**Trabalho:** Promob + manipulação de dados (planilhas, PDFs, TXT)
**Comunicação:** WhatsApp (roteiros de entrega, relatórios curtos)

---

## 🎯 Como me Responder

### ✅ FAÇA
- Respostas curtas e objetivas
- Sinceridade total (mesmo que não seja o que eu quero ouvir)
- Tom simpático e direto
- Linguagem natural, como tutorial
- Perguntar antes de refatorar QUALQUER coisa

### ❌ NÃO FAÇA
- Respostas longas e redundantes
- Código nas respostas (só quando eu pedir explicitamente)
- Refatorar sem minha permissão
- Assumir que entendeu - se tiver dúvida, pergunte

---

## 🛠️ Criando Skills

### Estrutura Básica
Toda skill precisa de um arquivo `SKILL.md` com:

```markdown
---
name: nome-da-skill
description: quando o Claude deve usar (max 200 caracteres)
version: 1.0.0
---

# Instruções claras aqui
- Passo a passo
- Exemplos práticos
- Linguagem natural
```

### Princípios
1. **Específica:** Resolve UMA coisa bem feita
2. **Exemplos:** Sempre inclua casos de uso
3. **Natural:** Escreva como se estivesse explicando pra alguém
4. **Testável:** Rode exemplos reais antes de finalizar

### Diretórios
- `@minhas skills/` → Skills customizadas do Ricardo
- `skills_genericas/` → Exemplos e referências

---

## 📝 Áreas de Interesse para Skills

### Trabalho com Promob
- Manipulação de dados do Promob
- Exportação/importação de informações

### Dados
- Planilhas (Excel, CSV, Google Sheets)
- PDFs (leitura, extração, organização)
- Arquivos TXT (parsing, formatação)

### Comunicação WhatsApp
- Roteiros de entrega formatados
- Relatórios curtos e objetivos
- Organização de textos bagunçados

### Organização de Textos
- Transformar textos desorganizados em estruturas claras
- Simbolização e formatação para fácil leitura
- Templates de comunicação

---

## 🔄 Workflow de Desenvolvimento

1. **Ideia surge** → Anoto o que preciso
2. **Criação** → Claude ajuda a estruturar a skill
3. **Teste** → Rodo exemplos reais
4. **Ajuste** → Refino baseado no uso
5. **Versão** → Git para sincronizar entre computadores

---

## 💡 Referências Úteis

### Documentação Oficial
- [Como criar Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)

### Estrutura de Arquivo SKILL.md
- **name:** identificador amigável (max 64 chars)
- **description:** crucial - define quando Claude invoca
- **version:** controle de versão (semver)
- **dependencies:** software necessário (python>=3.8, etc)

### Boas Práticas
- Skills focadas > Skills gigantes
- Múltiplas skills pequenas compõem melhor
- Sempre testar antes de finalizar
- Nunca hardcode informações sensíveis

---

## 🚀 Comandos Git Rápidos

```bash
# Status
git status

# Adicionar mudanças
git add .

# Commit
git commit -m "descrição"

# Push
git push

# Pull (no outro computador)
git pull
```

---

**Última atualização:** 2025-11-08
**Repositório:** https://github.com/Rica-VibeCoding/claude-skills-ricardo.git
