from django.shortcuts import render, redirect, get_object_or_404

from categories.models import Category
from .models import Product

def product_list(request):
    search = request.GET.get('search', '').strip()
    category_id = request.GET.get('category', '').strip()

    products = Product.objects.all()
    categories = Category.objects.all()

    if search:
        products = products.filter(name__icontains=search)

    if category_id and category_id != "All Categories":
        products = products.filter(category_id=category_id)

    ctx = {'products': products, 'categories': categories}
    return render(request, 'products/list.html', ctx)

# def product_detail(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     return render(request, 'categories/detail.html', {'category': category})
#
def product_create(request):
    # if request.method == 'POST':
    #     form = CategoryForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('categories:list')
    # form = CategoryForm()
    return render(request, 'products/form.html')
#
# def product_update(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     if request.method == 'POST':
#         form = CategoryForm(request.POST, request.FILES)
#         if form.is_valid():
#             category.name = form.cleaned_data['name']
#             category.description = form.cleaned_data['description']
#             category.image = form.cleaned_data['image']
#             category.save()
#             return redirect('categories:list')
#     form = CategoryForm(initial={
#         'name': category.name,
#         'description': category.description,
#         'image': category.image
#     })
#
#     return render(request, 'categories/form.html', {'category': category, 'form': form})
#
# def product_delete(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     if request.method == 'POST':
#         category.delete()
#         return redirect('categories:list')
#     return render(request, 'categories/delete-confirm.html', {'category': category})