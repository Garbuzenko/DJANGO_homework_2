from django.shortcuts import render
from django.urls import reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def recipes_view(request, recipesVal):
    template_name = 'calculator/index.html'
    servings = float(request.GET.get('servings'))
    print(servings)
    context = {}

    context['recipe'] = DATA.get(recipesVal)
    if servings:
        for ingredient, amount in context['recipe'].items():
            context['recipe'][ingredient] = amount * servings
            print(ingredient)
        # for c in context['recipe']:
        #     c.get('ingredient') = c.get('amount')
        # context['recipe'] = DATA.get(recipesVal)

    print(DATA.get(recipesVal))
    return render(request, template_name, context)
def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home')
    }
    for d in DATA:
        pages[d] = d + '/'

    print(pages)

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)