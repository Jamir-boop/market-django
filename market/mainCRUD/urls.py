from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.index, name="home"),
    path("producto/", views.producto, name="producto"),
    path("agregar_producto/", views.agregar_prod, name="agregar"),
    path("editar_producto/<int:id_producto>/", views.editar_producto, name="editar_producto"),
    path("eliminar_producto/<int:id_producto>/", views.eliminar_producto, name="eliminar_producto"),
    path("register/", views.register, name='register'),
    path("login/", LoginView.as_view(template_name='mainCRUD/admin/login.html'), name='login'),
    path("logout/", LogoutView.as_view(template_name='mainCRUD/admin/logout.html'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("search/", views.search, name="search"),
    path("barra/", views.barra_nav, name="barra_nav"),
]
