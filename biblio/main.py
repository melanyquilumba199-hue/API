from fastapi import FastAPI

from biblio.database import create_db_and_tables
from biblio.routers.usuarios import router as usuarios_router
from biblio.routers.libros import router as libros_router
from biblio.routers.prestamos import router as prestamos_router


app = FastAPI(
    title="API de Gestión de Biblioteca",
    description="API para gestionar usuarios, libros y préstamos.",
    version="1.0.0"
)

app.include_router(libros_router)
app.include_router(prestamos_router)
app.include_router(usuarios_router)


@app.on_event("startup")
def iniciar_base_de_datos():
    create_db_and_tables()


@app.get("/")
def inicio():
    return {
        "mensaje": "API de Biblioteca funcionando correctamente"
    }