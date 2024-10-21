from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def about(request):
    # Рендерить страницу about из templates/about.html
    return render(request, 'about.html')

def login(request):
    # Рендерить страницу about из templates/about.html
    return render(request, 'login.html')


def create_auction(request):
    return  render(request, 'create_auction.html')


def register(request):
    return render(request, 'register.html')


def qr_inter(request):
    return render(request, 'qr_inter.html')


def fill_auction(request):
    return render(request, 'fill_auction.html')


from .forms import AuctionForm
from .models import Auction

def create_auction(request):
    if request.method == 'POST':
        form = AuctionForm(request.POST)
        if form.is_valid():
            auction = form.save()
            return redirect('fill_auction')  # редирект на страницу fill_auction
    else:
        form = AuctionForm()
    
    return render(request, 'create_auction.html', {'form': form})
