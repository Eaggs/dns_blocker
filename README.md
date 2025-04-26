# 🛡️ AdBlock DNS for Windows

Privatni lokalni DNS adblocker za Windows 10/11, inspirisan Pi-hole-om, koji blokira online reklame pomoću custom DNS servera napisanog u Pythonu.

---

## 🚀 Karakteristike

✅ Blokira online reklame na nivou DNS zahteva  
✅ Radi lokalno na tvojoj Windows mašini  
✅ Može da se pokreće kao servis (uz NSSM)  
✅ Customizovana blocklista (možeš da dodaš npr. Twitch ad domene)  
✅ Nema instalacije eksternih aplikacija  

---

## 📦 Tehnologije

- [Python 3.10+](https://www.python.org/)
- [dnslib](https://pypi.org/project/dnslib/)
- Windows Service (preko [NSSM](https://nssm.cc/))
- Custom blockliste

---

## 📥 Instalacija

1. **Kloniraj projekat**
   ```bash
   git clone https://github.com/tvojusername/dns_blocker.git
   cd dns_blocker
2. Instaliraj zavisnosti
   pip install -r requirements.txt
3. Nađi slobodan UDP port Pokreni skriptu:
   python find_free_port.py

5. Postavi taj port u dns_blocker.py
 UDPServer(("127.0.0.1", PORT), DNSHandler).serve_forever()

7. Pokreni DNS server
   python dns_blocker.py
9. Testiraj da li je port zauzet U Command Promptu:
   netstat -ano | findstr :PORT



   📑 Konfiguracija DNS-a

U Windows Network Settings podesi DNS server na:
127.0.0.1
Napomena: Ako koristiš port različit od 53 — moraš ga ručno proslediti preko resolvera ili lokalnog forwardera.

📦 Instalacija servisa

1. Preuzmi NSSM
2. Instaliraj servis:
   nssm install AdBlockDNS
     Application path: C:\path\to\python.exe
     Arguments: C:\path\to\dns_blocker.py
     Start type: Automatic
     Log on as: Local System
     

