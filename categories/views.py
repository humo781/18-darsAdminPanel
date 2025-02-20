from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoryForm
from .models import Category

def home(request):
    return render(request, 'index.html')

def category_list(request):
    search = request.GET.get('search')

    if search:
        categories = Category.objects.filter(name__icontains=search)
    else:
        categories = Category.objects.all()

    ctx = {'categories': categories}
    return render(request, 'categories/list.html', ctx)

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'categories/detail.html', {'category': category})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('categories:list')
    form = CategoryForm()
    return render(request, 'categories/form.html', {'form': form})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category.name = form.cleaned_data['name']
            category.description = form.cleaned_data['description']
            category.image = form.cleaned_data['image']
            category.save()
            return redirect('categories:list')
    form = CategoryForm(initial={
        'name': category.name,
        'description': category.description,
        'image': category.image
    })

    return render(request, 'categories/form.html', {'category': category, 'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('categories:list')
    return render(request, 'categories/delete-confirm.html', {'category': category})
