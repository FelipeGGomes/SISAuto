#!/usr/bin/env bash
# Sair em caso de erro
set -o errexit

echo "Instalando dependências..."
pip install -r requirements.txt

echo "Coletando arquivos estáticos..."
python manage.py collectstatic --no-input

echo "Aplicando migrações no banco de dados (Supabase)..."
python manage.py migrate

echo "Criando Superusuário (se não existir)..."
if [[ -n "${DJANGO_SUPERUSER_USERNAME}" ]] && [[ -n "${DJANGO_SUPERUSER_PASSWORD}" ]]; then
    python manage.py createsuperuser --noinput || true
    echo "Superusuário verificado/criado com sucesso!"
fi