from fastapi import APIRouter, requests, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST
from model.schemas.usuarios import UsuarioLi, getUsuario
from flask import jsonify
from database.Conexion import conexion
from model.Autenticarse import Autenticarse
from model.Menu import menus
from typing import List
import json
inventario12 = APIRouter()


@inventario12.get("/")
def root():
    return {"message": "Hola soy una api con ruta, jsjsjs"}


@inventario12.get("/api/inventario/log/<correol><pasw>", response_model=getUsuario)
def usuario(correol: str, pasw: str):
    log = Autenticarse(correol, pasw)
    retorno1 = log.autenticar()
    if retorno1 != HTTP_400_BAD_REQUEST:
        usuarioMenu = menus()
        retorno = usuarioMenu.buscarUsuario(correol)
        return retorno
    else:
        return Response(status_code=retorno1)
