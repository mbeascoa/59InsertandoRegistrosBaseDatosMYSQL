from datetime import date
import mysql.connector as bd

bd_conexion = bd.connect(host='localhost', port='3306',
                         user='root', password='', database='Hospital')

cursor = bd_conexion.cursor()

ConsultaAlta = ("INSERT INTO emp "
                "(emp_no,apellido,oficio,dir,fecha_alt,salario, comision,dept_no) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

datosEmpleados = (1111, 'Benito', 'Programador', 7566, date(1976, 6, 4), 100000, 100, 20)

cursor.execute(ConsultaAlta, datosEmpleados)

bd_conexion.commit()

cursor.close()
bd_conexion.close() 

