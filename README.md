# Programmentwurf Sternensammler
A* Suchverfahren  
## Ziel
Es soll ein Programm erstellt werden, welches ein Labyrinth aus gegebenen Informationen aus verschiedenen csv Dateien generiert und dies dann anhand einer gegebener Start und Ziel Koordinate  sowie Energiemenge löst.  Der A-Stern Algorithmus soll hierzu verwendet werden.
## Parameter und Variablen
Hier werden die wichtigsten Parameter und deren Sinn erklärt.

**Labyrinth**: 2 Dimensionales Array der Größe 10 mal 10 indem der Inhalt des Labyrinth gespeichert wird. Alle Felder des Arrays werden bei Initialisierung auf 0 für Leer gesetzt. Das Labyrinth besitzt aber auch  wie Sterne und Energie die eingesammelt werden können und Mauern welches die Bewegung einschränken

**Mauern**: Mauern werden zwischen 2 Felder gesetzt und verhindern das man von dem einen Feld auf  das andere kommt. Die Position der Mauern im Labyrinth wird aus einer csv Datei eingelesen.

**Sterne**: Sterne werden auf Felder gesetzt und geben 2 Punkte wenn sie durch das betreten eines Feldes eingesammelt werden. Die Position der Sterne im Labyrinth wird aus einer csv Datei eingelesen.

**Energie**: Energie wird auf Felder gesetzt und gibt 5 Energiepunkte wenn sie durch das betreten eines Feldes eingesammelt wird. Wenn die Gesamtenergie aufgebraucht ist und das Ziel noch nicht erreicht so ist das Programm gescheitert. Die Position der Energie im Labyrinth wird aus einer csv Datei eingelesen. Die Anfangsenergie wird im CLI Betrieb al Parameter übergeben oder bei der GUI  in einem Feld eingegeben.

**Start und Ziel Koordinate**: Start und Ziel Koordinaten werden im CLI Betrieb als Parameter übergeben. Im GUI Betrieb in einem Feld eingegeben. Die Eingabe ist in beiden Fällen ein String welches aus x und y Koordinate besteht getrennt von einem Komma bsp. „3, 2“ Koordinate x = 3 y = 2.

### Feldererklärung
+ 0 = Leeres Feld
+ 1 = Feld mit angrenzender Mauer
+ 2 = Feld mit Energie
+ 3 = Feld mit Energie und angrenzender Mauer
+ 4 = Feld mit Stern
+ 5 = Feld mit Stern und angrenzender Mauer

Es ist nicht möglich von einem Feld mit angrenzender  Mauer (1) auf ein anderes Feld mit angrenzender Mauer zu gehen (1, 3, 5).   Wenn man ein Feld mit Energy (2, 3) oder Stern (4, 5) betritt so wird dies um den Standardwert des Feldes reduziert (-2 bei Energie oder -4 bei Stern) dadurch wird diese Feld dann zu einem Leeren Felod oder einem mit Mauer (0, 1) und der Stern oder die Energie wird eingesammelt
## Umsetzung
Das Programm wurde als Python Script implementiert welches in 2 verschiedenen Modi verwendet werden kann. Eine Command Line Interface (CLI) welches das Ergebnis für ein Pfad durch das  Labyrinth liefert. Sowie eine Grafische Benutzeroberfläche wo man mehrere verschiedene Labyrinthe mit Unterschiedlichen Start und Ziel Koordinaten laufen lassen kann.
Die Ausgabe ist in beiden Versionen der Pfad, die anzahl Gesammelter Sterne Mal 2 genommen, die übrig gebiebene Energiemenge und ob man es bis zum Ziel geschaft hatt mit der Energie.
Für die umsetztung wurden einige Biblotheken von Python verwendet. Diese Sind zum verwenden von der Anwendung nötig.
+ Pandas: Bibliothek für die Verwaltung von Daten
+ Numpy: Bibliothek für den Umgang mit Vektoren und Matrizen
+ Tkinter:  Bibliothek um GUIs in Python zu Erstellen
+ Sys
+ Argparse:  Bibliothek um die CLI interface zu erstellen
## Verwendung mit Beispiele
### Command Line Interface (CLI)
Die CLI bestitzt 2 Hauptoptionen man kann die Hilfe aufrufen oder die Eigenliche Anwendung Verwenden. Die Hilfe wird mit dem nachfolgendem Befehl aufgerufen.
```shell script
foo@bar:~/Astart-DHBW-KI$ python3 A-Star-Search.py -h
usage: A-Star-Search.py [-h] [-s START] [-g GOAL] [-se STARTENERGY]
                          [-w WALLS] [-st STARS] [-e ENERGY]

optional arguments:
  -h, --help            show this help message and exit
  -s START, --start START
                        Startvalue as: "x,y"
  -g GOAL, --goal GOAL  Goalvalue as: "x,y"
  -se STARTENERGY, --startenergy STARTENERGY
                        Energy as number
  -w WALLS, --walls WALLS
                        Path to wall csv
  -st STARS, --stars STARS
                        Path to star csv
  -e ENERGY, --energy ENERGY
                        Path to energy csv

```

Hier sieht man auch die Parameter die Benötigt werden um die Anwendung im CLI Betrieb auszuführen. Es werden alle Parameter Benötigt sowie im folgendem Beispiel gezeigt wird. Wenn nicht alle Parameter Gegeben sind wird die GUI Version aufgerufen.
```shell script
foo@bar:~/Astart-DHBW-KI$ python3 A-Star-Search.py -s "0,0" -g "9,9" -se 15 -w "CSV-Data/S_A01_Mauer.csv" -st "CSV-Data/S_A01_Stern.csv" -e "CSV-Data/S_A01_Energie.csv"
Start CMD
### Enter start as: x,y | default 0, 0
### Enter goal as: x,y | default 9, 9
### Enter energy as number default 5
15
### 1) Generate Clean Maze ###
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
### 2) Get Wall data from csv if empty uses example csv ###
### 3) Set Wall Data in maze ###
### 4) Get Energy data from csv if empty uses example csv###
### 5) Set Star Data in maze ###
### 6) Get Star data from csv if empty uses example csv###
### 7) Set Star Data in maze ###
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 4. 0. 0. 0. 3. 1. 0. 0.]
 [0. 1. 1. 1. 0. 4. 1. 1. 0. 0.]
 [0. 1. 1. 1. 0. 0. 0. 0. 4. 0.]
 [0. 0. 4. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 4. 0. 0. 0.]
 [0. 0. 0. 4. 0. 0. 1. 1. 0. 0.]
 [0. 0. 0. 0. 0. 0. 1. 1. 0. 4.]
 [0. 0. 2. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 4. 0. 0. 0. 0. 0.]]
star
star
### 8) A* was successful ###
### 9) Print Path ###
[(0, 0), (1, 1), (1, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8), (7, 9), (8, 9), (9, 9)]
### 10) Print energy ###
3
### 11) print stars ###
4

Process finished with exit code 0

```

### Graphical User Interface (GUI)
Um die Grafische Benutzeroberfläche aufzurufen wird der Script ohne Parameter ausgeführt.
```shell script
foo@bar:~/Astart-DHBW-KI$ python3 A-Star-Search.py 
```
Dann können die Start und Zielwerte sowie Anfangsenergie in der GUI angegeben werden und die Dateien für die Sterne, Energie und Mauern können über den Dateibrowser ausgewählt werden.
![GUI](GUI-Screenshot.png)