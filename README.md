
<h1 id="capa">Projeto final - 5ª edição LuizaCode</h1>

##Carrinho de compras - Petshop

<h3 id="índice">Índice</h3>

* [Capa](#capa)
* [Índice](#índice)
* [Descrição do Projeto](#descrição-do-projeto)
* [Pessoas Desenvolvedoras do Projeto](#pessoas-desenvolvedoras)
* [Como rodar o projeto?](#como-rodar-o-projeto)
* [Apresentação das atividades](#apresentação-das-atividades)
* [Tecnologias utilizadas](#tecnologias-utilizadas)
* [Pessoas Contribuidoras](#pessoas-contribuidoras)
* [Conclusão](#conclusão)

<h3 id="descrição-do-projeto">Descrição do projeto</h3>
<br/>
<p>Este projeto teve como objetivo o desenvolvimento de um carrinho de compras voltado ao mercado Pet utilizando o <a href="https://fastapi.tiangolo.com/">FastAPI</a> e o <a href="https://www.mongodb.com/">MongoDB</a>, tecnologias trabalhadas durante o bootcamp.</p>

<h3 id="pessoas-desenvolvedoras">Pessoas Desenvolvedoras do Projeto:</h3>

<p>Ana Vitória <br/>
Camila Reis <br/>
Larissa <br/>
Maisa Pacheco <br/>
Siomara Murta</p>

<h3 id="como-rodar-o-projeto">Como rodar o projeto?:</h3>
<br/>
<p> • Crie um ambiente virtual, digitando no terminal da pasta do projeto o seguinte comando: 

    $ python -m venv venv

• Ative o ambiente virtual, digitando no terminal: 

```
- Linux
$ source venv/bin/activate

- Windows
$ venv\Scripts\activate
```
• Após ativar o ambiente virtual, faça a instalação dos seguintes requerimentos com o comando: 

```
$ pip install -r requirements.txt
```
• Faça a conexão com o MongoDB, criando um arquivo .env e informando a sua string de conexão, conforme o exemplo do arquivo .env.example.

• As libs que serão utilizadas serão:
```
$ motor = Driver Python async for MongoDB
$ pydantic = Data validation for Python
```
• Para rodar a aplicação local, utilize o comando:
```
$ uvicorn main:app --reload
```
 
<h2>!!!! Depois verificar se precisamos atualizar com informações do Docker e do Heroku.</h2>

<br/>

<h3 id="apresentação-das-atividades">Apresentação das atividades:</h3>

<p>O projeto foi divido nas seguintes etapas:
<br/>

<p>
<a href="#gestao-do-usuario">Gestão do usuário</a> | <a href="#gestao-do-endereco-do-usuario">Gestão do endereço do usuário</a> | <a href="#criando-um-carrinho-para-o-usuario">Criando um carrinho de compras para o usuário</a> | <a href="#acrescentando-produtos-no-carrinho">Acrescentando produtos ao carrinho do usuário</a> | <a href="#formulando-pedido-fechado">Formulando um pedido fechado</a> 
</p>

<p>E o desenvolvimeno da aplicação nas seguintes pastas:

- src: Pasta principal da aplicação.
<br/>
     - models: Módulo para persistência (repositório) com o banco de dados.<br/>
     - rules: Módulos para as regras (casos de uso) da aplicação.<br/>
     - controllers: Módulos para de controle e/ou comunicação com o FastAPI.</p>

<h3 id="gestao-do-usuario">Gestão do usuário</h3>

Utilizando o arquivo cases_test_user.http, localizado na pasta endpoints criamos os esboços das APIs que foi empregado exclusivamente nos testes da etapa de gestão do usuário.

Para que fosse possível executar as rotas existentes, usamos a extensão Rest Client do Visual Code.









          













<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
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
  
