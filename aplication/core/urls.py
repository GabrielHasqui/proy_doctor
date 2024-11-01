from django.urls import path
from aplication.core.views.home import *
from aplication.core.views.patient import *
from aplication.core.views.blood_type import *
from aplication.core.views.specialty import *
 
app_name='core' # define un espacio de nombre para la aplicacion
urlpatterns = [
  # ruta principal
  path('', HomeTemplateView.as_view(),name='home'),
  # rutas doctores 
  # path('doctor_list/', views.doctor_List,name="doctor_list"),
  # path('doctor_create/', views.doctor_create,name="doctor_create"),
  # path('doctor_update/<int:id>/', views.doctor_update,name='doctor_update'),
  # path('doctor_delete/<int:id>/', views.doctor_delete,name='doctor_delete'),
  # urls de pacientes
  path('patient_list/',PatientListView.as_view() ,name="patient_list"),
  path('patient_create/', PatientCreateView.as_view(),name="patient_create"),
  path('patient_update/<int:pk>/', PatientUpdateView.as_view(),name='patient_update'),
  path('patient_delete/<int:pk>/', PatientDeleteView.as_view(),name='patient_delete'),
  path('patient_detail/<int:pk>/', PatientDetailView.as_view(),
  name='patient_detail'),
  # urls de tipos de sangre
  path('blood_type_list/', BloodTypeListView.as_view(),name="blood_type_list"),
  path('blood_type_create/', BloodTypeCreateView.as_view(),name="blood_type_create"),
  path('blood_type_update/<int:pk>/', BloodTypeUpdateView.as_view(),name='blood_type_update'),
  path('blood_type_delete/<int:pk>/', BloodTypeDeleteView.as_view(),name='blood_type_delete'),
  # urls de especialidades
  path('specialty_list/', SpecialtyListView.as_view(),name="specialty_list"),
  path('specialty_create/', SpecialtyCreateView.as_view(),name="specialty_create"),
  path('specialty_update/<int:pk>/', SpecialtyUpdateView.as_view(),name='specialty_update'),
  path('specialty_delete/<int:pk>/', SpecialtyDeleteView.as_view(),name='specialty_delete'),

]