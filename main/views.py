from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from main.models import Wleta
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    wleta_items = Wleta.objects.all().order_by("-added_date")
    return render(request, 'main/index.html', {"wleta_items": wleta_items})

@csrf_exempt
def add_wleta(request):
  current_date = timezone.now()
  full_name = request.POST["full_name"]
  wleta_list = request.POST["wleta_list"]
  created_obj = Wleta.objects.create(added_date=current_date, full_name = full_name, wleta_list= wleta_list)
  lenght_of_tools = Wleta.objects.all().count()
  return HttpResponseRedirect("/")

@csrf_exempt
def delete_wleta(request, wleta_id):
  Wleta.objects.get(id=wleta_id).delete()
  return HttpResponseRedirect("/")