from django.db import transaction
from django.http import Http404
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from products.forms import ProductForm
from products.models import Product


class ProductListView(ListView, LoginRequiredMixin):
    """
    List of products
    """
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    extra_context = {'title': 'Products'}

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = self.kwargs.get('category_pk')
        return context


class ProductListInCategoriesView(ListView, LoginRequiredMixin):
    """
    List of products in specific category
    """
    model = Product
    extra_context = {'title': 'Products'}

    def get_queryset(self):
        category_id = self.kwargs.get('pk')
        return Product.objects.filter(category=category_id, is_published=True)


class ProductCreateView(CreateView, LoginRequiredMixin):
    """
    Product creation
    """
    model = Product
    extra_context = {'title': 'Create product'}
    form_class = ProductForm
    success_url = reverse_lazy('products:product_list')

    def form_validate(self, form):
        self.object.seller = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    """
    Product update
    """
    model = Product
    form_class = ProductForm
    template_name = "products/product_form.html"
    success_url = reverse_lazy('products:product_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.seller != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object

    def form_valid(self, form):
        with transaction.atomic():
            if form.is_valid():
                self.object = form.save()
        return super().form_valid(form)


class ProductDetailView(DetailView):
    """
    Product detail
    """
    model = Product
    extra_context = {'title': 'Product'}


class ProductDeleteView(DeleteView):
    """
    Product deleting
    """
    model = Product
    success_url = reverse_lazy('categories:category_list')
