from rest_framework import serializers
from jobs.models import Joboffer

class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joboffer
        fields = '__all__'
        
    def validate(self, data):
        if Joboffer.objects.filter(company_name__contains='PUB').count() > 3:
            raise serializers.ValidationError('Hai inserito troppo inserzioni')
        return data
    
    def validate_salary(self, value):
        if value < 0:
            raise serializers.ValidationError('Il salario non può essere negativo')
        return value
        