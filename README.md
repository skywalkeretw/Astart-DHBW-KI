# Astart-DHBW-KI
A* implementation for a maze as a project for the module artificial intelligence at the DHBW

---
## Dokumentation
### Ziel
Es soll ein Programm erstellt werden, welches den Besten weg durch ein Labyrinth findet. Hierzu soll der A* Algorithmus verwendet werden.
### Parameter
Beim Labyrinth handelt es sich um ein n mal n großes Feld (2 Dimensionales Array der Größe 10x10).Angegeben wurde das es mit einem 10 mal 10 großes Feld Funktionieren soll.  
Start und Ziel werden als Korodinaten angegeben (x, y).
Das Labyrinth soll zudem verschidene Objekte beinhalten: Sterne, Mauern und Energie.
Die Position dieser Objekte werden aus 3 verschiedenen csv Dateien eingelesen.  
Energie und Sterne werden als Kordinaten in den csv Dateien gespeichert und dann ind dem Feld mit der angegebenen Position Platziert.  
Bei den Mauern wird in der csv 2 Koordinaten angegeben zwischen dem sich eine Mauer befinden soll. 
#### Feldererklärung
Die Felder des Labirinth werden mit Zahlen gekennzeichnet um seinen Inhalt darzustellen
+ 0 = Leeres Feld  
+ 1 = Feld mit angrenzender Mauer  
+ 2 = Feld mit Energy  
+ 3 = Feld mir Energy und angrenzender Mauer (Feld mit Mauer (1) plus (+) Feld mit Energy (2))
+ 4 = Feld mit Stern
+ 5 = Feld mit Stern und angrenzender Mauer  (Feld mit Mauer (1) plus (+) Feld mit Stern (3))   

Es ist nicht möglich von einem feld mit Mauer (1) auf ein anderes Feld mit Mauer zu gehen (1, 3, 5).  
Wenn man ein Feld mit Energy (2, 3) oder Stern (4, 5) betritt so wird dies um den Standardwert des Feldes reduziert (-2 oder -4)
dadurch wird diese Feld dann zu einem Leeren Felod oder einem mit Mauer (0, 1) und der Stern oder die Energie wird eingesammelt


### Verwendung:
Die Anwendung kan in 2 verschidenen Modi verwendet werden. Einmal eine CLI Anwedung welces einmal durchläuft und das Ergebnis ausgibt.
Und ein Grafische Benutzeroberfläche wo die Eingabewerte mehrfach eingegeben und angepasst werden können.

Ausgegeben wird in beiden Fällen der Pfad, die Anzahl gesammelter Sterne sowie die übrig gebliebene Energie.   

CLI Bsp.   
Alle Optionalen Parameter werden für den CLI Betrieb benötigt
```shell script
foo@bar:~/Astart-DHBW-KI$ python3 A-Star-Version1.py -s "0,0" -g "9,9" -se 15 -w "CSV-Data/S_A01_Mauer.csv" -st "CSV-Data/S_A01_Stern.csv" -e "CSV-Data/S_A01_Energie.csv"
```
ClL help 
```shell script
foo@bar:~/Astart-DHBW-KI$ python3 A-Star-Version1.py -h
usage: A-Star-Version1.py [-h] [-s START] [-g GOAL] [-se STARTENERGY]
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
GUI bsp
```shell script
foo@bar:~/Astart-DHBW-KI$ python3 A-Star-Version1.py 
```




```console
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]  
[0. 0. 4. 0. 0. 0. 3. 1. 0. 0.]  
[0. 1. 1. 1. 0. 4. 1. 1. 0. 0.]  
[0. 1. 1. 1. 0. 0. 0. 0. 4. 0.]  
[0. 0. 4. 0. 0. 0. 0. 0. 0. 0.]  
[0. 0. 0. 0. 0. 0. 4. 0. 0. 0.]  
[0. 0. 0. 4. 0. 0. 1. 1. 0. 0.]  
[0. 0. 0. 0. 0. 0. 1. 1. 0. 4.]  
[0. 0. 2. 0. 0. 0. 0. 0. 0. 0.]  
[0. 0. 0. 0. 4. 0. 0. 0. 0. 0.]  
```

