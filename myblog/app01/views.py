from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        return HttpResponse('post')

class SiginView(View):

    def get(self, request):
        return render(request, 'signin.html')

    def post(self, request):
        return HttpResponse('post')


class IndexView(View):

    def get(self, request):
        return render(request, 'oindex.html')

    def post(self, request):
        return HttpResponse('post')
    
class OwnIndexView(View):

    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        return HttpResponse('post')