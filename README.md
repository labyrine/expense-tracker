# expense-tracker

***Sovellus kulutuksen seurantaan***

- Jokaisella käyttäjällä on oma kulutushistoria, jota he voivat muokata ja tarkastella.
  
Sovelluksen ominaisuuksia
- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen (login ja register sivut)
- Käyttäjä voi luoda uuden menon tai tulon antamalla summan, päivämäärän, kategorian ja kuvauksen (create_income ja create-expense sivut)
- Käyttäjä voi etsiä tiettyä menoa tai tuloa suodattamalla summan, päivämäärän, kategorian tai kuvauksen perusteella (history sivu)
- Käyttäjä voi muokata aiemmin tallentamaansa menoa tai tuloa (history sivu)
- Käyttäjä voi poistaa tallentamansa menon tai tulon (history sivu)
- Käyttäjä voi katsoa kulujensa kuukausiraportin, johon kuuluu menojen sekä tulojen omat summat, paljonko on kuukaudessa plussalla tai miinuksella sekä kategorioiden prosenttiosuudet kuukauden menoista. (Kuukausiraportti sivu, ei vielä luotu)
- Käyttäjä voi nähdä asettamansa budjetin valitsemalleen kuukaudelle ja sen vieressä kuukauden menot ja tiedon siitä onko budjettia ylitetty. Samoin hän voi nähdä kategorialle kuukaudeksi annetun budjetin, kyseisen kategorian kulut yhteensä ja onko budjettia ylitetty vai ei. (Kuukausiraportti sivu, ei vielä luotu)
- Käyttäjä voi hakea keskivertokulutuksen päivän, kuukauden sekä kategorian mukaan (suunnittelematon sijainti)
- Käyttäjä voi asettaa itselleen budjetin tietylle kuukaudelle tai kategorialle. (Luo bugjetti sivu, ei vielä luotu)

**Sovelluksen nykyinen tilanne**

Sovelluksessa toimii tällä hetkellä rekisteröityminen, kirjautuminen sisään ja ulos sekä menon ja tulon luominen. Tulon ja menon luomisessa ei ole vielä virheilmoituksia. Myös historia-sivulle pystyy menemään, mutta siellä ei tällä hetkellä ole mitään. Rekisteröitymisen ja kirjautumisen sivujen ulkoasua on päivitetty. Muiden sivujen ulkoasua ei ole muokattu.

**Ohjeet sovelluksen testaamiseen**

Kloonaa tämä repositorio omalle koneellesi komennolla<br>
$ git clone https://github.com/labyrine/expense-tracker.<br> 
Tämä luo juurikansion expense-tracker. Siirry sen sisälle.

Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:<br>
DATABASE_URL=\<tietokannan-paikallinen-osoite\><br>
SECRET_KEY=\<salainen-avain\>

(Ohje Linuxille)<br>
  Sitten aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla<br>
  $ python3 -m venv venv<br>
  $ source venv/bin/activate<br>
  $ pip install -r ./requirements.txt

Määritä tietokannan skeema komennolla<br>
  $ psql < schema.sql

Sovelluksen voi käynnistää komennolla<br>
  $ flask run
                   
***Suunnitelma tietokannan rakenteelle***

**Taulut**

1. Käyttäjät
- Käyttäjä id
- Käyttäjänimi
- Salasana

2. Menot
- Meno id
- Käyttäjä id (Taulusta 1)
- Päivämäärä
- Summa
- Kategoria menot nimi
- Kuvaus

3. Kategoriat menot
- Kategoria menot id
- Kategorian menot nimi

4. Tulot
- Tulo id
- Käyttäjä id (Taulusta 1)
- Päivämäärä
- Summa
- Kategoria tulot nimi
- Kuvaus

5. Kategoria tulot
- Kategoria tulot id
- Kategoria tulot nimi

6. Budjetti
- Budjetti id
- Käyttäjä id (Taulusta 1)
- Kategoria menot id (Taulusta 3)
- Budjetin määrä
- Aloituspäivä
- Lopetuspäivä

7. Ilmoitukset (Jos jää aikaa, mutta saatan jättää pois)
- Ilmoitukset id
- Käyttäjä id (Taulusta 1)
- Viesti

Käyttäjä voi valita kategorian tulolle tai menolle, joka on sopivassa kategoria-taulussa. Taulun budjetti avulla käyttäjät voivat asettaa itselleen budjetin menojen kategorioille ja tietyille aikaväleille. Ilmoitukset taulusta löytyy viestit, joita kutsutaan, kun käyttäjä ylittää budjetin (Jos jää aikaa, mutta saatan jättää pois). 
