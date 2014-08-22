--
-- MySQL 5.5.38
-- Fri, 22 Aug 2014 20:09:26 +0000
--

CREATE TABLE `Ciudades` (
   `ID_Ciudad` int(3) not null,
   `Nombre_Ciudad` varchar(20),
   `ID_Provincia` int(3),
   `Codigo_Postal` decimal(5,0),
   PRIMARY KEY (`ID_Ciudad`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- [Table `Ciudades` is empty]

CREATE TABLE `Cliente` (
   `Cuit` int(11) not null,
   `Nombre` varchar(20),
   `Razon_Social` varchar(20) default 'null',
   `Actividad` varchar(20),
   `ID_Provincia` int(2),
   `ID_Ciudad` int(2),
   PRIMARY KEY (`Cuit`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- [Table `Cliente` is empty]

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

CREATE TABLE `Provincia` (
   `Provincia` varchar(20),
   `ID_Provincia` int(3) not null,
   PRIMARY KEY (`ID_Provincia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- [Table `Provincia` is empty]