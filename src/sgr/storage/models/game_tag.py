from sqlalchemy import String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship

from sgr.storage.database import Base
from sgr.storage.models.game import Game
from sgr.storage.models.tag import Tag


class GameTag(Base):
    __tablename__ = "game_tags"

    game_id: Mapped[int] = mapped_column(
        ForeignKey(Game.steam_id),
        primary_key=True,
    )

    tag_id: Mapped[int] = mapped_column(
        ForeignKey(Tag.tag_id),
        primary_key=True,
    )

    game: Mapped[Game] = relationship(
        back_populates="tag_associations"
    )

    tag: Mapped[Tag] = relationship(
        back_populates="game_associations"
    )