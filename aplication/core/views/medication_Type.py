from django.urls import reverse_lazy
from aplication.core.forms.medication_Type import Medication_TypeForm
from aplication.core.models import TipoMedicamento, Medicamento
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit
from django.db.models.deletion import ProtectedError
from django.shortcuts import redirect


class Medication_TypeListView(ListView):
    model = TipoMedicamento
    template_name = 'core/medication_type/list.html'
    context_object_name = 'medication_types'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return TipoMedicamento.objects.filter(
                Q(nombre__icontains=query) |
                Q(descripcion__icontains=query)
            )
        return TipoMedicamento.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Medical'
        context['title1'] = 'Consulta de tipos de medicamento'
        return context


class Medication_TypeCreateView(CreateView):
    model = TipoMedicamento
    form_class = Medication_TypeForm
    template_name = 'core/medication_type/form.html'
    success_url = reverse_lazy('core:medication_type_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        patient = self.object
        save_audit(self.request, patient, action='A')
        messages.success(self.request, f'Éxito al crear el tipo de medicamento {patient.nombre}.')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Error al enviar el formulario. Corrige los errores.')
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Medical'
        context['title1'] = 'Crear tipo de medicamento'
        return context


class Medication_TypeUpdateView(UpdateView):
    model = TipoMedicamento
    form_class = Medication_TypeForm
    template_name = 'core/medication_type/form.html'
    success_url = reverse_lazy('core:medication_type_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        patient = self.object
        save_audit(self.request, patient, action='A')
        messages.success(self.request, f'Éxito al actualizar el tipo de medicamento {patient.nombre}.')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Error al enviar el formulario. Corrige los errores.')
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Medical'
        context['title1'] = 'Actualizar tipo de medicamento'
        return context


class Medication_TypeDeleteView(DeleteView):
    model = TipoMedicamento
    template_name = 'core/medication_type/delete.html'
    success_url = reverse_lazy('core:medication_type_list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            messages.success(request, "Tipo de medicamento eliminado con éxito.")
            return redirect(self.success_url)
        except ProtectedError:
            messages.error(request, "Este tipo de medicamento no se puede eliminar porque está en uso en uno o más medicamentos.")
            return redirect(self.success_url)


class Medication_TypeDetailView(DetailView):
    model = TipoMedicamento

    def get(self, request, *args, **kwargs):
        medication_type = self.get_object()
        data = {
            'id': medication_type.id,
            'nombre': medication_type.nombre,
            'descripcion': medication_type.descripcion,
            'activo': medication_type.activo,
        }
        return JsonResponse(data)