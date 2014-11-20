import re
import random
import string
from faker import Faker
fake = Faker()
comm_lst = []
act_lst = []
city_lst = []
client_lst = []
mach_lst = []
contact_lst = []
vend_lst = []
zone_lst = []
zonas = { 0: 'noroeste', 1: 'noreste', 2: 'norte', 3: 'sur', 4: 'este', \
                5: 'oeste', 6: 'sudeste', 7: 'sudoeste'}
provincias = [
"Buenos Aires",
"Catamarca",
"Chaco",
"Chubut",
"Cordoba",
"Corrientes",
"Entre Rios",
"Formosa",
"Jujuy",
"La Pampa",
"La Rioja",
"Mendoza",
"Misiones",
"Neuquen",
"Rio Negro",
"Salta",
"San Juan",
"San Luis",
"Santa Cruz",
"Santa Fe",
"Santiago del Estero",
"Tierra del Fuego",
"Tucuman"
]

zone_client = []
mach_client = []
client_vend = []
client_comm = []

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

def draw_contact():
    name = fake.name()
    if contact_lst == []:
        return name
    if repeat_c_name(name, contact_lst):
        draw_contact()
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
        return str(name)
    if repeat_c_name(name, act_lst):
        draw_job()
    else:
        return str(name)

class Provincia():
    def __init__(self, id_provincia, name):
        self.id_provincia = id_provincia
        self.name = name

class Cliente():
    def __init__(self, cuit, name, razonsocial, id_ciudad, id_prov, id_act):
        self.cuit = cuit
        self.name = name
        self.razonsocial = razonsocial
        self.id_ciudad = id_ciudad
        self.id_prov = id_prov
        self.id_act = id_act

class Ciudad():
    def __init__(self, id, name, id_prov, codigopostal):
        self.id = id
        self.name = name
        self.id_prov = id_prov
        self.codigopostal = codigopostal

class Actividad():
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Maquina():
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Vendedor():
    def __init__(self, id, name, id_zona):
        self.id = id
        self.name = name
        self.id_zona = id_zona

class Contacto():
    def __init__(self, id, name, c_cuit, cumpleanos, phone, mail):
        self.id = id
        self.name = name
        self.c_cuit = c_cuit
        self.cumpleanos = cumpleanos
        self.phone = phone
        self.mail = mail

class Comunicacion():
    def __init__(self, id, id_vend, id_act, comunicacion):
        self.id = id
        self.id_vendedor = id_vend
        self.id_actividad = id_act
        self.comunicacion_realizada = comunicacion

class Zona():
    def __init__(self, id, name):
        self.id = id
        self.name = name

def random_cuit():
    return str(random.randint(000000000,999999999))

def random_zone_id():
    return str(random.randint(0,7))

def random_province_id():
    return str(random.randint(0,len(provincias)))

def random_c_post():
    return str(random.randint(00000,99999))

def random_city_name():
    return (random.choice(city_lst).name)

def random_city_id():
    return (random.choice(city_lst).id)

def random_act_id():
    return (random.choice(act_lst).id)

def random_phone():
    return (str(random.randint(0000000001, 9999999999)))


def create_vendedor(n):
    for i in range(20):
        v = Vendedor(i, draw_name(), random_zone_id())
        #v.id = i
        #v.name = draw_name()
        #v.id_zona = str(random.randint(1,7))
        vend_lst.append(v)

def create_city(n):
    for i in range(n):
        c = Ciudad(i, draw_city(), random_province_id(),
                    random_c_post())
        #c.id = i
        #c.name = draw_city()
        #c.id_prov = str(random.randint(0,22))
        #c.codigopostal = str(random.randint(00000, 99999))
        #c.id_zona = str(random.randint(1,7))
        city_lst.append(c)

def create_client(n):
    for i in range(n):
        c = Cliente(random_cuit(), draw_name(), randomword(), random_city_id(), 
                    random_province_id(), random_act_id())
        #c.name = draw_name()
        #c.id_ciudad = random.choice(city_lst).id  
        #c.razonsocial = randomword()
        #c.id_act = random.choice(act_lst).id
        #c.id_prov = str(random.randint(1,23))
        #c.cuit = str(random.randint(100000000,999999999))   
        client_lst.append(c)

