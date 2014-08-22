Consulta 1:

SELECT * 
FROM Contacto
WHERE  day(Cumpleaños) = day(now()) && month(Cumpleaños) = month(now()) 


Consulta 2:

SELECT Telefono,Email,Nombre
FROM Contacto, Cliente
WHERE  day(Cumpleaños) = day(now()) && month(Cumpleaños) = month(now()) 

