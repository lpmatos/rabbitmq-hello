# RabbitMQ

RabbitMQ é um servidor de mensageria de código aberto (open source) desenvolvido em Erlang, implementado para suportar mensagens em um protocolo denominado Advanced Message Queuing Protocol (AMQP). Ele possibilita lidar com o tráfego de mensagens de forma rápida e confiável, além de ser compatível com diversas linguagens de programação. Possuir interface de administração nativa e pode ser multiplataforma.

## Conceitos

### Mensagem

Uma mensagem é dividida em duas partes:

* Payload - é o corpo com os dados que serão transmitidos. Suporta vários tipos de dados como um array JSON até um filme MPEG.
* Label - é responsável pela descrição do payload e também como o RabbitMQ saberá quem irá receberá a mensagem.

### Fila

Onde as mensagens ficam e são retiradas pelos consumers.

### Publisher

Responsável por incluir cada nova mensagem na fila, ou seja, enviar a mensagem.

### Consumer

Como diz o próprio nome é o agente responsável por consumir, retirar, a informação da fila.

## Características

### Persistência

As mensagens no RabbitMQ por padrão ficam armazenadas na memória, isso nos garante uma velocidade muito boa para armazená-las e consumi-las. O lado ruim disso é que se o servidor do RabbitMQ for reiniciado as mensagens serão apagadas e as vezes dependendo da mensagem não podemos deixar isso acontecer. Então é possível dizer para o RabbitMQ persistir as mensagens gravando elas no disco, isso garante que mesmo que o servidor reinicie as mensagens não sejam apagadas. O lado ruim de persistir essas informações em disco é que causa impacto no servidor. Cabe a você tomar a melhor decisão.

### Durabilidade

Quando falamos de durabilidade no RabbitMQ o conceito é bastante semelhante da persistência das mensagens. Só que dessa vez estamos falando das Filas e das Exchanges. Nós podemos definir que elas sejam duráveis fazendo com que caso o servidor seja reiniciado elas não sejam apagadas.

Aviso importante: Caso você não possa perder as mensagem dentro do RabbitMQ você precisar definir ela como persistente e as filas como duráveis. Não adianta nada só dizer que a mensagem é persistente se a fila for apagada.

### Acknowledge

No RabbitMQ temos o conceito do acknowledge, basicamente é dizer que uma mensagem pode ser apagada da fila depois dela ter sido consumida. Este conceito na minha opinião é um dos mais importantes, porque com ele caso acontecesse algum erro durante o consumo da mensagem podemos fazer com que a mensagem volta para fila de forma automática.

### Auto delete

Outro conceito muito interessante que devemos prestar atenção é o do auto-delete, com ele podemos fazer que com as filas sejam apagadas assim que não houver mais consumidores ligadas a ela. Este recurso é muito utilizado quando usamos o pattern como o RPC (Remote procedure call).
