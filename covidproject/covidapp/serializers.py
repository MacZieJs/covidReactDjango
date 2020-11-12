from rest_framework import serializers
from covidapp.models import Register

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'

