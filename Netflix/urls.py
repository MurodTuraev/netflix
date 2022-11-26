"""Netflix URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title = "Movie application REAT API",
        default_version = 'v1',
        description = "Redoc docs for API",
        contact = openapi.Contact("Murod Turaev <tml.murod@mail.ru>"),
    ),
    public = True,
    permission_classes = (AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movie.urls')),
    # path('docs/', schema_view.with_ui('swagger'), name = 'swagger-docs'),
    path('redoc/', schema_view.with_ui('redoc'), name = 'redoc-docs'),
]
