import pandas as pd
from faker import Faker

faker = Faker('pt-BR')

dados_pessoas = []

for _ in range(100):
    pessoa = {
        'nome': faker.name(),
        'cpf': faker.cpf(),
        'email': faker.email(),
        'endereco': faker.address(),
        'data_nascimento': faker.date_of_birth(minimum_age=18, maximum_age=80),
        'idade': faker.random_int(min=18, max=80),
        'telefone': faker.phone_number(),
        'salario': faker.random_int(min=1000, max=10000),
        'avaliacao': faker.random_int(min=1, max=5),
        'vendas': faker.random_int(min=10, max=500),
    }
    dados_pessoas.append(pessoa)

df = pd.DataFrame(dados_pessoas)

print(df.to_string())  # mostra só as primeiras linhas

df.to_csv('pessoa_faker.csv', index=False, encoding='utf-8')
