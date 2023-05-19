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
- 
***Suunnitelma tietokannan rakenteelle***
**Taulut**

1. Käyttäjät
-Käyttäjä id
-Käyttäjänimi
-Salasana

2. Menot
-Meno id
-Käyttäjä id (Taulusta 1)
-Päivämäärä
-Summa
-Kategoria menot nimi
-Kuvaus

3. Kategoriat menot
-Kategoria menot id
-Kategorian menot nimi

4. Tulot
-Tulo id
-Käyttäjä id (Taulusta 1)
-Päivämäärä
-Summa
-Kategoria tulot nimi
-Kuvaus

5. Kategoria tulot
-Kategoria tulot id
-Kategoria tulot nimi

6. Budjetti
-Budjetti id
-Käyttäjä id (Taulusta 1)
-Kategoria menot id (Taulusta 3)
-Budjetin määrä
-Aloituspäivä
-Lopetuspäivä

7. Ilmoitukset
-Ilmoitukset id
-Käyttäjä id (Taulusta 1)
-Viesti

Käyttäjä voi valita kategorian tulolle tai menolle, joka on sopivassa kategoria-taulussa. Taulun budjetti avulla käyttäjät voivat asettaa itselleen budjetin menojen kategorioille ja tietyille aikaväleille. Ilmoitukset taulusta löytyy viestit, joita kutsutaan, kun käyttäjä ylittää budjetin. 
