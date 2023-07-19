from django.shortcuts import render
from django.views import generic, View


class Home(generic.TemplateView):
    """ This view is used to display the home page """
    template_name = "index.html"


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


class CreateAccountView(View):
    def get(self, request):
        return render(request, 'create_account.html')
