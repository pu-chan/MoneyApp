from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),
    path('', RedirectView.as_view(url='/todo/')),
]
