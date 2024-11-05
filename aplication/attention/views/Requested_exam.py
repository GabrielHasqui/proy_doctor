from django.urls import reverse_lazy
from aplication.attention.forms.Requested_exam import RequestedExamForm
from aplication.attention.models import ExamenSolicitado
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class RequestedExamListView(ListView):
    template_name = "attention/requested_exam/list.html"
    model = ExamenSolicitado
    context_object_name = 'Examenes_Solicitados'
    query = None
    paginate_by = 5
    
    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get('q')
        if q1 is not None: 
            self.query |= Q(nombre_examen__icontains=q1) 
            self.query |= Q(paciente__icontains=q1)  
        return self.model.objects.filter(self.query).order_by('nombre_examen')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Medical"
        context['title1'] = "Consulta de Exámenes Solicitados"
        return context
    

class RequestedExamCreateView(CreateView):
    model = ExamenSolicitado
    template_name = 'attention/requested_exam/form.html'
    form_class = RequestedExamForm
    success_url = reverse_lazy('attention:requested_exam_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Registro de Exámenes Solicitados'
        context['grabar'] = 'Grabar Examen Solicitado'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        requested_exam = self.object
        save_audit(self.request, requested_exam, action='A')
        messages.success(self.request, f"Éxito al crear el examen solicitado {requested_exam.nombre_examen}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
class RequestedExamUpdateView(UpdateView):
    model = ExamenSolicitado
    template_name = 'attention/requested_exam/form.html'
    form_class = RequestedExamForm
    success_url = reverse_lazy('attention:requested_exam_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Actualización de Exámenes Solicitados'
        context['grabar'] = 'Actualizar Examen Solicitado'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        requested_exam = self.object
        save_audit(self.request, requested_exam, action='M')
        messages.success(self.request, f"Éxito al actualizar el examen solicitado {requested_exam.nombre_examen}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))

class RequestedExamDeleteView(DeleteView):
    model = ExamenSolicitado
    template_name = 'attention/requested_exam/delete.html'
    success_url = reverse_lazy('attention:requested_exam_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Eliminar Examen Solicitado'
        context['grabar'] = f'¿Está seguro de eliminar el examen solicitado {self.object.nombre_examen}?'
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        requested_exam = self.get_object()
        save_audit(request, requested_exam, action='E')
        messages.success(request, f"Éxito al eliminar el examen solicitado {requested_exam.nombre_examen}.")
        return super().delete(request, *args, **kwargs)

class RequestedExamDetailView(DetailView):
    model = ExamenSolicitado
    
    def get(self, request, *args, **kwargs):
        requested_exam = self.get_object()
        data = {
            'id': requested_exam.id,
            'nombre_examen': requested_exam.nombre_examen,
            'paciente': str(requested_exam.paciente),
            'resultado': requested_exam.resultado.url if requested_exam.resultado else '',
            'comentario': requested_exam.comentario,
            'estado': requested_exam.estado
        }
        return JsonResponse(data)
