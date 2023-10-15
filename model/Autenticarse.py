from database.Conexion import conexion
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST
from werkzeug.security import generate_password_hash, check_password_hash
 

class Autenticarse:
    
 def __init__(self, correo, passw):
        self.correo = correo
        self.passw = passw
        
        
 def autenticar(self):
        retorno =""
        seleccionar = conexion.cursor()
        resultado = seleccionar.execute(
        "select USUARIOS.ID_USUARIO, USUARIOS.NOMBRES, USUARIOS.APELLIDOS, USUARIOS.CONTRASENIA, USUARIOS.CORREO_ELECTRONICO, USUARIOS.IMAGEN_USUARIO, USUARIOS.ID_ROL from\
        Inventarios12.USUARIOS  where usuarios.CORREO_ELECTRONICO ='" + self.correo+"'")
        usuario = resultado.fetchone()
        if usuario is not None:
            contra = usuario[3]
            check_pass = check_password_hash(contra, self.passw)
            if check_pass:
              retorno = HTTP_201_CREATED
            else:
                retorno = HTTP_400_BAD_REQUEST
        
        else:
            retorno =  HTTP_400_BAD_REQUEST
        return retorno
    


     
     