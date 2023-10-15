from database.ConexionOracle import connection
class Bodegas():
    def __init__(self) -> None:
        pass
    
    def VerBodegas(self):
        cn = connection.cursor()
        query ="SELECT * FROM BODEGAS"
        r = cn.execute(query).fetchall()
        item =[]
        for row in r:
            dictionary={}
            dictionary["ID_BODEGA"]= row[0]
            dictionary["NOMBRE_BODEGA"]= row[1]
            dictionary["LOCALIZACION"]= row[2]
            dictionary["PAIS"]= row[3]
            item.append(dictionary)
        return item