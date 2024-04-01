from fastapi import APIRouter, Response, status, HTTPException
from config.db import conn
from schemas.transactions import transaction_entity, transactions_entity
from models.transactions import Transaction
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from bson import ObjectId # sonvierte el string a un ObjectId
# from passlib.hash import sha256_crypt # permite cifrar contraseñas con un hash con el método encrypt. Se debe instalar la librería

transactions = APIRouter()
    
@transactions.get("/transactions", response_model = list[Transaction], tags=["transactions"])
def get_transactions():
    return transactions_entity(conn.MishiPay.transactions.find())

@transactions.post("/transactions", response_model=Transaction, tags=["transactions"])
def create_transaction(transaction: Transaction):
    # Validar que ambos usuarios existen
    sender = conn.MishiPay.user.find_one({"email": transaction.sender_email})
    reciever = conn.MishiPay.user.find_one({"email": transaction.reciever_email})
    
    if sender is None or reciever is None:
        raise HTTPException(status_code=404, detail="El número al que intentas enviar el dinero no está registrado")

    # Validar que el usuario que envía dinero tiene suficiente saldo
    if sender['money'] < transaction.amount:
        raise HTTPException(status_code=400, detail="No tienes suficiente dinero para hacer la transacción")

    new_transaction = dict(transaction)
    id = conn.MishiPay.transactions.insert_one(new_transaction).inserted_id
    transaction_id_str = str(id)  # Convertir ObjectId a string

    created_transaction = conn.MishiPay.transactions.find_one({"_id": id})
    
    # Actualizar la lista de transacciones de los usuarios involucrados
    sender_email = created_transaction['sender_email']
    reciever_email = created_transaction['reciever_email']
    
    # Actualizar el saldo del usuario que envía el dinero
    conn.MishiPay.user.update_one({"email": sender_email}, {"$push": {"transactions": transaction_id_str}, "$inc": {"money": -transaction.amount}})
    
    # Actualizar el saldo del usuario que recibe el dinero
    conn.MishiPay.user.update_one({"email": reciever_email}, {"$push": {"transactions": transaction_id_str}, "$inc": {"money": transaction.amount}})
    
    return transaction_entity(created_transaction)


@transactions.delete("/transactions", status_code=status.HTTP_204_NO_CONTENT, tags=["transactions"]) # Únicamente se usará en desarrollo
def delete_all_transactions():
    conn.MishiPay.transactions.delete_many({})
    return Response(status_code=HTTP_204_NO_CONTENT)

@transactions.post("/many-transactions", status_code=status.HTTP_204_NO_CONTENT, tags=["transactions"])
def list_of_transactions():
    pass