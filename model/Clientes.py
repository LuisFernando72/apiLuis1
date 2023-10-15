from database.ConexionOracle import connection
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
import cx_Oracle


class Clientes():
    def __init__(self) -> None:
        pass

    def clienteConst(self, idcliente, nombres, apellidos, nit, genero, fecha_ingreso, correo, fechamodificacion):
        self.idcliente = idcliente
        self.nombres = nombres
        self.apellidos = apellidos
        self.nit = nit
        self.genero = genero
        self.fecha_ingreso = fecha_ingreso
        self.correo = correo
        self.fechamodificacion = fechamodificacion

    def agregarCliente(self):
        try:
            cn = connection.cursor()
            query = "INSERT INTO CLIENTES(NOMBRES, APELLIDOS, NIT, GENERO, FECHA_INGRESO, CORREO, FECHA_MODIFICACION)VALUES\
                    (:1,:2, :3, :4,:5,:6,:7)"
            r = cn.execute(query, (self.nombres, self.apellidos, self.nit, self.genero,
                                   self.fecha_ingreso, self.correo, self.fechamodificacion))
            connection.commit()
            cn.close()
            return HTTP_201_CREATED
        except cx_Oracle.Error as error:
            print("AgregarCliente ", error)
            return HTTP_400_BAD_REQUEST

    def eliminarCliente(self):
        try:
            cn = connection.cursor()
            query = "DELETE CLIENTES WHERE ID_CLIENTE= " + str(self.idcliente)
            r = cn.execute(query)
            connection.commit()
            cn.close()
            return HTTP_200_OK
        except cx_Oracle.Error as error:
            print("EliminarCliente  ", error)
            return HTTP_400_BAD_REQUEST

    def actualizarCliente(self):
        try:
            cn = connection.cursor()
            query = "UPDATE CLIENTES SET NOMBRES=:1, APELLIDOS=:2, NIT=:3, GENERO =:4, CORREO=:5, FECHA_MODIFICACION=:6 WHERE ID_CLIENTE =:7"
            r = cn.execute(query,(self.nombres, self.apellidos, self.nit,
                              self.genero, self.correo, self.fechamodificacion, self.idcliente))
            connection.commit()
            cn.close()
            return HTTP_200_OK
        except cx_Oracle.Error as error:
            print("ActualizarCliente  ", error)
            return HTTP_400_BAD_REQUEST

    def verClientes(self):
        cn = connection.cursor()
        query = "select * from clientes"
        r = cn.execute(query).fetchall()
        item = []
        for row in r:
            dicionary = {}
            dicionary["idcliente"] = row[0]
            dicionary["nombres"] = row[1]
            dicionary["apellidos"] = row[2]
            dicionary["nit"] = row[3]
            dicionary["genero"] = row[4]
            dicionary["fecha_ingreso"] = row[5]
            dicionary["correo"] = row[6]
            dicionary["fecha_modificacion"] = row[7]
            item.append(dicionary)
        return item
