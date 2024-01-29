from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class user:
    url: str
    mane :str
    aege: int 
    surmanme:str
    nombre : str



@app.get('/user')


async def root ():
    
    
    return[{ 'name:','moure ','apgina eb'},  
            { 'mesasne:','hello word '},
            { 'mesasne:','hello word '},
            { 'mesasne:','hello word '},
            { 'mesasne:','hello word '}]
            
            
    
   



#uvicorn app:app --reload

#pip install uvicorn