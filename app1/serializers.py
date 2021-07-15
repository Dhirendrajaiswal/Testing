import datetime

from rest_framework import serializers

from .models import *

class EmployeeTableSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = EmployeeTable
        fields = ('empid', 'empfirstname', 'emplastname','empdob','status')