def create_contacto(n):
    for i in range(len(client_lst)):
        c = Contacto(i, draw_contact(), random_cuit(), fake.date(), random_phone(), fake.safe_email())
        #c.name = draw_name()
        #c.id = i
        #c.c_cuit = client_lst[i].cuit
        #c.cumpleanos = fake.date() 
        #c.mail = fake.safe_email()
        contact_lst.append(c)

def create_activities(n):
    for i in range(n):
        j = Actividad(i, draw_job())
        #j.id = i
        #j.name = draw_job()
        act_lst.append(j)

def create_maquinas(n):
    for i in range(5):
        m = Maquina(i, randomword())
        #m.id = i
        #m.name = randomword() 
        mach_lst.append(m)

def create_comunicacion(n):
    for i in range(len(vend_lst)):
        c = Comunicacion(i, vend_lst[i].id, act_lst[i].id, fake.date())
        comm_lst.append(c)

def create_maquina_zone():
    m = Maquina(len(mach_lst), "Pipita-9000")
    mach_lst.append(m)
    for i in range(8):
        c = random.choice(client_lst)
        mach_client.append((c.cuit, m.id))
        zone_client.append((c.cuit, i))
    for i in range(len(client_lst)):
        mach_client.append((client_lst[i].cuit, random.choice(mach_lst).id))
    for i in range(len(client_lst)):
        zone_client.append((client_lst[i].cuit, random_zone_id()))

def create_client_comm_vend():
    for i in range(len(client_lst)):
        c = client_lst[i]
        v = random.choice(vend_lst)
        client_vend.append((c.cuit, v.id))
        com = Comunicacion(i, v.id, c.id_act, fake.date())
        comm_lst.append(com)
        client_comm.append((c.cuit, com.id))
    for i in range(500):
        c = random.choice(client_lst)
        v = random.choice(vend_lst)
        client_vend.append((c.cuit, v.id))
        com = Comunicacion(i, v.id, c.id_act, fake.date())
        comm_lst.append(com)
        client_comm.append((c.cuit, com.id))

        
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
    f.write("`Actividad`(`Nombre_Actividad`)")
    f.write("\nVALUES\n")
    for i in range(len(act_lst)):
        f.write("('"+ str(act_lst[i].name) + "' ), \n")

    f.write("\n")
    f.close()

