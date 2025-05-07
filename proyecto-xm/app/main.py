# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import EnergyData, Base, engine, SessionLocal
from datetime import date
import os

# Crea tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Energética XM")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/status")
def status():
    return {"status": "ok"}

@app.get("/datos")
def get_datos(fecha: date, db: Session = Depends(get_db)):
    registros = db.query(EnergyData).filter(EnergyData.fecha == fecha).all()
    if not registros:
        raise HTTPException(status_code=404, detail="No hay datos para esa fecha")
    return registros
