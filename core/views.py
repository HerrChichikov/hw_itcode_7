from django.db.models import Count
from django.views.generic import DetailView

from core import models


class Test(DetailView):
    model = models.Account
    template_name = 'core/tests.html'
    context_object_name = 'account'
    title = 'Запросы с аккаунтом'
    course = models.Account.objects.filter(pk__gt = 2).all()

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_title()
        context["course"] = self.course
        return context
