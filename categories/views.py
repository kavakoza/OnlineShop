from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from categories.forms import CategoryCreateForm
from categories.models import Category


class CategoryListView(ListView, LoginRequiredMixin):
    """
    List of categories
    """
    model = Category
    template_name = 'categories/category_list.html'
    context_object_name = 'categories'
    extra_context = {'title': 'Categories'}

    def get_categories(self):
        key = 'categories'
        categories = self.get(key)
        if categories is None:
            categories = Category.objects.all()
            self.set(key, categories)
        else:
            categories = Category.objects.all()

        return categories


class CategoryCreateView(LoginRequiredMixin, CreateView):
    """
    Category creation
    """
    model = Category
    form_class = CategoryCreateForm
    success_url = reverse_lazy('categories:category_list')
    extra_context = {'title': 'Create Category'}
