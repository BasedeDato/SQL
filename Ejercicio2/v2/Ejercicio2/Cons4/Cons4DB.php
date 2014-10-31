<html>
	<head></head>
	<body>

	<?php
                $connection = mysql_connect("kali", "db2014_g09", "margarita88") or die("¡Error al conectarse!".mysql_error());
		
		$vendedor = $_GET['Vendedor'];
		
		if($vendedor && $vendedor != "Seleccione Un Vendedor"){
			$query = "select ID_Vendedor, count(Comunicacion_Realizada) as cant_com_realizada, month(Comunicacion_Realizada) as mes
						from Comunicaciones
						where date(Comunicacion_Realizada) < date(now()) and ID_Vendedor=(Select ID_Vendedor from Vendedor
						where Nombre_Vendedor = '".$vendedor."')
						group by ID_Vendedor, month(Comunicacion_Realizada)";
		}else{
			echo "Vendedor no seleccionado<br>";
			echo "Vuelva atras y seleccione un vendedor";
		}
		mysql_select_db("db2014_g09", $connection);
		
		$result = mysql_query($query, $connection);
		if (!$result) {
			
			die(mysql_error());
		}

		else {
			echo "Comunicaciones Pendiente<br><br>";
			echo "<table border='1px solid'>";

			// Obtengo todos los nombres de las columnas
			$data = array(); 
			if(mysql_num_rows($result) != 0){
				$aux = Array();
				while($row = mysql_fetch_array($result)) {
					$aux = Array();
					$aux[]= $row["ID_Vendedor"];
					$aux[]= $row["cant_com_realizada"];
					$aux[]= $row["mes"];
					$data[] = $aux;
					unset($aux);
				}
				echo "<tr>ID_Vendedor  </tr>";
				echo "<tr>cant_com_realizada</tr>";
				echo "<tr>mes</tr>";
				
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
			}else {
				echo "La consulta no arrojo resultado<br><br>";
			}
		}
		
		if($vendedor && $vendedor != "Seleccione Un Vendedor"){
			$query = "select ID_Vendedor, count(Comunicacion_Realizada) as cant_com_realizada, month(Comunicacion_Realizada) as mes
					from Comunicaciones
					where date(Comunicacion_Realizada) >= date(now()) and ID_Vendedor = (Select ID_Vendedor from Vendedor where (Nombre_Vendedor = '".$vendedor."'))
					group by ID_Vendedor, month(Comunicacion_Realizada)";
		}else{
			echo "Vendedor no seleccionado<br>";
			echo "Vuelva atras y seleccione un vendedor";
		}
		mysql_select_db("db2014_g09", $connection);
		
		$result = mysql_query($query, $connection);
		if (!$result) {
			
			die(mysql_error());
		}

		else {
			echo "Comunicaciones Realizadas<br><br>";
			echo "<table border='1px solid'>";

			// Obtengo todos los nombres de las columnas
			$data = array(); 
			if(mysql_num_rows($result) != 0){
				$aux = Array();
				while($row = mysql_fetch_array($result)) {
					$aux = Array();
					$aux[]= $row["ID_Vendedor"];
					$aux[]= $row["cant_com_realizada"];
					$aux[]= $row["mes"];
					$data[] = $aux;
					unset($aux);
				}
				echo "<tr>ID_Vendedor  </tr>";
				echo "<tr>cant_com_realizada  </tr>";
				echo "<tr>mes</tr>";
				
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
