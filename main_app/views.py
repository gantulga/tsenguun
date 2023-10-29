from django.shortcuts import render
from main_app.models import Category, Article
import datetime

# Create your views here.
def index(request):
    print("indexruu orloo")
    all_category = Category.objects.all()
    print(all_category)
    return render(request, 'frontend/index.html', {'cats':all_category})

def category(request, id):
    category = Category.objects.get(pk=id)
    print(category)
    return render(request, 'frontend/category.html', {'category':category, 'ognoo':datetime.datetime.now()})


def article(request, id):
    article = Article.objects.get(pk=id)
    return render(request, 'frontend/article.html', {'article':article})
