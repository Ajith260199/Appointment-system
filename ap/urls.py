from django.urls import path
from . import views

urlpatterns = [
    path('',views.ap_booking),
    path('cancel',views.ap_cancel),
    path('reschedule', views.ap_reschedule)

]
