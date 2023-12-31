<h1 align="center">📱 API de Empréstimo</h1>

## 📜 Descrição

Esta aplicação tem como objetivo simular a solicitação de empréstimo de clientes.

## 📚 Funcionalidades

- <b>Cadastro de clientes</b>:
  O administrador pode cadastrar novos clientes que estão interessados em realizar um empréstimo.

- <b>Gerenciamento de clientes</b>:
  O administrador pode gerenciar as informações dos clientes, sendo possível obter informações específicas de um cliente, atualizar as informações e deletar as informações.

- <b>Cadastro da conta bancária de um cliente</b>:
  O administrador pode cadastrar informações da conta bancária de um cliente e linkar ao perfil do mesmo.

- <b>Gerenciamento da conta bancária de um cliente</b>:
  O administrador pode gerenciar as informações da conta bancária de um cliente, sendo possível visualizar, atualizar e deletar essas informações.

- <b>Cadastro de cartões de crédito de um cliente</b>:
  O administrador pode cadastrar as informações de cartões de crédito de um cliente e linkar ao perfil do mesmo.

- <b>Gerenciamento de cartões de crédito de um cliente</b>:
  O administrador pode gerenciar as informações de cartões de crédito de um cliente, sendo possível visualizar, atualizar e deletar essas informações.

- <b>Cadastro de tabelas de taxa</b>:
  O administrador pode cadastrar novas tabelas de taxa.

- <b>Gerenciamento de tabelas de taxa</b>:
  O administrador pode gerenciar as informações as informações de uma tabela de taxa específica.

- <b>Cadastro das informações de parcelas de uma tabela de taxa</b>:
  O administrador pode cadastrar informações de parcelas de uma tabela de taxa, adicionando taxas de juros para cada parcela e a comissão.

- <b>Listagem das informações de parcelas de uma tabela de taxa</b>:
  Ao enviar o valor de interesse por query params, é simulado o valor total e o valor da parcela para cada parcela de uma tabela de taxa.

- <b>Gerenciamento das informações de parcelas de uma tabela de taxa</b>:
  O administrador pode gerenciar as informações de parcelas de uma tabela de taxa, sendo possível obter, atualizar e deletar essas informações.

- <b>Cadastro das informações de uma solicitação de empréstimo</b>:
  O administrador pode cadastrar informações de uma solicitação de empréstimo, adicionando todas as informações necessárias para um empréstimo, linkando com um cliente, com uma tabela de taxa e com um tipo de parcela.

- <b>Gerenciamento das informações de uma solicitação de empréstimo</b>:
  O administrador pode gerenciar as informações de uma solicitação de empréstimo, sendo possível obter, atualizar e deletar essas informações.

## 🛠 Tecnologias utilizadas

- Python;
- Django;
- Django Rest-Framework;
- Django Cors-Headers;
- Drf-Spetacular;
- Gunicorn;
- Pillow;
- Psycopg2-Binary;
- Python-Dotenv;
- Whitenoise;
- PostgreSQL;

## 💻 Rodando o projeto

<b>Observação</b>:
Para esse projeto foram utilizadas as versões 9.6.2 do node e 3.11.3 do python.

Url do deploy para testar no insomnia: https://loan-api-lrkm.onrender.com

Caso prefira clonar o repositório:

- Primeiramente é necessário clonar o repositório -> na página do repositório, há um botão azul escrito "code", ao clicar no mesmo irá mostrar um dropdown com as opções HTTPS, SSH, GitHub CLI. Escolha a opção SSH e copie o conteúdo. Após isso, abra um terminal, escreva git clone juntamente com o conteúdo copiado (como mostra na imagem abaixo);

<img src="/chave-ssh.png">

<img src="/terminal.png">

-Para abrir o projeto no vscode, abra o terminal no local aonde foi clonado o projeto e escreva:

```bash
code .
```

- Realizar a criação de um arquivo .env na raiz (copie o conteúdo do .env.example para o .env criado);
- Crie um banco de dados no postgres e configure as variáveis de ambiente no arquivo .env que estào relacionadas com as informações do banco de dados criado.
- Depois insira o seguinte comando no terminal ao iniciar o projeto para instalar todas as dependências necessárias:

1. Para criar um ambiente virtual:

```bash
python -m venv venv
```

2. Para ativar o ambiente virtual:

```bash
# Linux:
source venv/bin/activate

# Windows (Powershell):
.\venv\Scripts\activate

# Windows (Git Bash):
source venv/Scripts/activate
```

3. Com o ambiente virtual ativado, instale todas as ferramentas utilizadas nesse projeto:

```bash
pip install -r requirements.txt
```

4. Rode todas as migrações:

```bash
python manage.py makemigrations
```

