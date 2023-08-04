from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, QueryDict

from core import models


class DetailHome(DetailView):
    model = models.Home
    template_name = 'core/home_detail.html'
    context_object_name = 'home'
    title = 'Детальный Home'

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_title()
        context["school"] = models.School.objects.all()
        return context


class ListHome(ListView):
    model = models.Home
    template_name = 'core/home_list.html'
    context_object_name = 'homes'
    title = 'Cписок Home'

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_title()
        return context


class HomeCreate(CreateView):
    template_name = 'core/home_create.html'
    model = models.Home
    fields = ('house', 'city', 'num')

    def form_valid(self, form):
        form.instance.street = 'form_valid'
        return super().form_valid(form)


class HomeUpdate(UpdateView):
    template_name = 'core/home_update.html'
    model = models.Home
    fields = '__all__'


class HomeDelete(DeleteView):
    template_name = 'core/home_delete.html'
    model = models.Home
    success_url = reverse_lazy('core:home_list')


def attestation_view(request):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    path = request.path
    full_path = request.get_full_path_info()
    port = request.get_port()
    body = request.body
    method = request.method
    encoding = request.encoding
    headers = request.headers

    response = HttpResponse()
    status_code = response.status_code
    content = response.content
    headers = response.headers
    items = response.items()

    return HttpResponse(f"""
        <p>host: {host}</p>
        <p>user_agent-agent: {user_agent}</p>
        <p>path: {path}</p>
        <p>full_path: {full_path}</p>
        <p>port: {host}</p>
        <p>body: {path}</p>
        <p>method: {user_agent}</p>
        <p>encoding: {encoding}</p>
        <p>headers: {headers}</p>
        <p>-----------------------------</p>
        <p>status_code: {status_code}</p>
        <p>content: {content}</p>
        <p>headers: {headers}</p>
        <p>items: {items}</p>
    """)
