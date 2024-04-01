from fastapi import FastAPI
from routes.user import users
from routes.transactions import transactions
from docs import tags_metadata

# models: modelos que realmente se están guardando en la base de datos
# schemas: forma en la que se va a describir los datos con los que se va a interactuar en el código
# Para crear el archivo requirements.txt se usa pip freeze > requirements.txt

app = FastAPI(
    title="API REST MishiPay",
    description="API REST para las funcionalidades básicas (usuarios y transacciones)",
    openapi_tags=tags_metadata
    )

app.include_router(users)
app.include_router(transactions)
