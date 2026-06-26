from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import datetime, timezone
from sqlalchemy import String, DateTime
from sqlalchemy.orm import mapped_column, Mapped, relationship

from sgr.storage.database import Base
if TYPE_CHECKING:
    from sgr.storage.models.game import Game
    from sgr.storage.models.user_library import UserLibrary





class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(100), nullable=False)

    first_name: Mapped[str | None] = mapped_column(String(100))
    last_name: Mapped[str | None] = mapped_column(String(100))

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc),
    )

    library_entries: Mapped[list["UserLibrary"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )

    @property
    def games(self) -> list["Game"]:
        return [entry.game for entry in self.library_entries]
