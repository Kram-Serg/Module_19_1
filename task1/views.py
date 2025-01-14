from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *
from django.core.paginator import Paginator

# Create your views here.


def menu_index(request):
    title = 'мой сайт'
    back = 'Вернуться на главную страницу'
    cart = 'Корзина'

    context = {'title': title, 'back': back, 'cart': cart}
    return render(request, 'fourth_task/menu.html', context)


def start_index(request):
    title = 'мой сайт'
    back = 'Вернуться на главную страницу'
    cart = 'Корзина'
    context = {'title': title, 'back': back, 'cart': cart}
    return render(request, 'fourth_task/start.html', context)


def buy_index(request):
    title = 'мой сайт'
    back = 'Вернуться на главную страницу'
    cart = 'Корзина'
    games = Game.objects.all()
    context = {'title': title, 'back': back, 'cart': cart,
               'games': games
               }
    return render(request, 'fourth_task/buy.html', context)


def cart_index(request):
    title = 'мой сайт'
    back = 'Вернуться на главную страницу'
    cart = 'Корзина'
    context = {'title': title, 'back': back, 'cart': cart}
    return render(request, 'fourth_task/cart.html', context)


# users = ['Sergei', 'Ilya', 'Olesya']


# Create your views here.

# def sign_up_by_html(request):
#     info = {}
#
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         repeat_password = request.POST.get('repeat_password')
#         age = int(request.POST.get('age'))
#
#         if username in users:
#             info['error'] = 'Пользователь уже существует'
#             return HttpResponse('Пользователь уже существует')
#         elif password != repeat_password:
#             info['error'] = 'Пароли не совпадают'
#             return HttpResponse('Пароли не совпадают')
#         elif age < 18:
#             info['error'] = 'Вы должны быть старше 18'
#             return HttpResponse('Вы должны быть старше 18')
#         else:
#             info['message'] = f'Приветствуем, {username}'
#         return HttpResponse(f'Приветствуем, {username}')
#
#     return render(request, 'fifth_task/registration_page.html', {'info': info})


def sign_up_by_django(request):
    info = {}
    buyers = Buyer.objects.values_list('name', flat=True)
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username in buyers:
                info['error'] = 'Пользователь уже существует'
                return HttpResponse('Пользователь уже существует')
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return HttpResponse('Пароли не совпадают')
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
                return HttpResponse('Вы должны быть старше 18')
            else:
                info['message'] = f'Приветствуем, {username}'
            return HttpResponse(f'Приветствуем, {username}')
    else:
        form = UserRegister()

    return render(request, 'fifth_task/registration_page.html', {'form': form})


def news_index(request):
    news_all = News.objects.all().order_by('-date')
    paginator = Paginator(news_all, 3)
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    return render(request, 'news.html', {'news': news})
