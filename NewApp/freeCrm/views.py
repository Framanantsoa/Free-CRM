from django.shortcuts import render, redirect
from freeCrm.services import *

API_URL="http://127.0.0.1:5000/"
TITLE="Free-CRM"


def getDataFromURL(url):
    response = requests.get(url=url)
    data = response.json() if response.status_code==200 else None
    
    return data


# DASHBOARD
def vueTableauBord(request):
    data = {"title":TITLE, "content":f"Hello {API_URL}"}

    return render(request, "dashboard.html", {"data":data})


# def vueDetails(request, id):
#     pass


# def vueModification(request):
#     pass


