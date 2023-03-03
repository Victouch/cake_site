from django.shortcuts import render

# Create your views here.
def master_chefs(request):
    return render(request, "master_chefs/team.html")