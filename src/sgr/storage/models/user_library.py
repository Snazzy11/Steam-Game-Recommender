from datetime import datetime, timezone

from sqlalchemy import String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship

from sgr.storage.database import Base
from sgr.storage.models.game import Game
from sgr.storage.models.user import User

class UserLibrary(Base):
    __tablename__ = "user_library"

    user_id: Mapped[int] = mapped_column(
        ForeignKey(User.id),
        primary_key=True,
    )

    game_id: Mapped[int] = mapped_column(
        ForeignKey(Game.steam_id),
        primary_key=True,
    )

    playtime: Mapped[int | None] = mapped_column(Integer)

    last_update: Mapped[datetime | None] = mapped_column(DateTime)

    user: Mapped[User] = relationship(
        back_populates="library_entries"
    )

    game: Mapped[Game] = relationship(
        back_populates="library_entries"
    )