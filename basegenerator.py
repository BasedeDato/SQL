import re
import random
import string
from faker import Faker
fake = Faker()
act_lst = []
city_lst = []
client_lst = []
mach_lst = []
vend_lst = []
zonas = { 1: 'noroeste', 2: 'noreste', 2: 'norte', 3: 'sur', 4: 'este', \
        5: 'oeste', 6: 'sudeste', 7: 'sudoeste'}

def repeat_c_name(name, lst):
    for each in lst:
        if name == each.name:
            return True
        else:
            return False

def draw_name():
    name = fake.name()
    if client_lst == []:
        return name
    if repeat_c_name(name, client_lst):
        draw_name()
    else:
        return str(name)

def draw_city():
    name = fake.city()
    assert(name!=None)
    if city_lst == []:
        return name
    if repeat_c_name(name, city_lst):
        draw_city()
    else:
        return str(name)

def draw_job():
    name = fake.job()
    if act_lst == []:
        return name
    if repeat_c_name(name, act_lst) or ',' in name:
        draw_job()
    else:
        return str(name)

class Cliente():
    def __init__(self):
        self.cuit = None
        self.name = None
        self.razonsocial = None
        self.id_ciudad = None
        self.id_prov = None
        self.id_act = None
        self.codigopostal = None

class Ciudad():
    def __init__(self):
        self.id = None
        self.name = None
        self.id_zona = None
        self.id_prov = None

class Actividad():
    def __init__(self):
        self.id = None
        self.name = None

class Maquina():
    def __init__(self):
        self.id = None
        self.name = None

class Vendedor():
    def __init__(self):
        self.id = None
        self.name = None
        self.id_zona = None

def create_vendedor(n):
    for i in range(n):
        v = Vendedor()
        v.id = i
        v.name = draw_name()
        v.id_zona = str(random.randint(1,7))
        vend_lst.append(v)

def create_city(n):
    for i in range(n):
        c = Ciudad()
        c.id = i
        c.name = draw_city()
        c.id_prov = str(random.randint(1,23))
        c.id_zona = str(random.randint(1,7))
        city_lst.append(c)

def create_client(n):
    for i in range(n):
        c = Cliente()
        c.name = draw_name()
        c.id_ciudad = random.choice(city_lst).id  
        c.razonsocial = randomword()
        c.id_act = random.choice(act_lst).id
        c.id_prov = str(random.randint(1,23))
        c.codigopostal = str(random.randint(00000, 99999))
        c.cuit = str(random.randint(100000000,999999999))   
        client_lst.append(c)

def create_activities(n):
    for i in range(n):
        j = Actividad()
        j.id = i
        j.name = draw_job()
        act_lst.append(j)

def create_maquinas(n):
    for i in range(n):
        m = Maquina()
        m.id = i
        m.name = randomword() 
        mach_lst.append(m)

def clean_strings(lst):
    for i in range(len(lst)):
       lst[i].name = re.sub(r'[^a-zA-Z0-9]',' ', str(lst[i].name))

def randomword():
   return ''.join(random.choice(string.lowercase) for i in 
range(int(random.choice(string.digits))+1))

def randommail():
   return ''.join(random.choice(string.lowercase) for i in 
range(int(random.choice(string.digits))+int(random.choice(string.digits))))
"""
f = open('ClienteDB','w')

g = open('ContactoDB','w')

i = 1
f.write("INSERT INTO") 
f.write("`Cliente`(`Cuit`,`Nombre`,`Razon_Social`,`ID_Ciudad`,`ID_Provincia`\
        ,`ID_Actividad`,`Codigo_Postal`)")
f.write("\nVALUES\n")

g.write("INSERT INTO") 
g.write("`Contacto`(`Cuit`,`Telefono`,`Cumpleanos`,`ID_Contacto`,")
g.write("`Nombre_Contacto`,`Email`)")
g.write("\nVALUES\n")

for i in range (500):
    ciudad = str(random.randint(1,500))
    prov = str(random.randint(1,23))
    cuit = str(random.randint(100000000,999999999))   
    telefono = str(random.randint(1000000000,9999999999))   
    ano = str(random.randint(1900,2008))
    mes = str(random.randint(1,12))
    dia = str(random.randint(1,31))
    cumpleanos = ano +"-"+ mes +"-"+ dia
    f.write("('"+str(cuit)+"','"+randomword()+"','"+randomword()+"','"+
            randomword()+ "' ,'"+ prov + "' , '" + ciudad + "' ), \n")
    g.write("('"+str(cuit)+"','"+telefono+"','"+cumpleanos+"','"+
            str(i)+ "' ,'"+ randomword() + "' , '" + randommail()  + "@"+ 
randommail()+"' ), \n")

print f


g.close
f.close
"""

def generate_date():
    ano = str(random.randint(1900,2008))
    mes = str(random.randint(1,12))
    dia = str(random.randint(1,31))
    return ano +"-"+ mes +"-"+ dia


