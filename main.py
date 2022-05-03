from fastapi import FastAPI
from uuid import UUID, uuid4
from typing import List
from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("4dbbc17f-f2df-40d9-b647-c7bdb0ba8a17"),
        first_name='Stas',
        last_name='Lukyanov',
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    ),
    User(
        id=UUID("5028db0d-1207-46a9-8a9c-92c3d54004e4"),
        first_name='Maria',
        last_name='Ivanova',
        gender=Gender.female,
        roles=[Role.student]
    )
]

@app.get('/')
async def root():
    return {"APP status": "Active"}

@app.get('/api/v1/users')
async def fetch_users():
     return db

@app.post('/api/v1/users')
async def register_user(user: User):
    db.append(user)
    return {"user_id": user.id}

@app.delete('api/v1/users/{user_id}')
async def delete_user(user_id: UUID):
    db = list(filter(lambda item: item.id != user_id, db))
