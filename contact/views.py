from django.views.generic import CreateView

from .models import ContactRequest


class ContactRequestView(CreateView):
    model = ContactRequest
    fields = ('first_name', 'last_name',
              'answer', 'message', 'email')
    success_url = '/'
    template_name = 'contact/home.html'
