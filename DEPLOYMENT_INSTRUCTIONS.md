# 🚀 GUIA DE DEPLOYMENT - Internet Search API Homepage

## Opção 1: Deploy Automático via Dashboard Railway (RECOMENDADO)

### Passo 1: Aceder ao Railway Dashboard
1. Abra: **https://railway.app**
2. Faça login com a sua conta GitHub

### Passo 2: Ir ao Projeto
1. No dashboard, procure por: `hugo-leal-internet-search-api-homepage`
2. Clique para abrir o projeto

### Passo 3: Iniciar Deploy
1. Clique na aba **Deployments**
2. Veja o último deploy na lista
3. **Opção A:** Se houver um botão verde "Deploy", clique nele
4. **Opção B:** Se estiver um deploy com erro, clique em **Redeploy**

### Passo 4: Monitorar Deploy
1. Veja a barra de progresso
2. Espere 2-3 minutos
3. Status mudará para ✅ quando estiver pronto

### Passo 5: Aceder à Homepage
1. Após sucesso, verá uma URL pública gerada
2. Padrão: `https://hugo-leal-search-api-production.up.railway.app`
3. Copie e abra no navegador
4. 🎉 Homepage ao vivo!

---

## Opção 2: Deploy via Railway CLI (Para Developers)

### Pré-requisitos
```bash
npm install -g @railway/cli
```

### Passos

#### 1. Login no Railway
```bash
railway login
```
- Abre navegador automaticamente
- Autoriza a sua conta GitHub
- Retorna ao terminal após confirmação

#### 2. Navegar ao Repositório
```bash
cd hugo-leal-internet-search-api-homepage
```

#### 3. Conectar ao Projeto Railway
```bash
railway link
```
- Selecione o projeto: `hugo-leal-internet-search-api-homepage`
- Confirme a conexão

#### 4. Fazer Deploy
```bash
railway up
```
- Compila a aplicação
- Faz upload para Railway
- Inicia o servidor
- Mostra logs em tempo real

#### 5. Abrir no Navegador
```bash
railway open
```
- Abre automaticamente a URL pública

---

## Opção 3: Deploy via Git Push (Automático)

Railway pode estar configurado para fazer deploy automático quando faz push para o GitHub.

### Verificar Configuração
1. Railway Dashboard
2. Project Settings
3. Procure por "GitHub" ou "Integrations"
4. Se conectado, Railway faz deploy automaticamente

### Fazer Deploy Automático
```bash
git push origin main
```
- Railway detecta a mudança automaticamente
- Faz deploy em 2-3 minutos
- Vê o progresso no dashboard

---

## ✅ Checklist de Deploy

- [ ] Acedeu a https://railway.app
- [ ] Encontrou o projeto `hugo-leal-internet-search-api-homepage`
- [ ] Clicou em Deploy ou Redeploy
- [ ] Esperou 2-3 minutos
- [ ] Viu status ✅ (sucesso)
- [ ] Copiou a URL gerada
- [ ] Abriu a URL no navegador
- [ ] Viu a homepage profissional online 🎉

---

## 🎯 Resultado Esperado

Quando o deploy terminar com sucesso, verá:

```
┌─────────────────────────────────────────┐
│      Internet Search API Homepage       │
│                                         │
│  ✨ Header com navegação                │
│  🎨 Hero section com gradiente azul    │
│  📋 6 cards de capacidades              │
│  🏗️  Princípios de arquitetura          │
│  📊 Fluxo de serviço (8 passos)        │
│  💰 Valor entregue ao cliente          │
│  📞 Secção de contacto                  │
│  🔗 Footer com links                    │
│                                         │
│  Responsivo ✅ (mobile/tablet/desktop)  │
└─────────────────────────────────────────┘
```

---

## 🔴 Se der Erro na Deploy

### Erro 502 - Application Failed to Respond
**Solução:** Consulte `TROUBLESHOOTING.md`
- Verifique os logs no Railway
- Tente Redeploy
- Se persistir, execute os passos de debug

### Erro de Autenticação
**Solução:**
1. Faça logout: `railway logout`
2. Faça login novamente: `railway login`
3. Tente deploy novamente

### Erro: "Project not found"
**Solução:**
1. Verifique se o projeto existe em https://railway.app
2. Use `railway link` para conectar ao projeto correto

---

## 📊 Monitorar Deploy em Tempo Real

### Via Dashboard
1. Railway.app → Projeto
2. Aba **Logs**
3. Procure por linhas como:
   - `Server starting on http://0.0.0.0:8000`
   - `✅ Application ready`

### Via CLI
```bash
railway logs --tail
```
- Mostra logs em tempo real
- Pressione Ctrl+C para sair

---

## 🌐 URL Final

Após deploy bem-sucedido:

```
https://hugo-leal-search-api-production.up.railway.app
```

Esta URL:
- ✅ É pública na internet
- ✅ Pode ser partilhada
- ✅ Funciona em qualquer navegador
- ✅ É atualizada automaticamente com Git pushes (se configurado)

---

## 📋 Passos Rápidos (TL;DR)

```bash
# 1. Login
railway login

# 2. Ir ao diretório
cd hugo-leal-internet-search-api-homepage

# 3. Conectar ao projeto
railway link

# 4. Deploy
railway up

# 5. Abrir no navegador
railway open
```

**Tempo total:** ~5 minutos ⏱️

---

## ✨ Próximos Passos Após Deploy

### Imediatamente
1. ✅ Teste a homepage no navegador
2. ✅ Verifique responsividade (redimensione a janela)
3. ✅ Teste os links de navegação

### Curto Prazo
1. Considere configurar domínio personalizado
2. Configure email de contacto real no footer
3. Considere adicionar analytics (Google Analytics)

### Médio Prazo
1. Atualize a homepage com conteúdo específico
2. Considere adicionar blog ou documentação
3. Configure automatização de deploy contínua (CI/CD)

---

## 💡 Dicas

- **Redeploy rápido:** `railway redeploy` (sem recompilação completa)
- **Listar projetos:** `railway list`
- **Ver variáveis:** `railway vars`
- **Configurar ENV:** `railway vars set VAR_NAME=value`

---

## 🆘 Suporte

Se tiver problemas:
1. Consulte `TROUBLESHOOTING.md` (neste repositório)
2. Visite https://docs.railway.app
3. Contacte Railway Support: https://railway.app → Avatar → Support

---

**Status:** ✅ PRONTO PARA DEPLOY  
**Data:** 23 de Setembro de 2026  
**Versão:** 2.0

