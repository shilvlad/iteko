from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('main.urls')),
    path('helpdesk/', include('helpdesk.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),

]