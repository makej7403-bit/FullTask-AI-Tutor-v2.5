import firebase_admin
from firebase_admin import auth as firebase_auth
from firebase_admin import credentials
import os

def init_firebase():
    # Load service account JSON from env var or a mounted secret file
    sa_json = os.environ.get("FIREBASE_SA_JSON")
    if sa_json:
        cred = credentials.Certificate(sa_json)
        firebase_app = firebase_admin.initialize_app(cred)
        return firebase_app
    return None

_ = init_firebase()

def verify_token(id_token: str):
    try:
        decoded = firebase_auth.verify_id_token(id_token)
        return {"uid": decoded.get("uid"), "email": decoded.get("email")}
    except Exception:
        return None
