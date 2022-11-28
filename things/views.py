from django.shortcuts import render, redirect
from .forms import ThingsForm
from .models import Thing

def home(request):
    form = ThingsForm()
    if(request.method == 'POST'):
        form = ThingsForm(request.POST)
        if(form.is_valid()):
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            quantity = form.cleaned_data.get('quantity')
            newthing = Thing.objects.create(
                name=name,
                description=description,
                quantity=quantity
            )
            newthing.save()
            return redirect('home')
    return render(request, 'home.html', {'form': form})
