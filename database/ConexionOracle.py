import cx_Oracle

username = 'USER_CRUD'
password = 'fer123'
dsn =  cx_Oracle.makedsn('Intel-Luis-el-crack1', '1521', service_name='XE')
port = 1521
# encoding = 'UTF-8' 

try:
    connection = cx_Oracle.connect(
        username,
        password,
        dsn
        )
    
    print(connection.version)
    print("CONEXION EXITOSA!!")

except cx_Oracle.Error as error:
    print(error)





