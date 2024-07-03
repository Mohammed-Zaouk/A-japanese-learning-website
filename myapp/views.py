from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, Insert_form
from .models import Insert_model
from django.http import JsonResponse
import requests

def home(request):
    return render(request, 'base/home.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    return render(request, 'base/login_page.html')

@login_required
def logout_page(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered! Welcome!")
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'base/register.html', {'form': form})

@login_required
def Insert_page(request):
    if request.method == 'POST':
        form = Insert_form(request.POST)
        if form.is_valid():
            word = form.save(commit=False)
            word.user = request.user  # Associate the word with the logged-in user
            word.save()
            response = {
                'english': word.english,
                'kanji': word.kanji,
                'hiragana': word.hiragana
            }
            return JsonResponse(response)
        else:
            return JsonResponse({'error': form.errors}, status=400)
    else:
        form = Insert_form()
    return render(request, 'base/insert_page.html', {'form': form})

@login_required
def Display_page(request):
    show = Insert_model.objects.filter(user=request.user)  # Filter by the logged-in user
    return render(request, 'base/display.html', {'show': show})

@login_required
def customer_record(request, pk):
    record = Insert_model.objects.get(id=pk, user=request.user)  # Ensure the user owns the record
    return render(request, 'base/record.html', {'record': record})

@login_required
def delete(request, pk):
    record = Insert_model.objects.get(id=pk, user=request.user)  # Ensure the user owns the record
    record.delete()
    messages.success(request, "Record Deleted Successfully...")
    return redirect('Display')

@login_required
def update(request, pk):
    update = Insert_model.objects.get(id=pk, user=request.user)  # Ensure the user owns the record
    form = Insert_form(request.POST or None, instance=update)
    if form.is_valid():
        form.save()
        messages.success(request, "Record Has Been Updated!")
        return redirect('Display')
    return render(request, 'base/update.html', {'form': form})

def kanji_list(request, level):
    base_url = "https://jisho.org/api/v1/search/words"
    query = f"{level} kanji"
    response = requests.get(base_url, params={"keyword": query})
    if response.status_code == 200:
        kanji_data = response.json().get('data', [])
    else:
        kanji_data = []
    
    return render(request, 'base/kanji_list.html', {'kanji_list': kanji_data, 'level': level})

def test_list(request):
    return render(request, 'base/Test.html', {})