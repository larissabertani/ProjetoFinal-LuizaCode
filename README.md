<h1>Projeto final - 5ª edição LuizaCode</h1>

<h3>Carrinho de compras - Petshop</h3>


<h5>Grupo 9:</h5>
<h6>Ana Vitória</h6>
<h6>Camila Reis</h6>
<h6>Larissa</h6>
<h6>Maisa Pacheco</h6>
<h6>Siomara Murta</h6>


* [Título e Imagem de capa](#Título-e-Imagem-de-capa) 
* [Badges](#badges)
* [Índice](#índice)
* [Descrição do Projeto](#descrição-do-projeto)
* [Status do Projeto](#status-do-Projeto)
* [Funcionalidades e Demonstração da Aplicação](#funcionalidades-e-demonstração-da-aplicação)
* [Acesso ao Projeto](#acesso-ao-projeto)
* [Tecnologias utilizadas](#tecnologias-utilizadas)
* [Pessoas Contribuidoras](#pessoas-contribuidoras)
* [Pessoas Desenvolvedoras do Projeto](#pessoas-desenvolvedoras)
* [Licença](#licença)
* [Conclusão](#conclusão)

Este projeto teve como objetivo o desenvolvimento de um carrinho de compras voltado ao mercado Pet utilizando o [FastAPI](https://fastapi.tiangolo.com/)
e o [MongoDB](https://www.mongodb.com/), tecnologias trabalhadas durante o bootcamp.


## Título e Imagem de capa






















Eu pensei de fazer pelas etapas:
- Fazer uma apresentação geralzona do projeto;
- Falar sobre o que precisa fazer pro projeto rodar;
- Separar cada partezinha do projeto e falar o que faz cada parte.

Aí no último item, ia separar pelo cadastro de usuários, cadastro de endereço do usuário;
Montagem do pedido, carrinho de compras aberto e carrinho fechado;
Cadastro de produtos no sistema e a manipulação desses produtos 

Isso meio que pra separar o que vai ser de acesso ao usuário final e o que é o acesso admin de controle da empresa

# shopping-cart
MongoDB database integration for LuizaCode's shopping-cart project

## libs
* motor = Driver Python async for MongoDB
* pydantic = Data validation for Python 

## Install
* Create venv
    ```
    At the terminal in the project's folder 
    $ python -m venv venv
    ```
    Linux
    ```
    $ source venv/bin/activate
   ```
   Windows
    ```
    $ .\venv\Scripts\activate
   ```
   After the the inserted command, it should appear the virtual environment name
* Install requirements
     ```
     $ pip install -r requirements.txt
     ```
* Connect mongodb
  
     ```´

     $ create a .env file with your mongoDB connect string according to .env.example file 
     ```
     
  
     | name_env | value |
     |------------|------------|
     |DATABASE_URI|connection string Atlas|
          

* Run
  ```
  $ uvicorn main:app 
   ```

* How to test
  ```
  Open the cases test files and test the routes
  Tip: you can install the "Rest Client" extension in the Visual Studio Code to run tests in the *.http files directly
     ```
  
