from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship

from sgr.storage.database import Base
if TYPE_CHECKING:
    from sgr.storage.models.user import User
    from sgr.storage.models.game import Game


class UserLibrary(Base):
    __tablename__ = "user_library"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        primary_key=True,
    )

    game_id: Mapped[int] = mapped_column(
        ForeignKey("games.steam_id"),
        primary_key=True,
    )

    # Todo ondelete cascades where necessary

    playtime: Mapped[int | None] = mapped_column(Integer)

    last_update: Mapped[datetime | None] = mapped_column(DateTime)

    user: Mapped["User"] = relationship(
        back_populates="library_entries"
    )

    game: Mapped["Game"] = relationship(
        back_populates="library_entries"
    )
