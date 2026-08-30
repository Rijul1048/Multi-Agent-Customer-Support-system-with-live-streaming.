from django.urls import path
from . import views

urlpatterns = [
    path('',views.order_list, name="order_list"),
    path('<int:order_id>', views.order_details, name="order_details")
]
