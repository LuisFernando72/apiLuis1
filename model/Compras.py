from database.ConexionOracle import connection
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
import cx_Oracle
class Compras():
    def __init__(self) -> None:
        pass
    
    def getidCompra(self,valor):
        cn = connection.cursor()
        r = cn.execute("SELECT ID_COMPRA FROM COMPRAS WHERE TO_CHAR(FECHA_INGRESO,'dd/mm/yyyy hh24:mi:ss')= '"+valor+"'").fetchone()
       # cn.close()
        return r[0]
    def getidProducto(self,valor):
        
        cn = connection.cursor()
        r = cn.execute("SELECT ID_PRODUCTO FROM PRODUCTOS WHERE PRODUCTO = '"+valor+"'").fetchone()
        #cn.close()
        return r[0]
    #SELECT ID_PRODUCTO FROM PRODUCTOS WHERE PRODUCTO ='Blur pitaya'
    
    def InsertarCompra(self,ID_PROVEEDOR, FECHA_ORDEN, FECHA_INGRESO):
        
        try:
            cn = connection.cursor()
            query = "INSERT INTO COMPRAS(ID_PROVEEDOR, FECHA_ORDEN, FECHA_INGRESO)\
            VALUES("+str(ID_PROVEEDOR)+",TO_DATE('"+FECHA_ORDEN +"','dd/mm/yyyy hh24:mi:ss'), "+"TO_DATE('"+FECHA_INGRESO +"','dd/mm/yyyy hh24:mi:ss'))"
            
            cn.execute(query)
            connection.commit()
           # cn.close()
           # return HTTP_201_CREATED
        except cx_Oracle.Error as error:
            print("Error compra ", error)
            #return HTTP_400_BAD_REQUEST
        
    def InsertarDetalle(self,ID_COMPRA,ID_PRODUCTO,CANTIDAD, PRECIO_UNITARIO):
        print(ID_COMPRA)
        print(ID_PRODUCTO)
        try:
            cn = connection.cursor()
            query = "INSERT INTO COMPRAS_DETALLES(ID_COMPRA, ID_PRODUCTO, CANTIDAD, PRECIO_UNITARIO) VALUES (:1,:2,:3,:4)"
            cn.execute(query,(ID_COMPRA,ID_PRODUCTO,CANTIDAD, PRECIO_UNITARIO))
            connection.commit()
            #cn.close()
            #return HTTP_201_CREATED
        except cx_Oracle.Error as error:
            print("ERROR DETALLE ", error)
           # return HTTP_400_BAD_REQUEST
           
      
    def vistaCompras(self):
        item = []
        try:
            cn = connection.cursor()
            query = "SELECT P.ID_PRODUCTO, C.ID_CATEGORIA, M.ID_MARCA,I.ID_INVENTARIO,PP.ID_PROVEEDOR, B.ID_BODEGA,\
            CC.ID_COMPRA, C.NOMBRE_CATEGORIA,M.NOMBRE_MARCA, P.PRODUCTO, P.DESCRIPCION, P.IMAGEN, CP.PRECIO_UNITARIO, P.PRECIO_VENTA,\
            I.NO_DOCUMENTO, PP.PROVEEDOR, CP.CANTIDAD, B.NOMBRE_BODEGA, CC.FECHA_INGRESO FROM PRODUCTOS P, CATEGORIAS C, MARCAS M,\
            COMPRAS_DETALLES CP,INVENTARIOS I, PROVEEDORES PP, BODEGAS B,  COMPRAS CC WHERE P.ID_PRODUCTO = CP.ID_PRODUCTO AND\
            P.ID_INVENTARIO = I.ID_INVENTARIO AND CP.ID_COMPRA = CC.ID_COMPRA AND C.ID_CATEGORIA = P. ID_CATEGORIA AND\
            P.ID_MARCA = M.ID_MARCA AND I.ID_BODEGA = B.ID_BODEGA AND CC.ID_PROVEEDOR = PP.ID_PROVEEDOR"
            r = cn.execute(query).fetchall()
           
            for row in r:
                dictionary = {}
                dictionary["ID_PRODUCTO"] = row[0]
                dictionary["ID_CATEGORIA"] = row[1]
                dictionary["ID_MARCA"] = row[2]
                dictionary["ID_INVENTARIO"] = row[3]
                dictionary["ID_PROVEEDOR"] = row[4]
                dictionary["ID_BODEGA"] = row[5]
                dictionary["ID_COMPRA"] = row[6]
                dictionary["NOMBRE_CATEGORIA"] = row[7]
                dictionary["NOMBRE_MARCA"] = row[8]
                dictionary["PRODUCTO"] = row[9]
                dictionary["DESCRIPCION"] = row[10]
                dictionary["IMAGEN"] = row[11]
                dictionary["PRECIO_UNITARIO"] = row[12]
                dictionary["PRECIO_VENTA"] = row[13]
                dictionary["NO_DOCUMENTO"] = row[14]
                dictionary["PROVEEDOR"] = row[15]
                dictionary["CANTIDAD"] = row[16]
                dictionary["NOMBRE_BODEGA"] = row[17]
                dictionary["FECHA_INGRESO"] = str(row[18])
                item.append(dictionary)
        except cx_Oracle.Error as error:
            print("ERROR VISTA COMPRAS ", error)
        
        return item    
                
    def ActualizarStock(self, idproducto, cantidad, preciou):
        cn = connection.cursor()
        r = cn.execute("select cantidad from compras_detalles  where id_producto = "+str(idproducto)).fetchone()
       # cn.close()
        stock = r[0] + cantidad
        
        try:
            cn = connection.cursor()
            
            cn.execute("update compras_detalles set cantidad = "+str(stock)+", precio_unitario = "+ str(preciou)+" where id_producto ="+ str(idproducto))
            connection.commit()
            #cn.close()
            #return HTTP_201_CREATED
        except cx_Oracle.Error as error:
            print("ERROR STOCK ", error)
    
    
    def actualizarProvcompra(self, idproveedor, idcompra):

        try:
            cn = connection.cursor()
            
            cn.execute("update compras set id_proveedor ="+ str(idproveedor)+"where id_compra ="+ str(idcompra))
            connection.commit()
            #cn.close()
            #return HTTP_201_CREATED
            print("exito prov")
        except cx_Oracle.Error as error:
            print("ERROR ACTUALIZAR PROVEEDOR ", error)
        

    def actualizarBodcompra(self, idbodega, idinventario):
        try:
            cn = connection.cursor()
            cn.execute("update inventarios set id_bodega="+ str(idbodega)+"where id_inventario ="+ str(idinventario))
            connection.commit()
            #cn.close()
            #return HTTP_201_CREATED
        except cx_Oracle.Error as error:
            print("ERROR BODEGA COMPRA ", error)