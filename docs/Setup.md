# Setup-Anleitung

## Voraussetzungen
1. **Docker installieren**
   - Lade Docker Desktop von [docker.com](https://www.docker.com) herunter und installiere es.
   - Überprüfe die Installation:
     ```bash
     docker --version
     ```
     **Beispielausgabe**: `Docker version 27.4.0, build bde2b89`

2. **Python-Abhängigkeiten**
   - Installiere Python (3.8 oder neuer) und `pip`:
     ```bash
     python --version
     pip --version
     ```

---

## Schritte
### 1. Docker-Container starten
1. Starte den Ollama-Container:
   ```bash
   docker run --name ollama-container -p 11434:11434 -d ollama/ollama
   ```
2. Lade das Llama2-Modell in den Container:
   ```bash
   docker exec -it ollama-container ollama pull llama2:7b
   ```
3. Überprüfe, ob der LLM-Server läuft:
   ```bash
   curl -X POST http://localhost:11434/v1/completions    -H "Content-Type: application/json"    -d '{"model": "llama2:7b", "prompt": "Was ist 2 + 2?"}'
   ```
   **Erwartete Ausgabe**: `2 + 2 = 4`

---

### 2. Python-Skript ausführen
1. Klone das Repository:
   ```bash
   git clone https://github.com/simogabr/test-case-generator.git
   cd test-case-generator
   ```
2. Installiere die Python-Abhängigkeiten:
   ```bash
   pip install -r requirements.txt
   ```
3. Führe das Skript aus:
   ```bash
   python src/generate_test_case.py
   ```

---

### 3. CI/CD-Pipeline testen
- Prüfe die `ci.yml`-Pipeline durch Pushen einer Änderung:
   ```bash
   git add .
   git commit -m "Test commit"
   git push origin main
   ```
- Überprüfe die Ergebnisse in der GitHub-Actions-Oberfläche.

## Entwicklungsumgebung einrichten

### 1. Projektverzeichnis erstellen
Erstelle ein neues Verzeichnis für dein Projekt:
```bash
mkdir mein_projekt
cd mein_projekt
```

### 2. Virtuelle Umgebung einrichten
Richte eine Python-virtuelle Umgebung ein, um Abhängigkeiten isoliert zu installieren:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Abhängigkeiten installieren
Installiere notwendige Python-Pakete:
```bash
pip install requests
```

### 4. Skript testen
Erstelle ein kleines Python-Testskript, um sicherzustellen, dass alles funktioniert:
```bash
echo "import requests; print(requests.get('https://api.github.com').status_code)" > test.py
python test.py
```

Wenn alles korrekt eingerichtet ist, solltest du als Ausgabe den HTTP-Statuscode `200` sehen.

### 5. VS Code einrichten
1. **Projekt in VS Code öffnen**:
   ```bash
   code .
   ```
2. **Virtuelle Umgebung auswählen**:
   - Öffne die Command Palette (`Strg + Umschalt + P`).
   - Wähle `Python: Select Interpreter`.
   - Wähle den Interpreter aus, der auf `venv` verweist.

### 6. Pip aktualisieren (optional)
Halte Pip aktuell:
```bash
python -m pip install --upgrade pip
```

Jetzt ist deine Entwicklungsumgebung vollständig eingerichtet und bereit, Python-Code auszuführen!

