from django.urls import path
from .views.Attention_hours import *

app_name = 'attention'  

urlpatterns = [
    # Attention Hours   
    path('attention_hours/', AttentionHoursListView.as_view(), name='attention_hours_list'),
    path('attention_hours/create/', AttentionHoursCreateView.as_view(), name='attention_hours_create'),
    path('attention_hours/update/<int:pk>/', AttentionHoursUpdateView.as_view(), name='attention_hours_update'),
    path('attention_hours/delete/<int:pk>/', AttentionHoursDeleteView.as_view(), name='attention_hours_delete'),
    path('attention_hours/detail/<int:pk>/', AttentionHoursDetailView.as_view(), name='attention_hours_detail'),
]