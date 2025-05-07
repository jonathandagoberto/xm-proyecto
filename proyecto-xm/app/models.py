# app/models.py
from sqlalchemy import Column, Integer, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class EnergyData(Base):
    __tablename__ = "energy_data"
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, nullable=False, index=True)
    costo_operativo = Column(Numeric)
    ingresos = Column(Numeric)
    precio_energia = Column(Numeric)
    volumen_transaccionado = Column(Numeric)
    indice_servicio = Column(Numeric)
    tiempo_respuesta = Column(Numeric)
    generacion_energetica = Column(Numeric)

# Motor y sesión (se usarán en main.py y etl.py)
import os
DB_URL = os.getenv("DATABASE_URL", "postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD@db/$POSTGRES_DB")
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
