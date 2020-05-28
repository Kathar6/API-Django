from django.urls import path

from . import views

app_name = "components"

urlpatterns = [
    path('', views.ComponentCategoryListView.as_view(), name="component_category"),
    path('<int:category>/', views.ComponentListView.as_view(), name="components"),
    path('<int:category>/<int:pk>', views.ComponentDetailView.as_view(), name="component_detail"),
    path('<int:category>/<int:pk>/buy', views.BuyComponentView.as_view(), name="buy_component"),
]