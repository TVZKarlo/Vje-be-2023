CREATE TABLE komponenta (
id_komponente INTEGER PRIMARY KEY AUTOINCREMENT,
PN CHAR(50) INTEGER,
cijena CHAR(50) NOT NULL,
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
trosak INTEGER
);

CREATE TABLE blagajna (
id_racuna INTEGER PRIMARY KEY AUTOINCREMENT,
blagajna INTEGER,
ukupna_zarada INTEGER
);

INSERT INTO kategorija (naziv) VALUES
    ('IC'),
    ('Tranzistor'),
    ('Relay'),
    ('Otpornik'),
    ('Kondenzator'),
    ('Zavojnica');

INSERT INTO blagajna (blagajna, ukupna_zarada)  VALUES
    ('0','0');