<html>
	<head></head>
	<body>

		<?php
                        $connection = mysql_connect("kali", "db2014_g09", "margarita88") or die("¡Error al conectarse!".mysql_error());
			
			$query = " select distinct table1.ID_Maquina as Maquinas_En_Todas_Zonas
						from
						((((( 
							((select ID_Maquina
							from Cliente_Maquina natural join Cliente_Zona
							where ID_Zona = 1) as table1
							inner join
							(select ID_Maquina
							from Cliente_Maquina natural join Cliente_Zona
							where ID_Zona = 2) as table2 on table1.ID_Maquina = table2.ID_Maquina)
							inner join
							(select ID_Maquina
							from Cliente_Maquina natural join Cliente_Zona
							where ID_Zona = 1) as table3 on table1.ID_Maquina = table3.ID_Maquina and table2.ID_Maquina = table3.ID_Maquina)
							inner join
							(select ID_Maquina
							from Cliente_Maquina natural join Cliente_Zona
							where ID_Zona = 1) as table4 on table1.ID_Maquina = table4.ID_Maquina and table2.ID_Maquina = table4.ID_Maquina and table3.ID_Maquina = table4.ID_Maquina)
							inner join
							(select ID_Maquina
							from Cliente_Maquina natural join Cliente_Zona
							where ID_Zona = 1) as table5 on table1.ID_Maquina = table5.ID_Maquina and table2.ID_Maquina = table5.ID_Maquina and table3.ID_Maquina = table5.ID_Maquina and table3.ID_Maquina = table5.ID_Maquina)
							inner join
							(select ID_Maquina
							from Cliente_Maquina natural join Cliente_Zona
							where ID_Zona = 1) as table6 on table1.ID_Maquina = table5.ID_Maquina and table2.ID_Maquina = table5.ID_Maquina and table3.ID_Maquina = table5.ID_Maquina and table4.ID_Maquina = table5.ID_Maquina)
						)
						";
			
			mysql_select_db("db2014_g09", $connection);
			
			$result = mysql_query($query, $connection);
			if (!$result) {
				
				die(mysql_error());
			}

			else {

				echo "<table border='1px solid'>";

				// Obtengo todos los nombres de las columnas
				$data = array(); 
				if(mysql_num_rows($result) != 0){
					$aux = Array();
					while($row = mysql_fetch_array($result)) {
						$aux = Array();
						$aux[]= $row["Maquinas_En_Todas_Zonas"];
						$data[] = $aux;
						unset($aux);
					}
					
					
					// Para cada fila
					foreach ($data as $row) {
					   echo "<tr>";
					   // Recorro cada columna
					   foreach ($row as $column) {
							// y obtengo su valor
						  echo "<td>".$column."</td>";
					   }
					   echo "</tr>";	
					}
					echo "</table>";
					echo ("Total de Datos:");
					echo(sizeof($data));
				}
				
				
				else {
					echo "La consulta no arrojo resultado";
				}
			}

				// Cerramos la conexión 
			mysql_close($connection);
		?>
	</body>
</html>
