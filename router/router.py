from fastapi import APIRouter
from sherme.user_sherma import UserSchema
from config.db  import conn
from model.users import users 



user =APIRouter()


@user.get('/')
def root():
    
 return { 'menssage':  'hola user '}


@user.post('/api/user')
async def create_user(data_user:UserSchema):
    new_user=data_user.dict()
    conn.execute(users.insert().values(new_user))
    print(data_user)
    return 'exicto'
