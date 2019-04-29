from django.urls import  path
from converter import views

urlpatterns = [
     path('my_projects/', views.project_list),
     path('my_projects/<int:pk>/', views.project_list_detail),
     path('my_projects/<int:pk>/my_classes/', views.class_list),
     path('my_projects/<int:pk>/my_classes/<int:pk1>/', views.class_list_detail),
     path('my_projects/<int:pk>/my_classes/<int:pk1>/fields/', views.class_fields),
     path('my_projects/<int:pk>/my_classes/<int:pk1>/fields/<int:pk2>/', views.class_fields_detail),
     path('my_projects/<int:pk>/my_classes/<int:pk1>/methods/', views.class_methods),
     path('my_projects/<int:pk>/my_classes/<int:pk1>/methods/<int:pk2>/', views.class_methods_detail),
     path('my_projects/<int:pk>/my_classes/<int:pk1>/methods/<int:pk2>/inputs/', views.method_inputs),
     path('my_projects/<int:pk>/my_classes/<int:pk1>/methods/<int:pk2>/inputs/<int:pk3>/', views.method_inputs_detail),

     path('my_projects/create_class/', views.create_class),
     path('generate_code/', views.generate_code),
     path('test/', views.test)
]