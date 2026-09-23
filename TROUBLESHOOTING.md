# 🔧 Troubleshooting - Internet Search API Homepage

## 🔴 Erro 502 - Application Failed to Respond

### O que é?
O servidor não conseguiu responder a tempo ou crashed.

### Soluções (nesta ordem)

#### 1. **Redeploy (Tenta primeiro isto!)**
1. Aceda a https://railway.app
2. Clique no projeto
3. Vá a **Deployments**
4. Clique em "Deploy"
5. Aguarde 2-3 minutos

✅ **Problema resolvido?** Pronto! Às vezes é apenas um glitch.

---

#### 2. **Verificar os Logs**
1. Vá a https://railway.app
2. Clique no projeto
3. Selecione a aba **Logs**
4. Procure por:
   - `Error` — Erros de inicialização
   - `Exception` — Exceções Python
   - `Traceback` — Stack trace

**Se vir algo como:**
```
ModuleNotFoundError: No module named 'http.server'
```
→ Significa que o Procfile estava errado (já foi corrigido)

---

#### 3. **Verificar as Variáveis de Ambiente**
1. Vá a **Project Settings**
2. Procure por **Environment Variables**
3. Verifique se `PORT` está definido (Railway define automaticamente)

---

#### 4. **Health Check**
1. No Railway, vá a **Settings**
2. Procure por **Health Check**
3. Configure assim:
   ```
   Path: /
   Port: 8000 (ou valor do PORT)
   Timeout: 30 segundos
   ```

---

## 🟡 Erro 404 - Not Found

### Causa
Railway está servindo a página mas não encontra o ficheiro.

### Solução
1. Verifique se `index.html` está na **raiz** do repositório
2. Verifique que o nome do ficheiro é exatamente `index.html` (case-sensitive)
3. Teste localmente:
   ```bash
   python3 server.py
   # Depois aceda a http://localhost:8000
   ```

---

## 🟡 Erro 503 - Service Unavailable

### Causa
Servidor está down ou em manutenção.

### Solução
1. Aguarde 5 minutos
2. Tente novamente
3. Se persistir, redeploy (ver secção 502)

---

## ✅ Testar Localmente

### Antes de Fazer Deploy

```bash
# Clone o repositório
git clone https://github.com/geovasconcelos/hugo-leal-internet-search-api-homepage.git
cd hugo-leal-internet-search-api-homepage

# Inicie o servidor local
python3 server.py

# Abra no navegador
# http://localhost:8000
```

**Tudo funcionando?** ✅ Pronto para Railway.

---

## 🚀 Redeploy Rápido

Se nada funcionar, tente um redeploy limpo:

### Via Railway Dashboard
1. Vá a https://railway.app
2. Projeto → **Deployments**
3. Clique no último deploy
4. Clique em **Redeploy** (canto superior direito)

### Via Railway CLI
```bash
railway redeploy
```

---

## 🔍 Verificação de Health Check

Railway pode estar marcando a app como "unhealthy" e matando-a.

### Verificar
1. Vá a **Project Settings**
2. Procure por **Health Check**
3. Se estiver ativado, clique em **Edit**
4. Configure:
   - **Path:** `/`
   - **Port:** `8000`
   - **Timeout:** `30` segundos
   - **Initial Delay:** `10` segundos

---

## 📊 Monitorar Logs em Tempo Real

```bash
# Se tem Railway CLI instalada
railway logs --tail

# Mostra logs em tempo real conforme vão aparecendo
```

---

## 🐛 Debug Detalhado

### Ativar Debug Mode
Se precisar de mais informação, pode editar `server.py`:

```python
# Adicione no topo de server.py
import logging
logging.basicConfig(level=logging.DEBUG)
```

Depois redeploy.

---

## 💾 Verificar Ficheiros no Railway

Para confirmar que os ficheiros foram carregados corretamente:

1. Vá a **Project Settings**
2. Procure **Volumes** (se disponível)
3. Ou use SSH se estiver disponível

---

## 🆘 Se Nada Funcionar

### Contacte Railway Support
1. Aceda a https://railway.app
2. Clique no avatar (canto inferior esquerdo)
3. **Support** → **Open a Ticket**
4. Cole os logs e descreva o problema

### Informação útil para o ticket
- Request ID (aparece na página de erro)
- Logs completos (copie de Railway → Logs)
- Valor de `$PORT` no Procfile
- Versão do seu projeto (git commit)

---

## ✨ Checklist de Troubleshooting

- [ ] Tentou fazer redeploy?
- [ ] Verificou os logs no Railway?
- [ ] Testou localmente com `python3 server.py`?
- [ ] Confirma que `index.html` existe?
- [ ] Verificou variáveis de ambiente?
- [ ] Configurou health check corretamente?
- [ ] Esperou 2-3 minutos após deploy?

Se ainda não funcionar, temos um problema técnico mais profundo.

---

## 📞 Suporte

Para ajuda específica:
- **Documentação Railway:** https://docs.railway.app
- **HTTP Servers:** https://docs.railway.app/deploy/healthchecks
- **Node.js / Python:** https://docs.railway.app/guides/
- **This Project:** Consulte o `README.md` do repositório

---

**Última atualização:** 23 de Setembro de 2026
**Status:** Railway Server v2.0 (Melhorado)
