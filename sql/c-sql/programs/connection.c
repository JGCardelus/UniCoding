#include <stdio.h>
#include <stdlib.h>
#include <mysql/mysql.h>

static char *host = "localhost"; // localhost o IP
static char *user = "root";
static char *pass = "889927";
static char *dbname = "EMPLEADOS";

unsigned int port = 3306;
static char *unix_socket = NULL;
unsigned int flag = 0;

int main()

{

	MYSQL *con;

	con= mysql_init(NULL);
	if( (mysql_real_connect(con, host, user, pass, dbname, port, unix_socket, flag)) )
	{
	 printf("Conexion Correcta\n");
	 printf("Adios usuario: %s\n", user); 
	}
	else
	{
	 printf("Fallo en Conexion\n");
	 //printf("\nMensaje ERROR:%s\n", mysql_error(con)); //display mensaje del error
	 //printf("\nCódigo ERROR:[%d]\n", mysql_errno(con)); //display código del error
	 fprintf(stderr,"\nERROR:%s[%d]\n", mysql_error(con), mysql_errno(con)); //imprime error a stderr
	}

	 mysql_close(con);

		
	return EXIT_SUCCESS;
}