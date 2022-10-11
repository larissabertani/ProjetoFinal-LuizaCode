
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

<p>Ana Vitória Luz<br/>
Camila Reis <br/>
Larissa Bertani<br/>
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
<a href="#gestao-do-usuario">Gestão do usuário</a> | <a href="#gestao-do-endereco-do-usuario">Gestão do endereço do usuário</a> | <a href="#criando-um-carrinho-para-o-usuario">Criando um carrinho de compras para o usuário</a> | <a href="#formulando-pedido-fechado">Formulando um pedido fechado</a> 
</p>

<p>E o desenvolvimeno da aplicação foi realizado dentro das seguintes pastas:

- src: Pasta principal da aplicação.
<br/>
  - models: Módulo para persistência (repositório) com o banco de dados.<br/>
  - rules: Módulos para as regras (casos de uso) da aplicação.<br/>
  - controllers: Módulos para de controle e/ou comunicação com o FastAPI.</p>

<h3 id="gestao-do-usuario">Gestão do usuário</h3>

Utilizando o arquivo cases_test_user.http, criamos os esboços das APIs que foram empregados exclusivamente nos testes da etapa de gestão do usuário.

Para que fosse possível executar as rotas existentes, usamos a extensão Rest Client do Visual Code.

No arquivo user.py, que está dentro da pasta "schemas", criamos classes relacionadas ao usuário, contedo as informações necessárias para criá-lo, atualizá-lo e para obtê-lo como resposta para outras etapas da aplicação.

Já na pasta "rules", o arquivo user_rules.py abrigou as regras de negócio definida para o cadastro do usuário. Desta maneira, apenas é possível cadastrar um usuário por endereço de e-mail. Este arquivo também contém as funções para que seja possível obter uma lista de usuários, consultar um usuário por seu user_id e por seu user_email, atualizar os dados de um usuário e por fim excluí-lo do banco.

Na função de exclusão do usuário entendemos que ao retirar um cliente do sistema, os dados relacionados a ele, como o endereço, por exemplo, deveriam ser também excluídos.

Para o usuário que deseja se descadastrar, caso haja uma pedido que ainda não esteja finalizado, ele também será excluído, ou seja, um carrinho de compras que esteja aberto também é excluído junto ao seu dono.

Entretanto, pedidos já finalizados devem permanecer sem alteração  para que seja possível acompanhar o detalhamento das vendas realizadas.

A pasta "models", contém também um arquivo de nome user.py e ele contém as conexões com o banco de dados, para que as funções definidas no arquivo user_rules.py tenham efeito também no banco.

Por fim, as rotas que permitem que as requisições sejam efetuadas ficam localizadas na pasta "controllers", no arquivo routes_user_async.py.

##Instruções da Gestão do usuário

Com a aplicação preparada para rodar e com a conexão com o Mongo ativa, iniciamos o cadastro de um novo usuário, usando a rota api/users/.

Para criar um novo usuário usamos o método POST /api/users/, se conseguirmos criar um usuário no banco de dados, o retorno será com o código HTTP 201 Created, e no corpo de resposta haverá todos os dados do usuário criado:

```json
{
  {
  "description": "OK",
  "result": {
     "_id": "<_id>",
     "name": "<name>",
     "email": "<email>",
     "password": "<password>",
     "is_active": "<is_active",
     "is_admin": "<is_admin>"
  }
}
}
```
Havendo uma nova tentativa de cadastro com um e-mail já utilizado, a API retornará o código HTTP 201, mas a mensagem informará que não foi possível prosseguir:

```json
{
  "description": "Já existe um cliente cadastrado com este e-mail!",
  "result": null
}
```
Se desejar obter uma lista dos usuários já cadastrados no banco, será possível utilizar a requisição GET /api/users/ e se for preciso buscar um usuário no qual o e-mail é conhecido, basta utilizar o método GET /api/users/<user_email>. O retorno de ambos os endpoints é semelhante, pois devolvem o código HTTP 200 e um json com o resultado, que deverá conter uma lista de usuários ou um dicionário com os dados do usuário buscado, conforme o caso.

