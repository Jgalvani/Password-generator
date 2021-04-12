from django.urls import path, include

import generator

urlpatterns = [
    path('', include('generator.urls')),
]
