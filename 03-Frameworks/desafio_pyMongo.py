import datetime
import pprint
import pymongo as pyM

#Trocar <password> pela sua senha
client = pyM.MongoClient("mongodb+srv://pymongo:<password>@cluster0.gpsohw0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.test

collection = db.test_collection
print(db.list_collection)

post = [{
    "id": "001",
    "nome": "João",
    "cpf": "12345678910",
    "endereco": "R. Teste, 456",
    "contas": [{
        "id": "001",
        "tipo": "corrente",
        "agencia": "314",
        "num": "456789",
        "id_cliente": "001",
        "saldo": 630.98
    }, {
        "id": "002",
        "tipo": "salario",
        "agencia": "216",
        "num": "654321",
        "id_cliente": "001",
        "saldo": 2935.45
    }]
},{
    "id": "002",
    "nome": "Ana",
    "cpf": "9876543210",
    "endereco": "Avenida ABC, 20",
    "contas": [{
        "id": "003",
        "tipo": "poupança",
        "agencia": "314",
        "num": "456789",
        "id_cliente": "002",
        "saldo": 300.65
    }, {
        "id": "004",
        "tipo": "salario",
        "agencia": "216",
        "num": "985236",
        "id_cliente": "002",
        "saldo": 1205.63
    }]
}]

#Submetendo as informações
posts = db.posts
result = posts.insert_many(post)
print(posts.inserted_ids)

#Recuperação de registros
print("\nRecuperando registros de João")
pprint.pprint(db.posts.find_one({"id": "001"}))

print("\nTodos os registros presentes na coleção")
for post in posts.find():
    pprint.pprint(post)

print("\nBusca de todas as contas:")
for post in posts.find({}):
    pprint.pprint(post['contas'])


client.drop_database('test')
print(db.list_collection_names())

