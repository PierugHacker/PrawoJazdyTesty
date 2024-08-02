<h1 align="center">PrawoJazdyTesty</h1>

## O projekcie

Prosty serwer strony z pytaniami do prawa jazdy każdej kategorii.
Oficialna baza pytań z gov.pl, https://www.gov.pl/web/infrastruktura/prawo-jazdy
Wszystkie pytania jakie mogą być na egzaminie teoretycznym na prawo jazdy każdej kategorii według gov.pl

![Screenshot_2024-07-27_15-17-05](https://github.com/user-attachments/assets/ebd32071-1e18-406b-993f-dae138be2b6a)


### Zbudowane przy użuciu
Python z pakietem flask
HTML oraz czysty JavaScript i CSS
Żadnych idiotycznych frameworków ani innych kretynizmów.



<!-- GETTING STARTED -->
## Uruchomienie i użytkowanie

<h3>Wymagania</h3>
Zainstalowany Python 3.10 lub nowszy oraz pakiet flask 3.0.3 lub nowszy.

<h3>Uruchomienie</h3>
W folderze projektu wpisumemy 

  ```sh
  python main.py
  ```
lub w Windows'ie

  ```sh
  python3 main.py
  ```

Zobaczymy następujący obraz

![Screenshot_2024-07-27_15-25-52](https://github.com/user-attachments/assets/9e6917b1-bb69-4bfd-b8b8-34eb71265267)

Nie przejmujemy się uwagą o fakcie, iż jest to serwer deweloperski, nie to większego znaczenia.
Chyba, że ktoś chce postawić to na faktycznym serwerze to wtedy faktycznie WSGI jest zalecne (najlpiej Apache2).

Wchodzimy na domyślny adres http://127.0.0.1:5000 (lub ewentualnie z innym portem jak zmienisz w kodzie).
Ukazuje nam się strona główna:

![Screenshot_2024-07-27_15-29-44](https://github.com/user-attachments/assets/ac4c032d-4613-4c2c-a4cb-c467b2c0085b)



### Dodatkowe Uwagi, informacje i podziękowania.
Dołączam do projektu bazę pytań (stąd duża waga) ponieważ oryginalnie pliki video od gov.pl były w formacie wmv, którego niestety nie da się odtworzyć w przeglądarce,
co zmusiło mnie do konwersji wszystkich nagrań video do formatu mp4, ponando musiałem zmienić w pliku csv z pytaniami nazwy plików na te z poprawnym rozszerzeniem.
Oryginalnie całość wizualizacji ważyła 8.4 GB, a po konwersji do formatu mp4 mamy 3.4 GB

Jeżeli ktoś chciałby zachostować tę, że stronę proszę o uprzedni kontakt ze mną.

Chciałbym na końcu podziękować Sobie za to, że to napisałem w 2 godziny, bo wszystkie dostępne strony z rzekomymi pytaniami do prawa jazdy mają ilość reklam
większą niż masa słońca w gramach bądź wymagają zakupu płatnej subskrypcji za stronę, którą można napisać w dwie godziny (mi by było osobiście wstyd brać pieniądze za 200 linijek kodu w pythonie)
