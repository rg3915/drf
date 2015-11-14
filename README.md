# Django Rest Framework trainning and tests

Eu resolvi estudar um pouco mais de [DRF][0] depois do tutorial do [Hugo Brilhante][1] na [Python Brasil][2].

> **Obs**: se você não sabe Django sugiro que leia este [tutorial][4] antes.

Pra quem não sabe, para usar API Web usamos REST, no caso, [Django Rest Framework][0], framework web do [Django][3].

> **Nota:** este tutorial não é exatamente igual ao do Hugo, é baseado nele.

Então para criar a API, no meu caso, eu usei:

* Ambiente: venv
* Projeto: myproject
* App: core
* Model: Person
* Fields: first_name, last_name, email, active (boolean), created

![img](img/person.jpg)


## Configurando um novo ambiente

```bash
$ virtualenv venv # python 2, ou
$ # virtualenv -p python3 venv # python 3
$ source venv/bin/activate
$ git clone https://github.com/rg3915/drf.git
$ cd drf
$ pip install -r requirements.txt
```

Veja o requirements.txt

	Django==1.8.6
	django-filter==0.11.0
	djangorestframework==3.3.1
	drf-nested-routers==0.10.0

## Step-0 Projeto inicial

Abra o arquivo `settings.py` e em `INSTALLED_APPS` acrescente

```python
INSTALLED_APPS = (
	...
    'rest_framework',
    'core',
)
```

## Step-1 Serializer

### `models.py`: Criando o modelo `Person`

```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ['first_name']
        verbose_name = u'pessoa'
        verbose_name_plural = u'pessoas'

    def __str__(self):
        return self.first_name + " " + self.last_name

    full_name = property(__str__)
```



### `serializers.py`: Criando `PersonSerializer`

Precisamos proporcionar uma forma de [serialização][5] e desserialização das instâncias de `person` em uma representação JSON.

```bash
$ touch serializers.py
```

Edite

```python
from rest_framework import serializers
from core.models import Person

class PersonSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    active = serializers.BooleanField(default=True)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create and return a new `Person` instance, given the validated data.
        :param validated_data:
        """
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Person` instance, given the validated data.
        """

        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
```

A primeira parte da classe define os campos que serão serializados. Os métodos `create()` e `update()` criam e atualizam as instâncias, respectivamente, quando chamados.

Uma classe de serialização é similar a uma classe `Form` do Django, e inclui validações similares para os campos, tais como `required`, `max_length` e `default`.


### Fazendo a migração

```bash
$ ./manage.py makemigrations core
$ ./manage.py migrate
```

### Trabalhando com a serialização

Abra o `shell` do Django.

```bash
$ ./manage.py shell
```

Primeiro vamos criar uma pessoa.

```python
>>> from core.models import Person
>>> from core.serializers import PersonSerializer
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser

>>> person = Person(first_name='Regis', last_name='Santos',email='regis@email.com')
>>> person.save()
```

Agora que já temos alguns dados podemos ver a serialização da última instância.

```python
>>> serializer = PersonSerializer(person)
>>> serializer.data
# {'active': True, 'pk': 1, 'last_name': 'Santos', 'created': '2015-11-14T18:26:42.776285Z', 'first_name': 'Regis', 'email': 'regis@email.com'}
```

Neste ponto nós traduzimos a instância do modelo em tipos de dados nativos do Python. Para finalizar o processo de serialização nós vamos renderizar os dados em `json`.

```python
>>> content = JSONRenderer().render(serializer.data)
>>> content
# b'{"pk":1,"first_name":"Regis","last_name":"Santos","email":"regis@email.com","active":true,"created":"2015-11-14T18:26:42.776285Z"}'
```


A desserialização é similar.

```python
>>> from core.models import Person
>>> from core.serializers import PersonSerializer
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser
>>> from django.utils.six import BytesIO

>>> person = Person.objects.get(pk=1)
>>> serializer = PersonSerializer(person)
>>> content = JSONRenderer().render(serializer.data)
>>> stream = BytesIO(content)
>>> data = JSONParser().parse(stream)
>>> serializer = PersonSerializer(data=data)
>>> serializer.is_valid()
# True
>>> serializer.validated_data
# OrderedDict([('first_name', 'Regis'), ('last_name', 'Santos'), ('email', 'regis@email.com'), ('active', True), ('created', datetime.datetime(2015, 11, 14, 18, 26, 42, 776285, tzinfo=<UTC>))])
>>> serializer = PersonSerializer()
>>> print(repr(serializer))
# PersonSerializer():
#     pk = IntegerField(read_only=True)
#     first_name = CharField(max_length=30)
#     last_name = CharField(max_length=30)
#     email = EmailField()
#     active = BooleanField(default=True)
#     created = DateTimeField()
```

## Step-2 ModelSerializer
















## Instalando `httpie`

```bash
$ sudo pip install httpie
$ http http://127.0.0.1:8000/persons/
```








[0]: http://www.django-rest-framework.org/
[1]: https://github.com/hugobrilhante/drf-tutorial-pybr11
[2]: http://pythonbrasil.github.io/pythonbrasil11-site/
[3]: https://www.djangoproject.com/
[4]: http://pythonclub.com.br/tutorial-django-17.html
[5]: https://pt.wikipedia.org/wiki/Serializa%C3%A7%C3%A3o