def dump_commun_table():
    f = open('bases/CommunicationDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Comunicaciones`(`ID_Actividad`,`ID_Vendedor`,`Comunicacion_Realizada`)")
    f.write("\nVALUES\n")
    for i in range(len(comm_lst)):
        f.write("('"+ str(comm_lst[i].id_actividad) + "'\
                ,'"+ str(comm_lst[i].id_vendedor) +"','"+comm_lst[i].comunicacion_realizada+"'), \n")

    f.write("\n")
    f.close()

def dump_city_table():
    f = open('bases/CiudadDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Ciudad`(`Nombre_Ciudad`,`ID_Provincia`,\
            `Codigo_Postal`)")
    f.write("\nVALUES\n")
    for i in range(len(city_lst)):
        f.write("('" + str(city_lst[i].name) +"','"+str(city_lst[i].id_prov)+
                "','"+str(city_lst[i].codigopostal)+"'), \n")

    f.write("\n")
    f.close()

def dump_city_province_table():
    f = open('bases/Cuidad_ProvinciaDB', 'w')
    f.write("INSERT INTO")
    f.write("`Ciudad_Provincia`(`ID_Ciudad`,`ID_Provincia`)")
    f.write("\nVALUES\n")
    for i in range(len(city_lst)):
        f.write("('"+str(city_lst[i].id)+"','"+str(city_lst[i].id_prov)+"'), \n")
    
    f.write("\n")
    f.close()

def dump_provincia_table():
    f = open('bases/ProvinciaDB', 'w')
    f.write("INSERT INTO")
    f.write("`Provincia`(`Nombre_Provincia`)")
    f.write("\nVALUES\n")
    for i in range(len(provincias)):
        f.write("('"+str(provincias[i])+"'), \n")

    f.write("\n")
    f.close()

def dump_vendedor_table():
    f = open('bases/VendedorDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Vendedor`(`Nombre_Vendedor`,`ID_Zona`)")
    f.write("\nVALUES\n")
    for i in range(len(vend_lst)):
        f.write("('"+ str(vend_lst[i].name) + "'\
                ,'"+ str(vend_lst[i].id_zona) +"'), \n")

    f.write("\n")
    f.close()

def dump_maquina_table():
    f = open('bases/MaquinaDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Maquina`(`Nombre_Maquina`)")
    f.write("\nVALUES\n")
    for i in range(len(mach_lst)):
        f.write("('" + str(mach_lst[i].name) + "' ), \n")

    f.write("\n")
    f.close()

def dump_zona_table():
    f = open('bases/ZonaDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Zona`(`Nombre_Zona`)")
    f.write("\nVALUES\n")
    for each in zonas:
        f.write("('"+ str(zonas[each]) +"'), \n")

    f.write("\n")
    f.close()

def dump_client_table():
    f = open('bases/ClienteDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Cliente`(`Cuit`,`Nombre`,`Razon_Social`,`ID_Ciudad`,`ID_Provincia`\
        ,`ID_Actividad`)")
    f.write("\nVALUES\n")
    for i in range(len(client_lst)):
        f.write("('"+ str(client_lst[i].cuit) + "','" + str(client_lst[i].name) + "'\
                ,'"+ str(client_lst[i].razonsocial) +"','"+str(client_lst[i].id_ciudad)+"','"+ str(client_lst[i].id_prov) +"','"+ str(client_lst[i].id_act) +"'), \n")

    f.write("\n")
    f.close()

def dump_contacto_table():
    f = open('bases/ContactoDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Contacto`(`Cuit`,`Telefono`,`Cumpleanos`,`Nombre_Contacto`,`Email`\
        ,`ID_Contacto`)")
    f.write("\nVALUES\n")
    for i in range (len(contact_lst)):
        f.write("('"+str(contact_lst[i].c_cuit)+"','"+str(contact_lst[i].phone)+"','"+str(contact_lst[i].cumpleanos)+"','"+str(contact_lst[i].name)+"','"+str(contact_lst[i].mail)+"','"+str(contact_lst[i].id)+"'), \n")
    f.write("\n")
    f.close()

def dump_campaign_table():
    f = open('bases/CampanaDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Campana`(`Fecha_Inicio`,`Fecha_Fin`,`ID_Actividad`,\
            `ID_Maquina`)")
    f.write("\nVALUES\n")
    for i in range(150):
        f.write("('" + generate_date() + "'\
                ,'"+ generate_date() +"','"+str(random.choice(act_lst).id)+"',\
                '"+ str(random.choice(mach_lst).id) +"'), \n")

    f.write("\n")
    f.close()

def dump_campana_commun_table():
    f = open('bases/Campana_CommunDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Campana_Comunicacion`(`ID_Campana`,`ID_Comunicacion`)")
    f.write("\nVALUES\n")
    for i in range(len(act_lst)):
        f.write("('"+ str(random.randint(0,150)) + "','" + str(random.choice(comm_lst).id) + "' ), \n")

    f.write("\n")
    f.close()

def dump_zona_ciudad_table():
    f = open('bases/Zona_CiudadDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Zona_Ciudad`(`ID_Zona`,`ID_Ciudad`)")
    f.write("\nVALUES\n")
    for i in range(len(zone_lst)):
        f.write("('"+ str(zone_lst[i].id) + "','" + str(zone_lst[i].id_ciudad) + "' ), \n")

    f.write("\n")
    f.close()

def dump_cliente_vendedor_table():
    f = open('bases/Cliente_VendedorDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Cliente_Vendedor`(`Cuit`,`ID_Vendedor`)")
    f.write("\nVALUES\n")
    for i in range(len(client_vend)):
        f.write("('"+ str(client_vend[i][0]) + "','" + str(client_vend[i][1]) + "' ), \n")

    f.write("\n")
    f.close()

def dump_client_contacto_table():
    f = open('bases/Cliente_ContactoDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Cliente_Contacto`(`Cuit`,`ID_Contacto`)")
    f.write("\nVALUES\n")
    for i in range(len(client_lst)):
        f.write("('"+ str(client_lst[i].cuit) + "','" + str(random.randint(0,999)) + "' ), \n")

    f.write("\n")
    f.close()

def dump_client_maquina_table():
    f = open('bases/Cliente_MaquinaDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Cliente_Maquina`(`Cuit`,`ID_Maquina`,`Cantidad`)")
    f.write("\nVALUES\n")
    for i in range(len(mach_client)):
        f.write("('"+ str(mach_client[i][0]) + "','" + str(mach_client[i][1]) + "','" + str(random.randint(0, 200)) +"' ), \n")

    f.write("\n")
    f.close()

def dump_cliente_zona():
    f = open('bases/Cliente_ZonaDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Cliente_Zona`(`Cuit`,`ID_Zona`)")
    f.write("\nVALUES\n")
    for i in range(len(zone_client)):
        f.write("('"+ str(zone_client[i][0]) + "','" + str(zone_client[i][1]) + "' ), \n")
    f.write("\n")
    f.close()

def dump_maquina_campana():
    f = open('bases/Campana_MaquinaDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Campana_Maquina`(`ID_Campana`,`ID_Maquina`)")
    f.write("\nVALUES\n")
    for i in range(300):
        f.write("('"+ str(random.randint(0,150)) + "','" + str(random.choice(mach_lst).id) + "' ), \n")
    f.write("\n")
    f.close()

def dump_cliente_actividad():
    f = open('bases/Cliente_ActividadDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Cliente_Actividad`(`Cuit`,`ID_Actividad`)")
    f.write("\nVALUES\n")
    for i in range(len(client_lst)):
        f.write("('"+ str(client_lst[i].cuit) + "','" + str(random.choice(client_lst).id_act) + "' ), \n")
    f.write("\n")
    f.close()

def dump_client_commun():
    f = open('bases/Cliente_ComunicacionDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Cliente_Comunicaciones`(`Cuit`,`ID_Comunicacion`)")
    f.write("\nVALUES\n")
    for i in range(len(client_comm)):
        f.write("('"+ str(client_comm[i][0]) + "','" + str(client_comm[i][1]) + "' ), \n")
    f.write("\n")
    f.close()

def dump_ciudad_provincia():
    f = open('bases/Ciudad_ProvinciaDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Cuidad_Provincia`(`ID_Ciudad`,`ID_Provincia`)")
    f.write("\nVALUES\n")
    for i in range(len(city_lst)):
        f.write("('"+ str(city_lst[i].id) + "','" + str(random.randint(0,23)) + "' ), \n")
    f.write("\n")
    f.close()

def dump_client_city():
    f = open('bases/Cliente_CiudadDB', 'w')
    f.write("INSERT INTO") 
    f.write("`Cliente_Ciudad`(`Cuit`,`ID_Ciudad`)")
    f.write("\nVALUES\n")
    for i in range(len(client_lst)):
        f.write("('"+ str(client_lst[i].cuit) + "','" + str(client_lst[i].id_ciudad) + "' ), \n")
    f.write("\n")
    f.close()


create_activities(200)
clean_strings(act_lst)
create_city(150)
clean_strings(city_lst)
create_client(500)
clean_strings(client_lst)
create_maquinas(500)
clean_strings(mach_lst)
create_vendedor(200)
clean_strings(vend_lst)
create_contacto(300)
clean_strings(contact_lst)
create_client_comm_vend()
create_maquina_zone()
dump_act_table()
dump_commun_table()
dump_city_table()
dump_provincia_table()
dump_vendedor_table()
dump_maquina_table()
dump_zona_table()
dump_client_table()
dump_campaign_table()

dump_city_province_table()

dump_contacto_table()
dump_client_contacto_table()
dump_client_maquina_table()
dump_cliente_zona()
dump_cliente_actividad()
dump_client_commun()
dump_client_city()
dump_cliente_vendedor_table()

dump_campana_commun_table()
dump_maquina_campana()
