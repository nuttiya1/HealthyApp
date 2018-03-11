from django.shortcuts import redirect, render
from django.http import HttpResponse
from fitjang.models import Activity

def homepage(request):

    if request.method == 'POST':
        Activity.objects.create(
        activity_text=request.POST['item_activity'],
        weight_data=int(request.POST['val_weight']),
        amount_of_time=int(request.POST['val_time']),
        mets=returnMETS(request.POST['item_activity'])
            )
        return redirect('/')

    items = Activity.objects.all()

    return render(request, 'homepage.html', {'items': items})

def returnMETS(items):
    if items == "run":
        return 7.0
#     act.activity_text = request.POST.get('act_text', 'Mac donold')
#     act.save()
#
# #    if request.method == 'POST':
# #        Activity.objects.create(text=request.POST.get['activity_text'])request.POST['item_activity']
#
#     return render(request, 'homepage.html', {'new_activity': act.activity_text})

#######
#def new_data(request):
#    new_list = List.objects.create()
#    Text.objects.create(text=request.POST['data_text'], list=new_list)

#def add_data(request, data_id):
#    new_list = List.objects.get(id=data_id)
#    Data.objects.create(text=request.POST['data_text'], list=new_list)
########

def exercise(request):
     return render(request, 'exercise.html')
