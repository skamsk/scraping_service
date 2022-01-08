from datetime import datetime

from django.shortcuts import render


def home(request):
    date = datetime.now().date()
    name = "STEPAN"
    _context ={'name': name, 'date': date}
    return render(request, 'home.html', _context)