from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produit
from .forms import ProduitForm
from django.db.models import F
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm


@login_required
def dashboard(request):
    produits = Produit.objects.all()
    total = produits.count()
    stock_faible = produits.filter(quantite__lte=F('seuil_alerte')).count()

    return render(request, 'stock/dashboard.html', {
        'produits': produits,
        'total_produits': total,
        'stock_faible': stock_faible,
    })

@login_required
def produit_create(request):
    form = ProduitForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'stock/produit_form.html', {'form': form})

@login_required
def produit_update(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    form = ProduitForm(request.POST or None, instance=produit)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'stock/produit_form.html', {'form': form})

@login_required
def produit_delete(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == "POST":
        produit.delete()
        return redirect('dashboard')
    return render(request, 'stock/produit_confirm_delete.html', {'produit': produit})
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to the dashboard after login
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    
    return render(request, 'registration/login.html', {'form': form})



