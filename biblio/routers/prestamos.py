from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select

from biblio.database import engine
from biblio.models import Prestamo


router = APIRouter(
    prefix="/prestamos",
    tags=["Préstamos"]
)


@router.post("/")
def crear_prestamo(prestamo: Prestamo):
    with Session(engine) as session:
        session.add(prestamo)
        session.commit()
        session.refresh(prestamo)
        return prestamo


@router.get("/")
def listar_prestamos():
    with Session(engine) as session:
        prestamos = session.exec(select(Prestamo)).all()
        return prestamos

@router.get("/{prestamo_id}")
def obtener_prestamo(prestamo_id: int):
    with Session(engine) as session:
        prestamo = session.get(Prestamo, prestamo_id)

        if not prestamo:
            raise HTTPException(
                status_code=404,
                detail="Préstamo no encontrado"
            )

        return prestamo


@router.put("/{prestamo_id}")
def actualizar_prestamo(prestamo_id: int, datos: Prestamo):
    with Session(engine) as session:
        prestamo = session.get(Prestamo, prestamo_id)

        if not prestamo:
            raise HTTPException(
                status_code=404,
                detail="Préstamo no encontrado"
            )

        prestamo.usuario_id = datos.usuario_id
        prestamo.libro_id = datos.libro_id
        prestamo.fecha_prestamo = datos.fecha_prestamo
        prestamo.fecha_devolucion = datos.fecha_devolucion
        prestamo.estado = datos.estado

        session.add(prestamo)
        session.commit()
        session.refresh(prestamo)

        return prestamo

@router.delete("/{prestamo_id}")
def eliminar_prestamo(prestamo_id: int):
    with Session(engine) as session:
        prestamo = session.get(Prestamo, prestamo_id)

        if not prestamo:
            raise HTTPException(
                status_code=404,
                detail="Préstamo no encontrado"
            )

        session.delete(prestamo)
        session.commit()

        return {
            "mensaje": "Préstamo eliminado correctamente"
        }