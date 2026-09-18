from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select

from biblio.database import engine
from biblio.models import Libro


router = APIRouter(
    prefix="/libros",
    tags=["Libros"]
)


@router.post("/")
def crear_libro(libro: Libro):
    with Session(engine) as session:
        session.add(libro)
        session.commit()
        session.refresh(libro)
        return libro


@router.get("/")
def listar_libros():
    with Session(engine) as session:
        libros = session.exec(select(Libro)).all()
        return libros

@router.get("/{libro_id}")
def obtener_libro(libro_id: int):
    with Session(engine) as session:
        libro = session.get(Libro, libro_id)

        if not libro:
            raise HTTPException(
                status_code=404,
                detail="Libro no encontrado"
            )

        return libro


@router.put("/{libro_id}")
def actualizar_libro(libro_id: int, datos: Libro):
    with Session(engine) as session:
        libro = session.get(Libro, libro_id)

        if not libro:
            raise HTTPException(
                status_code=404,
                detail="Libro no encontrado"
            )

        libro.titulo = datos.titulo
        libro.autor = datos.autor
        libro.categoria = datos.categoria
        libro.anio_publicacion = datos.anio_publicacion
        libro.disponible = datos.disponible

        session.add(libro)
        session.commit()
        session.refresh(libro)

        return libro

@router.delete("/{libro_id}")
def eliminar_libro(libro_id: int):
    with Session(engine) as session:
        libro = session.get(Libro, libro_id)

        if not libro:
            raise HTTPException(
                status_code=404,
                detail="Libro no encontrado"
            )

        session.delete(libro)
        session.commit()

        return {
            "mensaje": "Libro eliminado correctamente"
        }