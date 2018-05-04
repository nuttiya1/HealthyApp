from django.shortcuts import redirect, render
from django.http import HttpResponse
from fitjang.models import Activity, Mets
 
def homepage(request):
    items = Activity.objects.all()
    return render(request, 'homepage.html', {'items': items})

def add_activity(request):
    Mets_ = Mets.objects.get(name = request.POST['item_activity'])
    Activity.objects.create(
    activity_text = request.POST['item_activity'],
    weight_data = int(request.POST['val_weight']),
    amount_of_time = int(request.POST['val_time']),
    calories = Mets_.value*int(request.POST['val_weight'])*int(request.POST['val_time'])/60
        )
    return redirect('/')

def delete_row_table(request):
    del_id = request.POST['del_id']
    Activity.objects.get(id=del_id).delete()
    return redirect('/')

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

def food(request):
    return render(request, 'food.html')
