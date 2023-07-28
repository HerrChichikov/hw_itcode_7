from django.views.generic import DetailView
from django.http import HttpResponse, QueryDict

from core import models


class Test(DetailView):
    model = models.Account
    template_name = 'core/tests.html'
    context_object_name = 'account'
    title = 'Запросы с аккаунтом'

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_title()
        return context


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
