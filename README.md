# Installationsanleitung

## Anwendung
Diese Applikation generiert ein JSON File aus einem Experiment, welches mit User Inputs selbst erstellt wird
## Setup
- Repository herunterladen und entzippen
- Ins Repository wechseln und ein Virtuelles Enviorment anlegen: ```python -m venv .venv```
- Virtuelles Enviorment aktivieren: ```.\.venv\Scripts\activate```
    - Sollte ein Fehler auftreten ```Set-ExecutionPolicy Unrestricted -Scope Process``` ausführen und nochmals aktivieren
- Packages mit ```pip install -r requirements.txt``` installieren
- Die Anwendung mit ```python main.py``` in einer Komandozeile ausführen und Userinputs mit richtigen Werten befüllen
- Nach erfolgreicehm beenden des Programms wurde eine experiment.json Datei erstellt. Diese beinhaltet ale zuvor einegenen Daten
- Anmerkung: Datei wird bei erneuter Ausführung mit akutellen Weten überschrieben