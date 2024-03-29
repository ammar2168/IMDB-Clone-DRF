from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('dashboard/', admin.site.urls),
    path('api/movies/', include('watchlist_app.api.urls')),
    path('api/account/', include('user_app.api.urls'))
]
