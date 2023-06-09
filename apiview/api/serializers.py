from rest_framework import serializers
from .models import Data
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('id','name','roll','city')

        