from django.urls import path
import attacks.phishing.views as views

urlpatterns = [
    path("send-sms/", views.send_msg, name="send-sms")
]
