from rest_framework import serializers
from .models import *
class JobsSerialiser(serializers.ModelSerializer):
    class Meta:
        model=WebCompanyJobs
        fields="__all__"