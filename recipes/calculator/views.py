from django.shortcuts import render, reverse

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
}


def home_view(request):
    template_name = 'calculator/index.html'
    pages = {f'Рецепт {k}': k for k in DATA}
    context = {'pages': pages}
    return render(request, template_name, context)


def _rec(name, number):
    template_name = f'calculator/{name}.html'
    pages = {k: v * number for k, v in DATA[name].items()}
    return template_name, pages


def rec_omlet(request):
    quantity = int(request.GET.get('servings', '1'))
    param = _rec('omlet', quantity)
    context = {'pages': param[1]}
    return render(request, param[0], context)


def rec_buter(request):
    quantity = int(request.GET.get('servings', '1'))
    param = _rec('buter', quantity)
    context = {'pages': param[1]}
    return render(request, param[0], context)


def rec_pasta(request):
    quantity = int(request.GET.get('servings', '1'))
    param = _rec('pasta', quantity)
    context = {'pages': param[1]}
    return render(request, param[0], context)







