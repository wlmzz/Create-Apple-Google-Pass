
#  Wallet Integration - Guida completa (IT / EN)

---

## 🇮🇹 Guida completa in italiano

### 1. Registrazione ai programmi Developer

#### Apple
1. Vai su https://developer.apple.com/programs/ e iscriviti all’Apple Developer Program (99$/anno).
2. Dopo la registrazione:
   - Vai su Certificates, Identifiers & Profiles.
   - Crea un nuovo Pass Type ID (es: `pass.com.tuodominio.loyalty`).
   - Scarica e installa il certificato Pass Type ID e il certificato Apple WWDR.

#### Google
1. Vai su https://pay.google.com/business/console e crea un Issuer Account.
2. Abilita Google Wallet API sul tuo progetto Google Cloud.
3. Crea una chiave di servizio e scarica il JSON.
   - Prendi l’email del service account (per `iss`).
   - Estrai la chiave privata `.pem`.

---

###  2. Configura il tuo progetto Python

1. Inserisci i certificati nella cartella `certs`:
   ```
   certs/
   ├── passcertificate.pem
   ├── AppleWWDR.pem
   └── google_private_key.pem
   ```
2. Modifica `create_pkpass.py` e `create_google_jwt.py` con i tuoi dati (passTypeIdentifier, teamIdentifier, service_account_email, issuerId/classId).

---

### ✍ 3. Genera la carta

1. Modifica `pass_template/pass.json` mettendo `barcode.message` con l’email dell’utente.
2. Esegui:
   ```
   python create_pkpass.py
   python create_google_jwt.py
   ```
Otterrai il file `.pkpass` e un link per Google Wallet.

---

###  4. Come collegarlo a Wix

####  Flusso
- Utente si registra sul tuo form Wix.
- Wix invia un HTTP POST al tuo server Python/Flask con i dati.
- Il server crea la Apple Wallet pass e il link Google Wallet, e risponde con:
  ```json
  {
    "apple_link": "https://tuosito.com/download/loyalty_card.pkpass",
    "google_link": "https://pay.google.com/gp/v/save/eyJ..."
  }
  ```
- Wix mostra due pulsanti per far aggiungere la carta al Wallet.

####  Come QR con email
Nel `barcode.message` del pass Apple e nel `barcode.value` Google metti sempre l’email utente.

---

###  Come mostrarlo in Wix (snippet HTML)

```html
<script>
async function createWalletCard() {
    const email = document.getElementById('email').value;
    const res = await fetch('https://tuo-server.com/create_card', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: email })
    });
    const data = await res.json();
    document.getElementById('apple-btn').href = data.apple_link;
    document.getElementById('google-btn').href = data.google_link;
    document.getElementById('wallet-links').style.display = 'block';
}
</script>

<input type="email" id="email" placeholder="Inserisci la tua email" />
<button onclick="createWalletCard()">Registrati e crea card</button>

<div id="wallet-links" style="display:none;">
    <a id="apple-btn" class="button">Aggiungi a Apple Wallet</a>
    <a id="google-btn" class="button">Aggiungi a Google Wallet</a>
</div>
```

---

## 🇬🇧 Full guide in English

### 1. Sign up to developer programs

#### Apple
1. Go to https://developer.apple.com/programs/ and join Apple Developer Program ($99/year).
2. Then:
   - Go to Certificates, Identifiers & Profiles.
   - Create a Pass Type ID (ex: `pass.com.yourdomain.loyalty`).
   - Download/install the Pass Type ID cert and Apple WWDR cert.

#### Google
1. Go to https://pay.google.com/business/console and create an Issuer Account.
2. Enable Google Wallet API on your Google Cloud project.
3. Create a service account key JSON and extract:
   - service account email (for `iss`)
   - private key `.pem`.

---

### 2. Configure your Python project

Put your certs in `certs/` and edit `create_pkpass.py` / `create_google_jwt.py` with your IDs.

---

### ✍ 3. Generate the pass

1. Edit `pass_template/pass.json` with `barcode.message` = user email.
2. Run:
   ```
   python create_pkpass.py
   python create_google_jwt.py
   ```

---

### 4. Connect to Wix

#### Flow
- User registers on your Wix form.
- Wix makes HTTP POST to your Python server with user data.
- Server creates Apple Wallet pass and Google link, returns JSON.
- Wix shows two buttons to let the user add the card to Wallet.

####  QR with email
Always encode user email in Apple `barcode.message` and Google `barcode.value`.

---

### How to show on Wix (HTML snippet)

```html
<script>
async function createWalletCard() {
    const email = document.getElementById('email').value;
    const res = await fetch('https://your-server.com/create_card', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: email })
    });
    const data = await res.json();
    document.getElementById('apple-btn').href = data.apple_link;
    document.getElementById('google-btn').href = data.google_link;
    document.getElementById('wallet-links').style.display = 'block';
}
</script>

<input type="email" id="email" placeholder="Enter your email" />
<button onclick="createWalletCard()">Register and create card</button>

<div id="wallet-links" style="display:none;">
    <a id="apple-btn" class="button">Add to Apple Wallet</a>
    <a id="google-btn" class="button">Add to Google Wallet</a>
</div>
```

---

## 🚀 Powered by NRC Company
