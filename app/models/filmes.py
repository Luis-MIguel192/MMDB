"""Modelos relacionados a filmes, pessoas e elenco.

Este módulo define os modelos para o sistema de filmes, incluindo:
- Filme: Informações básicas dos filmes
- Pessoa: Atores, diretores, etc.
- Elenco: Relacionamento entre filmes e pessoas com seus cargos
"""
import uuid
from datetime import date
from typing import Optional

from sqlalchemy import Date, ForeignKey, Integer, String, Text, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app import db
from app.models.mixins import AuditMixin, BasicRepositoryMixin


class Filme(db.Model, BasicRepositoryMixin, AuditMixin):
    """Modelo para filmes."""
    __tablename__ = "filmes"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    titulo: Mapped[str] = mapped_column(String(200), nullable=False)
    titulo_original: Mapped[Optional[str]] = mapped_column(String(200))
    sinopse: Mapped[Optional[str]] = mapped_column(Text)
    ano_lancamento: Mapped[Optional[int]] = mapped_column(Integer)
    data_lancamento: Mapped[Optional[date]] = mapped_column(Date)
    duracao_minutos: Mapped[Optional[int]] = mapped_column(Integer)
    genero: Mapped[Optional[str]] = mapped_column(String(100))
    classificacao: Mapped[Optional[str]] = mapped_column(String(10))  # G, PG, PG-13, R, etc.
    poster_url: Mapped[Optional[str]] = mapped_column(String(500))

    # Relacionamentos
    elenco: Mapped[list['Elenco']] = relationship(back_populates='filme', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Filme {self.titulo} ({self.ano_lancamento})>'


class Pessoa(db.Model, BasicRepositoryMixin, AuditMixin):
    """Modelo para pessoas (atores, diretores, etc.)."""
    __tablename__ = "pessoas"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    nome_completo: Mapped[Optional[str]] = mapped_column(String(200))
    data_nascimento: Mapped[Optional[date]] = mapped_column(Date)
    nacionalidade: Mapped[Optional[str]] = mapped_column(String(50))
    biografia: Mapped[Optional[str]] = mapped_column(Text)
    foto_url: Mapped[Optional[str]] = mapped_column(String(500))

    # Relacionamentos
    participacoes: Mapped[list['Elenco']] = relationship(back_populates='pessoa', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Pessoa {self.nome}>'


class Elenco(db.Model, BasicRepositoryMixin, AuditMixin):
    """Modelo para relacionamento entre filmes e pessoas com seus cargos."""
    __tablename__ = "elenco"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    filme_id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey('filmes.id', ondelete='CASCADE'),
        nullable=False
    )
    pessoa_id: Mapped[uuid.UUID] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey('pessoas.id', ondelete='CASCADE'),
        nullable=False
    )
    cargo: Mapped[str] = mapped_column(String(50), nullable=False)  # Ator, Diretor, Produtor, etc.
    personagem: Mapped[Optional[str]] = mapped_column(String(100))  # Nome do personagem (para atores)
    ordem: Mapped[Optional[int]] = mapped_column(Integer)  # Ordem de importância no elenco

    # Relacionamentos
    filme: Mapped['Filme'] = relationship(back_populates='elenco')
    pessoa: Mapped['Pessoa'] = relationship(back_populates='participacoes')

    def __repr__(self):
        return f'<Elenco {self.pessoa.nome if self.pessoa else "?"} - {self.cargo} em {self.filme.titulo if self.filme else "?"}>'