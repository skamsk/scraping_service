from django.shortcuts import render

from scraping.forms import FindForm
from scraping.models import Vacancy


def home_view(request):
    # print(request.GET)
    city = request.GET.get('city')
    language = request.GET.get('language')
    form = FindForm()
    print(city, language)
    qs = []
    if city or language:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if language:
            _filter['language__slug'] = language
        qs = Vacancy.objects.filter(**_filter)
    return render(request, 'scraping/home.html', {'object_list': qs, 'form': form})