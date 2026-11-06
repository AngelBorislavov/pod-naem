from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from list.models import Rent
from .forms import RentForm
# Create your views here.
def all_rents(request):
    context = {
        'rents': Rent.objects.all()
    }
    return render(request, 'list/list.html', context)

def new_rent(request):
    form = RentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RentForm()
        return redirect('all_rents')
    context = {
        'form': form
    }
    
    return render(request, 'list/new_rent.html', context)

@require_POST
def delete_rent(request, rent_id):
    rent = get_object_or_404(Rent, id=rent_id)
    rent.delete()
    return redirect('all_rents')
