from core.models import Person
from core.serializers import CoreSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO

person = Person.objects.get(pk=1)
serializer = CoreSerializer(person)
content = JSONRenderer().render(serializer.data)
stream = BytesIO(content)
data = JSONParser().parse(stream)
serializer = CoreSerializer(data=data)
# passando a instancia 'person' ele chama o método update
# CoreSerializer(person, data=data)
serializer.is_valid()
serializer.validated_data
serializer = CoreSerializer()
print(repr(serializer))
