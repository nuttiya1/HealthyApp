from django.shortcuts import render
from fitjang.models import Activity

# Create your views here.

def homepage(request):
    act = Activity()
    act.activity_text = request.POST.get('act_text', '')
    act.save()


#    if request.method == 'POST':
#        Activity.objects.create(text=request.POST.get['activity_text'])

    return render(request, 'homepage.html', {'new_activity': act.activity_text})

#def new_data(request):
#    new_list = List.objects.create()
#    Text.objects.create(text=request.POST['data_text'], list=new_list)

#def add_data(request, data_id):
#    new_list = List.objects.get(id=data_id)
#    Data.objects.create(text=request.POST['data_text'], list=new_list)

def show(request):
#    new_list = List.objects.get(id=data_id)
    return render(request, 'show.html')
