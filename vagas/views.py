from django.shortcuts import render 
 
from vagas.dados import VAGAS 
 
 
def home(request): 
    return render(request, "vagas/home.html") 
 
 
def mural(request):

    remotas = 0

    for vaga in VAGAS:
        if vaga["modalidade"] == "Remoto":
            remotas = remotas + 1

    contexto = {
        "vagas": VAGAS,
        "total": len(VAGAS),
        "remotas": remotas,
    }

    return render(request, "vagas/mural.html", contexto)