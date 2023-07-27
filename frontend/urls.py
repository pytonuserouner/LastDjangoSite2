from django.urls import path
from django.views.generic import TemplateView
from .views import catalog, profile, payment
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', TemplateView.as_view(template_name="frontend/index.html")),
    path('about/', TemplateView.as_view(template_name="frontend/about.html")),
    path('cart/', TemplateView.as_view(template_name="frontend/cart.html")),

    #path('catalog/', TemplateView.as_view(template_name="frontend/catalog.html")),
    path('catalog/', catalog, name='catalog'),
    path('catalog/<int:id>/', catalog, name='catalog'),
    path('profile/', profile, name='profile'),
    #path('catalog/<int:id>/', TemplateView.as_view(template_name="frontend/catalog.html")),
    path('history-order/', TemplateView.as_view(template_name="frontend/historyorder.html")),
    path('order-detail/<int:id>/', TemplateView.as_view(template_name="frontend/oneorder.html")),
    path('orders/<int:id>/', TemplateView.as_view(template_name="frontend/order.html")),
    #path('payment/<int:id>/', TemplateView.as_view(template_name="frontend/payment.html")),
    path('payment/<int:id>/', payment, name='payment'),

    path('payment-someone/', TemplateView.as_view(template_name="frontend/paymentsomeone.html")),
    path('product/<int:id>/', TemplateView.as_view(template_name="frontend/product.html")),
    #path('profile/', TemplateView.as_view(template_name="frontend/profile.html")),
    path('progress-payment/', TemplateView.as_view(template_name="frontend/progressPayment.html")),
    path('sale/', TemplateView.as_view(template_name="frontend/sale.html")),
    path('sign-in/', TemplateView.as_view(template_name="frontend/signIn.html")),
    path('sign-up/', TemplateView.as_view(template_name="frontend/signUp.html")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)