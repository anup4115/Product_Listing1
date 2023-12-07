"""
URL configuration for productlisting project.

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
from django.contrib import admin
from django.urls import path
from products import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('create/', views.Create,name='create'),
    path('search/', views.Search,name='search'),
    path('delete/<int:id>', views.Delete,name='delete'),
    path('update/<int:id>', views.Update,name='update'),
    path('events/', views.event_calendar, name='event_calendar'),
    path('events/<int:event_id>/', views.event_details, name='event_details'),
    path('events/<int:event_id>/book/', views.book_event, name='book_event'),
    path('send-message/', views.send_message, name='send_message'),
]
