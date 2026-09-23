# Internet Search API - Homepage

Homepage profissional e responsiva para o serviço de **Internet Search API** — uma solução de busca de informação gerenciada.

## 📋 Sobre

Esta é uma página web moderna que apresenta:

- ✨ **Design responsivo** — funciona perfeitamente em desktop, tablet e mobile
- 🎨 **Visual profissional** — paleta de cores consistente com gradientes modernos
- ⚡ **Performance** — HTML/CSS puro, sem dependências externas
- 🔍 **SEO-friendly** — metadados apropriados e estrutura semântica
- 📱 **Mobile-first** — otimizado para dispositivos móveis

## 🚀 Quickstart Local

### Requisitos
- Python 3.7+

### Executar Localmente

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/internet-search-api-homepage.git
cd internet-search-api-homepage

# Inicie o servidor web local
python -m http.server 8000

# Abra no navegador
# http://localhost:8000
```

## 🌐 Deploy no Railway

### Passo 1: Preparar o Repositório Git

```bash
# Inicialize git (se não feito)
git init
git add .
git commit -m "Initial commit: Internet Search API homepage"
```

### Passo 2: Criar Repositório no GitHub

1. Aceda a [github.com/new](https://github.com/new)
2. **Opção A (Com seu nome):** Crie um repositório chamado `hugo-leal-internet-search-api-homepage`
   - URL fica: `https://github.com/seu-usuario/hugo-leal-internet-search-api-homepage`
3. **Opção B (Simples):** Crie um repositório chamado `internet-search-api-homepage`
4. Siga as instruções para fazer push do repositório local

```bash
# Para Opção A (com seu nome):
git remote add origin https://github.com/seu-usuario/hugo-leal-internet-search-api-homepage.git

# Para Opção B (simples):
git remote add origin https://github.com/seu-usuario/internet-search-api-homepage.git

git branch -M main
git push -u origin main
```

### Passo 3: Deploy no Railway

1. **Aceda a [railway.app](https://railway.app)**
2. **Crie uma Nova Conta** (ou faça login)
3. **Crie um Novo Projeto**
   - Clique em "Create New Project"
   - Selecione "GitHub Repo"
4. **Conecte o GitHub**
   - Autorize o Railway a aceder aos seus repositórios
   - Selecione `internet-search-api-homepage`
5. **Configure o Deploy**
   - Railway detectará automaticamente que é uma aplicação estática
   - Clique em "Deploy"
6. **Aceda à Sua Homepage**
   - Após alguns segundos, Railway fornecerá um URL público
   - Ex: `https://internet-search-api-homepage.up.railway.app`

### Passo 4: Personalizar Nome/URL no Railway

O Railway gera URLs automáticas. Para incluir o seu nome:

#### Opção A: Renomear o Serviço no Railway (Recomendado)
1. No dashboard do Railway, clique no seu projeto
2. Clique na aba **Service** ou **Settings**
3. Procure o campo "Service Name"
4. Altere para algo como: `hugo-leal-search-api` ou `hugo-leal-homepage`
5. Salve as alterações
6. A URL será atualizada para incluir o novo nome

#### Opção B: Configurar Domínio Personalizado

Se deseja usar o seu próprio domínio (ex: `hugoleal.dev`):

1. No dashboard do Railway, vá para **Project Settings**
2. Navegue até **Networking** ou **Domains**
3. Configure o seu domínio personalizado
4. Atualize os registos DNS na sua registadora (normalmente CNAME)

#### Exemplos de URLs Finais

- **Railway automática:** `https://internet-search-api-homepage-production.up.railway.app`
- **Com nome personalizado:** `https://hugo-leal-search-api-production.up.railway.app`
- **Com domínio próprio:** `https://hugoleal.dev`

## 📁 Estrutura do Projeto

```
internet-search-api-homepage/
├── index.html          # Homepage (ficheiro principal)
├── package.json        # Metadados do projeto
├── Procfile           # Configuração para Railway
├── README.md          # Este ficheiro
└── .gitignore         # Ficheiros a ignorar no git
```

## 🎨 Personalização

Para adaptar a homepage:

### Alterar Cores
No topo do `<style>` em `index.html`, modifique as variáveis CSS:

```css
:root {
    --primary: #2563eb;        /* Cor principal */
    --primary-dark: #1e40af;   /* Cor principal escura */
    --secondary: #10b981;      /* Cor secundária */
    --text-dark: #1f2937;      /* Texto escuro */
    /* ... outras cores */
}
```

### Alterar Conteúdo
- Edite os textos directamente no HTML
- Modifique o email de contacto na secção CTA (procure `mailto:contacto@example.com`)
- Atualize links nas secções de navegação

### Adicionar Seções
Copie a estrutura de qualquer `<section>` e adapte o conteúdo.

## 🔗 Links Úteis

- 📚 [Documentação Railway](https://docs.railway.app)
- 🐙 [GitHub Pages](https://pages.github.com) — Alternativa gratuita
- 🎨 [Tailwind CSS](https://tailwindcss.com) — Para estender os estilos
- 📱 [Responsive Design](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design)

## 📋 Checklist de Deploy

- [ ] Repositório criado no GitHub
- [ ] Ficheiros iniciais committed
- [ ] Conta Railway criada
- [ ] Repositório conectado ao Railway
- [ ] Deploy realizado com sucesso
- [ ] URL pública acessível
- [ ] Domínio personalizado configurado (opcional)
- [ ] Email de contacto atualizado
- [ ] Links de navegação testados

## 🔒 Segurança

- Este projeto contém apenas HTML/CSS estático
- Não há dados sensíveis ou segredos
- Todos os links mailto apontam para contacto@example.com — **atualize para o seu email**

## 📄 Licença

MIT License — Sinta-se livre para reutilizar e adaptar

## 💬 Suporte

Para dúvidas sobre Railway ou GitHub, consulte a documentação oficial destes serviços.

---

**Criado para Internet Search API © 2024**
