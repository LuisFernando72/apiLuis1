from database.ConexionOracle import connection

class Marcas():
    def __init__(self) -> None:
        pass
    
    def VerMarcas(self):
        cn = connection.cursor()
        query= "SELECT * FROM MARCAS"
        r = cn.execute(query).fetchall()
        item=[]
        for row in r:
            dictionary={}
            dictionary["ID_MARCA"]=row[0]
            dictionary["NOMBRE_MARCA"] =row[1]
            item.append(dictionary)
        return item            
            
        