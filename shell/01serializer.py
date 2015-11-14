from core.models import Person
from core.serializers import CoreSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

person = Person(first_name='Regis', last_name='Santos',
                email='regis@email.com')
person.save()

serializer = CoreSerializer(person)
serializer.data

content = JSONRenderer().render(serializer.data)
content
