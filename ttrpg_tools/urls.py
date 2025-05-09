"""
URL configuration for ttrpg_tools project.

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
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("knave/", include("knave_generators.urls")),
    path("mausritter/", include("mausritter.urls")),
    path("monolith/", include("monolith.urls")),
    path(
        "into-the-odd/",
        include(
            "into_the_odd.urls",
        ),
    ),
    path("electric-bastionland/", include("electric_bastionland.urls")),
    path("cairn/", include("cairn.urls")),
    path("liminal-horror/", include("liminal_horror.urls")),
    path("mothership/", include("mothership.urls")),
    path("mothership/gradient-descent/", include("gradientdescent.urls")),
    path("cloud-empress/", include("cloudempress.urls")),
    path("assassins-demons-and-dying-gods/", include("addg.urls")),
    path("grimwild/", include("grimwild.urls")),
    path("mythic-bastionland/", include("mythic_bastionland.urls")),
]
