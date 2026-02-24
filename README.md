# 🚗 SISAuto - Sistema de Controle de Acesso Veicular SUDEMA

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

Um sistema moderno, rápido e responsivo desenvolvido em Django para o gerenciamento seguro de acesso de veículos, utilizando validação em tempo real via QR Code dinâmico.

## 📌 Visão Geral

O **SISAuto** foi projetado para modernizar e substituir controles manuais de estacionamento. O sistema permite o cadastro ágil de servidores, visitantes e seus respectivos veículos, gerando instantaneamente um QR Code único e criptografado. 

Esse QR Code serve como uma credencial digital. Ao ser escaneado pela equipe de portaria ou segurança, o sistema consulta o banco de dados em tempo real e retorna o status de acesso (Liberado/Bloqueado), exibindo as informações do veículo e do condutor.

## 🚀 Principais Funcionalidades

- **Cadastro Integrado:** Formulário intuitivo para registro de dados pessoais (Nome, CPF, Setor) e do veículo (Placa, Modelo).
- **Validação Inteligente no Frontend:** Máscaras automáticas (JavaScript) para CPF e Telefone, melhorando a experiência do usuário.
- **Segurança Anti-Duplicidade:** O backend em PostgreSQL bloqueia automaticamente tentativas de cadastro com CPFs ou placas já existentes no pátio.
- **Geração de QR Code em Memória:** Geração instantânea do QR Code em Base64 nativamente pelo Python. Nenhuma imagem física é salva, economizando armazenamento e garantindo alta performance.
- **Validação Anti-Fraude:** Os links gerados no QR Code utilizam `UUIDs` (Identificadores Únicos Universais) em vez de IDs sequenciais, impossibilitando a adivinhação de URLs por terceiros.
- **Interface Responsiva e Neutra:** Frontend desenhado com Bootstrap 5, garantindo perfeita visualização em monitores da portaria ou nas telas de celulares.

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python 3, Django 5+
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla), Bootstrap 5, Bootstrap Icons
- **Banco de Dados:** PostgreSQL (Configurável para SQLite local)
- **Bibliotecas Auxiliares:** `qrcode[pil]` (Geração de códigos), `Pillow` (Processamento de imagens)

## ⚙️ Como executar o projeto localmente

### Pré-requisitos
Certifique-se de ter o [Python](https://www.python.org/) e o [Git](https://git-scm.com/) instalados em sua máquina.

### Passo a passo

1. **Clone este repositório:**
```bash
git clone [https://github.com/FelipeGomes/sisauto.git](https://github.com/FelipeGomes/sisauto.git)

```
2. **Acesse a pasta do projeto:**
```bash
cd sisauto
```

3. **Crie e ative um ambiente virtual:**
```bash
# Windows:
python -m venv venv
venv\Scripts\activate

# Linux/macOS:
python3 -m venv venv
source venv/bin/activate
```

4. **Crie e ative um ambiente virtual:**
```bash
pip install -r requirements.txt
```

5. **Realize as migrações do banco de dados:**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Crie um superusuário (Administrador):**
```bash
python manage.py createsuperuser
```

7. **Inicie o servidor local:**
```bash
python manage.py runserver
```

8. **Acesse no seu navegador:**
```bash
📝 Tela de Cadastro: http://127.0.0.1:8000/cadastrar_cliente/

⚙️ Painel Administrativo: http://127.0.0.1:8000/admin/
```
