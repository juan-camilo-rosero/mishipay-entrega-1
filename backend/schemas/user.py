def user_entity(item) -> dict: # va a devolver un diccionario
    return {
        "id": str(item["_id"]),
        "tel": item["tel"],
        "email": item["email"],
        "name": item["name"],
        "money": item["money"],
        "transactions": item["transactions"]
    }

def users_entity(entity) -> list: # va a devolver un diccionario
    return [user_entity(user) for user in entity]

# sirve para generar la documentación
