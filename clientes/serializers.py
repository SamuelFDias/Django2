from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        """Validando campos da API"""
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': 'Não inclua números nesse campo.'})
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': 'Número de CPF inválido.'})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': 'O rg deve ter 9 digítos.'})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': 'O número de celular seguir esse modelo: 11 12345-1234.'})
        return data