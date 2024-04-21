from rest_framework import serializers
from .models import *
class studentseriali(serializers.ModelSerializer):
    class Meta:
        model = Student
        fiedls = '__all__'