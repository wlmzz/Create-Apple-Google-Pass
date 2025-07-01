import json
import zipfile
import hashlib
import subprocess
from pathlib import Path

PASS_DIR = Path("pass_template")
OUTPUT_PKPASS = "loyalty_card.pkpass"

manifest = {}
for file in PASS_DIR.iterdir():
    with open(file, 'rb') as f:
        sha1 = hashlib.sha1(f.read()).hexdigest()
    manifest[file.name] = sha1

with open(PASS_DIR / "manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)

subprocess.run([
    "openssl", "smime", "-binary", "-sign",
    "-signer", "certs/passcertificate.pem",
    "-certfile", "certs/AppleWWDR.pem",
    "-noattr", "-outform", "DER",
    "-in", str(PASS_DIR / "manifest.json"),
    "-out", str(PASS_DIR / "signature")
])

with zipfile.ZipFile(OUTPUT_PKPASS, 'w') as pkpass:
    for file in PASS_DIR.iterdir():
        pkpass.write(file, file.name)

print(f"✅ Apple Wallet pass creato: {OUTPUT_PKPASS}")