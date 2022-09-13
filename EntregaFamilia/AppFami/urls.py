from django.urls import path
from AppFami.views import *

urlpatterns = [
    
    path('madre/',madre),
    path('hermano/',hermano),
    path('hermano1/',hermano1),
    path('padre/',padre),
    
    ]