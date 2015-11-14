from rest_framework import serializers
from core.models import Person


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('pk', 'first_name', 'last_name',
                  'email', 'active', 'created')
