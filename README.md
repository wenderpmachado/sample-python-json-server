# Exemplo de [requisições](http://docs.python-requests.org/en/master/) python ao [json-server](https://github.com/typicode/json-server)

## Pré-requisito

- Ter instalado o node.js
- Ter instalado o curl
- Ter instalado o python

## Instalação

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip install pipenv
pipenv install
python -m pip install -U autopep8 --user
npm install -g json-server
```

## Execução

Em um `primeiro` terminal, levante a API:

```
json-server --watch db.json
```

Em um `segundo` terminal, execute o programa:

```
python requisicao.py
```

## Acesso API

[http:/localhost:3000]()