from .models import Category

def category(request):
    query_set = Category.objects.all()
    return {'categories':query_set}