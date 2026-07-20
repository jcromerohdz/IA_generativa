from django.views.generic import ListView, DetailView
from django.db.models import Prefetch
from .models import Product, BillOfMaterials

class ProductListView(ListView):
    model = Product
    template_name = 'materials/product_list.html'
    context_object_name = 'products'  # Nombre de la variable en el template


class ProductDetailView(DetailView):
    model = Product
    template_name = 'materials/product_detail.html'
    context_object_name = 'product'

    def get_queryset(self):
        """Optimización de queries SQL mediante Prefetching para evitar N+1 queries."""
        return Product.objects.prefetch_related(
            Prefetch(
                'bom_relations',
                queryset=BillOfMaterials.objects.select_related('component', 'component__inventory')
            )
        )