def dump_act_table():
    f = open('bases/ActivdadDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Activdad`(`ID_Actividad`,`Nombre_Actividad`)")
    f.write("\nVALUES\n")
    for i in range(len(act_lst)):
        f.write("('"+ str(act_lst[i].id) + "','" + str(act_lst[i].name) + "' ), \n")

    f.close()

def dump_commun_table():
    f = open('bases/CommunicationDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Comunicaciones`(`ID_Comunicacion`,`ID_Actividad`,`ID_Vendedor`)")
    f.write("\nVALUES\n")
    for i in range(len(vend_lst)):
        f.write("('"+ str(i) + "','" + str(random.choice(act_lst).id) + "'\
                ,'"+ str(random.randint(0,200)) +"'), \n")

    f.close()

def dump_city_table():
    f = open('bases/CiudadDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Ciudad`(`ID_Ciudad`,`Nombre_Ciudad`,`ID_Zona`,`ID_Provincia`)")
    f.write("\nVALUES\n")
    for i in range(len(city_lst)):
        f.write("('"+ str(city_lst[i].id) + "','" + str(city_lst[i].name) + "'\
                ,'"+ str(random.randint(1,7)) +"','"+str(city_lst[i].id_prov)+"'), \n")

    f.close()

def dump_vendedor_table():
    f = open('bases/VendedorDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Vendedor`(`ID_Vendedor`,`Nombre_Vendedor`,`ID_Zona`)")
    f.write("\nVALUES\n")
    for i in range(len(vend_lst)):
        f.write("('"+ str(vend_lst[i].id) + "','" + str(vend_lst[i].name) + "'\
                ,'"+ str(random.randint(1,7)) +"'), \n")

    f.close()

def dump_maquina_table():
    f = open('bases/MaquinaDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Maquina`(`ID_Maquina`,`Nombre_Maquina`)")
    f.write("\nVALUES\n")
    for i in range(len(mach_lst)):
        f.write("('"+ str(mach_lst[i].id) + "','" + str(mach_lst[i].name) + "' ), \n")

    f.close()

def dump_zona_table():
    f = open('bases/ZonaDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Zona`(`ID_Zona`,`ID_Ciudad`,`Nombre_Zona`)")
    f.write("\nVALUES\n")
    for i in range(1,8):
        f.write("('"+ str(i) + "','" + str(random.randint(0,400)) + "'\
                ,'"+ str(zonas[i]) +"'), \n")

    f.close()

def dump_client_table():
    f = open('bases/ClienteDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Cliente`(`Cuit`,`Nombre`,`Razon_Social`,`ID_Ciudad`,`ID_Provincia`\
        ,`ID_Actividad`,`Codigo_Postal`)")
    f.write("\nVALUES\n")
    for i in range(len(client_lst)):
        f.write("('"+ str(client_lst[i].cuit) + "','" + str(client_lst[i].name) + "'\
                ,'"+ str(client_lst[i].razonsocial) +"','"+str(client_lst[i].id_ciudad)+"','"+ str(client_lst[i].id_prov) +"','"+ str(client_lst[i].id_act) +"',\
                '"+ str(client_lst[i].codigopostal) +"'), \n")

    f.close()

def dump_campaign_table():
    f = open('bases/CampanaDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Campana`(`ID_Campana`,`Fecha_Inicio`,`Fecha_Fin`,`ID_Actividad`,\
            `ID_Maquina`)")
    f.write("\nVALUES\n")
    for i in range(150):
        f.write("('"+ str(i) + "','" + generate_date() + "'\
                ,'"+ generate_date() +"','"+str(random.choice(act_lst).id)+"',\
                '"+ str(random.choice(mach_lst).id) +"'), \n")

    f.close()

def dump_campana_commun_table():
    f = open('bases/Campana_CommunDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Campana_Comunicacion`(`ID_Campana`,`ID_Comunicacion`)")
    f.write("\nVALUES\n")
    for i in range(len(act_lst)):
        f.write("('"+ str(random.randint(0,150)) + "','" + str(random.randint(0,200)) + "' ), \n")

    f.close()

def dump_zona_ciudad_table():
    f = open('bases/Zona_CiudadDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Zona_Ciudad`(`ID_Zona`,`ID_Ciudad`)")
    f.write("\nVALUES\n")
    for i in range(len(city_lst)):
        f.write("('"+ str(random.randint(1,7)) + "','" + str(city_lst[i].id) + "' ), \n")

    f.close()

def dump_cliente_vendedor_table():
    f = open('bases/Cliente_VendedorDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Cliente_Vendedor`(`Cuit`,`ID_Vendedor`)")
    f.write("\nVALUES\n")
    for i in range(len(vend_lst)):
        f.write("('"+ str(client_lst[i].cuit) + "','" + str(random.choice(vend_lst).id) + "' ), \n")

    f.close()

def dump_client_contacto_table():
    f = open('bases/Cliente_ContactoDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Cliente_Contacto`(`Cuit`,`ID_Contacto`)")
    f.write("\nVALUES\n")
    for i in range(len(client_lst)):
        f.write("('"+ str(client_lst[i].cuit) + "','" + str(random.randint(0,999)) + "' ), \n")

    f.close()

def dump_client_maquina_table():
    f = open('bases/Cliente_MaquinaDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Cliente_Maquina`(`Cuit`,`ID_Maquina`)")
    f.write("\nVALUES\n")
    for i in range(len(mach_lst)):
        f.write("('"+ str(random.choice(client_lst).cuit) + "','" + str(mach_lst[i].id) + "' ), \n")

    f.close()

create_activities(400)
clean_strings(act_lst)
create_city(150)
clean_strings(city_lst)
create_client(500)
clean_strings(client_lst)
create_maquinas(500)
clean_strings(mach_lst)
create_vendedor(200)
clean_strings(vend_lst)
dump_act_table()
dump_commun_table()
dump_city_table()
dump_vendedor_table()
dump_maquina_table()
dump_zona_table()
dump_client_table()
dump_campaign_table()
dump_campana_commun_table()
dump_zona_ciudad_table()
dump_cliente_vendedor_table()
dump_client_contacto_table()
dump_client_maquina_table()
