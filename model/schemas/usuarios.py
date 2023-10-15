from pydantic import BaseModel
from typing import Optional

class UsuarioLi(BaseModel):
    id: Optional[str]
    correo: str
    password : str

class getUsuario(BaseModel):
    iduser:Optional[str]
    nombres: str
    apellidos: str
    correo:str
    idperfil: str
    pintarMenu: str

class baseCliente(BaseModel):
    idcliente:int
    nombres:str
    apellidos:str
    nit:str
    genero:int
    fecha_ingreso:str
    correo:str
    fecha_modificacion: str