5. Rode o servidor:

```bash
python manage.py runserver
```

## 📌 Endpoints:

## Client

<h2 align ='center'> Criação de cliente </h2>

`POST api/clients/ - FORMATO DA REQUISIÇÃO`

```json
{
  "name": "Felipe de Almeida Dias",
  "phone": "14997101478",
  "cpf": "12345678912"
}
```

Caso dê tudo certo, a resposta será assim:

```json
{
  "id": 1,
  "name": "Felipe de Almeida Dias",
  "cpf": "12345678912",
  "phone": "14997101478",
  "bank": null,
  "cards": []
}
```

<h2 align ='center'> Listar todos os clientes </h2>

`GET api/clients/ - FORMATO DA REQUISIÇÃO`

Sem corpo de requisição.

Caso dê tudo certo, a resposta será assim:

```json
[
  {
    "id": 1,
    "name": "Felipe de Almeida Dias",
    "cpf": "12345678912",
    "phone": "14997101478",
    "bank": {
      "id": 1,
      "bank_label": "001 – Banco do Brasil S.A.",
      "account_type_label": "savings account",
      "account_number": "378282246310005"
    },
    "cards": []
  }
]
```

<h2 align ='center'> Obter informações de um cliente </h2>

`GET api/clients/<str:cpf>/ - FORMATO DA REQUISIÇÃO`

Sem corpo de requisição.

Caso dê tudo certo, a resposta será assim:

```json
{
  "id": 1,
  "name": "Felipe de Almeida Dias",
  "cpf": "12345678912",
  "phone": "14997101478",
  "bank": {
    "id": 1,
    "bank_label": "001 – Banco do Brasil S.A.",
    "account_type_label": "savings account",
    "account_number": "378282246310005"
  },
  "cards": []
}
```

<h2 align ='center'> Atualizar informações de um cliente </h2>

`PATCH api/clients/<str:cpf>/ - FORMATO DA REQUISIÇÃO`

```json
{
  "name": "Felipe Dias"
}
```

Caso dê tudo certo, a resposta será assim:

```json
{
  "id": 1,
  "name": "Felipe Dias",
  "cpf": "12345678912",
  "phone": "14997101478",
  "bank": {
    "id": 1,
    "bank_label": "001 – Banco do Brasil S.A.",
    "account_type_label": "savings account",
    "account_number": "378282246310005"
  },
  "cards": []
}
```

<h2 align ='center'> Deletar informações de um cliente </h2>

`DELETE api/clients/<str:cpf>/ - FORMATO DA REQUISIÇÃO`

Sem corpo de requisição.

Sem corpo de resposta (status - 204)

## Account

<h2 align ='center'> Cadastro de conta bancária </h2>

`POST api/accounts/<str:cpf>/ - FORMATO DA REQUISIÇÃO`

```json
{
  "bank_label": "001 – Banco do Brasil S.A.",
  "account_type_label": "current account",
  "account_number": "378282246310005"
}
```

Obs: no campo "account_type_label" apenas é permitido os valores "current account" e "savings account"

Caso dê tudo certo, a resposta será assim:

```json
{
  "id": 1,
  "bank_label": "001 – Banco do Brasil S.A.",
  "account_type_label": "current account",
  "account_number": "378282246310005"
}
```

<h2 align ='center'> Obter informações de uma conta bancária </h2>

`GET api/account/<str:account_number>/ - FORMATO DA REQUISIÇÃO`

Sem corpo de requisição

Caso dê tudo certo, a resposta será assim:

```json
{
  "id": 1,
  "bank_label": "001 – Banco do Brasil S.A.",
  "account_type_label": "savings account",
  "account_number": "378282246310005"
}
```

<h2 align ='center'> Atualizar informações de uma conta bancária </h2>

`PATCH api/account/<str:account_number>/ - FORMATO DA REQUISIÇÃO`

```json
{
  "account_type_label": "savings account"
}
```

Caso dê tudo certo, a resposta será assim:

```json
{
  "id": 1,
  "bank_label": "001 – Banco do Brasil S.A.",
  "account_type_label": "savings account",
  "account_number": "378282246310005"
}
```

<h2 align ='center'> Deletar informações de uma conta bancária </h2>

`DELETE api/account/<str:account_number>/ - FORMATO DA REQUISIÇÃO`

Sem corpo de requisição.

Sem corpo de resposta (status - 204)

## Card

<h2 align ='center'> Cadastro de um cartão de crédito </h2>

`POST api/cards/client/<str:cpf>/ - FORMATO DA REQUISIÇÃO`

Obs: headers -> Multipart Form

<img src="/print-card-create.png">

Caso dê tudo certo, a resposta será assim:

