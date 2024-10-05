"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
'''from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
# myapp/urls.py
from django.urls import path
from .views import create_resume, view_resume

urlpatterns = [
    path('create/', create_resume, name='create_resume'),
    path('view/', view_resume, name='view_resume'),
]
'''
"""ResumeBuilder URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
'''from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from BuildResume.views import login

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('',include("BuildResume.urls"))
    path('admin/', admin.site.urls),
    path('', login, name='login'),
    #path('', login, name='login'),  # Use the login view for the empty path
    path('buildresume/', include("BuildResume.urls")),
    #path('signup/', signup, name='signup'),  # Optionally, you can use signup view as well
]'''
from django.contrib import admin
from django.urls import path, include
from BuildResume.views import login, signup, details, design, resume
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/login/', permanent=False), name='index'),  # Redirect to the login page
    path('login/', login, name='login'),  # Correct the path for the login view
    path('signup/', signup, name='signup'),
    path('details/', details, name='details'),
    path('design/', design, name='design'),
    path('resume/', resume, name='resume'),
    path('buildresume/', include("BuildResume.urls")),
    # other paths
]