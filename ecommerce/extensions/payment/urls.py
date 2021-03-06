""" Payment-related URLs """
from django.conf.urls import url

from ecommerce.extensions.payment import views

urlpatterns = [
    url(r'^cybersource/notify/$', views.CybersourceNotifyView.as_view(), name='cybersource_notify'),
    url(r'^paypal/execute/$', views.PaypalPaymentExecutionView.as_view(), name='paypal_execute'),
    url(r'^paypal/profiles/$', views.PaypalProfileAdminView.as_view(), name='paypal_profiles'),
    url(r'^iamport/$', views.paymentdata,  name='iamport_payment'),
    url(r'^iamport/pay/$', views.IamportView.as_view(),  name='iamport_payment'),
]
