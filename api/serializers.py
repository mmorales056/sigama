from rest_framework import serializers
from api.models import Contacts

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model= Contacts
        fields= (
            'name',
            'email',
            'state',
            'city'
        )

