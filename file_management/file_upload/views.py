from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy
from .forms import LoginForm, FileUploadForm
from .models import UploadedFile

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'file_upload/login.html', {'form': form})


@login_required
def home_view(request):
    if request.user.is_client:
        if request.method == 'POST':
            form = FileUploadForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = FileUploadForm()
        return render(request, 'file_upload/home_client.html', {'form': form})
    elif request.user.is_admin:
        files = UploadedFile.objects.all()
        return render(request, 'file_upload/home_admin.html', {'files': files})
    else:
        # Handle cases where the user is neither client nor admin
        return redirect('login')


class FileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = UploadedFile
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.request.user.is_admin