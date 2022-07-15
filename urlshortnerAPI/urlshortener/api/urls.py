from django.urls import path 
from . import views 

urlpatterns = [
    path('links/<str:custom_name>', views.Link_list, name='premium'),
    path('links/', views.Link_list, name="basic"),
    path('redirect/<str:url_short_name>', views.redirect_to_url, name='redirect')
]
