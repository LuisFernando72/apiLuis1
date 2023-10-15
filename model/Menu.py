from database.Conexion import conexion
 
class menus:
    def __init__(self):
        pass

    def mostrar_menu(self, menu, submenu):
        self.menu = menu
        self.submenu = submenu
        
    def  menuBuscar(self, idrol):
        self.idrol = idrol
    
  
    def buscarUsuario(self, correo2):
        seleccionar = conexion.cursor()
        resultado = seleccionar.execute("select USUARIOS.ID_USUARIO, USUARIOS.NOMBRES, USUARIOS.APELLIDOS, USUARIOS.CORREO_ELECTRONICO,\
            USUARIOS.ID_ROL from Inventarios12.USUARIOS  where usuarios.CORREO_ELECTRONICO ='" + correo2+"'")
        usuario = resultado.fetchone()
        idRol = usuario[4]
        
        dictPerfil = {}
        dictPerfil["iduser"] = "NULL"
        dictPerfil["nombres"] = usuario[1]
        dictPerfil["apellidos"] = usuario[2]
        dictPerfil["correo"] = usuario[3]
        dictPerfil["idperfil"] = str(usuario[4])
        
        d = menus()
        
        selectmenu= d.menuBuscar(idRol)
        dictPerfil["pintarMenu"] = selectmenu
        seleccionar.close()
        
        return dictPerfil
    
    
    
    def menuBuscar(self, id_rol):
        select_menu = conexion.cursor()
        select_menu2 = conexion.cursor()
        query = "SELECT * FROM Inventarios12.MENU INNER JOIN Inventarios12.PERFILES ON PERFILES.ID_MENU = MENU.SUBMODULO\
        and PERFILES.ID_ROL ="+ str(id_rol)+";"
        select_menu.execute(query) 
        resultado = select_menu.fetchall()
        print(resultado)
        result = []
        result2 = []
        for row in resultado:
            item_dict = {}
            item_dict2 = {}
            if row[5] == "Menu":
                item_dict["id"] = str(row[1])
                item_dict["nombre"] = str(row[2])
                item_dict["enlaze"] = str(row[3])
                item_dict["icono"] = str(row[4])
                item_dict["tipo"] = str(row[5])
                result.append(item_dict)
            else:
               
                item_dict2["id"] = str(row[1])
                item_dict2["nombre"] = str(row[2])
                item_dict2["enlaze"] = str(row[3])
                item_dict2["icono"] = str(row[4])
                item_dict2["rol_menu"] = str(row[5])
                result2.append(item_dict2)
           
            
        r = menus()
     
        r.mostrar_menu(result, result2)
        html = r.pintar_menu()
        print(html) 
        return html
    
    
    def pintar_menu(self):
        listaMenu = self.menu
        listaSubmenu = self.submenu
         
        kk = ""
        kk += "<a href=\"#\" class=\"brand\">\n"
        kk += "<img src=\"/static/img/logoTortuga.png\"/>\n"
        kk += "<span class=\"text\">INVENTARIO</span></a>\n"

        # COMIENZO DEL MENU
        kk += "<ul class=\"side-menu top\">  <li title=\"Dashboard\"> <a href=\"#\">\n"
        kk += "<i class=\"bx bxs-dashboard\"></i> <span class=\"text\">Dashboard</span> </a> </li>\n"

        for m in listaMenu:
            #<li class="opcion" title="Generales" id="Generales">
            kk += "<li class=\"opcion\" title=\""+m["nombre"]+"\" id=\""+m["nombre"]+"\">"
            kk += "<a href=\"#\">\n"
            kk += "<i class =\"" + m["icono"] + "\" ></i>\n"
            kk += m["nombre"] + "<b>▼</b></a>\n"
            kk += "<ul class=\"submenu\"" + " id=\""+m["nombre"] + "\" >\n"

            for s in listaSubmenu:
                if m["id"] == s["id"]:
                    kk += "<li tittle =\"" + \
                        s["nombre"] + "\" id=\"" + s["nombre"] + "\" >\n"
                    kk += "<a href=\""+s["enlaze"] + "\" >\n"
                    kk += "<i class=\""+s["icono"] + "\"></i>\n"
                    kk += "<span class=\"text\">" + \
                        s["nombre"]+" </span>\n </a> \n</li>\n"

            kk += "</ul>\n </li>\n"

        kk += "<li style=\"margin-top: 10px;\" title=\"Cerrar sesión\">\n"
        kk += " <a href=\"/cerrar_sesion\" class=\"logout\">\n <i class=\"bx bx-log-out-circle\"></i>\n"
        kk += "<span class=\"text\">Cerrar sesión</span>\n </a>\n </li>\n </ul>\n"
        
        
        return kk


    def menu(self):
        return self.menu

    def submenu(self):
        return self.submenu
