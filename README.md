<h1 align="center">PrawoJazdyTesty</h1>

## O projekcie

Prosty serwer strony z pytaniami do prawa jazdy każdej kategorii.
Oficialna baza pytań z gov.pl, https://www.gov.pl/web/infrastruktura/prawo-jazdy
Wszystkie pytania jakie mogą być na egzaminie teoretycznym na prawo jazdy każdej kategorii według gov.pl

![Screenshot_2024-07-27_15-17-05](https://github.com/PierugHacker/PrawoJazdyTesty/blob/main/media/govpl-info.png)


### Zbudowane przy użuciu
Python z pakietem flask oraz pywebview (dla ładnego okienka),
HTML oraz czysty JavaScript i CSS
Żadnych idiotycznych frameworków ani innych kretynizmów.



<!-- GETTING STARTED -->
## Uruchomienie i użytkowanie

<h3>Wymagania</h3>
Zainstalowany Python 3.10 lub nowszy z pakietami: Flask 3.0.3 lub nowszy, pywebview 5.1 lub nowszy

<h3>Uruchomienie</h3>
Projekt możemy uruchomić na 2 sposoby.
<br>
<b>I) Pobrać gotową wersję z Releases i zainstalować</b>
<br>
<b>II) Ręcznie uruchomić program z kodu źródłowego, aby to zrobić:</b>
  <br><br>
  <b>1</b> Pobieramy zmodfyikowaną Bazę Pytań (wszystkie pliki wmv przekonwertowane do mp4 oraz zmienione rozszerzenia w nazwach plików w pytania.csv) <br>
  Link: https://drive.google.com/file/d/15xsihQS22okwUa74PaNec0t20TQkcecg/view?usp=sharing
  <br><br>
  <b>2</b> Rozpakowywujemy pobrany plik BazaPytan.zip do folderu engine tak aby wyglądało to następująco: <br><br>
  
   ![Screenshot_2024-07-27_15-17-05](https://github.com/PierugHacker/PrawoJazdyTesty/blob/main/media/engine-folder.png)
  
  <b>3</b> W folderze projektu uruchamiamy plik (dwukrotym kliknięciem) main.pyw lub wpisumemy
  
    ```sh
    python3 main.pyw
    ```
  
  Jeżeli zdecydujemy się na wpisanie komendy zamiast dwukrotnego kliknięcia to zobaczymy następujący obraz
  
  ![Screenshot_2024-07-27_15-25-52](https://github.com/PierugHacker/PrawoJazdyTesty/blob/main/media/running.png)
  
  Nie przejmujemy się uwagą o fakcie, iż jest to serwer deweloperski, nie to większego znaczenia.
  Chyba, że ktoś chce postawić to na faktycznym serwerze to wtedy faktycznie WSGI jest zalecne (najlpiej Apache2).

  Uruchomi się nam okienko z załadowaną stroną, jeżeli natomiast chcemy skorzystać z pełnej przeglądarki to
  wchodzimy na domyślny (wskazany na wcześniejszej rycinie) adres http://127.0.0.1:5000
  Ukazuje nam się strona główna:
  
  ![Screenshot_2024-07-27_15-29-44](https://github.com/PierugHacker/PrawoJazdyTesty/blob/main/media/homepage.png)



### Dodatkowe Uwagi, informacje i podziękowania.
Oryginalnie całość wizualizacji ważyła 8.4 GB, a po konwersji do formatu mp4 mamy 3.4 GB

Jeżeli ktoś chciałby zachostować tę, że stronę proszę o uprzedni kontakt ze mną.

Chciałbym na końcu podziękować Sobie za to, że to napisałem w 2 godziny, bo wszystkie dostępne strony z rzekomymi pytaniami do prawa jazdy mają ilość reklam
większą niż masa słońca w gramach bądź wymagają zakupu płatnej subskrypcji za stronę, którą można napisać w dwie godziny (mi by było osobiście wstyd brać pieniądze za 200 linijek kodu w pythonie)
