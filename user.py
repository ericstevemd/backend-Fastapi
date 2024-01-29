from fastapi import FastAPI
from pydantic import BaseModel
from  enum  import Enum

app =FastAPI()

#inicia el server :  uvicorn  user:app --reload 

 #.\env\Scripts\activate




#entidad user 

class User(str ,Enum):
    id:int
    nome :str
    surname :str
    url:str
    age: int 
    
    

#user_list=[User(id=1 ,nome='eric ' ,surname='moya',url='htpp//facebook.com',ege=32)]




@app.get('/usersjosn')
async def  user():
    return [{ 'name':'eric ' ,'sureme':'moya' },
            { 'name':'eric ' ,'sureme':'moya' },
            { 'name':'eric ' ,'sureme':'moya' },
            { 'name':'eric ' ,'sureme':'moya' },
            { 'name':'eric ' ,'sureme':'moya' }]


@app.get('/user/{id}')
def user(id:int):
   # users=filter(lambda user:user.id==id, user_list)
    try:
      return {'id':id }
     
    except:
       return { 'error':'no se ha encontrado el usuario'}
   
   


@app.get('/userquery/')
def user(id:int):
   # users=filter(lambda user: user.id==id, user_list)

    try:
      return {'id':id}
    except:
       return {'error':'n se ha encontrado el usuario'}
   



