from sqlalchemy import INTEGER, Column, String, Boolean
from sqlalchemy.orm import relationship

from core.configs import settings

class UsuarioModel(settings.DBBaseModel):
    __tablename__ = 'usuarios'

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    sobrenome = Column(String(100), nullable=False)
    email = Column(String(100), index=True, nullable=False, unique=True)
    senha = Column(String(100), nullable=False)
    eh_admin = Column(Boolean, default=False)
    artigos = relationship('ArtigoModel', back_populates='criador', cascade='all, delete-orphan',
                           uselist=True, lazy='joined')


    def __repr__(self):
        pass