# Projeto Registo de Cliques

## Visão Geral
Uma aplicação web simples para registar cliques em botões com carimbo de data/hora e contador sequencial diário.

## Estrutura do Projeto
- `src/app.py`: Backend Flask com integração PostgreSQL (SQLAlchemy).
- `src/templates/index.html`: Frontend HTML/JS.

## Tech Stack
- **Backend**: Python 3.11, Flask, Flask-SQLAlchemy
- **Base de Dados**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript

## Desenvolvimento
- O servidor corre no porto 5000.
- A base de dados é inicializada automaticamente ao iniciar o `app.py`.

## Requisitos do Enunciado
- 4 botões identificados.
- Contador sequencial diário (reinicia a cada novo dia).
- Registo de data e hora (HH:mm).
- Persistência em base de dados.
