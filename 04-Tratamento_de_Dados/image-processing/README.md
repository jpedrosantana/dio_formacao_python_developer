# image_processing_package

### Description

Repositório usado como explicação nas aulas de **Criando um Pacote de Processamento de Imagens com Python** pela Formação Python Developer oferecida pela Digital Innovation One e ministrado pela Karina Tiemi;

O fork desse repositório tem como propósito a utilização do exemplo usado em aula para fazer a publicação do pacote no Test  Pypi e Pypi, o desenvolvimento do código foi inteiramente feito pela Karina.

### Comandos para publicar no Test Pypi

- Criar uma conta em https://test.pypi.org/account/register/

- Executar o comando abaixo

```bash
python -m twine upload --repository-url https://test.pypi.org/legacy/dist*
```

- Após publicação, no Test Pypi será possível copiar a url para instalação do pacote, ou rode o comando abaixo:

```bash
pip install –-index-url https://test.pypi.org/simple/ image-processing
```

- Os passos no Pypi são os mesmos acima, o link para registro é o https://pypi.org/account/register/

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install package_name

```bash
pip install package_name
```

## Usage

```python
from package_name.module1_name import file1_name
file1_name.my_function()
```

## Author

Karina Tiemi

## License

[MIT](https://choosealicense.com/licenses/mit/)
