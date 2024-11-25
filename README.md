SENTIMENT ANALYSIS API.

Esta es una API RESTful construida con FastAPI que permite realizar análisis de sentimientos sobre textos proporcionados. La API utiliza el modelo de procesamiento de lenguaje natural TextBlob, que es capaz de identificar el sentimiento general de un texto y clasificarlo en tres categorías: positivo, negativo o neutral. Los resultados del análisis se almacenan en una base de datos PostgreSQL, lo que permite realizar un seguimiento y almacenamiento de los análisis realizados.

Requisitos previos.    
Antes de empezar, asegúrate de tener instalado lo siguiente:

1.-Docker (importante tenerlo actualizado a la última versión)  
2.-Docker Compose  
3.-Git  
4.-Su editor de código de preferencia  
5.-Postman  (para probar la api)

Cómo usar este proyecto:

1. CLONAR EL RESPOSITORIO.  
Clona este repositorio en tu máquina local,con el siguiente comando:

git clone https://github.com/Fernandosoriano/sentiment_analysis_fastapi.git

2. CONFIGURAR LAS VARIABLES DE ENTORNO.  
En esta parte debe crear un archivo .env en la raíz del proyecto, puede basarse en el contenido que hay dentro del
.env.example, borrando la parte de la extensión que dice .example, y a continuación rellene el archivo con sus propias credenciales para la creación de su BD,
deje fijos los siguientes valores:    
POSTGRES_HOST=database     
POSTGRES_PORT=5432

4. CONSTRUIR Y LEVANTAR LOS CONTENEDORES.  
Coloquese en una terminal que contenga el proyecto principal y ejecute el siguiente comando para construir y levantar los servicios de la aplicación y la base de datos (postgresql):   

docker-compose up --build

4. INGRESE AL CONTENEDOR DE LA API.  
Una vez que los contenedores estén corriendo, abra otra terminal e ingrese al contenedor de la aplicación;
para esto, realice los siguientes pasos:

  4.1
  liste todos los contenedores que tiene activos con el comando:

  docker ps

  4.2
  Con este comando ud. Podra saber el nombre del contenedor que esta corriendo 
  la api, una vez que conozca dicho nombre, ejecute el siguiente comando:  

docker exec -it nombre_del_contenedor_api bash  
ejemplo :docker exec -it sentimient_analysis-app-1 bash

Con este comando ud. Estara ingresando al contenedor que está corriendo la api.

5- CREACIÓN DE TABLA SENTIMENTS.  
Una vez que esté dentro del contenedor que corre la api, debe crear la tabla sentiments
necesaria para el correcto funcionamiento de la api, para eso corra el siguiente comando:

alembic revision --autogenerate -m "Create sentiment table"

6.-REALIZAR MIGRACIONES.  
Una vez creada la tabla sentiments, ahora tendrá que efectuar las migraciones a 
su BD de postgres, para hacer eso, asegurese de seguir dentro del contenedor de la api
y ejecute el siguiente comando:

alembic upgrade head


A continuación ud. Podra empezar a probar los endpoints que puede encontrar
en la siguiente carpeta: https://drive.google.com/drive/folders/1kIP8jYhl_MiMEUqa97CdQ3AI2z6GQZNN?usp=drive_link.

la cual contiene una collection de postman con los siguientes endpoints para probar:

1.-POST (http://127.0.0.1:8000/analyze_sentiment/) Permite almacenar registros de análisis de sentimiento en la base de datos.  
2.-GET (http://127.0.0.1:8000/sentiments/) Permite consultar todos los registros disponibles en la base de datos.   
3.-DELETE (http://127.0.0.1:8000/sentiments/) Permite borrar todos los registros de la base de datos.  
4.-DELETE (http://127.0.0.1:8000/sentiments/id) Permite borrar un registro específico de la base de datos por ID.

7.-IMPORTACION DE POSTMAN COLLECTION.    
En este punto tendra que importar la collection desde postman, y ahora debera ser capaz de realizar las peticiones de esta collection.


Autor: Fernando Valle Soriano





















