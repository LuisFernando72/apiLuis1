from pydantic import BaseModel

class baseProducto(BaseModel):
    ID_PRODUCTO: int
    ID_CATEGORIA: int#
    ID_MARCA:int#
    PRODUCTO: str #
    DESCRIPCION:str 
    IMAGEN:str #
    PRECIO_COSTO:float#
    PRECIO_VENTA:float
    ID_INVENTARIO:int#
    ID_PROVEEDOR:int
    CANTIDAD:int
    ID_BODEGA:int
    ID_COMPRA:int

class baseBusquedaAvanzada(BaseModel):
    PRODUCTO: str
    DESCRIPCION:str
    IMAGEN:str
    PRECIO_VENTA:float
    NOMBRE_CATEGORIA:str
    NOMBRE_MARCA:str
    NO_INVENTARIO:str

#DROPS
class baseCategorias(BaseModel):
    ID_CATEGORIA:int
    NOMBRE_CATEGORIA:str
    ESTADO: int
    FECHA_CREACION:str
    FECHA_ACTUALIZACION:str

class baseMarcas(BaseModel):
    ID_MARCA:int
    NOMBRE_MARCA:str

class baseInventario(BaseModel):
    ID_INVENTARIO:int
    NO_DOCUMENTO:str
    TIPO_OPERACION:str
    FECHA_INICIO:str
    FECHA_ACTUALIZACION:str
    ID_BODEGA:int
    
class baseBodega(BaseModel):
    ID_BODEGA:int
    NOMBRE_BODEGA:str
    LOCALIZACION:str
    PAIS:str
    
class baseProveedores(BaseModel):
    ID_PROVEEDOR:int
    PROVEEDOR:str
    NIT:str
    TELEFONO:str
    
