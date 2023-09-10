from utilities import unos_intervala
from komponenta import unos_komponente, ispis_komponenti, Komponenta
from projekt import unos_projekta, ispis_projekata
import sqlite3

con = sqlite3.connect("baza.db")
cur = con.cursor()

komponente_ = []
komponente = []
projekti = []

# punjenje liste komponenti sa podacima iz baze podataka
query = """ 

    SELECT PN, cijena, id_kategorije FROM komponenta;
"""

data = cur.execute(query).fetchall()

for row in data:
    komponente_.append(list(row))
# pretvaranje elemenata liste u instance klase "Komponenta"
for komponenta_ in komponente_:
    komponenta = Komponenta(komponenta_[0], komponenta_[1], komponenta_[2])
    komponente.append(komponenta)

# punjenje liste komponenti podacima iz baze podataka
query1 = """ 

    SELECT datum, opis, trosak FROM projekt;
"""

data1 = cur.execute(query1).fetchall()

for row1 in data1:
    projekti.append(list(row1))


running = True
while running:
    print('-'*20)
    print('1. Unos nove komponente')
    print('2. Unos novog projekta')
    print('3. Ispis svih komponenti')
    print('4. Ispis svih projekata')
    print('5. Ispis zarade')
    print('6. Ispis blagajne')
    print('7. Zaustavi program')
    print('-'*20)

    akcija = unos_intervala(1,7)

    if akcija == 1:
       komponente.append(unos_komponente(len(komponente)+1)) # unos nove komponente i spremanje u bazu podataka

       query = f""" 

           INSERT INTO komponenta (kategorija, PN, id_komponente)
           VALUES ("{komponente[len(komponente)-1].kategorija}", "{komponente[len(komponente)-1].PN}", "{komponente[len(komponente)-1].kategorija}")

           """
       cur.execute(query)
       con.commit()

    elif akcija == 2:
        projekti.append(unos_projekta(len(projekti)+1)) #unos novog projekta i spremanje u bazu podataka
        query = f""" 

                   INSERT INTO projekt (datum, opis, trosak)
                   VALUES ("{projekti[len(projekti) - 1].datum}", "{projekti[len(projekti) - 1].opis}", "{projekti[len(projekti) - 1].trosak}")

                   """
        cur.execute(query)
        con.commit()

        # privući vrijednost ukupne zarade iz baze podataka
        query1 = " SELECT ukupna_zarada FROM blagajna WHERE id_racuna = 1"
        zarada = cur.execute(query1).fetchone()[0]
        int_zarada = int(zarada)
        uzarada = int_zarada + projekti[len(projekti) - 1].cijena

        #dodavanje nove vrijednosti ukupne zarade u bazu podataka
        query2 = f"""
        
            UPDATE blagajna
            SET ukupna_zarada='{uzarada}'
            WHERE id_racuna=1;
                 
                 """
        cur.execute(query2)
        con.commit()

        # azuriranje stanja blagajne
        x = uzarada / len(komponente)  # pojedinacna zarada, decimalna
        y = int(x)  # cijeli broj pojedinacne zarade
        z = y % 10  # ostatak od desetice
        pojedinacna_zarada = y - z  # pojedinacna zarada zaokruzena na manju deseticu
        b = int_zarada - len(komponente) * pojedinacna_zarada
        query4 = f"""

              UPDATE blagajna
              SET blagajna='{b}'
              WHERE id_racuna=1;

                """
        cur.execute(query4)
        con.commit()

    elif akcija == 3:
        if len(komponente) == 0:
            print('Nema unesenih komponenti.')
        elif len(komponente) != 0:
            # ispis svih komponenti spremljenih u bazu podataka
            query = """ 
            
                SELECT PN, cijena,  FROM komponenta
                LEFT JOIN kategorija ON komponenta.id_kategorije = kategorija.id;
                
            """
            data = cur.execute(query).fetchall()
            # ispis bez zareza i navodnika
            for row in data:
                row_string = ' '.join(str(item) for item in row)
                print(row_string)

    elif akcija == 4:
        if len(projekti) == 0:
            print('Nema unesenih projekata.')
        elif len(projekti) != 0:
            # ispis svih projekata spremljenih u bazu podataka
            query = """ 
    
                        SELECT datum, opis, trosak
                        FROM projekt
    
                    """
            data = cur.execute(query).fetchall()
            # ispis bez zareza i navodnika
            for row in data:
                row_string = ' '.join(str(item) for item in row)
                print(row_string)

    elif akcija == 5:
        if len(komponente) == 0:
            print('Nema unesenih komponenti.')
        elif len(komponente) != 0:
            print('Odaberite komponentu:')
            ispis_komponenti(komponente)
            odabrana_komponenta = unos_intervala(1, len(komponente))
            komponente[odabrana_komponenta-1].ispis()

            # privući vrijednost ukupne zarade iz baze podataka
            query1 = " SELECT ukupna_zarada FROM blagajna WHERE id_racuna = 1"
            zarada = cur.execute(query1).fetchone()[0]
            int_zarada = int(zarada)
            x = int_zarada/len(komponente) #pojedinacna zarada, decimalna
            y = int(x) #cijeli broj pojedinacne zarade
            z = y % 10 #ostatak od desetice
            pojedinacna_zarada = y - z #pojedinacna zarada zaokruzena na manju deseticu
            print(f'Zarada: {pojedinacna_zarada}')

    elif akcija == 6:
        # privući vrijednost ukupne zarade iz baze podataka
        query1 = " SELECT ukupna_zarada FROM blagajna WHERE id_racuna = 1"
        zarada = cur.execute(query1).fetchone()[0]
        int_zarada = int(zarada)
        x = int_zarada / len(komponente)  # pojedinacna zarada, decimalna
        y = int(x)  # cijeli broj pojedinacne zarade
        z = y % 10  # ostatak od desetice
        pojedinacna_zarada = y - z  # pojedinacna zarada zaokruzena na manju deseticu
        stanje_blagajne = int_zarada - len(komponente)*pojedinacna_zarada

        #novo stanje blagajne u bazi podataka
        query = f"""

                    UPDATE blagajna
                    SET blagajna='{stanje_blagajne}'
                    WHERE id_racuna=1;

                         """
        cur.execute(query)
        con.commit()

        print(f'Stanje blagajne: {stanje_blagajne}')

    elif akcija == 7:
        running = False

