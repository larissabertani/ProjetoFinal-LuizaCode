
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
<a href="#gestao-do-usuario">Gestão do usuário</a> | <a href="#gestao-do-endereco-do-usuario">Gestão do endereço do usuário</a> | <a href="#gestao-dos-produtos">Gestão dos produtos</a> | <a href="#criando-um-carrinho-para-o-usuario">Criando um carrinho de compras para o usuário</a> | <a href="#formulando-pedido-fechado">Formulando um pedido fechado</a> 
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
Havendo uma nova tentativa de cadastro com um e-mail já utilizado, a API retornará o código HTTP 202 Accepted e a mensagem informará que este usuário já possui um cadastro:

```json
{
  "detail": "Já existe um cliente cadastrado com este e-mail!"
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
Em uma situação de exceção, a mensagem retornada informará o código HTTP 404 Not Found e a descrição: 

```json
{
  "detail": "Não há usuário com este email para ser deletado!"
}
```

<h3 id="gestao-do-endereco-do-usuario">Gestão do endereço do usuário</h3>

Após cadastrar um usuário, é possível acrescentar informações a ele, cadastrando também um endereço que futuramente poderá ser usado para a cobrança da compra ou para o recebimento do pedido.

O arquivo cases_test_address.http, neste caso é o que contempla os esboços das APIs.

No arquivo address.py, que está dentro da pasta "schemas", criamos classes relacionadas ao endereço, contedo as informações necessárias para criá-lo, atualizá-lo e para obtê-lo como resposta para outras etapas da aplicação, como por exemplo, no fechamento do pedido.

Já na pasta "rules", o arquivo address_rules.py abrigou as regras de negócio definida para o endereço e sua manipulação. A principal regra associada a um endereço é a de que ele precisa obrigatóriamente ser associado a um usuário existente, através do e-mail do usuário, para que possa ser criado no banco de dados.

Além da criação do endereço, este arquvio também estabelece as regras para que os endereços de um usuário possam ser consultados e/ou excluídos, utilizando o e-mail do usuário como o dado para realizar a busca dos endereços.

A pasta "models", contém um arquivo de nome address.py e ele exibe as funções de conexões com o banco de dados, para que as funções definidas no arquivo address_rules.py tenham efeito também no banco.

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

Se desejar consultar a lista dos endereços de um usuário já cadastrado no banco, será possível utilizar a requisição GET /api/address/<user_email>. O retorno deste endpoint será uma lista contendo os endereços relacionados ao usuário pesquisado.

```json
[
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
```
Entretanto, se o endereço de e-mail utilizado na URL não for encontrado no banco de dados, o retorno será o código HTTP 404 Not Found e a mensagem exibida é:

```json
{
  "detail": "Não há usuário cadastrado com este email!"
}
```
Havendo necessidade de exclusão de endereços que não pertencem mais ao usuário, por exemplo, caso ele tenha se mudado, o endpoint utilizado será o DELETE /api/address/<user_email>. Para confirmar a exclusão do endereço, o código HTTP 200 é retornado junto a mensagem:

```json
{
  "description": "Endereço deletado com sucesso!",
  "result": null
}
```
Em uma situação de exceção, o código será HTTP 404 Not Found e a mensagem retornada será: 

```json
{
  "detail": "Não há endereço para ser deletado para este usuário!"
}
```

<h3 id="gestao-dos-produtos">Gestão dos produtos</h3>

A área de gestão de produtos foi desenvolvida pensando na equipe administradora do LuPets Team, para disponibilizar os produtos que estarão a venda.

O primeiro passo foi criar na pasta "schemas" um arquivo product.py, contendo a classe do produto. Nela definimos que o nome do produto poderá ter no máximo 100 caracteres. Também incluímos no produto o animal ao qual o produto é dedicado e a categoria do produto para que seja possível disyinguir se ele é de alimentação, higiene ou brinquedo, por exemplo.

Neste arquivo também criamos outras classes para que seja possível realizar a atualização dos dados do produto e também obtê-lo como resposta para outras etapas da aplicação.

Já na pasta "rules", o arquivo product_rules.py abrigou as regras de negócio definida para o produto e sua manipulação. Há algumas regras associadas a criação do produto que são:

- Um produto deverá ter um código único;
- O preço de um produto deverá ser sempre superior a  R$ 0,01;
- Para que o produto seja cadastrado, o estoque dele deverá ser superior a 0.

Além da criação do produto, este arquvio também estabelece as regras para que os produtos possam ser consultados pelo código único ou pelo nome; para que eles possam ser atualizados ou retirados do site.

Na pasta "models", criamos o product.py que abriga as funções de conexões com o banco de dados, para que as funções definidas no arquivo produtc_rules.py tenham efeito também no banco.

Por fim, as rotas que permitem que as requisições sejam efetuadas ficam localizadas na pasta "controllers", no arquivo routes_products_async.py, assim como as demais.

##Instruções da Gestão dos produtos

Após garantir que a aplicação está preparada para rodar e com a conexão com o Mongo ativa, podemos iniciar o cadastro de um produto, usando a rota api/products/.

Para cadastrar um produto usamos o método POST /api/products. Ao finalizar o cadastro, o retorno obtido será com o código HTTP 201 Created, e no corpo de resposta haverá todos os dados do produto criado:

```json
{
  "description": "OK",
  "result": {
    "_id": "<_id>",
    "name": "<name>",
    "description": "<description>",
    "price": "<price>",
    "image": "<image>",
    "code": "<code>",
    "type_animal": "<type_animal>",
    "category": "<category>",
    "qt_stock": "<qt_stock>"
  }
}
```
Se desejar consultar os produtos pelo id, código ou nome, basta utilizar o método GET /api/products/ passando o código do item ou o nome do mesmo após o "products/".

Para buscar produtos pelo nome, caso o mesmo tenha espaços, por exemplo "Ração LuPets para cães Adultos", sugerimos o uso do "%20" para substituir os espaços: Ração%20LuPets%20para%20cães%20Adultos.

O retorno dos endpoints de consulta será com o código HTTP 200 e um json com os dados do item pesquisado:

```json
{
  "description": "OK",
  "result": {
    "_id": "<_id>",
    "name": "<name>",
    "description": "<description>",
    "price": "<price>",
    "image": "<image>",
    "code": "<code>",
    "type_animal": "<type_animal>",
    "category": "<category>",
    "qt_stock": "<qt_stock>"
  }
}
```
Entretanto, se o produto informado na URL não for encontrado no banco de dados, o retorno será o código HTTP 404 Not Found e a mensagem exibida é:

```json
{
  "detail": "Não existe produto com este código!"
}
ou
{
  "detail": "Não existe produto com este nome!"
}
```
Havendo necessidade de atualizar os dados do produto, como no caso de uma promoção ou alterações na descrição, será possível utilizando o método PUT /api/products/<product_code> junto aos novos dados do item. Ao finalizar a atualização, o código retornado é o HTTP 200 e a mensagem é:

```json
{
  "description": "Produto alterado com sucesso!",
  "result": null
}
```
Caso o código do produto não esteja informado corretamente na requisição, será retornado código HTTP 404 Not Found e a mensagem:

```json
{
  "detail": "Não existe produto com o código informado!"
}
```
Se o produto for descontinuado, o endpoint utilizado será o DELETE /api/products/<product_code>. Para confirmar a exclusão do item, o código HTTP 200 é retornado junto a mensagem:

```json
{
  "description": "Produto deletado com sucesso!",
  "result": null
}
```
Em uma situação de exceção, o código será HTTP 404 Not Found e a mensagem retornada será: 

```json
{
  "detail": "Não há produto com este código para ser deletado!"
}
```
Nesta etapa, o arquivo cases_test_product.http, foi o que contemplou os esboços das APIs.

<h3 id="criando-um-carrinho-para-o-usuario">Criando um carrinho de compras para o usuário</h3>

Retornando aos clientes LuPets, iniciamos os passos para a construção de um carrinho de compras que poderá ou não se tornar um pedido em nossa loja.

Para auxiliar com as requisições, temos também um arquivo que contém os esboços das API's: cases_test_cart.

As classes relacionadas ao carrinho ficaram registradas no arquivo cart.py, dentro da pasta "schemas". A classe criada para os produtos do carrinho, herdou a classe criada para produtos e a classe para a construção do carrinho, herdou a classe do usuário.

Há também outras classes para que seja possível obtê-lo como resposta para outras etapas da aplicação, como a finalização do pedido.

Em "rules", o arquivo cart_rules.py abrigou as regras para que um usuário tivesse um carrinho. Para iniciar, somente é possível ter um carrinho um usuário que já esteja cadastrado na loja e ele somente conseguirá ser criado se adcionarmos um produto que também já esteja no banco de dados.

Após a criação de um carrinho é possível adicionar novos produtos, retirar produtos, finalizá-lo para que ele se torne um pdido ou excluí-lo, no caso de haver desistência da compra.

Na pasta "models", criamos o cart.py que abriga as funções de conexões com o banco de dados, para que as funções definidas no arquivo cart_rules.py tenham efeito também no banco.

Por fim, as rotas que permitem que as requisições sejam efetuadas ficam localizadas na pasta "controllers", no arquivo routes_pcart_async.py, assim como as demais.

##Instruções para a criação do carrinho

Após garantir que a aplicação está preparada para rodar e com a conexão com o Mongo ativa, será necessário garantir alguns passos:

- Que ao menos um usuário esteja cadastrado na loja;
- Que o usuário cadastrado possua ao menos um endereço cadastrado;
- Que ao menos um produto esteja cadastrado na loja.

Para um carrinho usamos o método POST /api/cart/<user_id>/<product_code>. A inclusão de um produto é o que cria um carrinho de compras, o retorno obtido que garante que o carrinho está criado é com o código HTTP 201 Created, e no corpo de resposta os seguintes dados:

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
    "cart_items": [
      {
        "product": {
          "_id": "<_id>",
          "name": "<name>",
          "description": "<description>",
          "price": "<price>",
          "image": "<image>",
          "code": "<code>",
          "type_animal": "<type_animal>",
          "category": "<category>",
          "qt_stock": "<qt_stock>",
        },
        "qtd_product": "<qtd_product>"
      }
    ],
    "total_price": "<total_price>"
  }
}
```
Caso uma das condições para a criação do carrinho não seja satisfeita, haverá o erro HTTP 404 Not Found e as mensagens poderão ser:

```json
{
  "detail": "Não existe produto com este código!"
}
ou 
{
  "detail": "Não há usuário cadastrado com este id."
}
```
Se desejar um administrador da loja, desejar consultar o carrinho de um usuário, ele deverá utilizar o método GET /api/cart/<user_id>.

O retorno do endpoint de consulta será com o código HTTP 200 e um json com os dados do carrinho e do usuário, como ocorre na criação do carrinho.

Entretanto, se o usuário informado na URL não for encontrado no banco de dados, o retorno será o código HTTP 404 Not Found e a mensagem exibida é:

```json
{
  "detail": "Este id não possui carrinho aberto!"
}
```
Caso haja a desistência da compra de um produto, o usuário conseguirá removê-lo de seu carrinho. Para isso é executada a requisição DELETE /api/cart/<user_id>/<product_code>.Ao finalizar a remoção, o código retornado é o HTTP 200 OK. 

Se alguma das informações solicitadas não estiver correta, será retornado código HTTP 404 Not Found e a mensagem:

```json
{
  "detail": "Não existe produto com o código informado!"
}
```
Se o produto for descontinuado, o endpoint utilizado será o DELETE /api/products/<code>. Para confirmar a exclusão do item, o código HTTP 200 é retornado junto a mensagem:

```json
{
  "description": "Produto deletado com sucesso!",
  "result": null
}
```
Em uma situação de exceção, o código será HTTP 404 Not Found e a mensagem retornada será: 

```json
{
  "detail": "Não há produto com este código para ser deletado!"
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
  
