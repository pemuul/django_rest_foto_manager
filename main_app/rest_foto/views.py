from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required

from .forms import UploadFileForm
from .models import Foto
import datetime


# Create your views here.
def index(request):
    response = "You're looking at the results of question."
    return HttpResponse(response)

@login_required
def test(request):
    response = "Test Ok"
    return HttpResponse(response)

@login_required
def new_image(request):
    template = loader.get_template('rest_foto/new_image.html')
    context = {
        'latest_question_list': ['список чего-то'],
        'inp' : '',
    }

    if request.method == 'POST': 

        #form = UploadFileForm(request.POST, request.FILES)
        form_data = request.POST.dict()
        description = form_data.get('description')
        geo = form_data.get('geo')
        peoples = form_data.get('peoples')

        uploaded_file = request.FILES.get('file')

        # при подргузки фотогрфии 
        if (uploaded_file != None) :#and (uploaded_file.filename != ''):
            Foto.objects.create(description = description, foto_im=uploaded_file, people_name_in_foto=peoples, geo=geo, pub_date='2023-01-10 00:00')
            
    return HttpResponse(template.render(context, request))

def filter_foto(request):

    form_data = request.POST.dict()
    geo = form_data.get('geo', '')
    description = form_data.get('description', '')
    people_name = form_data.get('people_name', '')

    # __icontains это фильтр like 
    fotos = Foto.objects.filter(people_name_in_foto__icontains=people_name, geo__icontains=geo, description__icontains=description)
    #fotos = fotos.all()

    context = {
        'fotos': fotos,
        'geo' : geo,
        'description' : description,
        'people_name' : people_name,
    }
    template = loader.get_template('rest_foto/filter_foto.html')

    return HttpResponse(template.render(context, request))

def foto(request, foto_id):
    try:
        foto = Foto.objects.get(id=foto_id)
    except:
        raise Http404("Данного ID не существует")

    context = {
        'foto': foto,
    }
    template = loader.get_template('rest_foto/foto.html')

    return HttpResponse(template.render(context, request))