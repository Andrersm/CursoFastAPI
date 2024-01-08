from pydantic import BaseModel, HttpUrl


class ArtigoSchema(BaseModel):
    id: int | None = None
    titulo: str
    descricao: str 
    url_fonte: str
    usuario_id: int | None = None

    class Config:
        orm_mode = True