from database.ConexionOracle import connection


class Categorias():
    def __init__(self) -> None:
        pass
    
    def VerCategorias(self):
        c = connection.cursor()
        query = "SELECT * FROM CATEGORIAS"
        r = c.execute(query).fetchall()
        item =[]
        for row in r:
            dictionary={}
            dictionary["ID_CATEGORIA"] = row[0]
            dictionary["NOMBRE_CATEGORIA"] = row[1]
            dictionary["ESTADO"] = row[2]
            dictionary["FECHA_CREACION"] = str(row[3])
            dictionary["FECHA_ACTUALIZACION"]= str(row[4])
            item.append(dictionary)
        
        return item                