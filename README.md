# expense-tracker

***Sovellus kulutuksen seurantaan***

- Jokaisella käyttäjällä on oma kulutushistoria, jota he voivat muokata ja tarkastella.
  
**Sovelluksen toimivia ominaisuuksia**

Kirjaudu ja rekisteröidy
- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen
Etusivu
- Näyttää kaikki tulot yhteensä, kaikki menot yhteensä ja niiden erotus.
Menon ja tulon luominen
- Käyttäjä voi luoda uuden menon tai tulon antamalla summan, päivämäärän, kategorian ja kuvauksen
Historia
-Käyttäjä näkee listan antamistaan tuloista ja menoista
- Käyttäjä voi muokata aiemmin tallentamaansa menoa tai tuloa 
- Käyttäjä voi poistaa tallentamansa menon tai tulon 
Kuukausiraportti
- Käyttäjä voi katsoa kulujensa kuukausiraportin, johon kuuluu menojen sekä tulojen omat summat, paljonko on kuukaudessa plussalla tai miinuksella sekä kategorioiden prosenttiosuudet kuukauden menoista.
- Käyttäjä voi nähdä asettamansa budjetin valitsemalleen kuukaudelle ja sen vieressä kuukauden menot ja tiedon siitä onko budjettia ylitetty. Samoin hän voi nähdä kategorialle kuukaudeksi annetun budjetin, kyseisen kategorian kulut yhteensä ja onko budjettia ylitetty vai ei.
Budjetti
- Käyttäjä voi asettaa itselleen budjetin tietylle kuukaudelle tai kategorialle tietyksi kuukaudeksi.

**Alkuperäisestä suunnitelmasta puuttuvat asiat**
- Historia: Käyttäjä voi etsiä tiettyä menoa tai tuloa suodattamalla summan, päivämäärän, kategorian tai kuvauksen perusteella.
- Käyttäjä voi hakea keskivertokulutuksen päivän, kuukauden sekä kategorian mukaan.
- Taulu, jonka tarkoitus oli säilyttää viestejä, joita kutsuttaisiin, kun käyttäjä ylittää budjetin.

**Muuta**
- Valitsin vuodet raportin muodostamiseen siten, että sovellukseen voi syöttää vanhempiakin tuloja ja menoja ja saada niistä raportin. Tämä olisi hyödyksi, jos on esimerkiksi säästänyt kuitteja. Halusin myös, että sovellus toimisi sellaisenaan pitkään ja siksi valitsin vähän umpimähkään viimeiseksi vuodeksi 2020.

**Parannettavaa**
- Kirjaudu ja rekisteröidy sivut eivät käytä muille html-tiedostoille yhteistä layout-tiedostoa
- Etusivulla kirjaudu ulos teksti voi tulla muun tiedon päälle riippuen ikkunan koosta
- Ohjelmointityylin parantaminen

**Ohjeet sovelluksen testaamiseen - sovellus toimii vain paikallisesti**

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

6.Kuukausi-budjetti
- Budjetti id
- Käyttäjä id (Taulusta 1)
- Budjetin määrä
- Aloituspäivä
- Lopetuspäivä
- 
7. Kategoria-budjetti
- Budjetti id
- Käyttäjä id (Taulusta 1)
- Kategoria menot nimi (Taulusta 3)
- Budjetin määrä
- Aloituspäivä
- Lopetuspäivä

