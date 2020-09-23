from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import uuid
import boto3

from .models import Rock, Color, Photo
from .forms import PolishedForm
# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):

    error_message = ''

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        
        return  redirect('index')
    else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}

    return render(request, 'registration/signup.html', context)



def rocks_index(request):
    return render(request, 'cats/index.html', {'rocks': rocks})

def cats_detail(request, rock_id):
    rock = Rock.objects.get(id=rock_id)
    polished_form = PolishedForm()
    colors_rock_doesnt_have = Color.objects.exclude(id__in=rock.colors.all().values_list('id'))
    return render(request, 'rocks/detail.html', {
        'rock', rock,
        'polished_form': polished_form,
        'colors': colors_rock_doesnt_have
    })

def add_polished(request, rock_id):
    form = PolishedForm(request.POST)

    if form.is_valid():
        new_polished = form.save(commit=False)
        new_polished.rock_id = rock_id
        new_polished.save()
    return redirect('detail', rock_id=rock_id)

def add_photo(request, rock_id):
    photo_file = request.FILES.get('photo-file', None)

    if photo_file:

        s3 = boto3.client('s3')

        key = uuid.uuid().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]

        try: 
            s3.upload_fileobj(photo_file, BUCKET, key)

            url = f"{S3_BASE_URL}{BUCKET}/{key"

            photo = photo(url=url, rock_id=rock_id)

            photo.save()
        except:
            print('An error occured uploading file to s3')
    return redirect('detail', rock_id=rock_id)

def assoc_color(request, rock_id, color_id):
    Rock.objects.get(id=cat_id).rocks.add(color_id)
    return redirect('detail', rock_id=rock_id)

class RockCreate(CreateView):
    model = Rock
    fields = ['name', 'category', 'descrition', 'age']

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

class RockUpdate(UpdateView):
    model = Rock
    fields = ['category', 'description', 'age']

class RockDelete(DeleteView):
    model = Rock
    success_url = '/rocks/'

def colors_index(request):
    colors = Color.objects.all()
    return render(request, 'colors/index.htmk', { 'colors': colors })

def colors_detail(request, color_id):
    color = Color.objects.get(id=color_id)
    return render(request, 'colors/detail.html', {'color': color})

class ColorCreate(CreateView):
    model = Color
    fields = '__all__'

class ColorUpdate(UpdateView):
    model = Color
    fields = 'color'

class ColorDelete(DeleteView):
    model = Color
    success_url = '/colors/'
