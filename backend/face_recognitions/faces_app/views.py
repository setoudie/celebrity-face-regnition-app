from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'face_app/index.html')

def all_celebrities(request):
    return render(request, 'face_app/celebrities.html')
