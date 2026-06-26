from sqlalchemy import (
    String,
    Integer,
    Text,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from sgr.storage.models.game_tag import GameTag
from sgr.storage.models.tag import Tag
from sgr.storage.models.user_library import UserLibrary
from sgr.storage.database import Base


class Game(Base):
    __tablename__ = "games"

    steam_id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(255), nullable=False)

    # recommendation_vector: Mapped[int | None] = mapped_column(Integer)

    description: Mapped[str | None] = mapped_column(Text)

    library_entries: Mapped[list[UserLibrary]] = relationship(
        back_populates="games",
        cascade="all, delete-orphan",
    )

    tag_associations: Mapped[list[GameTag]] = relationship(
        back_populates="game",
        cascade="all, delete-orphan",
    )

    @property
    def tags(self) -> list[Tag]:
        return [assoc.tag for assoc in self.tag_associations]

