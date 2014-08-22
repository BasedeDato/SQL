--
-- MySQL 5.5.38
-- Fri, 22 Aug 2014 20:06:02 +0000
--

CREATE TABLE `Contacto` (
   `Cuit` int(11),
   `Telefono` decimal(10,0),
   `Cumpleanos` date,
   `ID_Contacto` int(3) not null,
   `Nombre_Contacto` varchar(20),
   `Email` varchar(60),
   PRIMARY KEY (`ID_Contacto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- [Table `Contacto` is empty]