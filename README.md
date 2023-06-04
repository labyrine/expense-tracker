# expense-tracker

***Sovellus kulutuksen seurantaan***

- Jokaisella käyttäjällä on oma kulutushistoria, jota he voivat muokata ja tarkastella.
Sovelluksen ominaisuuksia
- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen
- Käyttäjä voi luoda uuden menon tai tulon antamalla summan, päivämäärän, kategorian ja kuvauksen
- Käyttäjä voi etsiä tiettyä menoa tai tuloa suodattamalla summan, päivämäärän, kategorian tai kuvauksen perusteella
- Käyttäjä voi muokata aiemmin tallentamaansa menoa tai tuloa
- Käyttäjä voi poistaa tallentamansa menon tai tulon
- Käyttäjä voi katsoa kulujensa yhteenvedon, johon kuuluu käytetty raha yhteensä, paljonko hän on ylipäätään plussalla tai miinuksella sekä keskivertokulutus kategorioittain
- Käyttäjä voi hakea keskivertokulutuksen päivän, kuukauden sekä kategorian mukaan
- Käyttäjä voi hakea kuukaudelta, että paljonko hän on plussalla tai miinuksella
- Käyttäjä voi asettaa itselleen budjetin tietylle aikavälille tai kategorialle, jonka ylittämisestä sovellus kertoo

**Sovelluksen nykyinen tilanne**

Sovelluksessa toimii tällä hetkellä rekisteröityminen sekä kirjautuminen sisään ja ulos. 

**Ohjeet sovelluksen testaamiseen**

Kloonaa tämä repositorio omalle koneellesi komennolla
$ git clone https://github.com/labyrine/expense-tracker 
Tämä luo juurikansion expense-tracker. Siirry sen sisälle.

Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:
DATABASE_URL=<tietokannan-paikallinen-osoite>
SECRET_KEY=<salainen-avain>

(Ohje Linuxille)
Sitten aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r ./requirements.txt

Määritä tietokannan skeema komennolla
$ psql < schema.sql

Sovelluksen voi käynnistää komennolla
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

7. Ilmoitukset
- Ilmoitukset id
- Käyttäjä id (Taulusta 1)
- Viesti

Käyttäjä voi valita kategorian tulolle tai menolle, joka on sopivassa kategoria-taulussa. Taulun budjetti avulla käyttäjät voivat asettaa itselleen budjetin menojen kategorioille ja tietyille aikaväleille. Ilmoitukset taulusta löytyy viestit, joita kutsutaan, kun käyttäjä ylittää budjetin. 