No momento de descadastrar um usuário, a requisição deverá ser realizada utilizando o método DELETE /api/users/<user_email>. Com o processo de exclusão finalizado, o código retornado é o HTTP 200 e a mensagem:

```json
{
  "description": "Usuário deletado com sucesso!",
  "result": null
}
```
Em uma situação de exceção, a mensagem retornada será: 

```json
{
  "description": "Não há usuário com este email para ser deletado!",
  "result": null
}
```

<h3 id="gestao-do-endereco-do-usuario">Gestão do endereço do usuário</h3>

Após cadastrar um usuário, é possível incrementar informações a ele, cadastrando também um endereço  que futuramente poderá ser usado para a cobrança da compra ou para o recebimento do pedido.

O arquivo cases_test_address.http, neste caso é o que contempla os esboços das APIs.

No arquivo address.py, que está dentro da pasta "schemas", criamos classes relacionadas ao endereço, contedo as informações necessárias para criá-lo, atualizá-lo e para obtê-lo como resposta para outras etapas da aplicação, como por exemplo, o fechamento do pedido.

Já na pasta "rules", o arquivo address_rules.py abrigou as regras de negócio definida para o endereço e sua manipulação. A principal regra associada a um endereço é a de que ele precisa ser associado a um usuário existente, através do e-mail dele, para que possa ser criado.

Além da criação do endereço, este arquvio também estabelece as rgras para que os endereços de um usuário possam ser consultados e/ou excluídos, utilizando o e-mail do usuário como o campo para a busca dos dados.

A pasta "models", contém também um arquivo de nome address.py e ele contém as conexões com o banco de dados, para que as funções definidas no arquivo address_rules.py tenham efeito também no banco.

Por fim, as rotas que permitem que as requisições sejam efetuadas ficam localizadas na pasta "controllers", no arquivo routes_addredd_async.py, assim como as de gestão do usuário.

##Instruções da Gestão do endereço do usuário

Com a aplicação preparada para rodar e com a conexão com o Mongo ativa podemos iniciar o cadastro de um endereço, após informar o e-mail de um usuário já cadastrado na aplicação. A rota que deverá ser usada é api/address/.

Para associar um endereço a um novo usuário usamos o método POST /api/address/<user_email>. Ao finalizar o cadastro, o retorno obtido será com o código HTTP 201 Created, e no corpo de resposta haverá todos os dados do usuário criado e a sua lista de endereços:


```json
{
  "description": "OK",
  "result": {
    "user": {
      "_id": "<_id>",
     "name": "<name>",
     "email": "<email>",
     "password": "<password>",
     "is_active": "<is_active",
     "is_admin": "<is_admin>"
    },
    "addresses": [
      {
        "street": "<street>",
        "number": "<number",
        "zipcode": "<zipcode",
        "district": "district",
        "city": "<city",
        "state": "<state",
        "is_delivery": "is_delivery"
      }
    ]
  }
}
```

Se desejar consultar a lista dos endereços de um usuário já cadastrados no banco, será possível utilizar a requisição GET /api/address/<user_email>. O retorno de ambos os endpoints é semelhante, pois devolvem o código HTTP 200 e um json com o resultado, que deverá conter uma lista de usuários ou um dicionário com os dados do usuário buscado, conforme o caso.

No momento de descadastrar um usuário, a requisição deverá ser realizada utilizando o método DELETE /api/users/<user_email>. Com o processo de exclusão finalizado, o código retornado é o HTTP 200 e a mensagem:

```json
{
  "description": "Usuário deletado com sucesso!",
  "result": null
}
```
Em uma situação de exceção, a mensagem retornada será: 

```json
{
  "description": "Não há usuário com este email para ser deletado!",
  "result": null
}
```





          













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
  
