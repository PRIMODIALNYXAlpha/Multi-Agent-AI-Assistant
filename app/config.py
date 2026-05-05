from dotenv import load_dotenv
import os

# Force load .env from root directory
load_dotenv(dotenv_path=".env")

def get_secret(key):
    value = os.getenv(key)

    if not value:
        print(f"❌ Missing ENV variable: {key}")
    else:
        print(f"✅ Loaded {key}")

    return value