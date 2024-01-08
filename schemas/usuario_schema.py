from pydantic import BaseModel, EmailStr
from typing import List

from schemas.artigo_schema import ArtigoSchema


class UsuarioSchemaBase(BaseModel):
    id: int | None = None
    nome: str | None = None
    sobrenome: str | None = None
    email: str
    senha: str
    eh_admin: bool = False

    class Config:
        orm_mode = True


class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str


class UsuariosSchemaArtigos(UsuarioSchemaBase):
    artigos: List[ArtigoSchema] | None = None 


class UsuarioSchemaUp(UsuarioSchemaBase):
    nome: str | None = None
    sobrenome: str | None = None
    email: EmailStr | None = None
    senha: str | None = None
    eh_admin: bool | None = None

