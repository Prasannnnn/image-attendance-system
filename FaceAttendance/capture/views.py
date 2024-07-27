from django.shortcuts import render, redirect
from .forms import PersonForm

def capture_image(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PersonForm()
    return render(request, 'capture_image.html', {'form': form})

def success(request):
    return render(request, 'success.html')
