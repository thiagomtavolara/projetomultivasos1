Regador Dashboard
=================
Este dashboard é como um regador: todas as plantas precisam.

O repositório apresenta um dashboard base em Dash para ser seguido em outros dashboards desenvolvidos pelo grupo.

## Configurando o projeto
A melhor maneira de se criar e manter o projeto é a partir de um ambiente virtual Python, onde os requisitos são instalados e iguais para todos. Para fazer isso, siga os passos abaixo:
 
### Windows
1. Clone o repositório para uma pasta local.
2. Baixe e instale o Python em https://www.python.org/. Lembre-se de marcar a opção "adicionar caminho" na instalação.
3. Teste o Python executando `python` na janela de comando.
4. Instale o ambiente virtual: `pip install virtualenv`
5. Entre no diretório do projeto: `cd [PASTA DO PROJETO]`
6. Crie um ambiente virtual: `virtualenv --python [PASTA DE INSTALAÇÃO DO PYTHON]\python.exe venv`
7. Ative o ambiente virtual: `.\venv\Scripts\activate`
8. Instale os requisitos: `pip install -r requirements_dash.txt`

### Mac/Linux
1. Clone o repositório para uma pasta local.
2. Baixe e instale o Python em https://www.python.org/. Lembre-se de marcar a opção "adicionar caminho" na instalação.
3. Teste o Python executando `python3 --version` no terminal.
4. Instale o ambiente virtual: `pip install virtualenv`
5. Entre no diretório do projeto: `cd [PASTA DO PROJETO]`
6. Crie um ambiente virtual: `python3 -m venv venv`
7. Ative o ambiente virtual:`source venv/bin/activate`
8. Instale os requisitos: `pip install -r requirements_dash.txt`

## Abrir o dashboard
Para abrir o dashboard, execute o comando `python app.py` na pasta raiz do repositório. Este comando executa um servidor Dash, que deve estar em execução para usar o painel. 


## Modificar o dashboar
O dashboard foi construído para ser modular e permitir que novas páginas e cards (seções dentro de uma página) sejam adicionadas de forma isolada.

As especificações do dashboard são:

- Baseado em Dash
- Use a biblioteca Dash Bootstrap Components para simplificar e padronizar o layout
- Layouts separados em páginas
- Seções em páginas separadas como cards bootstrap

A pasta do painel está estruturada da seguinte maneira:

- assets - contém os arquivos de estilo (CSS) e as figuras
- pages - contém um arquivo para cada página do dashboard
- utils - contém todas as outras funções que fazem parte do painel, como gráficos e metodologias

Se você quiser contribuir para o dashboard, certifique-se de entender um pouco de como funciona o Bootstrap e siga o modelo usado no projeto. Especialmente, mantenha todas as visualizações dentro dos cartões Bootstrap.


## Atualizar o repositório Git
A melhor forma de manter os códigos é utilizando o Git. Para isso, gere um novo repositório dentro da organização GIMSCOP e siga os passos para fazer o upload.

## Atualizar arquivo requirements.txt
Sempre que uma nova biblioteca for instalada no ambiente virtual, é importante que o arquivo requirements seja atualizado. Dessa forma, outros usuários do dashboard também irão instalar a mesma versão da bibliteca.

Para atualizar o arquivo requirements.txt basta rodar o comando:

`pip freeze > requirements.txt`