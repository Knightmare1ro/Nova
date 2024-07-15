<?php
    $nombre = $_POST['nombre'];
    $correo = $_POST['correo'];
    $direccion = $_POST['direccion'];
    $genero = $_POST['genero'];
    echo "Hola, $nombre! tu correo es $correo y vives en $direccion y te identificaste como $genero";
?>