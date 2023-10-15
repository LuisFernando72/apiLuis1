from database.ConexionOracle import connection
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
import cx_Oracle


class Producto():
    def __init__(self) -> None:
        pass

    def ConsProducto(self, ID_PRODUCTO, ID_CATEGORIA, ID_MARCA, PRODUCTO, DESCRIPCION, IMAGEN, PRECIO_COSTO, PRECIO_VENTA, ID_INVENTARIO):
        self.ID_PRODUCTO = ID_PRODUCTO
        self.ID_CATEGORIA = ID_CATEGORIA
        self.ID_MARCA = ID_MARCA
        self.PRODUCTO = PRODUCTO
        self.DESCRIPCION = DESCRIPCION
        self.IMAGEN = IMAGEN
        self.PRECIO_COSTO = PRECIO_COSTO
        self.PRECIO_VENTA = PRECIO_VENTA
        self.ID_INVENTARIO = ID_INVENTARIO

    def crearProducto(self):
        try:
            cn = connection.cursor()
            query = "INSERT INTO PRODUCTOS(ID_CATEGORIA, ID_MARCA, PRODUCTO, DESCRIPCION, IMAGEN, PRECIO_COSTO, PRECIO_VENTA, ID_INVENTARIO)\
            VALUES(:1,:2,:3,:4,:5,:6,:7,:8)"
            cn.execute(query, (self.ID_CATEGORIA, self.ID_MARCA, self.PRODUCTO, self.DESCRIPCION,
                       self.IMAGEN, self.PRECIO_COSTO, self.PRECIO_VENTA, self.ID_INVENTARIO))
            connection.commit()
            cn.close()
            return HTTP_201_CREATED
        except cx_Oracle.Error as error:
            print(error)
            return HTTP_400_BAD_REQUEST

    def vistaProductos(self):

        cn = connection.cursor()
        query = "SELECT * FROM PRODUCTOS"
        r = cn.execute(query).fetchall()
        result = []
        for row in r:
            item_dict = {}
            item_dict["ID_PRODUCTO"] = str(row[0])
            item_dict["ID_CATEGORIA"] = str(row[1])
            item_dict["ID_MARCA"] = str(row[2])
            item_dict["PRODUCTO"] = row[3]
            item_dict["DESCRIPCION"] = row[4]
            item_dict["IMAGEN"] = row[5]
            item_dict["PRECIO_COSTO"] = str(row[6])
            item_dict["PRECIO_VENTA"] = str(row[7])
            item_dict["ID_INVENTARIO"] = str(row[8])

            result.append(item_dict)
        return result

    def BuscarPorCategoria(self, categoria):
        cn = connection.cursor()
        query = "SELECT P.PRODUCTO,P.DESCRIPCION, P.IMAGEN, P.PRECIO_VENTA, C.NOMBRE_CATEGORIA, M.NOMBRE_MARCA, I.NO_DOCUMENTO AS NO_INVENTARIO FROM PRODUCTOS P, CATEGORIAS C, MARCAS M, INVENTARIOS I WHERE UPPER(C.NOMBRE_CATEGORIA) ='" + \
            categoria+"'"
        r = cn.execute(query).fetchall()
        result = []
        for row in r:
            item_dict = {}
            item_dict["PRODUCTO"] = row[0]
            item_dict["DESCRIPCION"] = row[1]
            item_dict["IMAGEN"] = row[2]
            item_dict["PRECIO_VENTA"] = row[3]
            item_dict["NOMBRE_CATEGORIA"] = row[4]
            item_dict["NOMBRE_MARCA"] = row[5]
            item_dict["NO_INVENTARIO"] = row[6]
            result.append(item_dict)
        return result

    def BuscarPorMarca(self, marca):
        cn = connection.cursor()
        query = "SELECT P.PRODUCTO,P.DESCRIPCION, P.IMAGEN, P.PRECIO_VENTA, C.NOMBRE_CATEGORIA, M.NOMBRE_MARCA, I.NO_DOCUMENTO AS NO_INVENTARIO FROM PRODUCTOS P, CATEGORIAS C, MARCAS M, INVENTARIOS I\
                WHERE UPPER(M.NOMBRE_MARCA) = '"+marca+"'"
        r = cn.execute(query).fetchall()
        result = []
        for row in r:
            item_dict = {}
            item_dict["PRODUCTO"] = row[0]
            item_dict["DESCRIPCION"] = row[1]
            item_dict["IMAGEN"] = row[2]
            item_dict["PRECIO_VENTA"] = row[3]
            item_dict["NOMBRE_CATEGORIA"] = row[4]
            item_dict["NOMBRE_MARCA"] = row[5]
            item_dict["NO_INVENTARIO"] = row[6]
            result.append(item_dict)
        return result

    def modificarProducto(self):

        try:
            cn = connection.cursor()
            query = "update productos set id_categoria = :1, id_marca =:2, producto =:3, descripcion=:4, imagen=:5, precio_costo=:6, precio_venta=:7, id_inventario =:8 where id_producto =:9"
            cn.execute(query, (
                self.ID_CATEGORIA,
                self.ID_MARCA,
                self.PRODUCTO,
                self.DESCRIPCION,
                self.IMAGEN,
                self.PRECIO_COSTO,
                self.PRECIO_VENTA,
                self.ID_INVENTARIO,
                self.ID_PRODUCTO,
            ))
            connection.commit()
            #cn.close()
            #return HTTP_201_CREATED
        except cx_Oracle.Error as error:
            print("aqui ",error)
            #return HTTP_400_BAD_REQUEST
    
    def eliminarProdcompras(self, idproducto):

        try:
            cn = connection.cursor()
            query = "delete compras_detalles where id_producto="+str(idproducto)
            cn.execute(query)
            connection.commit()
       
        except cx_Oracle.Error as error:
            print("modProdu ",error)
          

    def eliminarProducto(self, idproducto):
        try:
            cn = connection.cursor()
            query = "delete productos where id_producto="+str(idproducto)
            cn.execute(query)
            connection.commit()
       
        except cx_Oracle.Error as error:
            print("modProdu ",error)