# Testfall-Generierung

## JSON-Struktur
### Beispiel
```json
{
  "ECU": "BodyControlModule",
  "Mechanism": "SecurityAccess",
  "Details": {
    "Seed": "0xABCD1234",
    "Key": "0x1234EFGH"
  }
}
```

---

## Python-Skript: Ablauf
1. **JSON-Eingabe**:
   - Das Skript liest die JSON-Datei und extrahiert Schlüsselwerte wie `Seed` und `Key`.

2. **Prompt-Erstellung**:
   - Das Skript generiert basierend auf den JSON-Daten einen Prompt, der an das LLM gesendet wird.

3. **Anfrage an LLM**:
   - Beispiel:
     ```bash
     curl -X POST http://localhost:11434/v1/completions      -H "Content-Type: application/json"      -d '{"model": "llama2:7b", "prompt": "<dein Prompt>"}'
     ```

4. **Ergebnisse verarbeiten**:
   - Das LLM gibt einen vollständig generierten Testfall aus, der als Dokument gespeichert wird.

---

## Generierter Testfall: Beispiel
### Security Access $27
**Run Steps:**
- **Run Step 1**: Fordere Seed (Challenge) an.
- **Run Step 2**: Berechne die Antwort basierend auf dem Seed.
- **Run Step 3**: Sende die Antwort an die ECU.
- **Run Step 4**: Verifiziere Zugriff auf gesicherte Funktionen.

**Shutdown Steps:**
- Wechsle zurück in den Default Session Mode.

---

## Nächste Schritte
- JSON-Input um weitere Mechanismen erweitern (z. B. Secure Routing).
- Validierung der Testfälle mit realen ECUs.
- Automatisierte Tests in die CI/CD-Pipeline integrieren.
