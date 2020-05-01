#include <stdio.h>
#include <stdlib.h>
#include <string.h> 
#include <mysql/mysql.h>

static char *host = "localhost"; //server
static char *user = "root";
static char *pass = "root";
static char *dbname = "EMPLEADOS";

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
	

	
	con= mysql_init(NULL);

	//conexión a la base de datos
	if((mysql_real_connect(con, host, user, pass, dbname, port, unix_socket, flag)))
	{
		
		ires=mysql_query(con, "SELECT * FROM TEMPLE WHERE NUMDE= 110");
				printf("\n resultado ires: %d\n", ires);
		
		if(!ires)
		{
			//obtener el resultset
			res = mysql_store_result(con);

			cont=0;	
			while(row = mysql_fetch_row(res))
			{
			 printf("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n",row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]);
			cont++;	
			}
			
			printf("\n %d filas \n\n",cont);

			//libera la  variable res y cierra la conexión
			mysql_free_result(res);
			mysql_close(con);
		}
		else{
			 printf("Fallo en query\n"); 
			 fprintf(stderr,"\nERROR:%s[%d]\n", mysql_error(con), mysql_errno(con));
			 exit(1);
		}
	
	}
	else{
	 printf("Fallo en Conexion\n");  	 
	 fprintf(stderr,"\nERROR:%s[%d]\n", mysql_error(con), mysql_errno(con));
	 mysql_close(con);
	 exit(1);
	}
	
	return EXIT_SUCCESS;
	//return 0; 
}
