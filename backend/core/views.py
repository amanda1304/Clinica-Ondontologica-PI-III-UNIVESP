# core/views.py
from django.http import JsonResponse
from .supabase_client import supabase # Onde você configurou o cliente do Supabase

def meu_dados_view(request):
    # Busca os dados no Supabase usando o SDK
    # Substitua 'nome_da_tabela' pelo nome real no seu Supabase
    resposta = supabase.table('nome_da_tabela').select("*").execute()
    
    # Retorna os dados para o React em formato JSON
    return JsonResponse(resposta.data, safe=False)

# Create your views here.
