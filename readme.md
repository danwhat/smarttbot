## Sobre o projeto
 
Já pensou em guardar informações das criptomoedas de seu interesse e fazer consultas de histórico de preço sem precisar acessar serviços de terceiros? É justamente para isso que essa incrível aplicação foi criada.

Após a aplicação ser inicializada é só esperar:
- A cada minuto um novo candle será adicionado ao banco de dados com as informações de preço em dólar do **Bitcoin** e **Monero**.
- A cada 5 e 10 minutos outro candle será gerado utilizando como base as informações dos candles de 1 minuto gerados anteriormente.

## Tecnologias utilizadas

- A aplicação foi construída inteiramente em **Python**.
- Para persistência de dados foi utilizado **MySql**.
- Para conteinerização foi utilizado **Docker** com **Docker-compose**.

## Getting Started

Basta entrar na pasta do repositório e digitar o comando `docker-compose up`. Todas as dependências do programa serão baixadas e em seguida aparecerá a mensagem **"Iniciando aplicação"**.

Para consumir os dados gerados, utilize o programa de consulta de sua preferência (como mysql workbench ), através do banco de dados `smarttbot` no endereço `localhost:5001` com user e senha `root`.

## Dificuldades e Próximo Passos

Eu tenho menos familiaridade com Python do que achei que teria. Por isso precisei parar diversas vezes para entender "como tal coisa é feita em python". Isso me tomou um tempo precioso no fluxo de desenvolvimento, além de atrapalhar a aplicar algumas boas práticas como conceitos de SOLID e testes, afinal, era quase tudo novo para mim e eu estava aprendendo enquanto *codava*.

**Software funcionando é a medida primária de progresso.**

Seguindo esse principio, eu tenho orgulho do que consegui fazer em pouco tempo com uma linguagem que conhecia muito pouco. Mas enxergo muita coisa errada no meu código tanto na parte técnica quanto na estrutura do projeto. Por isso o próximo passo  seria **refatoração**.

Estudaria padrões de projeto em python e refatoraria o código presando pelo baixo acoplamento entre a partes. Isso facilitaria manutenções futuras e a implementação de testes unitários.

Além disso, uma coisa que me incomodou muito foi o uso de requests. Estudaria um pouco mais e implementaria socket, pois faz muito mais sentido que uma requisição por segundo para pegar as informações atualizadas.

## Conclusões finais

A qualidade da entrega não esta nem próxima do que eu planejava. Mas reforço que precisei aprender na hora quase tudo que foi implementado. Eu gosto muito de estudar e aprender com  pessoas mais experientes e por isso garanto entregar mais valor caso tenha alguém com experiência para me aconselhar por onde eu devo seguir e o que eu devo estudar.