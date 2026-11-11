from django.shortcuts import render

# Create your views hfrom django.shortcuts import render 
 
 
def home(request): 
    return render(request, "vagas/home.html")

