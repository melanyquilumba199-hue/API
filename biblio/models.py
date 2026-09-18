from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel, Field


class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    apellido: str
    email: str
    telefono: str


class Libro(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    autor: str
    categoria: str
    anio_publicacion: int
    disponible: bool = True


class Prestamo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    usuario_id: int
    libro_id: int
    fecha_prestamo: str
    fecha_devolucion: Optional[str] = None
    estado: str