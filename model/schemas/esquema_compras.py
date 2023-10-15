from pydantic import BaseModel

class baseCompras(BaseModel):
    ID_COMPRA:int
    ID_PROVEEDOR:int
    FECHA_ORDEN:str
    FECHA_INGRESO:str

class baseComprasDetalle(BaseModel):
    ID_COMPRA_DETALLE:int
    ID_COMPRA:int
    ID_PRODUCTO:int
    CANTIDAD:int
    PRECIO_UNITARIO:float
    
    
class baseVistaCompras(BaseModel):
    ID_PRODUCTO:int
    ID_CATEGORIA: int
    ID_MARCA: int
    ID_INVENTARIO: int
    ID_PROVEEDOR: int
    ID_BODEGA: int
    ID_COMPRA: int
    NOMBRE_CATEGORIA: str 
    NOMBRE_MARCA: str 
    PRODUCTO: str 
    DESCRIPCION: str 
    IMAGEN:str 
    PRECIO_UNITARIO:float
    PRECIO_VENTA:float
    NO_DOCUMENTO: str
    PROVEEDOR: str 
    CANTIDAD:int 
    NOMBRE_BODEGA: str
    FECHA_INGRESO: str 
    