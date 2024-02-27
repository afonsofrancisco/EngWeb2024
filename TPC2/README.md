# Construir páginas estáticas em HTML com base num ficheiro .JSON

## Objetivo:
1. Construir uma página individual para cada uma das cidades, através de um script em Python.
2. Construir a página índice através do node que hiperliga cada uma das ruas à sua página.

## Resolução:

Cada rua tem uma página `hmtl`. Para cada uma das página temos as seguintes informações:

- Nome da cidade e o seu número.
- Informações acerca da cidade, como o distrito, a sua população e uma breve descrição através das chaves **distrito**, **população** e **descrição**, respetivamente.
- Ligações a outras cidades, dentro da secção **ligações** do ficheiro json. Onde temos o id da ligação, a cidade origem e destino assim como a sua distância. Para cada cidade que percorria no código, percorre todas as entradas das ligações e filtrar apenas as que têm como origem a respetiva cidade.
- Hiperligação para voltar para o índice inicial.


Para o índice foi nos dito para utilizarmos o node. Desse modo, criamos um servidor em JavaScript que gere todo o tráfego e redirecionamento das páginas. Foi feito do seguinte modo:

- Em primeiro lugar, verificamos se estamos página índice, ou seja `/`. Se sim, então iremos, através do comando **axios**, buscar informação ao json dado, relativo às cidades: `axios.get("http://localhost:3000/cidades")`. Em seguida, iteramos sobre todas as cidades e vamos escrevendo na tela código em html sobre cada cidade, no caso indicamos o seu nome e criamos uma **anchor tag** para que ao clicar na hiperigação redirecione para a sua respetiva página. Cada página individual de uma cidade é acessada através do url indicando o seu id, por exemplo para aceder à cidade 1, teriamos de indicar `/c1`.
- Se não estivermos na página índice, então verificamos a parte final do url, se terminar em `c[número]` então tentamos ler através de `fs.readFile(fileName, (err, file)` o input dado. Se existir, carregamos o html da cidade, caso contrário aparecerá uma mensagem de erro no terminal.
- Se nenhum dos casos descritos acima se verificar, então escrevemos uma mensagem de erro no terminal.

### Rodar o programa
Para rodar o programa faça em terminais diferentes:

1. `json-server --watch mapa-virtual.json`
2. `node server.js`

Fazendo isso, irá aparecer no output do terminal **2.**, a seguinte mensagem:

`Servidor à escuta em http://localhost:2602/`

Onde poderá abrir o link e iniciar a navegação pelas várias cidades.