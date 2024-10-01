from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'face_app/index.html')

def all_celebrities(request):
    celebrities = [
        {
            "first_name": "Anne",
            "last_name": "Hathaway",
            "profession": "Actress"
        },
        {
            "first_name": "Arnold",
            "last_name": "Schwarzenegger",
            "profession": "Actor"
        },
        {
            "first_name": "Ben",
            "last_name": "Afflek",
            "profession": "Actor"
        },
        {
            "first_name": "Dwayne",
            "last_name": "Johnson",
            "profession": "Actor"
        },
        {
            "first_name": "Elton",
            "last_name": "John",
            "profession": "Musician"
        },
        {
            "first_name": "Jerry",
            "last_name": "Seinfeld",
            "profession": "Comedian"
        },
        {
            "first_name": "Kate",
            "last_name": "Beckinsale",
            "profession": "Actress"
        },
        {
            "first_name": "Keanu",
            "last_name": "Reeves",
            "profession": "Actor"
        },
        {
            "first_name": "Lauren",
            "last_name": "Cohan",
            "profession": "Actress"
        },
        {
            "first_name": "Madonna",
            "last_name": "",
            "profession": "Musician"
        },
        {
            "first_name": "Mindy",
            "last_name": "Kaling",
            "profession": "Actress"
        },
        {
            "first_name": "Simon",
            "last_name": "Pegg",
            "profession": "Actor"
        },
        {
            "first_name": "Sofia",
            "last_name": "Vergara",
            "profession": "Actress"
        },
        {
            "first_name": "Will",
            "last_name": "Smith",
            "profession": "Actor"
        }
    ]
    return JsonResponse(celebrities, safe=False)
