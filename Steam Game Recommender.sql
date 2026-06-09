CREATE TABLE "users" (
  "id" integer PRIMARY KEY,
  "username" varchar,
  "first_name" varchar,
  "last_name" varchar,
  "created_at" timestamp
);

CREATE TABLE "user_library" (
  "user_id" integer,
  "game_id" integer,
  "playtime" integer,
  "last_update" timestamp,
  PRIMARY KEY ("user_id", "game_id")
);

CREATE TABLE "games" (
  "steam_id" integer PRIMARY KEY UNIQUE,
  "name" varchar,
  "recommendation_vector" integer,
  "description" varchar
);

CREATE TABLE "tags" (
  "tag_id" integer PRIMARY KEY,
  "name" varchar
);

CREATE TABLE "game_tags" (
  "game_id" integer,
  "tag_id" integer,
  PRIMARY KEY ("game_id", "tag_id")
);

ALTER TABLE "user_library" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "user_library" ADD FOREIGN KEY ("game_id") REFERENCES "games" ("steam_id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "game_tags" ADD FOREIGN KEY ("game_id") REFERENCES "games" ("steam_id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "game_tags" ADD FOREIGN KEY ("tag_id") REFERENCES "tags" ("tag_id") DEFERRABLE INITIALLY IMMEDIATE;
