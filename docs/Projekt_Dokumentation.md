# Projekt-Dokumentation

## Einleitung
Der **Test Case Generator** ist ein universelles Framework zur automatisierten Generierung von Testfällen für verschiedene Cyber Security Mechanismen in ECUs. Das Ziel ist die flexible, skalierbare und effiziente Erstellung von Testfällen basierend auf JSON-Daten mithilfe eines Large Language Models (LLM).

Dieses Projekt verwendet Docker, um eine isolierte und wiederholbare Entwicklungsumgebung bereitzustellen, und integriert CI/CD-Mechanismen, um Code-Qualität und Stabilität sicherzustellen.

---

## Projektziele
- **Flexibilität**: Unterstützung für alle relevanten Cyber Security Mechanismen.
- **Erweiterbarkeit**: Einfache Integration neuer Mechanismen.
- **Automatisierung**: Minimierung manueller Aufgaben bei der Testfall-Generierung.
- **Nachvollziehbarkeit**: Lückenlose Dokumentation aller durchgeführten Schritte.

---

## Infrastruktur
### Architekturüberblick
1. **Docker**: Zum Ausführen der LLM-Modelle und des Servers.
2. **LLM-Modelle**: Wir verwenden **Llama2:7b**, das in einem Docker-Container bereitgestellt wird.
3. **Python-Skript**: Zur Kommunikation mit dem LLM-Server und zur Verarbeitung von JSON-Daten.
4. **CI/CD-Pipeline**: Automatische Validierung und Tests bei jedem Commit.

---

## Herausforderungen
- Lange Antwortzeiten bei der initialen LLM-Konfiguration.
- Sicherstellung der Konsistenz bei mehreren JSON-Datensätzen.
- Optimierung der CI/CD-Pipeline für größere Datenmengen.

---

## Ergebnisse
- Erfolgreich integrierte LLM-basierte Testfall-Generierung.
- Docker-Setup ermöglicht wiederholbare Tests.
- CI/CD-Pipeline sichert Code-Qualität.

---

## Nächste Schritte
- Optimierung der JSON-Struktur für weitere Mechanismen.
- Validierung mit realen Testdaten.
- Automatisierung der Infrastruktur für größere Projekte.
