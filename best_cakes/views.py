from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import GetInTouchForm


class BaseView(View):

    def get(self, request):
        return render(request, "base.html")


class IndexView(View):

    def get(self, request):
        return render(request, "index.html")


class AboutUsView(View):

    def get(self, request):
        return render(request, "about_us.html")


class ElementsView(View):

    def get(self, request):
        return render(request, "elements.html")


class TortView(View):

    def get(self, request):
        return render(request, "tort.html")


class GenericView(View):

    def get(self, request):
        return render(request, "generic.html")


class GetInTouchView(View):

    def get(self, request):
        form = GetInTouchForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['klonowska@yahoo.com']
            if cc_myself:
                recipients.append(email)

                send_mail(message, email, name, recipients)
                return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = GetInTouchForm()

        return render(request, 'base.html', {'form': form})






