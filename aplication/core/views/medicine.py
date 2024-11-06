from django.urls import reverse_lazy
from aplication.core.forms.medicine import MedicineForm
from aplication.core.models import Medicamento
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class MedicineListView(ListView):
    template_name = "core/medicine/list.html"
    model = Medicamento
    context_object_name = 'medicamentos'
    query = None
    paginate_by = 2
    
    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get('q')
        tipo = self.request.GET.get('tipo')
        if q1 is not None: 
            self.query.add(Q(nombre__icontains=q1), Q.OR) 
            self.query.add(Q(descripcion__icontains=q1), Q.OR) 
        if tipo:
            self.query.add(Q(tipo__icontains=tipo), Q.AND)
        return self.model.objects.filter(self.query).order_by('nombre')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Medicamentos"
        context['title1'] = "Consulta de Medicamentos"
        return context
    
class MedicineCreateView(CreateView):
    model = Medicamento
    template_name = 'core/medicine/form.html'
    form_class = MedicineForm
    success_url = reverse_lazy('core:medicine_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Registro de Medicamentos'
        context['grabar'] = 'Grabar Medicamento'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        medicine = self.object
        save_audit(self.request, medicine, action='A')
        messages.success(self.request, f"Éxito al crear el medicamento {medicine.nombre}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
class MedicineUpdateView(UpdateView):
    model = Medicamento
    template_name = 'core/medicine/form.html'
    form_class = MedicineForm
    success_url = reverse_lazy('core:medicine_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Medicamento'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        medicine = self.object
        save_audit(self.request, medicine, action='M')
        messages.success(self.request, f"Éxito al modificar el medicamento {medicine.nombre}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al modificar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
class MedicineDeleteView(DeleteView):
    model = Medicamento
    success_url = reverse_lazy('core:medicine_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Medicamento'
        context['description'] = f"¿Desea eliminar el medicamento: {self.object.nombre}?"
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar lógicamente el medicamento {self.object.nombre}."
        messages.success(self.request, success_message)
        return super().delete(request, *args, **kwargs)
    
class MedicineDetailView(DetailView):
    model = Medicamento
    
    def get(self, request, *args, **kwargs):
        medicine = self.get_object()
        data = {
            'id': medicine.id,
            'nombre': medicine.nombre,
            'tipo':str(medicine.tipo.nombre),
            'marca_medicamento': str(medicine.marca_medicamento),
            'descripcion': medicine.descripcion,
            'concentracion': medicine.concentracion,
            'cantidad': medicine.cantidad,
            'precio': medicine.precio,
            'comercial': medicine.comercial,
            'activo': medicine.activo,
            'imagen': medicine.imagen.url 
        }
        return JsonResponse(data)
