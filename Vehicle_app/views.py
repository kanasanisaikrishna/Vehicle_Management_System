from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def inputform(request):
    return render(request, 'inputform.html')

@login_required
def details(request):
    error_message = None
    if request.method == 'POST':
        po_number = request.POST.get('po_number')
        try:
            vehicle = Vehicle.objects.get(po_number=po_number)
            vehicle_number = vehicle.vehicle_number
            qualitystatus = vehicle.quality_status  # Assuming quality status is stored in the field `quality_status`
            vendor = vehicle.vendor
            product = vehicle.product
            return render(request, 'details.html', {'po_number': po_number,
                                                     'vendor': vendor, 'product': product,
                                                     'vehicle_number': vehicle_number,
                                                     'qualitystatus': qualitystatus})
        except Vehicle.DoesNotExist:
            error_message = "No vehicle found for the entered P.O. number."
    return render(request, 'inputform.html', {'error_message': error_message})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page, or wherever you want
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration_form.html', {'form': form})
