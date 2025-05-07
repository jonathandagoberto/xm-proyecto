CREATE TABLE energy_data (
  id SERIAL PRIMARY KEY,
  fecha DATE NOT NULL,
  costo_operativo NUMERIC,
  ingresos NUMERIC,
  precio_energia NUMERIC,
  volumen_transaccionado NUMERIC,
  indice_servicio NUMERIC,
  tiempo_respuesta NUMERIC,
  generacion_energetica NUMERIC
);

-- Índice para acelerar consultas por fecha
CREATE INDEX idx_energy_data_fecha ON energy_data(fecha);