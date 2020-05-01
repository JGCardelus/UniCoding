# Pasos
## Preparar el entorno
Instalar pyscreenshot y pillow, para hacer las capturas de pantalla

`
pip3 install pyscreenshot
pip3 install pillow
`

## Crear las bases de datos necesarias
Abrir una terminal desde *esta* carpeta y meterte en mysql (hay que crear una base de datos en la práctica)
`
sudo mysql -u root -p
`

Una vez dentro ejecutar query.sql, que crea la base de datos, las tablas y los archivos
`
\. query.sql;
`
Y salir de mysql
`
exit;
`

## Hacer la práctica
```
sudo python3 executer.py
```

Y todos los screenshots que necesitas aparecen en la carpeta *photos* :)
