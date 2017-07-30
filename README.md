# Eventex

Sistema de eventos encomendado pela Morena

[![Build Status](https://travis-ci.org/rgrlinux/eventex.svg?branch=master)](https://travis-ci.org/rgrlinux/eventex)
[![Code Health](https://landscape.io/github/rgrlinux/eventex/master/landscape.svg?style=flat)](https://landscape.io/github/rgrlinux/eventex/master)


## Como Desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5.
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env.
6. Execute os testes.

```console
git clone git@github.com:rgrlinux/eventex.git wtdd
cd wtdd
python -m venv .wtdd
source .wtdd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test 
```

## Como fazer o deploy?

1. Crie uma instância no Heroku.
2. Envie as configurações para o Heroku.
3. Defina uma SECRET_KEY segura para a instância.
4. Defina DEBUG=False.
5. Configure o serviço de email.
6. Envie o código para o Heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configura email
git push heroku master --force

```

# To do