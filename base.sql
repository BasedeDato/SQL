--
-- MySQL 5.5.38
-- Mon, 25 Aug 2014 17:43:55 +0000
--

CREATE TABLE `Ciudades` (
   `ID_Ciudad` int(3) not null,
   `Nombre_Ciudad` varchar(20),
   `ID_Provincia` int(3),
   `Codigo_Postal` decimal(5,0),
   PRIMARY KEY (`ID_Ciudad`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Ciudades` (`ID_Ciudad`, `Nombre_Ciudad`, `ID_Provincia`, 
`Codigo_Postal`) VALUES 
('0', 'qqlcgw', '10', '7226'),
('1', 'u', '2', '7740'),
('2', 'neemgo', '23', '9440'),
('3', 'gmv', '14', '8683'),
('4', 'pivkwdfgar', '18', '2452'),
('5', 'hjerpe', '6', '9789'),
('6', 'ygkcnlu', '10', '9234'),
('7', 'gipujm', '1', '9939'),
('8', 'nnhoofujr', '21', '5247'),
('9', 'gcggqm', '23', '1618'),
('10', 'wh', '4', '3941'),
('11', 'pputcb', '18', '1335'),
('12', 'cps', '2', '8708'),
('13', 'jldbwxw', '23', '2624'),
('14', 'qgz', '11', '8863'),
('15', 'ymh', '15', '1630'),
('16', 'iqsx', '6', '8859'),
('17', 'hb', '13', '2099'),
('18', 'doywzskrza', '3', '9561'),
('19', 'qfqolbqesz', '8', '5451'),
('20', 'bjdiis', '21', '3670'),
('21', 'yindu', '4', '6284'),
('22', 'lriyjr', '10', '7908'),
('23', 'g', '15', '7160'),
('24', 'aeh', '16', '9327'),
('25', 'aov', '11', '8954'),
('26', 'iekabwwa', '14', '9314'),
('27', 'ijncydvmhm', '10', '6618'),
('28', 'fydkifkqrw', '1', '6672'),
('29', 'wrszwoxc', '7', '6580'),
('30', 'fqo', '14', '9675'),
('31', 'npttqcx', '19', '1144'),
('32', 'fk', '14', '6006'),
('33', 'dfkmnkmi', '8', '7304'),
('34', 'h', '3', '8599'),
('35', 'u', '9', '4130'),
('36', 'innmyobw', '20', '6184'),
('37', 'gdfpf', '20', '9573'),
('38', 'esz', '14', '5606'),
('39', 'szm', '5', '3667'),
('40', 'kwva', '8', '8831'),
('41', 'pdotdtbzvv', '21', '1607'),
('42', 'wreher', '1', '1773'),
('43', 'bwkmso', '13', '2279'),
('44', 'iussxucdod', '3', '3285'),
('45', 'cbggs', '21', '5325'),
('46', 'lglhp', '21', '2616'),
('47', 'rjmcuayl', '13', '4642'),
('48', 'k', '3', '8069'),
('49', 'ux', '5', '4286'),
('50', 'bmhu', '10', '8971'),
('51', 'iybl', '8', '3717'),
('52', 'niewmzv', '3', '7578'),
('53', 'ffipfal', '8', '9991'),
('54', 'agnbejwxw', '20', '6531'),
('55', 'quxiedtof', '8', '5495'),
('56', 'lwjhvme', '5', '3460'),
('57', 'lbflbgrwyy', '2', '2588'),
('58', 'md', '16', '3929'),
('59', 'uslbgkxf', '3', '3613'),
('60', 'dup', '11', '7971'),
('61', 'ktkfsr', '6', '1276'),
('62', 'asie', '16', '7978'),
('63', 'fxjy', '13', '1520'),
('64', 'tb', '5', '6151'),
('65', 'lksfftm', '11', '2712'),
('66', 'x', '20', '3511'),
('67', 'rmkx', '8', '9262'),
('68', 'cz', '1', '7575'),
('69', 's', '19', '6234'),
('70', 'x', '3', '8091'),
('71', 'gr', '3', '6582'),
('72', 'klog', '7', '2751'),
('73', 'grbk', '7', '6008'),
('74', 'hkuwzqs', '19', '2323'),
('75', 'x', '2', '3522'),
('76', 'v', '19', '4441'),
('77', 'ok', '12', '2828'),
('78', 'uhrysxegxa', '21', '4250'),
('79', 'nhvvexzo', '13', '5281'),
('80', 'chhm', '13', '3424'),
('81', 'ifmngfuic', '7', '2969'),
('82', 'b', '17', '7912'),
('83', 'tokewmdd', '5', '1665'),
('84', 'uupgbg', '7', '2751'),
('85', 'iyn', '16', '4538'),
('86', 'zhta', '14', '9330'),
('87', 'dkqggaojh', '10', '5822'),
('88', 'nyikorltnc', '20', '4974'),
('89', 'dznzygzi', '8', '9538'),
('90', 'kbyigdje', '15', '1194'),
('91', 'fomfssx', '16', '9633'),
('92', 'yqxgwlee', '18', '9260'),
('93', 'mhqenjkfyk', '18', '5714'),
('94', 'elncnnh', '4', '9712'),
('95', 'hsi', '1', '2049'),
('96', 'opkce', '5', '2732'),
('97', 'sdsy', '8', '2691'),
('98', 'iwjqeiid', '6', '1276'),
('99', 'phschxm', '16', '7034');

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

INSERT INTO `Provincia` (`Provincia`, `ID_Provincia`) VALUES 
('Buenos_Aires', '1'),
('Catamarca', '2'),
('Chaco', '3'),
('Chubut', '4'),
('Córdoba', '5'),
('Corrientes', '6'),
('Entre Rios', '7'),
('Formosa', '8'),
('Jujuy', '9'),
('La Pampa', '10'),
('La Rioja', '11'),
('Mendoza', '12'),
('Misiones', '13'),
('Neuquén', '14'),
('Río Negro', '15'),
('Salta', '16'),
('San Juan', '17'),
('San Luis', '18'),
('Santa Cruz', '19'),
('Santa Fe', '20'),
('Santiago del Estero', '21'),
('Tierra del Fuego', '22'),
('Tucumán', '23');