```json
{
  "id": 1,
  "card_number": "1234567891234567",
  "expiration_date": "09/28",
  "cvv": "1234",
  "front_image": "http://127.0.0.1:8000/media/foto_5vYPgmK.jpg",
  "back_image": "http://127.0.0.1:8000/media/foto_Y2qTVWd.jpg",
  "selfie_image": "http://127.0.0.1:8000/media/foto_menot_qVUQrvk.jpg"
}
```

<h2 align ='center'> Listar todos os cartões de crédito de um cliente </h2>

`GET api/cards/client/<str:cpf>/ - FORMATO DA REQUISIÇÃO`

Sem corpo de requisição

Caso dê tudo certo, a resposta será assim:

```json
[
  {
    "id": 1,
    "card_number": "1234567891234567",
    "expiration_date": "09/28",
    "cvv": "1234",
    "front_image": "http://127.0.0.1:8000/media/foto_ZcjVi1x.jpg",
    "back_image": "http://127.0.0.1:8000/media/foto_LjuFTwt.jpg",
    "selfie_image": "http://127.0.0.1:8000/media/foto_menot_Q7am7Zf.jpg"
  }
]
```

<h2 align ='center'> Obter informações do cartão de crédito de um cliente </h2>

`GET api/cards/<str:card_number>/ - FORMATO DA REQUISIÇÃO`

Sem corpo de requisição

Caso dê tudo certo, a resposta será assim:

```json
{
  "id": 1,
  "card_number": "1234567891234567",
  "expiration_date": "09/28",
  "cvv": "1234",
  "front_image": "http://127.0.0.1:8000/media/foto_5vYPgmK.jpg",
  "back_image": "http://127.0.0.1:8000/media/foto_Y2qTVWd.jpg",
  "selfie_image": "http://127.0.0.1:8000/media/foto_menot_qVUQrvk.jpg"
}
```

<h2 align ='center'> Atualizar informações do cartão de crédito de um cliente </h2>

`PATCH api/cards/<str:card_number>/ - FORMATO DA REQUISIÇÃO`

```json
{
  "expiration_date": "09/29"
}
```

Caso dê tudo certo, a resposta será assim:

```json
{
  "id": 1,
  "card_number": "1234567891234567",
  "expiration_date": "09/29",
  "cvv": "1234",
  "front_image": "http://127.0.0.1:8000/media/foto_5vYPgmK.jpg",
  "back_image": "http://127.0.0.1:8000/media/foto_Y2qTVWd.jpg",
  "selfie_image": "http://127.0.0.1:8000/media/foto_menot_qVUQrvk.jpg"
}
```

<h2 align ='center'> Deletar informações do cartão de crédito de um cliente </h2>

`DELETE api/cards/<str:card_number>/ - FORMATO DA REQUISIÇÃO`

Sem corpo de requisição

Sem corpo de resposta (status - 204)

## RateTable

<h2 align ='center'> Cadastro de uma tabela de taxa </h2>

`POST api/rateTable/ - FORMATO DA REQUISIÇÃO`

```json
{
  "name": "Tabela Padrão"
}
```

Caso dê tudo certo, a resposta será assim:

```json
{
  "id": 1,
  "name": "Tabela Padrão",
  "installments": []
}
```

<h2 align ='center'> Listar todas as tabelas de taxa </h2>

`GET api/rateTable/ - FORMATO DA REQUISIÇÃO`

Sem corpo de requisição

Caso dê tudo certo, a resposta será assim:

```json
[
  {
    "id": 1,
    "name": "Tabela Padrão",
    "installments": []
  }
]
```

<h2 align ='center'> Obter informações de uma tabela de taxa </h2>

`GET api/rateTable/<int:pk>/ - FORMATO DA REQUISIÇÃO`

Sem corpo de requisição

Caso dê tudo certo, a resposta será assim:

```json
{
  "id": 1,
  "name": "Tabela Padrão",
  "installments": []
}
```

<h2 align ='center'> Atualizar informações de uma tabela de taxa </h2>

`PATCH api/rateTable/<int:pk>/ - FORMATO DA REQUISIÇÃO`

```json
{
  "name": "Tabela de Taxas A"
}
```

Caso dê tudo certo, a resposta será assim:

```json
{
  "id": 1,
  "name": "Tabela de Taxas A",
  "installments": []
}
```

<h2 align ='center'> Deletar informações de uma tabela de taxa </h2>

`DELETE api/rateTable/<int:pk>/ - FORMATO DA REQUISIÇÃO`

Sem corpo de requisição

Sem corpo de resposta (status - 204)

## Installment

<h2 align ='center'> Cadastro das informações de parcelas de uma tabela de taxa </h2>

`POST api/installment/table/<int:pk>/ - FORMATO DA REQUISIÇÃO`

