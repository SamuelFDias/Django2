import re
from validate_docbr import CPF

def nome_valido(nome):
    return nome.isalpha()

def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)

def rg_valido(numero_rg):
    return len(numero_rg) == 9 and numero_rg.isdigit()

def celular_valido(numero_celular):
    """Verifica se o celular é válido (11 91234-5678)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    reposta = re.findall(modelo, numero_celular)
    return reposta