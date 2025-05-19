from django.shortcuts import render


def about(request):
    """View-функция страницы 'О проекте'."""
    return render(request, 'pages/about.html')


def rules(request):
    """View-функция страницы 'Правила'."""
    return render(request, 'pages/rules.html')
