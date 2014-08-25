Consulta 1:

SELECT * 
FROM Contacto
WHERE  day(Cumpleaños) = day(now()) && month(Cumpleaños) = month(now()) 


Consulta 2:

SELECT Telefono,Email,Nombre
FROM Contacto, Cliente
WHERE  day(Cumpleaños) = day(now()) && month(Cumpleaños) = month(now()) 

Consulta 3: 

Select Nombre,Razon_Social
From Ciudades, Cliente
Where Cliente.ID_Ciudad = 224
and Ciudades.ID_Ciudad = 224
Order by Nombre


Consulta 4: 

Select *
From Ciudades, Provincia
Where Provincia = 'Cordoba'
And Ciudades.ID_Provincia = Provincia.ID_Provincia
Order by Codigo_Postal
