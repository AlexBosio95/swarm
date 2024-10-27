import os

# Ottieni la chiave API di OpenAI dall'ambiente
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Impostazioni per Redis (opzionale)
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)
REDIS_DB = os.getenv("REDIS_DB", 0)

# Controllo della configurazione
if not OPENAI_API_KEY:
    raise ValueError("La chiave API di OpenAI non è impostata. Verifica il file .env o le variabili di ambiente.")