# Construção de Páginas Estáticas em HTML

## Objetivo:
1. Construir uma página inicial que liste todos os nomes das ruas, com links para páginas específicas de cada rua.
2. Criar páginas individuais para cada rua, contendo informações detalhadas sobre a rua e um link para retornar à página de índice.

## Resolução:

### Página de Índice Inicial:
- Utilizando a biblioteca `os` do Python, foram obtidos os nomes dos arquivos `.xml` que representam as ruas existentes.
- A lista de ruas foi ordenada para apresentação.
- Cada rua possui um hyperlink para sua página HTML correspondente, gerado por um *script* Python.

### Páginas Individuais das Ruas:
- O parse de cada arquivo `.xml` foi realizado com as bibliotecas `xmltodict` e `BeautifulSoup`.
- As informações de cada rua, como nome, número, e detalhes, foram extraídas das tags relevantes.
- As casas foram listadas com detalhes específicos através da tag `lista-casas`.
- As imagens antigas foram incorporadas usando a tag `figura`, com os caminhos de arquivo apropriados.
- Imagens atuais das ruas, embora não incluídas nos `.xml`, foram acessadas a partir da pasta atual e vinculadas às respectivas ruas.
- Um link de retorno à página inicial foi incluído em cada página.

## Notas Importantes:
- O código é geral e funciona para ruas com estrutura correta
- Na página 58, as imagens antigas podem não carregar devido a um problema de formatação no nome do arquivo `.xml`.
- Para o código funcionar a pasta do material base deve estar dentro da parta `TPC1`.
