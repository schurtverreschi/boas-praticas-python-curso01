from pydantic import BaseModel


# Modelo base para produto
class ProdutoBase(BaseModel):
    nome: str
    categoria: str
    tags: list[str]


# Modelo para criar um produto
class CriarProduto(ProdutoBase):
    pass


# Modelo de produto com ID
class Produto(ProdutoBase):
    id: int


# Modelo para histórico de compras do usuário
class HistoricoCompras(BaseModel):
    produtos_ids: list[int]


# Modelo para preferências do usuário
class Preferencias(BaseModel):
    categorias: list[str] | None = None
    tags: list[str] | None = None
