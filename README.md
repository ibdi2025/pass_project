Cielom projektu 'Pass' je Python program na vytvaranie uzivatelskych uctov a ich zapisovanie do suboru 'pass.txt' spolu s hashom hesla.

Program bude vo finalnej verzii poskytovat nasledovne funkcionality:

(parent class 1)
- vytvorenie listu uz existujúcich username; pri prvom spusteni je list prazdny. list je nastaveny na 5 uzivatelov.
	(child of parent 1)
	- tlac listu

(parent class 2)
- vytvorenie suboru pass.tx ak neexistuej(def)
- vstup uzivatelskeho mena (def)
- kontrola uzivatelskeho mena oproti suboru pass.txt - databaze uzivatelov/hashov (def)
    - ak uzivatelske meno existuje, program sa ukonci
- vstup uzivatelskeho hesla
	(child of parent 2)
	- vytvorenie hashu hesla (def->child class->return to parent class)
- zapis uzivatelskeho mena a hashu do suboru pass.txt - databazy uzivatelov/hashov (def)
	(child of parent 2)
- kontrola uzivatelskeho hesla/hashu (def->child class->return to parrent class)

- nasledna akcia ak sa heslo/hash zhoduje
	uzivatelske meno a hash sa zapisu na externy web server