import datetime
import dbm

post1 = {"codigo": "ID-9987725",
        "prod_name": "Geladeira",
        "marcas": ["brastemp", "consul", "eletrolux"],
        "data_cadastro": datetime.datetime.utcnow()}

type(post1)
print(type(post1))

collection = db.posts



