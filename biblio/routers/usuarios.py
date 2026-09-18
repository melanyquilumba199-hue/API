from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select

from biblio.database import engine
from biblio.models import Usuario


router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)


@router.post("/")
def crear_usuario(usuario: Usuario):
    with Session(engine) as session:
        session.add(usuario)
        session.commit()
        session.refresh(usuario)
        return usuario


@router.get("/")
def listar_usuarios():
    with Session(engine) as session:
        usuarios = session.exec(select(Usuario)).all()
        return usuarios

@router.get("/{usuario_id}")
def obtener_usuario(usuario_id: int):
    with Session(engine) as session:
        usuario = session.get(Usuario, usuario_id)

        if not usuario:
            raise HTTPException(
                status_code=404,
                detail="Usuario no encontrado"
            )

        return usuario
@router.put("/{usuario_id}")
def actualizar_usuario(usuario_id: int, datos: Usuario):
    with Session(engine) as session:
        usuario = session.get(Usuario, usuario_id)

        if not usuario:
            raise HTTPException(
                status_code=404,
                detail="Usuario no encontrado"
            )

        usuario.nombre = datos.nombre
        usuario.apellido = datos.apellido
        usuario.email = datos.email
        usuario.telefono = datos.telefono

        session.add(usuario)
        session.commit()
        session.refresh(usuario)

        return usuario