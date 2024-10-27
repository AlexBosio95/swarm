import redis

# Configura Redis per la cache (opzionale)
cache = redis.Redis(host='localhost', port=6379, db=0)

# Funzione per memorizzare nella cache le risposte
def cache_response(key, value):
    cache.set(key, value)

# Funzione per recuperare le risposte dalla cache
def get_cached_response(key):
    return cache.get(key)

# Funzione per generare preventivi basati sul tipo di servizio richiesto
def generate_quote(service_type):
    service_prices = {
        "sviluppo web": 2000,
        "e-commerce": 3000,
        "seo": 1500,
        "design grafico": 1000
    }
    price = service_prices.get(service_type.lower(), "non disponibile")
    return f"Il preventivo per il servizio di {service_type} è di {price} euro."

# Funzione per le risposte dinamiche
def detailed_instructions(context_variables):
    user_name = context_variables.get("user_name", "cliente")
    preferred_contact = context_variables.get("preferred_contact", "email")
    return f"Ciao {user_name}, posso contattarti tramite {preferred_contact} per ulteriori informazioni sui nostri servizi?"

# Funzione di logging semplice per tracciare le richieste
def log_request(user_input, agent_name):
    print(f"Richiesta: {user_input} - Gestita dall'agente: {agent_name}")