from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Cargar las variables de entorno
load_dotenv()

# URL de conexión a PostgreSQL
DATABASE_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
)

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def test_connection():
    try:
        # Crear una sesión y probar la conexión
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        print("Conexión exitosa a la base de datos.")
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    test_connection()
