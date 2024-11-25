from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# Importa settings y Base
from app.config import settings
from app.models import Base

# Configuración del logger
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Agrega la metadata del modelo
target_metadata = Base.metadata

# URL de la base de datos
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

def run_migrations_offline():
    try:
        """Configura migraciones en modo offline."""
        url = config.get_main_option("sqlalchemy.url")
        context.configure(
            url=url,
            target_metadata=target_metadata,
            literal_binds=True,
            dialect_opts={"paramstyle": "named"},
        )
    except Exception as e:
        print(f'the next error has occurred: {e}')

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    try:
        """Configura migraciones en modo online."""
        connectable = engine_from_config(
            config.get_section(config.config_ini_section),
            prefix="sqlalchemy.",
            poolclass=pool.NullPool,
            )
        with connectable.connect() as connection:
            context.configure(
                connection=connection,
                target_metadata=target_metadata,
            )
            with context.begin_transaction():
                context.run_migrations()
    except Exception as e:
        print(e)

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
