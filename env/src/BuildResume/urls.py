from django.urls import path
from .views import login, resume, signup, details, design

urlpatterns = [
    path('login/', login, name='login'),
    path('resume/', resume, name='resume'),
    path('signup/', signup, name='signup'),
    path('details/', details, name='details'),
    path('design/', design, name='design'),
]
