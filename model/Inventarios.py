from database.ConexionOracle import connection
class Inventarios():
    def __init__(self) -> None:
        pass
    
    def VerInventario(self):
        cn = connection.cursor()
        query="SELECT * FROM INVENTARIOS"
        r = cn.execute(query)
        item=[]
        for row in r:
            dictionary = {}
            dictionary["ID_INVENTARIO"] = row[0]
            dictionary["NO_DOCUMENTO"] = row[1]
            dictionary["TIPO_OPERACION"] = row[2]
            dictionary["FECHA_INICIO"] = str(row[3])
            dictionary["FECHA_ACTUALIZACION"] = str(row[4])
            dictionary["ID_BODEGA"] = row[5]
            item.append(dictionary)
        return item