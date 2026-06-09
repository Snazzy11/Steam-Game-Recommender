from datetime import datetime

# TODO: Separate these
# TODO: Rename users 'id' to 'user_id'

from sqlalchemy import (
    String,
    Integer,
    Text,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(100), nullable=False)

    first_name: Mapped[str | None] = mapped_column(String(100))
    last_name: Mapped[str | None] = mapped_column(String(100))

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    library_entries: Mapped[list["UserLibrary"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )

    @property
    def games(self) -> list["Game"]:
        return [entry.game for entry in self.library_entries]


class Game(Base):
    __tablename__ = "games"

    steam_id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(255), nullable=False)

    recommendation_vector: Mapped[int | None] = mapped_column(Integer)

    description: Mapped[str | None] = mapped_column(Text)

    library_entries: Mapped[list["UserLibrary"]] = relationship(
        back_populates="game",
        cascade="all, delete-orphan",
    )

    tag_associations: Mapped[list["GameTag"]] = relationship(
        back_populates="game",
        cascade="all, delete-orphan",
    )

    @property
    def tags(self) -> list["Tag"]:
        return [assoc.tag for assoc in self.tag_associations]


class Tag(Base):
    __tablename__ = "tags"

    tag_id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    game_associations: Mapped[list["GameTag"]] = relationship(
        back_populates="tag",
        cascade="all, delete-orphan",
    )

    @property
    def games(self) -> list["Game"]:
        return [assoc.game for assoc in self.game_associations]


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

    playtime: Mapped[int | None] = mapped_column(Integer)

    last_update: Mapped[datetime | None] = mapped_column(DateTime)

    user: Mapped["User"] = relationship(
        back_populates="library_entries"
    )

    game: Mapped["Game"] = relationship(
        back_populates="library_entries"
    )


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