from database.ConexionOracle import connection
class Proveedores():
    def __init__(self) -> None:
        pass
    
    def verProveedores(self):
        cn = connection.cursor()
        query = "SELECT * FROM PROVEEDORES"
        r = cn.execute(query).fetchall()
        item =[]
        for row in r:
            dictionary={}
            dictionary["ID_PROVEEDOR"]= row[0]
            dictionary["PROVEEDOR"]= row[1]
            dictionary["NIT"]= row[2]
            dictionary["TELEFONO"]= row[3]
            item.append(dictionary)
        
        return item
    