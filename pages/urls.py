from django.urls import path 
from . import views 

urlpatterns = [
    path('index/',views.pagesIndex ,name = 'pagesindex'), # => lma a3ml urls.py elso3'yra 
    path('about/',views.pagesAbout,name ="pagesabout"), # =>http://localhost:8000/pages/about
    # path('',views.pagesAbout),       # =>http://localhost:8000/pages/about
     path('index.html/',views.renderHtml,name ="pagesindexhtml"),
    path('about.html/',views.renderHtml2,name ="pagesabouthtml"),
    path('cars/' , views.viewCars , name ="viewCars"),
     path('task1/' , views.task1 , name ="viewtask1"),

]
