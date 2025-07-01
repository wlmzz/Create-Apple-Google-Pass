import jwt
import datetime

service_account_email = "your-issuer@your-project.iam.gserviceaccount.com"
private_key = open("certs/google_private_key.pem").read()

data = {
  "iss": service_account_email,
  "aud": "google",
  "typ": "savetowallet",
  "iat": int(datetime.datetime.now().timestamp()),
  "payload": {
    "loyaltyObjects": [
      {
        "id": "issuerId.loyaltyObjectId",
        "classId": "issuerId.loyaltyClassId",
        "state": "active",
        "accountId": "987654",
        "accountName": "Mario Rossi",
        "loyaltyPoints": {"balance": {"string": "35 punti"}},
        "barcode": {"type": "qrCode", "value": "987654"}
      }
    ]
  }
}

signed_jwt = jwt.encode(data, private_key, algorithm="RS256")
print(f"✅ Link per Google Wallet:\nhttps://pay.google.com/gp/v/save/{signed_jwt}")