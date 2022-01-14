# Indentificador de Tokens 

### Introdução

Para resolver este problema, usamos a abordagem de filtrar cada palavra inserida e indentificar os tokens, para isso usamos expressões regulares.

### Autômato que marque a Linguagem

![automato](img/automato.jpeg)

### Primeiros Passos

Para esta primeira etapa vamos definir as nossas palavras reservadas, operadores relacionais, aritmeticos, atribuição e os delimitadores.

![palavras default](img/palavras.png)



### Indentificar lexemas validos e mostrar token

Nesta etapa foi criado esta função que tem objetivo de indentificar os nossos lexemas validos se o lexema é valido mostra o token caso o contrario não é exibido.

![function token](img/token.png)

# Teste

Nesta ultima etapa executamos um exemplo de teste para reconhecer uma palavra que esta atribuida a variavel script que em seguida passa por um processo de split para pegar cada item da palavra, depo identificado cada lexema e exibido os tokens, posteriormente exibida os ids das variaveis e por fim o tratamento das strings.

![teste](img/teste.png)

### Conclusão

O trabalho foi utilizou uma abordagem bem simples e o automato poderia ser otimizado para trabalhar em um cenario onde realmente objetivo fosse criar um analisador lexico onde o motor disso tudo seria uma maquina de turing e também usariamos orientação objetos para ter o processo de emcapsulamento onde teriamos alguns objetos definidos no construtor como cabeça, fita, numeros de linhas e palavras reservadas e para metodos algumas coisas como atualizador de estado, estado atual, avanacar estado e outros metodos que o problema fosse exigir, metodos para cada estado a maquina de turing e claro alguns tratamentos de erros que viria deste da leitura do arquivo de texto ao fim do classe. 
