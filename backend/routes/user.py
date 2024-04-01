from fastapi import APIRouter, Response, status, HTTPException
from config.db import conn
from schemas.user import users_entity, user_entity
from models.user import User
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from bson import ObjectId # sonvierte el string a un ObjectId
# from passlib.hash import sha256_crypt # permite cifrar contraseñas con un hash con el método encrypt. Se debe instalar la librería

users = APIRouter()

@users.get("/users", response_model=list[User], tags=["users"])
def find_all_users():
    return users_entity(conn.MishiPay.user.find())

@users.post("/users", response_model=User, tags=["users"])
def create_user(user: User):
    new_user = dict(user)
    existing_user = conn.MishiPay.user.find_one({"email": user.email})
    
    if (existing_user is not None):
        raise HTTPException(status_code=400, detail="El usuario que intenta crear ya existe")

    id = conn.MishiPay.user.insert_one(new_user).inserted_id

    created_user = conn.MishiPay.user.find_one({"_id": id})
    return user_entity(created_user)

@users.put("/users/{email}", response_model=User, tags=["users"])
def update_user(email: str, user: User):
    conn.MishiPay.user.find_one_and_update({"email": email}, {"$set": dict(user)})
    return user_entity(conn.MishiPay.user.find_one({"email": email}))

@users.get("/users/{email}", response_model=User, tags=["users"])
def find_user(email: str):
    return user_entity(conn.MishiPay.user.find_one({"email": email}))

@users.delete("/users/{str}", status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
def delete_user(email: str):
    result = conn.MishiPay.user.delete_one({"email": email})
    if result.deleted_count == 1:
        return Response(status_code=HTTP_204_NO_CONTENT)
    else:
        return Response(status_code=HTTP_404_NOT_FOUND, content="User not found")
