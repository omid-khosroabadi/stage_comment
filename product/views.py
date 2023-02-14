from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Product, Comment
from .forms import CommentForm


class ProductList(generic.ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'


class ProductDetail(generic.DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class CommentCreate(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        pk = int(self.kwargs['pk'])
        product = get_object_or_404(Product, id=pk)
        obj.product = product
        return super().form_valid(form)


