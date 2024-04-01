def transaction_entity(item) -> dict:
    return {
        "sender_email": item["sender_email"],
        "reciever_email": item["reciever_email"],
        "sender_name": item["sender_name"],
        "reciever_name": item["reciever_name"],
        "amount": item["amount"]
    }

def transactions_entity(entity) -> list: # va a devolver un diccionario
    return [transaction_entity(transaction) for transaction in entity]
