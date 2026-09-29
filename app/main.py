from fastapi import FastAPI

from app.routers import router_produtos, router_usuarios

# Constante global
MENSAGEM_HOME: str = "Bem-vindo à API de Recomendação de Produtos"


# Criando o App
app = FastAPI()

app.include_router(router_produtos.router)
app.include_router(router_usuarios.router)


# Iniciando o servidor
@app.get("/")
def home() -> dict[str, str]:
    return {"mensagem": MENSAGEM_HOME}
