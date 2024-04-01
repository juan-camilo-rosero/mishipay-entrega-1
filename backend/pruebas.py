from models.data_structures import Cola
transaccion = [
  {
    "sender_email": "a@gmail.com",
    "reciever_email": "b@gmail.com",
    "sender_name": "Andrés",
    "reciever_name": "Bernando",
    "amount": 160000
  },
  {
    "sender_email": "d@gmail.com",
    "reciever_email": "c@gmail.com",
    "sender_name": "string",
    "reciever_name": "string",
    "amount": 30000
  },
  {
    "sender_email": "c@gmail.com",
    "reciever_email": "d@gmail.com",
    "sender_name": "string",
    "reciever_name": "string",
    "amount": 543
  }
]

users = [
  {
    "email": "a@gmail.com",
    "tel": 300000000,
    "name": "Andrés",
    "money": 140000,
    "transactions": [
      "660766787555ec0289befcab"
    ]
  },
  {
    "email": "b@gmail.com",
    "tel": 310000000,
    "name": "Bernando",
    "money": 160000,
    "transactions": [
      "660766787555ec0289befcab"
    ]
  },
  {
    "email": "c@gmail.com",
    "tel": 0,
    "name": "string",
    "money": 29457,
    "transactions": [
      "660779c090970440b0df6c86",
      "6609df51f3dee30c8daedbc7"
    ]
  },
  {
    "email": "d@gmail.com",
    "tel": 0,
    "name": "string",
    "money": 770543,
    "transactions": [
      "660779c090970440b0df6c86",
      "6609df51f3dee30c8daedbc7"
    ]
  },
  {
    "email": "e@gmail.com",
    "tel": 3002856214,
    "name": "Esteban",
    "money": 360000,
    "transactions": []
  }
]

def find_dict_by_value(dicts, key, value):
    for d in dicts:
        if key in d and d[key] == value:
            return d
    return None

def variastransaccion(transacciones):
    cola = Cola()
    resultado = []
    for i in transacciones:
        cola.insertar(i)
    for j in range(len(transacciones)):
        actual = cola.obteneruno().valor  # Acceder al atributo 'valor' de Nodo
        sender = actual["sender_email"]  # Acceder al valor de sender_email en el diccionario actual
        receiver = actual["reciever_email"]  # Acceder al valor de receiver_email en el diccionario actual
        a = find_dict_by_value(users, "email", sender)
        b = find_dict_by_value(users, "email", receiver)
        if a["money"] < actual["amount"]:  # Acceder al valor de money en el diccionario a
            return "No tiene suficientes fondos"
        a["money"] -= actual["amount"]
        b["money"] += actual["amount"]
 
variastransaccion(transaccion)
print(users)