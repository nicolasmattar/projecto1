import mysql.connector
import pymysql
class goleadores:

    #menu
    def menu(pru):
        opcion=0
        while True:
            try:
                while opcion!=5:
                    print("--------------------------")
                    print("Menu")
                    print("1.Carga de jugadores")
                    print("2.Tabla de goleadores")
                    print("3.Consultar")
                    print("4.Mofificar")
                    print("5.Finalizar")
                    opcion=int(input("Ingrese su opcion:"))
                    if opcion==1:
                        pru.cargar()
                    elif opcion==2:
                        pru.listar()
                    elif opcion==3:
                        pru.consultar()
                    elif opcion==4:
                        pru.modificar()
                    elif opcion==5:
                        print("Gracias por usar nuestro programa") 
                        return print
                    elif opcion>5:
                        print("Por favor ingrese un opcion del menu")
            except ValueError:
                        print("-----------------------")
                        print("Debe ingresar números.")
            respuesta=input("Desea ingresar otro numero?[si/no]:")
            if respuesta=="no":
                print("Gracias por usar nuestro programa")  
                break 

     #cargar
    def cargar(lit):
        import mysql.connector
        conexion1=mysql.connector.connect(host="localhost", user="root", passwd="", database="goleadores")
        cursor1=conexion1.cursor()
        sql="insert into goleadores(Apellido, Nombre, Equipo, Goles) values (%s, %s, %s , %s)"
        try:
            canti=int(input("Ingrese la cantidad de jugadores a cargar:"))
            for x in range(canti):
                print("-----------------")
                print("Siguiente jugador")
                ape=input("Ingrese el apellido:")
                nom=input("Ingrese el nombre:")
                equi=input("Ingrese su equipo:")
                goles=int(input("Ingrese la cantidad de goles:"))
                datos=(ape,nom,equi,goles)
                cursor1.execute(sql, datos)
                conexion1.commit()
            conexion1.close()
        except ValueError:
            print("Debe ingresar un numero")

     #listar
    def listar(muy):
        import mysql.connector
        conexion1=mysql.connector.connect(host="localhost",user="root", passwd="", database="goleadores")
        cursor1=conexion1.cursor()
        cursor1.execute("select Apellido, Nombre, Equipo, Goles from goleadores ORDER BY Goles DESC")
        for fila in cursor1:
            print(fila)
        conexion1.close() 


     # Modificar
    def modificar(q):
        opcion=0
        while True:
            try:
                consu=input("Ingrese el apellido del jugador a consultar:")
                conexion1=pymysql.connect(host="localhost",user="root", passwd="", database="goleadores")
                cursor1=conexion1.cursor()
                mi_query = 'SELECT * FROM goleadores WHERE Apellido="%s"'%(consu)
                test=cursor1.execute(mi_query)
                if test> 0:
                    print(cursor1.fetchall())
                    while opcion!=5:
                        print("--------------------------")
                        print("Que desea modificar?")
                        print("1.Apellido")
                        print("2.Nombre")
                        print("3.Equipo")
                        print("4.Goles")
                        print("5.Volver")
                        opcion=int(input("Ingrese su opcion:"))
                        if opcion==1:
                            nuevo=input("Ingrese el nuevo dato:")
                            conexion1=pymysql.connect(host="localhost",user="root", passwd="", database="goleadores")
                            cursor1=conexion1.cursor()
                            mi_query1 = "UPDATE goleadores SET Apellido='%s' WHERE Apellido='%s'"%(nuevo, consu)
                            cursor1.execute(mi_query1)
                            conexion1.commit()
                            cursor1.close()
                            print("Cambio generado")
                        elif opcion==2:
                            nuevo=input("Ingrese el nuevo dato:")
                            conexion1=pymysql.connect(host="localhost",user="root", passwd="", database="goleadores")
                            cursor1=conexion1.cursor()
                            mi_query2 = 'UPDATE goleadores SET Nombre="%s" WHERE Apellido="%s"'%(nuevo, consu)
                            cursor1.execute(mi_query2)
                            conexion1.commit()
                            cursor1.close()
                            print("Cambio generado")
                        elif opcion==3:
                            nuevo=input("Ingrese el nuevo dato:")
                            conexion1=pymysql.connect(host="localhost",user="root", passwd="", database="goleadores")
                            cursor1=conexion1.cursor()
                            mi_query3 = 'UPDATE goleadores SET Equipo="%s" WHERE Apellido="%s"'%(nuevo, consu)
                            cursor1.execute(mi_query3)
                            conexion1.commit()
                            cursor1.close()
                            print("Cambio generado")
                        elif opcion==4:
                            nuevo=input("Ingrese el nuevo dato:")
                            conexion1=pymysql.connect(host="localhost",user="root", passwd="", database="goleadores")
                            cursor1=conexion1.cursor()
                            mi_query4 = 'UPDATE goleadores SET Goles="%s" WHERE Apellido="%s"'%(nuevo, consu)
                            cursor1.execute(mi_query4)
                            conexion1.commit()
                            cursor1.close()
                            print("Cambio generado")
                        elif opcion==5:
                            q.menu()
                        elif opcion>5:
                            print("Por favor ingrese un opcion del menu")
                else:
                    print("No se encuentra en la tabla")    
            except ValueError:
                        print("-----------------------")
                        print("Debe ingresar números.")
            respuesta=input("Desea modificar otro jugador?[si/no]:")
            if respuesta=="no":
                q.menu() 

    # consultar
    def consultar(z):
        import pymysql
        consu=input("Ingrese el apellido del jugador a consultar:")
        conexion1=pymysql.connect(host="localhost",user="root", passwd="", database="goleadores")
        cursor1=conexion1.cursor()
        mi_query = 'SELECT * FROM goleadores WHERE Apellido="%s"'%(consu)
        test=cursor1.execute(mi_query)
        if test> 0:
            print(cursor1.fetchall())
        else:
            print("No se encuentra en la base")
        cursor1.close()
    


#Programa
persona1=goleadores()
persona1.menu()