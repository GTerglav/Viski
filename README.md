# Viski
=======================

Analiziral bom viskije ocenjene v času od vključno jeseni 2019 do poletja 2015 na strani [Whiskey advocate](http://whiskyadvocate.com/ratings-and-reviews/).

**Vsebovane datoteke**  
V datoteki zajem_in_obdelava.py je koda za zajem podatkov. Najprej sem zajel stran za vsak mesec posebaj, rezultat tega je v mapi viski_out. 
Nato sem vsee html datoteke združil v eno index.html, ki je v mapi viski_out_full. V orodja.py so pomožna ordoja iz predavanj. Analiza podatkov se nahaja v viski_analiza.ipynb.

**Zajel sem:**
* ime
* vrsto
* vsebnost alkohola
* oceno
* ceno
* opis, ki ga poda ocenjevalec 
* ime ocenjevalca
* čas ocene(npr. zima 2018)


**Hipoteze:**
* Ali obstaja zveza med ceno in oceno? 
* Katera vrsta viskija se pojavi največkrat in kakšna je povprečna ocena?
* Kakšna je povprečna ocena, ki jo poda posamezen ocenjevalec?
* itd.
