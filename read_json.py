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

# Vorlage für den Testfall
template = f"""
Test Case Security Access $27
Test Item: Security Access
• Goal: to successfully test the UDS Service Secure Access $27 mechanism in the ECU.

Init Steps
Init Step 1: Prepare Tools, Documentation, and ECU for Security Access Testing
• Action: Gather the Holon Diagnostic Tool (or CANoe with DLL), the communication matrix, ECU documentation, UDS documentation, and the ECU's corresponding cryptographic key. Ensure the ECU is connected, communication is stable, and switch to a session which Security Access enabled (e.g., Programming Session via UDS Service $10).
• Expected Result: All tools and documents are ready, the ECU is connected, communication is stable, and the diagnostic session is configured to permit Security Access (e.g., Programming Session via UDS Service $10).

Run Steps
Run Step 1: Verify Access Denied for Secured Functions Before Security Access
• Action: Attempt to execute a secured function (e.g., RequestDownload using UDS Service $34) to confirm it is inaccessible before completing the Security Access process.
• Expected Result: The secured function cannot be executed. The ECU responds with a negative response code (e.g., NRC 0x33 = securityAccessDenied).

Run Step 2: Request Seed (Challenge) from the ECU
• Action: Send a Seed request using UDS Service $27 with subfunction 0x01 to request a challenge.
• Expected Result: ECU responds with a positive response (SID 0x67, subfunction 0x01) and sends the Seed (Seed = {seed}) back to the tool.

Run Step 3: Calculate the response Using the Seed
• Action: Use the Seed/challenge provided by the ECU and the cryptographic algorithm in the tool and the cryptographic key to calculate the response.
• Expected Result: A valid response is calculated based on the ECU’s challenge.

Run Step 4: Send the response to the ECU
• Action: Submit the calculated response to the ECU using UDS Service $27 with subfunction 0x02.
• Expected Result: ECU responds with a positive response (SID 0x67, subfunction 0x02), granting access to secured functions.

Run Step 5: Verify Access Granted for Secured Functions
• Action: Attempt to execute the same secured function (e.g., RequestDownload using UDS Service $34) after completing Security Access.
• Expected Result: The secured function is successfully executed, confirming that Security Access has been granted.

Run Step 6: Exit the Programming Session
• Action: Switch out of the Programming Session (e.g., using UDS Service $10 to change to a default session).
• Expected Result: The session is successfully switched, and the ECU no longer allows secured functions to be executed.

Run Step 7: Re-enter the Programming Session and Verify Secured Function Access Inaccessibility
• Action: Return to the Programming Session and attempt to execute the secured function again without performing Security Access.
• Expected Result: The secured function is inaccessible, as Security Access ($27) is required again in the new session.

Shutdown Step 1: Logout from the Programming Session (Optional)
• Action: Send a DiagnosticSessionControl (0x10) request with SubFunction Default Session (0x01) to switch the ECU from the current Programming Session to the Default Session. Verify the ECU responds with a positive response indicating a successful session switch.
• Expected Result: The ECU is logged out of the Programming Session.

Shutdown Step 2: Record All Results and End the Test
• Action: Document all responses, SIDs, and NRCs, and save the test data. Disconnect the diagnostic tool from the ECU.
• Expected Result: All test results are documented, and the ECU connection is safely terminated.
"""

# Ausgabe des generierten Testfalls
print("Generierter Testfall:")
print(template)

# API-Aufruf an das LLM im Docker-Container
def send_to_llm(prompt):
    url = "http://localhost:11434/v1/completions"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "llama2:7b",
        "prompt": prompt
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["text"]
    else:
        print("Fehler beim Abrufen der Antwort:", response.status_code)
        return None

# Anfrage an das Modell senden
generated_response = send_to_llm(template)
if generated_response:
    print("\nAntwort vom LLM:")
    print(generated_response)
