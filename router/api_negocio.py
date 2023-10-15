from fastapi import APIRouter, Response
from database.ConexionOracle import connection
from model.schemas.esquema_productos import baseProducto, baseBusquedaAvanzada, baseCategorias
from model.schemas.esquema_productos import baseMarcas, baseBodega, baseInventario, baseProveedores
from model.schemas.esquema_compras import baseVistaCompras
from model.Productos import Producto
from model.Categorias import Categorias
from model.Marcas import Marcas
from model.Inventarios import Inventarios
from model.Proveedores import Proveedores
from model.Bodegas import Bodegas
from model.Compras import Compras
from model.Clientes import Clientes
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from typing import List
from datetime import datetime
from model.schemas.usuarios import baseCliente

api = APIRouter()


@api.get("/")
def root():
    cn = connection.cursor()
    r = cn.cls("select * from USER_ADMIN_DATOS.MARCAS").fetchall()
    print("Marcas:")
    print(r)
    return {"inicio": "Hola"}

# Crear Producto


@api.post("/api/crearProducto")
def CrearProducto(dataP: baseProducto):
    p = Producto()
    precioVenta = (dataP.PRECIO_COSTO+(dataP.PRECIO_COSTO*1)/150)

    p.ConsProducto(0, dataP.ID_CATEGORIA, dataP.ID_MARCA, dataP.PRODUCTO, dataP.DESCRIPCION,
                   dataP.IMAGEN, dataP.PRECIO_COSTO, precioVenta, dataP.ID_INVENTARIO)
    p.crearProducto()
    tiempo = datetime.now()
    horaActual = tiempo.strftime('%d/%m/%Y %H:%M:%S')
    c = Compras()
    c.InsertarCompra(dataP.ID_PROVEEDOR, horaActual, horaActual)
    idCompra = c.getidCompra(horaActual)
    getid_Producto = c.getidProducto(dataP.PRODUCTO)

    c.InsertarDetalle(
        idCompra, getid_Producto, dataP.CANTIDAD, dataP.PRECIO_COSTO)
    return Response(status_code=HTTP_201_CREATED)


@api.put("/api/actualizarcompra", status_code=HTTP_201_CREATED)
def ModificarCompra(datam: baseProducto):
    p = Producto()
    precioVenta = (datam.PRECIO_COSTO+(datam.PRECIO_COSTO*1)/150)
    p.ConsProducto(datam.ID_PRODUCTO, datam.ID_CATEGORIA, datam.ID_MARCA, datam.PRODUCTO,
                   datam.DESCRIPCION, datam.IMAGEN, datam.PRECIO_COSTO, precioVenta, datam.ID_INVENTARIO)
    p.modificarProducto()
    c = Compras()
    c.actualizarProvcompra(datam.ID_PROVEEDOR, datam.ID_COMPRA)
    c.actualizarBodcompra(datam.ID_BODEGA, datam.ID_INVENTARIO)
    c.ActualizarStock(datam.ID_PRODUCTO, datam.CANTIDAD, datam.PRECIO_COSTO)
    return Response(status_code=HTTP_201_CREATED)


@api.delete("/api/eliminarCompra")
def EliminarCompra(datae: baseProducto):
    e = Producto()
    e.eliminarProdcompras(datae.ID_PRODUCTO)
    e.eliminarProducto(datae.ID_PRODUCTO)


@api.get("/api/obtnenerProducto", response_model=List[baseProducto])
def obtenerProducto():
    p = Producto()
    r = p.vistaProductos()
    return r


@api.get("/api/obtnenerCategoria", response_model=List[baseCategorias])
def obtenerCategoria():
    c = Categorias()
    r = c.VerCategorias()
    return r


@api.get("/api/obtnenerMarcas", response_model=List[baseMarcas])
def obtenerMarcas():
    m = Marcas()
    r = m.VerMarcas()
    return r


@api.get("/api/obtnenerInventarios", response_model=List[baseInventario])
def obtenerInventario():
    i = Inventarios()
    r = i.VerInventario()
    return r


@api.get("/api/obtnenerProveedor", response_model=List[baseProveedores])
def obtenerProveedor():
    pp = Proveedores()
    r = pp.verProveedores()
    return r


@api.get("/api/obtnenerBodega", response_model=List[baseBodega])
def obtenerBodega():
    b = Bodegas()
    r = b.VerBodegas()
    return r


@api.get("/api/obtnenerProducto/<categoria><marca>", response_model=List[baseBusquedaAvanzada])
def BusquedaAvanzada(categoria: str, marca: str):
    p = Producto()
    retorno = ""
    print(categoria.upper())
    print(marca.upper())
    # POR DEFECTO SE ENVIA NULL AL CAMPO QUE NO SE QUIERA FILTRAR
    if categoria.upper() != "NULL":
        retorno = p.BuscarPorCategoria(categoria.upper())
    if marca.upper() != "NULL":
        retorno = p.BuscarPorMarca(marca.upper())

    return retorno


@api.get("/api/pintarCompras", response_model=List[baseVistaCompras])
def VistaCompras():
    vista = Compras()
    retorno = vista.vistaCompras()
    return retorno

# AGREGAR PRODUCTOS DIRECTAMENTE A INVENTARIO, BODEGA STOCK ETC
# CLIENTES OPERACIONES


@api.get("/api/verClientes", response_model=List[baseCliente])
def verClientes():
    c = Clientes()
    retorno = c.verClientes()
    return retorno


@api.post("/api/agregarcliente")
def agregarCliente(datai: baseCliente):
    tiempo = datetime.now()
    horaActual = tiempo.strftime('%d/%m/%Y %H:%M:%S')
    c = Clientes()
    c.clienteConst(datai.idcliente, datai.nombres, datai.apellidos, datai.nit,
                   datai.genero, horaActual, datai.correo, horaActual)
    retorno = c.agregarCliente()
    
    return Response(status_code=retorno)

@api.put("/api/modificarcliente")
def modificarCliente(datam : baseCliente):
    tiempo = datetime.now()
    horaActual = tiempo.strftime('%d/%m/%Y %H:%M:%S')
    c = Clientes()
    c.clienteConst(datam.idcliente, datam.nombres, datam.apellidos, datam.nit,
                   datam.genero, horaActual, datam.correo, horaActual)
    retorno =c.actualizarCliente()
    return Response(status_code= retorno)

@api.delete("/api/eliminarcliente")
def eliminarCliente(datae: baseCliente):
    tiempo = datetime.now()
    horaActual = tiempo.strftime('%d/%m/%Y %H:%M:%S')
    c = Clientes()
    c.clienteConst(datae.idcliente, datae.nombres, datae.apellidos, datae.nit,
                   datae.genero, horaActual, datae.correo, horaActual)
    retorno = c.eliminarCliente()
    
    return Response(status_code= retorno)