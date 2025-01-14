# Uruchomienie projektu z wykorzystaniem WSL (Windows Subsystem for Linux)

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
