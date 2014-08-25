import random
import string

def randomword():
   return ''.join(random.choice(string.lowercase) for i in 
range(int(random.choice(string.digits))+1))

def randommail():
   return ''.join(random.choice(string.lowercase) for i in 
range(int(random.choice(string.digits))+int(random.choice(string.digits))))

f = open('ClienteDB','w')

g = open('ContactoDB','w')

i = 1
f.write("INSERT INTO") 
f.write("`Cliente`(`Cuit`,`Nombre`,`Razon_Social`,`Actividad`,`ID_Provincia`,")
f.write("`ID_Ciudad`)")
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
print g

g.close
f.close