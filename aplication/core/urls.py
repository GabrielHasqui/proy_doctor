from django.urls import path
from aplication.core.views.home import *
from aplication.core.views.patient import *
from aplication.core.views.blood_type import *
from aplication.core.views.specialty import *
from aplication.core.views.employees import *
from aplication.core.views.doctor import *
from aplication.core.views.diagnosis import *
from aplication.core.views.Category_Exam import *
from aplication.core.views.Type_Category import *
from aplication.core.views.audit import * 
from aplication.core.views.post import *
from aplication.core.views.medication_Type import *
from aplication.core.views.medicine_brand import *
from aplication.core.views.medicine import *

app_name = 'core'

urlpatterns = [
  # Home
  path('', HomeTemplateView.as_view(), name='home'),

  # Patient URLs
  path('patient_list/', PatientListView.as_view(), name="patient_list"),
  path('patient_create/', PatientCreateView.as_view(), name="patient_create"),
  path('patient_update/<int:pk>/', PatientUpdateView.as_view(), name='patient_update'),
  path('patient_delete/<int:pk>/', PatientDeleteView.as_view(), name='patient_delete'),
  path('patient_detail/<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),

  # Blood Type URLs
  path('blood_type_list/', BloodTypeListView.as_view(), name="blood_type_list"),
  path('blood_type_create/', BloodTypeCreateView.as_view(), name="blood_type_create"),
  path('blood_type_update/<int:pk>/', BloodTypeUpdateView.as_view(), name='blood_type_update'),
  path('blood_type_delete/<int:pk>/', BloodTypeDeleteView.as_view(), name='blood_type_delete'),
  path('blood_type_detail/<int:pk>/', BloodTypeDetailView.as_view(), name='blood_type_detail'),

  # Specialty URLs
  path('specialty_list/', SpecialtyListView.as_view(), name="specialty_list"),
  path('specialty_create/', SpecialtyCreateView.as_view(), name="specialty_create"),
  path('specialty_update/<int:pk>/', SpecialtyUpdateView.as_view(), name='specialty_update'),
  path('specialty_delete/<int:pk>/', SpecialtyDeleteView.as_view(), name='specialty_delete'),
  path('specialty_detail/<int:pk>/', SpecialtyDetailView.as_view(), name='specialty_detail'),

  # Employee URLs
  path('employee_list/', EmployeeListView.as_view(), name="employee_list"),
  path('employee_create/', EmployeeCreateView.as_view(), name="employee_create"),
  path('employee_update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee_update'),
  path('employee_delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee_delete'),
  path('employee_detail/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),

  # Doctor URLs
  path('doctor_list/', DoctorListView.as_view(), name="doctor_list"),
  path('doctor_create/', DoctorCreateView.as_view(), name="doctor_create"),
  path('doctor_update/<int:pk>/', DoctorUpdateView.as_view(), name='doctor_update'),
  path('doctor_delete/<int:pk>/', DoctorDeleteView.as_view(), name='doctor_delete'),
  path('doctor_detail/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),

  # Diagnosis URLs
  path('diagnosis_list/', DiagnosisListView.as_view(), name="diagnosis_list"),
  path('diagnosis_create/', DiagnosisCreateView.as_view(), name="diagnosis_create"),
  path('diagnosis_update/<int:pk>/', DiagnosisUpdateView.as_view(), name='diagnosis_update'),
  path('diagnosis_delete/<int:pk>/', DiagnosisDeleteView.as_view(), name='diagnosis_delete'),
  path('diagnosis_detail/<int:pk>/', DiagnosisDetailView.as_view(), name='diagnosis_detail'),

  # Category Exam URLs
  path('category_exam_list/', CategoryExamListView.as_view(), name="category_exam_list"),
  path('category_exam_create/', CategoryExamCreateView.as_view(), name="category_exam_create"),
  path('category_exam_update/<int:pk>/', CategoryExamUpdateView.as_view(), name='category_exam_update'),
  path('category_exam_delete/<int:pk>/', CategoryExamDeleteView.as_view(), name='category_exam_delete'),
  path('category_exam_detail/<int:pk>/', CategoryExamDetailView.as_view(), name='category_exam_detail'),

  # Type Category URLs
  path('type_category_list/', TypeCategoryListView.as_view(), name="type_category_list"),
  path('type_category_create/', TypeCategoryCreateView.as_view(), name="type_category_create"),
  path('type_category_update/<int:pk>/', TypeCategoryUpdateView.as_view(), name='type_category_update'),
  path('type_category_delete/<int:pk>/', TypeCategoryDeleteView.as_view(), name='type_category_delete'),
  path('type_category_detail/<int:pk>/', TypeCategoryDetailView.as_view(), name='type_category_detail'),
  
  # Post URLs
  path('post_list/', PostListView.as_view(),name="post_list"),
  path('post_create/', PostCreateView.as_view(),name="post_create"),
  path('post_update/<int:pk>/', PostUpdateView.as_view(),name='post_update'),
  path('post_delete/<int:pk>/', PostDeleteView.as_view(),name='post_delete'),
  path('post_detail/<int:pk>/', PostDetailView.as_view(),name='post_detail'),
  
  # Medication Type URLs
  path('medication_type_list/', Medication_TypeListView.as_view(), name="medication_type_list"),
  path('medication_type_create/', Medication_TypeCreateView.as_view(), name="medication_type_create"),
  path('medication_type_update/<int:pk>/', Medication_TypeUpdateView.as_view(), name='medication_type_update'),
  path('medication_type_delete/<int:pk>/', Medication_TypeDeleteView.as_view(), name='medication_type_delete'),
  path('medication_type_detail/<int:pk>/', Medication_TypeDetailView.as_view(), name='medication_type_detail'),
  
  # Medicine Brand URLs
  path('medicine_brand_list/', Medicine_BrandListView.as_view(), name="medicine_brand_list"),
  path('medicine_brand_create/', Medicine_BrandCreateView.as_view(), name="medicine_brand_create"),
  path('medicine_brand_update/<int:pk>/', Medicine_BrandUpdateView.as_view(), name='medicine_brand_update'),
  path('medicine_brand_delete/<int:pk>/', Medicine_BrandDeleteView.as_view(), name='medicine_brand_delete'),
  path('medicine_brand_detail/<int:pk>/', Medicine_BrandDetailView.as_view(), name='medicine_brand_detail'),
  
  # Medicine URLs
  path('medicine_list/', MedicineListView.as_view(), name="medicine_list"),
  path('medicine_create/', MedicineCreateView.as_view(), name="medicine_create"),
  path('medicine_update/<int:pk>/', MedicineUpdateView.as_view(), name='medicine_update'),
  path('medicine_delete/<int:pk>/', MedicineDeleteView.as_view(), name='medicine_delete'),
  path('medicine_detail/<int:pk>/', MedicineDetailView.as_view(), name='medicine_detail'),
  
  # Audit URLs
  path('audit_list/', AuditUserListView.as_view(), name="audit_list"),
  path('audit_detail/<int:pk>/', AuditUserDetailView.as_view(), name='audit_detail'),
  
]