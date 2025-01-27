# Lista flag

1. `flag={hidden_in_metadata}`
2. `flag={os_cmd_injection_vuln}`
3. `flag={ssti_vuln_flask}`
4. `flag={sql_injection_admin_access}`
5. `flag={code_injection_vuln}`
6. `flag={hidden_attribute}`
7. `flag={xss_vuln_flask}`

## Podpowiedzi

1. **`flag={hidden_in_metadata}`**  
   - Przydatne może okazać się narzędzie **ExifTool**.  

2. **`flag={os_cmd_injection_vuln}`**  
   - Zbadaj funkcję aplikacji, która pozwala na komunikację z systemem operacyjnym.  

3. **`flag={ssti_vuln_flask}`**  
   - Spróbuj użyć kodu szablonów Jinja, aby uzyskać dodatkowe informacje.  

4. **`flag={sql_injection_admin_access}`**  
   - Przyjrzyj się polu logowania i przeanalizuj sposób tworzenia zapytań do bazy danych.  

5. **`flag={code_injection_vuln}`**  
   - Poszukaj miejsc, gdzie aplikacja pozwala na wykonywanie kodu.  

6. **`flag={hidden_attribute}`**  
   - Przeglądaj źródło stron aplikacji w poszukiwaniu nietypowych elementów.  

7. **`flag={xss_vuln_flask}`**  
   - Sprobuj wstrzyknąć własny kod JavaScript w polu tekstowym.  
