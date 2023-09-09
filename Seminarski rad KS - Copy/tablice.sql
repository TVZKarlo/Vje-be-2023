CREATE TABLE komponenta (
id_komponente INTEGER PRIMARY KEY AUTOINCREMENT,
kategorija CHAR(50) NOT NULL,
PN CHAR(50) NOT NULL,
id_kategorije TINYINT
);

CREATE TABLE kategorija (
id INTEGER PRIMARY KEY AUTOINCREMENT,
naziv CHAR(50) NOT NULL
);

CREATE TABLE projekt (
id_projekta INTEGER PRIMARY KEY AUTOINCREMENT,
datum DATE NOT NULL,
opis CHAR(50),
trošak INTEGER
);

CREATE TABLE blagajna (
id_racuna INTEGER PRIMARY KEY AUTOINCREMENT,
računovodstvo INTEGER,
ukupna_zarada INTEGER
);

INSERT INTO instrument (naziv) VALUES
    ('Prim'),
    ('Basprim'),
    ('Harmonika'),
    ('Bas'),
    ('Bugarija'),
    ('Bubanj');

INSERT INTO blagajna (blagajna, ukupna_zarada)  VALUES
    ('0','0');