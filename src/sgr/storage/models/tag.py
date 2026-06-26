from sqlalchemy import String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship

from sgr.storage.database import Base
from sgr.storage.models.game import Game
from sgr.storage.models.game_tag import GameTag


class Tag(Base):
    __tablename__ = "tags"

    tag_id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    game_associations: Mapped[list[GameTag]] = relationship(
        back_populates="tag",
        cascade="all, delete-orphan",
    )

    @property
    def games(self) -> list["Game"]:
        return [assoc.game for assoc in self.game_associations]