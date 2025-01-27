import json
import requests

# JSON-Datei öffnen und lesen
with open("example.json", "r") as file:
    data = json.load(file)

# Wichtige Infos aus der JSON holen
ecu = data["ECU"]
mechanism = data["Mechanism"]
seed = data["Details"]["Seed"]
key = data["Details"]["Key"]

# Vorlage aus externer Datei laden
with open("template.txt", "r") as file:
    template = file.read()

# Testfall-Vorlage mit dynamischen Werten befüllen
filled_template = template.format(ecu=ecu, mechanism=mechanism, seed=seed, key=key)

# Prompt für LLM erstellen
print("Generierter Testfall-Prompt:")
print(filled_template)

# LLM-API-Request
try:
    response = requests.post(
        "http://localhost:11434/v1/completions",
        headers={"Content-Type": "application/json"},
        json={
            "model": "llama2:7b",
            "prompt": filled_template
        }
    )
    # Antwort verarbeiten
    if response.status_code == 200:
        result = response.json()["choices"][0]["text"]
        print("\nAntwort des LLM:")
        print(result)
    else:
        print(f"Fehler beim Abrufen der Antwort: {response.status_code} - {response.text}")
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")
