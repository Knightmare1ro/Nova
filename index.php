<!DOCTYPE html>
<html>
<head>
    <title>Formulario</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
    <div class="form-container">
        <form action="procesar.php" method="post">
            <h2>Registro de Usuario</h2>
            <label for="nombre">Nombre:</label>
            <input type="text" id="nombre" name="nombre"><br><br>

            <label for="correo">Correo:</label>
            <input type="text" id="correo" name="correo"><br><br>

            <label for="direccion">Dirección:</label>
            <input type="text" id="direccion" name="direccion"><br><br>

            <h2>¿Cuál es tu género?</h2>
            <label>Género:</label><br>
            <input type="radio" id="masculino" name="genero" value="Masculino">
            <label for="masculino">Masculino</label><br>
            <input type="radio" id="femenino" name="genero" value="Femenino">
            <label for="femenino">Femenino</label><br>
            <input type="radio" id="noDecir" name="genero" value="Prefiero no decir">
            <label for="noDecir">Prefiero no decir</label><br><br>
            
            <input type="submit" name="submit" value="Enviar">
        </form>
    </div>
</body>
</html>