```json
{
  "installment_number": 1,
  "installment_interest": 5,
  "comission": 1.22
}
```

Caso dê tudo certo, a resposta será assim:

```json
{
  "id": 1,
  "installment_number": 1,
  "installment_interest": 5,
  "comission": 1.22
}
```

<h2 align ='center'> Obter informações de uma parcela de uma tabela de taxa </h2>

`GET api/installment/retrieve/<int:pk>/ - FORMATO DA REQUISIÇÃO`

Sem corpo de requisição

<b>Observação</b>: para obter valores dinâmicos do valor da parcela e do valor total, é necessário enviar como query params o value, tendo como valor o valor de interesse do empréstimo.

Exemplo:
`http://127.0.0.1:8000/api/installment/retrieve/1/?value=1000`

Caso dê tudo certo, a resposta será assim:

```json
{
  "id": 1,
  "installment_number": 1,
  "installment_interest": 5,
  "comission": 1.22,
  "installment_value": 1050.0,
  "full_value": 1050.0
}
```

<h2 align ='center'> Atualizar informações de uma parcela de uma tabela de taxa </h2>

`PATCH api/installment/update/<int:pk>/ - FORMATO DA REQUISIÇÃO`

```json
{
  "comission": 1.3
}
```

Caso dê tudo certo, a resposta será assim:

```json
{
  "id": 1,
  "installment_number": 1,
  "installment_interest": 5,
  "comission": 1.3
}
```

<h2 align ='center'> Deletar informações de uma parcela de uma tabela de taxa </h2>

`DELETE api/installment/delete/<int:pk>/ - FORMATO DA REQUISIÇÃO`

Sem corpo de requisição

Sem corpo de resposta (status - 204)

## Solicitation

<h2 align ='center'> Cadastro das informações do empréstimo em uma solicitação </h2>

`POST api/solicitations/ - FORMATO DA REQUISIÇÃO`

<b>Observação:</b> como no front-end a solicitação vai sendo realizada em várias etapas, todos os campos dessa tabela são opcionais.

Assim como, o campo "contract_type" apenas aceita os valores "automatic" e "manual", havendo como default o valor "automatic"

```json
{
  "desired_value": 7000
}
```

Caso dê tudo certo, a resposta será assim:

```json
{
  "id": 1,
  "installment_interest": null,
  "installment_interest_value": null,
  "comission": null,
  "comission_value": null,
  "installment_value": null,
  "card_number": null,
  "desired_value": 7000.0,
  "total_loan": null,
  "contract_type": "automatic",
  "client": null,
  "installment": null,
  "rate_table": null
}
```

<h2 align ='center'> Listar todas as solicitações cadastradas </h2>

`GET api/solicitations/ - FORMATO DA REQUISIÇÃO`

Sem corpo de requisição

Caso dê tudo certo, a resposta será assim:

```json
[
  {
    "id": 1,
    "installment_interest": null,
    "installment_interest_value": null,
    "comission": 1.22,
    "comission_value": null,
    "installment_value": null,
    "card_number": null,
    "desired_value": 7000.0,
    "total_loan": null,
    "contract_type": "automatic",
    "client": null,
    "installment": null,
    "rate_table": null
  }
]
```

<h2 align ='center'> Obter as informações de uma solicitação </h2>

`GET api/solicitation/<int:pk>/ - FORMATO DA REQUISIÇÃO`

Sem corpo de requisição

Caso dê tudo certo, a resposta será assim:

```json
{
  "id": 1,
  "installment_interest": null,
  "installment_interest_value": null,
  "comission": 1.22,
  "comission_value": null,
  "installment_value": null,
  "card_number": null,
  "desired_value": 7000.0,
  "total_loan": null,
  "contract_type": "automatic",
  "client": null,
  "installment": null,
  "rate_table": null
}
```

<h2 align ='center'> Atualizar as informações de uma solicitação </h2>

`PATCH api/solicitation/<int:pk>/ - FORMATO DA REQUISIÇÃO`

```json
{
  "comission": 1.22
}
```

Caso dê tudo certo, a resposta será assim:

```json
{
  "id": 1,
  "installment_interest": null,
  "installment_interest_value": null,
  "comission": 1.22,
  "comission_value": null,
  "installment_value": null,
  "card_number": null,
  "desired_value": 7000.0,
  "total_loan": null,
  "contract_type": "automatic",
  "client": null,
  "installment": null,
  "rate_table": null
}
```

<h2 align ='center'> Deletar as informações de uma solicitação </h2>

`DELETE api/solicitation/<int:pk>/ - FORMATO DA REQUISIÇÃO`

Sem corpo de requisição

Sem corpo de resposta (status - 204)
