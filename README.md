# Test Case Generator

Der **Test Case Generator** wurde entwickelt, um automatisierte Testfälle für alle relevanten Cyber Security Mechanismen eines ECUs zu generieren. Das Ziel ist es, ein **flexibles und erweiterbares Framework** zu schaffen, das nicht auf spezifische Mechanismen beschränkt ist. 

### Vision
Dieses Projekt bietet die Grundlage für die Testfall-Generierung in einer Vielzahl von Szenarien. Beispiele für Cyber Security Mechanismen, die damit getestet werden können:
- Secure Routing
- SecOC (Secure Onboard Communication)
- Secure Update (z. B. Secure Flashing)
- IPsec mit PSK
- TLS-PSK Handshake

Das Framework ist jedoch **nicht auf diese Mechanismen beschränkt**, sondern für alle relevanten Cyber Security Mechanismen erweiterbar.

### Ordnerstruktur
- **/docs/**: Dokumentation und Projektübersicht.
- **/src/**: Quellcode des Projekts.
- **/tests/**: Testfälle und automatisierte Unit-Tests.
- **/ci-cd/**: CI/CD-Skripte und Konfigurationen.

### Nutzung
1. Klone dieses Repository:
   ```bash
   git clone https://github.com/simogabr/test-case-generator.git
   cd test-case-generator
   ```

2. Installiere die Abhängigkeiten:
   ```bash
   pip install -r requirements.txt
   ```

3. Passe die JSON-Dateien in **/data/** an, um spezifische Testfälle zu generieren.

4. Führe das Script aus:
   ```bash
   python src/generate_test_case.py
   ```

### Kontakt
Erstellt von Simon Gabriel.
