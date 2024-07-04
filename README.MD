## API cards

Este projeto implementa uma API para cadastro e consulta de números de cartão utilizando Django e Django REST Framework.

### Tecnologias Utilizadas

Django

Django REST Framework

### Pré-requisitos
Python 3.12.3

### Instalação das Dependências
crie o ambiente virtual: ```python -m venv venv```

Ative o ambiente virtual: ```venv\Scripts\activate```

Instale as dependências do projeto com o seguinte comando:

pip install -r requirements.txt

### Aplicação das Migrações

A aplicação está usando db.sqlite3 então não é necessário instalar o banco de dados.


Execute o seguinte comando para aplicar as migrações e criar as tabelas no banco de dados:

python manage.py migrate
### Funcionalidades

A API possui as seguintes funcionalidades:

Cadastro de cartão
Consulta de cartão

### Endpoints
Acesse o swagger para melhor visualização dos endpoints

api/cards/create/ - Cria um novo cartão
api/cards/list - Lista todos os cartões cadastrados
api/cards/detail/{number}/ - Detalha um cartão específico
api/cards/upload - Importa um arquivo txt com números de cartão

api/users/register - Registra um novo usuário
api/users/login - Realiza o login de um usuário
api/users/refreshtoken - Atualiza o token de um usuário