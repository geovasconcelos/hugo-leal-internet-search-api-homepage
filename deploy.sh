#!/bin/bash

# Deploy Script for Internet Search API Homepage
# Use: bash deploy.sh

set -e

echo "🚀 Internet Search API Homepage - Deploy Script"
echo "==============================================="
echo ""

# Verificar se railway está instalado
if ! command -v railway &> /dev/null; then
    echo "❌ Railway CLI não está instalada."
    echo ""
    echo "📦 Para instalar:"
    echo "   npm install -g @railway/cli"
    echo ""
    echo "Depois execute este script novamente."
    exit 1
fi

echo "✅ Railway CLI detectada"
railway --version
echo ""

# Verificar se estamos no repositório correto
if [ ! -f "index.html" ]; then
    echo "❌ Erro: index.html não encontrado"
    echo "Certifique-se de que está no diretório do projeto"
    exit 1
fi

echo "✅ Ficheiros do projeto detectados"
echo ""

# Fazer login
echo "🔐 Fazendo login no Railway..."
railway login --browserless
echo "✅ Login realizado"
echo ""

# Link ao projeto
echo "🔗 Conectando ao projeto Railway..."
railway link
echo "✅ Projeto conectado"
echo ""

# Deploy
echo "🚀 Iniciando deploy..."
railway up
echo ""

echo "✅ Deploy concluído com sucesso!"
echo ""
echo "📍 Para ver o status do deploy:"
echo "   railway logs --tail"
echo ""
echo "🌐 Para abrir no navegador:"
echo "   railway open"
echo ""
