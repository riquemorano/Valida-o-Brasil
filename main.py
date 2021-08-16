from telefone import Telefone
from cpf_cnpj import Documento
from cep import Cep
import requests
from data import Data

cep = "04351110"
cpf_henrique = Documento.cria_documento("46731494836")
cnpj_henrique = Documento.cria_documento("29251604000192")
telefone_henrique = Telefone("5511968287833")
cep_henrique = Cep(cep)

henrique = {"CPF": cpf_henrique.__str__() , "CNPJ": cnpj_henrique.__str__(), "Telefone": telefone_henrique.__str__(), "Cep": cep_henrique.__str__()}

#print(henrique)

bairro, cidade, uf = cep_henrique.acessaAPI()

print(bairro, cidade, uf)






