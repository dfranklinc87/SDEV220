BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "book" (
	"title"	TEXT,
	"author"	TEXT,
	"year"	INTEGER
);
INSERT INTO "book" ("title","author","year") VALUES ('The Weirdstone of Brisingamen','Alan Garner',1960),
 ('Perdido Street Station','China MiÃ©ville',2000),
 ('Thud!','Terry Pratchett',2005),
 ('The Spellman Files','Lisa Lutz',2007),
 ('Small Gods','Terry Pratchett',1992);
COMMIT;
