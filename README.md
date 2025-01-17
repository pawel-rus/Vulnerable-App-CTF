# Vulnerable Flask Application CTF

## Podatności w aplikacji
Aplikacja podatna jest na kilka różnych rodzajów ataków.

Poniżej znajduje się lista podatności, które są zaimplementowane w tej aplikacji:

1.  **OS Command Injection**
    *   Pozwala na wykonanie poleceń systemu operacyjnego na serwerze.

2.  **Server Side Template Injection (SSTI)**
    *   Pozwala na wstrzyknięcie i wykonanie kodu szablonu Jinja2.

3.  **Python code injection**
    *    Pozwala na wykonanie dowolnego kodu Pythona.

4.  **SQL Injection**
    *    Pozwala na pominięcie autoryzacji poprzez wstrzyknięcie złośliwego kodu SQL.

5.  **Cross-Site Scripting (XSS)**
    *    Pozwala na wstrzyknięcie złośliwego skryptu JavaScript do strony internetowej, który następnie jest wykonywany po stronie klienta.
6.  **Ukryte wskazówki w zawartości**   
    *   Aplikacja zawiera dodatkowe wskazówki w mniej oczywistych miejscach, takich jak zawartość niektórych elementów lub inne ukryte metadane.

## Zadanie dla uczestnika

- Twoim zadaniem jest znalezienie jak największej ilości flag ukrytych w aplikacji bądź na serwerze.

- Flagi zapisane są w formacie **flag={flag_name}**

- Identyfikacja, w jaki sposób udało Ci się znaleźć każdą flagę (np. opis podatności, której użyłeś).

- Przesłanie krótkiej notatki, zawierającej flagi oraz kroki, które podjąłeś, aby wykorzystać podatność.


---
# Uruchomienie z wykorzystaniem Dockera
1. **Zbuduj obraz:** Otwórz terminal w katalogu, gdzie znajduje się `Dockerfile` i uruchom:
   
        
        docker build -t vulnerable-flask-app .
        
2.  **Uruchom kontener:**

        
        docker run -p 5000:5000 vulnerable-flask-app
        
---

# Uruchomienie z wykorzystaniem WSL (Windows Subsystem for Linux)

## Kroki instalacji i uruchomienia

1.  **Instalacja WSL:**

    *   Otwórz **PowerShell** jako administrator i uruchom:
        ```powershell
        wsl --install
        ```

2.  **Sprawdzenie dostępnych dystrybucji:**

    *   Otwórz **PowerShell** i uruchom:
        ```powershell
        wsl -l -v
        ```
        
3.  **Uruchomienie dystrybucji Ubuntu w WSL:**

    *   Otwórz **PowerShell** i uruchom:
        ```powershell
        wsl -d ubuntu bash
        ```
        (zamień `ubuntu` na nazwę twojej dystrybucji, jeśli używasz innej)

4. **Przejdź do katalogu z projektem:**
   *   W terminalu WSL przejdź do folderu z repozytorium :
        ```bash
        cd Vulnerable-App-CTF
        ```

5.  **Aktualizacja pakietów i instalacja Pythona:**

    *   W terminalu WSL uruchom:
        ```bash
        sudo apt update
        sudo apt install python3 python3-pip python3-venv
        ```

6.  **Sprawdzenie wersji Pythona i pip:**

    *   Upewnij się, że Python i pip zostały poprawnie zainstalowane:
        ```bash
        python3 --version
        pip3 --version
        ```

7. **Stworzenie środowiska wirtualnego:**
    *   W terminalu WSL uruchom:
         ```bash
         python3 -m venv venv
         ```
8. **Aktywacja środowiska wirtualnego:**
    *   Uruchom:
        ```bash
        source venv/bin/activate
        ```

9.  **Instalacja zależności:**

    *   Uruchom:
        ```bash
        pip3 install -r requirements.txt
        ```

10. **Uruchomienie aplikacji:**
     *  Uruchom:
        ```bash
         python3 app.py
        ```
