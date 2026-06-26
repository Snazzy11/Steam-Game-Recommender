from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from sgr.storage.database import Base
if TYPE_CHECKING:
    from sgr.storage.models.tag import Tag
    from sgr.storage import Game


class GameTag(Base):
    __tablename__ = "game_tags"

    game_id: Mapped[int] = mapped_column(
        ForeignKey("games.steam_id"),
        primary_key=True,
    )

    tag_id: Mapped[int] = mapped_column(
        ForeignKey("tags.tag_id"),
        primary_key=True,
    )

    game: Mapped["Game"] = relationship(
        back_populates="tag_associations"
    )

    tag: Mapped["Tag"] = relationship(
        back_populates="game_associations"
    )
