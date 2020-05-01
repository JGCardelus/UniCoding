#include <stdio.h>
#include <stdlib.h>
#include <string.h> 
#include <mysql/mysql.h>

static char *host = "localhost"; //server
static char *user = "root";
static char *pass = "root";
static char *dbname = "PRUEBA";

unsigned int port = 3306;
static char *unix_socket = NULL;
unsigned int flag = 0;

int main ()

{
	MYSQL *con; //variable para conexión
	MYSQL_RES *res; // variable que contiene los resultados de la consulta
	MYSQL_ROW row; //variable para los campos de cada registro
	int cont;
	int ires;
	char query[1024];
	
	
	con= mysql_init(NULL);

	//conexión a la base de datos
	if((mysql_real_connect(con, host, user, pass, dbname, port, unix_socket, flag)))
	{
	  printf("\nConectado!\n");
 	  
	  sprintf(query, "UPDATE ALUMNOS SET EDAD=22 WHERE NOMBRE='Pedro'");
	  ires=mysql_query(con, query);
		
	  printf("\n resultado ires: %d\n", ires);
		
		if(!ires)
		{
		  //obtener ok
		  printf("\nUpdate %lu filas\n ", (unsigned long)mysql_affected_rows(con));	

		}
		else{
		  printf("\nFallo en update\n"); 
		  fprintf(stderr,"\nERROR:%s[%d]\n", mysql_error(con), mysql_errno(con));
		}
	// cierra la conexión
	mysql_close(con);	
	}
	else{
	 printf("Fallo en Conexion\n");  	 
	 fprintf(stderr,"\nERROR:%s[%d]\n", mysql_error(con), mysql_errno(con));

	}


	return EXIT_SUCCESS;
	//return 0; 
}
