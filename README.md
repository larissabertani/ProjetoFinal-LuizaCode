
<h1 id="capa">Projeto final - 5ª edição LuizaCode</h1>

<h2 id="subtitulo">Carrinho de compras - Petshop</h2>

<h3 id="índice">Índice</h3>

* [Capa](#capa)
* [Subtítulo](#subtitulo)
* [Índice](#índice)
* [Pessoas Desenvolvedoras do Projeto](#pessoas-desenvolvedoras)
* [Descrição do Projeto](#descrição-do-projeto)
* [Status do Projeto](#status-do-Projeto)
* [Funcionalidades e Demonstração da Aplicação](#funcionalidades-e-demonstração-da-aplicação)
* [Acesso ao Projeto](#acesso-ao-projeto)
* [Tecnologias utilizadas](#tecnologias-utilizadas)
* [Pessoas Contribuidoras](#pessoas-contribuidoras)
* [Licença](#licença)
* [Conclusão](#conclusão)

<h3 id="descrição-do-projeto">Descrição do projeto</h3>
<br/>
<p>Este projeto teve como objetivo o desenvolvimento de um carrinho de compras voltado ao mercado Pet utilizando o [FastAPI](https://fastapi.tiangolo.com/)
e o [MongoDB](https://www.mongodb.com/), tecnologias trabalhadas durante o bootcamp.</p>
<br/>
<h3 id="pessoas-desenvolvedoras">Pessoas Desenvolvedoras do Projeto:</h3>

<h5>Ana Vitória</h5>
<h5>Camila Reis</h5>
<h5>Larissa</h5>
<h5>Maisa Pacheco</h5>
<h5>Siomara Murta</h5>

<br/>















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
  
