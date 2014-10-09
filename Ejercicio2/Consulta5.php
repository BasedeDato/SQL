<html>
	<head></head>
	<body>
		<?php

			$connection = mysql_connect("localhost", "root", "", "db2014_g09") or die("¡Error al conectarse!".mysql_error());
			
			$query = "SELECT id_maquina FROM (SELECT cuit FROM cliente_zona INNER JOIN zona WHERE nombre_zona = 'zona1') AS Table1 INNER JOIN maquina";
	
			mysql_select_db("db2014_g09", $connection);
			
			$result = mysql_query($query, $connection);
			if (!$result) {
				
				die(mysql_error());
			}

			else {

				echo "<table border='1px solid'>";

				// Obtengo todos los nombres de las columnas
				$data = array(); 
				if(mysql_fetch_assoc($result)){
					
					while($row = mysql_fetch_assoc($result)) {
						$data[] = $row;
					}
					
					$colNames = array_keys(reset($data));
					foreach ($colNames as $colName) {
						echo "<th> $colName </th>";
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