from django.shortcuts import redirect, render
from django.http import HttpResponse
from fitjang.models import Activity, Mets

def homepage(request):

    if "input_box" in request.POST:
        Mets_ = Mets.objects.get(name = request.POST['item_activity'])
        Activity.objects.create(
        activity_text = request.POST['item_activity'],
        weight_data = int(request.POST['val_weight']),
        amount_of_time = int(request.POST['val_time']),
        calories = Mets_.value*int(request.POST['val_weight'])*int(request.POST['val_time'])/60
            )
        return redirect('/')

    items = Activity.objects.all()

    return render(request, 'homepage.html', {'items': items})

def delete_row_table(request):
    if "delete_table" in request.POST:
        activity = Activity.objects.all()
        item_id = int(request.POST.get('item_id'))
        item = Activity.objects.get(id=item_id)
        item.delete()
        return render(request, 'homepage.html', {'items': items})

def exercise(request):
     return render(request, 'exercise.html')

def chest(request):
     return render(request, 'chest.html')

def arms(request):
     return render(request, 'arms.html')

def legs(request):
     return render(request, 'legs.html')

def shoulder(request):
     return render(request, 'shoulder.html')

def back(request):
     return render(request, 'back.html')
