# app/etl.py
import os
import requests
from datetime import datetime
from models import EnergyData, Base, engine, SessionLocal
from dotenv import load_dotenv

load_dotenv()  # carga variables .env

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

API_KEY = os.getenv("XM_API_KEY")
BASE_URL = os.getenv("XM_BASE_URL")
session = SessionLocal()

def fetch_and_save(year: int, month: int):
    params = {"year": year, "month": month, "apikey": API_KEY}
    res = requests.get(BASE_URL, params=params)
    res.raise_for_status()
    data = res.json().get("results", [])
    for item in data:
        fecha = datetime.strptime(item["fecha"], "%Y-%m-%d").date()
        record = EnergyData(
            fecha=fecha,
            costo_operativo=item.get("costo_operativo"),
            ingresos=item.get("ingresos"),
            precio_energia=item.get("precio_energia"),
            volumen_transaccionado=item.get("volumen"),
            indice_servicio=item.get("indice_servicio"),
            tiempo_respuesta=item.get("tiempo_respuesta"),
            generacion_energetica=item.get("generacion")
        )
        session.merge(record)  # inserta o actualiza
    session.commit()

if __name__ == "__main__":
    for y in [2022, 2023, 2024]:
        for m in range(1, 13):
            fetch_and_save(y, m)
    print("ETL completado.")
