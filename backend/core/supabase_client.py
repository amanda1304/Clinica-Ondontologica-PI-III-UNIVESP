# core/supabase_client.py
import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv(os.path.join( ".env"))

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_PUBLISHABLE_KEY")


if not url:
    raise ValueError(f"ERRO CRÍTICO: VITE_SUPABASE_URL não encontrada. Verifique o arquivo .env em: {'.env'}")

# Para operações no Backend, o ideal é usar a SERVICE_ROLE_KEY (secreta) 
# em vez da PUBLISHABLE_KEY para ter permissão total no banco.
supabase: Client = create_client(url, key)

