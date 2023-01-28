# Estoque
Controle de estoque com Django, inclui fluxo de caixa completo com estoque, e importação/exportação de planilha de registros.

## Como rodar o projeto:

* Clone este repositório.
* Crie uma virtualenv com python 3.
* Ative a virtualEnv.
* Instale as dependencias.
* Rode as migrações.

```
git clone git@github.com:ryaMarks/ControleEstoque.git
python -m venv venv
sorce venv/bin/activate
pip install -r requeriments.txt
python contrib/env_gen.py
python manage.py migrate
```


### Links de consulta:


* [python-decouple](https://github.com/henriquebastos/python-decouple)
* [deploy no PythonAnywhere](https://tutorial.djangogirls.org/pt/deploy/)
* [Carregando arquivos estaticos no deploy](https://pt.stackoverflow.com/questions/262043/problemas-carregar-static-files-no-django-em-deploy-no-heroku)