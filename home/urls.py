from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
urlpatterns=[
    path('',views.home,name='home'),
    path('index/',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path("main/<int:id>",views.main,name='main'),
    path("buy/",views.buy,name="buy"),
    path("payment/",views.payment,name="payment"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
