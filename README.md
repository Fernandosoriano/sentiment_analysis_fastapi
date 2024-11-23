Sentiment Analysis API

Este proyecto es una API desarrollada para analizar sentimientos. Utiliza FastAPI como framework web y una base de datos PostgreSQL para almacenar los datos.
Está completamente containerizado con Docker y se gestiona con Alembic para las migraciones de base de datos.

Requisitos previos
Antes de empezar, asegúrate de tener instalado lo siguiente:

1.-Docker
2.-Docker Compose
3.-Git
4.-Su editor de código de preferencia

Cómo usar este proyecto:

1. Clonar el repositorio
Clona este repositorio en tu máquina local:

git clone https://github.com/Fernandosoriano/sentiment_analysis_fastapi.git

2. Configurar las variables de entorno
Crea un archivo .env en la raíz del proyecto, puede basarse en el contenido que hay dentro del
.env.example, haga una copia del mismo (puede usar: cp .env.example .env) y ponga sus propias
credenciales para la creación de su BD.


3. Construir y levantar los contenedores
Ejecuta el siguiente comando para construir y levantar los servicios de la aplicación y la base de datos:

docker-compose up --build

4. Realizar las migraciones
Una vez que los contenedores estén corriendo, favor de ingresar al contenedor de la aplicación para
ejecutar las migraciones. Para ingresaar al contenedor, ejecute el siguiente comando:

docker exec -it sentimient_analysis-app-1 bash

Una vez que esté dentro del contenedor, realice las migraciones, con el siguiente comando:

alembic upgrade head

Con este comando ud. estaría creando las tablas necesarias en la base de datos.

A continuación ud podria empezar a probar los siguientes endpoint de la api:

1.-http://127.0.0.1:8000/analyze_sentiment/ (POST)
2.-http://127.0.0.1:8000/sentiments/   (GET)
3.-http://127.0.0.1:8000/sentiments/ (DELETE)

De igual manera le proporcionre una colección de Postman en el correo electrónico con la que pueda testear directamente cada
endpoint.





















