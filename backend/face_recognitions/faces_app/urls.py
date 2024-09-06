from django.urls import path
from . import views
# from ..face_recognitions.urls import urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('celebrities/', views.all_celebrities, name='all_celebrities')
]