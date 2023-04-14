from django.shortcuts import render
from app.models import Github
# Create your views here.
def index(request):
    d=Github.objects.all()
    for i in d:
        print(i.image.url)
    data={"data":d}
    return render(request,"index.html",data)