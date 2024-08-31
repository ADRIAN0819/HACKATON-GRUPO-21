from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
from fastapi import FastAPI


class Producto(BaseModel):
    id: Optional[UUID] = None
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    stock: int
    
app = FastAPI()

print("Hackaton 1")
print("Hola mundo Celestial")