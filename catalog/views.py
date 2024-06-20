from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView
from catalog.models import Product, Version
from catalog.forms import ProductForm, VersionForm


# def home(request):
#     Products = Product.objects.all()
#     contex = {"Products": Products}
#     return render(request, "product_list.html", contex)


# def product_detail(request, pk):
#     Product_detal = Product.objects.get(pk=pk)
#     contex = {"Products": Product_detal}
#     return render(request, "product_detail.html", contex)

class ProductListView(ListView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        products = Product.objects.all()

        for product in products:
            versions = Version.objects.filter(name=product)
            active_versions = versions.filter(version_now=True)
            if active_versions:
                product.active_version = active_versions.last().version_name
            else:
                product.active_version = 'Нет активной версии'

        context_data['object_list'] = products
        return context_data


def contacts(request):
    return render(request, "shyprocontacts.html")


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()

        versions = Version.objects.filter(name=product)
        active_versions = versions.filter(version_now=True)
        if active_versions.exists():
            product.active_version = active_versions.first().version_name
        else:
            product.active_version = 'Нет активной версии'

        context['version'] = product.active_version
        context['version_list'] = versions


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context['formset'] = ProductFormset(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))
