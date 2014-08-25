import random
import string

def randomword():
   return ''.join(random.choice(string.lowercase) for i in 
range(int(random.choice(string.digits))+1))

f = open('CiudadesDB', 'w')


#INSERT INTO `Ciudades` (`ID_Ciudad`, `Nombre_Ciudad`, `ID_Provincia`, 
#`Codigo_Postal`) VALUES 
#('0', 'lalalala', '1', '5000');

i = 1
f.write("INSERT INTO") 
f.write("`Ciudades`(`ID_Ciudad`,`Nombre_Ciudad`,`ID_Provincia`,`Codigo_Postal`)"
)
f.write("\nVALUES\n")

for i in range (499):
    x = str(random.randint(1,23))
    y = str(random.randint(1000,9999))
    f.write("('"+str(i+1)+"','"+randomword()+"','"+x+"','"+y+"'),\n")

print f

f.close


