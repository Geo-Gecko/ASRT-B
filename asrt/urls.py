
from django.contrib import admin
from django.urls import path
from sliders.views import view as slidersView
from mapGrids.views import view as mapGridsView
from location.views import view as locationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sliders/', slidersView),
    path('mapGrids/', mapGridsView),
    path('location/',locationView)

]
