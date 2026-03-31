# core/views.py
from django.http import JsonResponse
from .supabase_client import supabase

def listar_pacientes(request):
    # O comando é quase igual ao JavaScript/Flask
    response = supabase.table('pacientes').select("*").execute()
    
    return JsonResponse(response.data, safe=False)