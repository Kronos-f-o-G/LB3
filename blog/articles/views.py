from django.shortcuts import render
from .models import Article

def archive(request):
    # Передаем в шаблон все статьи из базы
    return render(request, 'archive.html', {"posts": Article.objects.all()})