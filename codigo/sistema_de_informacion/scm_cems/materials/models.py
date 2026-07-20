from django.db import models
from django.core.validators import MinValueValidator

class ComponentCategory(models.TextChoices):
    PANEL = 'PNL', 'Panel (LCD/OLED)'
    MAIN_BOARD = 'MB', 'Main Board (Tarjeta Principal)'
    POWER_SUPPLY = 'PWR', 'Power Supply (Fuente de Poder)'
    BEZEL = 'BZL', 'Bezel / Chasis'
    PACKAGING = 'PKG', 'Empaque y Cartón'
    ACCESSORY = 'ACC', 'Accesorios (Control, Cables, Pedestal)'


class Product(models.Model):
    """Representa el modelo de televisor final a ensamblar."""
    name = models.CharField(max_length=150, verbose_name="Nombre del Modelo")
    sku = models.CharField(max_length=50, unique=True, verbose_name="SKU / Código Único")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción Técnica")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto (Televisor)"
        verbose_name_plural = "Productos (Televisores)"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.sku} - {self.name}"


class Component(models.Model):
    """Representa los componentes individuales en el catálogo general."""
    part_number = models.CharField(max_length=100, unique=True, verbose_name="Número de Parte")
    name = models.CharField(max_length=150, verbose_name="Nombre del Componente")
    category = models.CharField(
        max_length=3,
        choices=ComponentCategory.choices,
        default=ComponentCategory.ACCESSORY,
        verbose_name="Categoría"
    )
    safety_stock = models.PositiveIntegerField(
        verbose_name="Stock de Seguridad Mínimo",
        validators=[MinValueValidator(1)]
    )

    class Meta:
        verbose_name = "Componente"
        verbose_name_plural = "Componentes"
        ordering = ['part_number']

    def __str__(self):
        return f"[{self.get_category_display()}] {self.part_number} - {self.name}"


class BillOfMaterials(models.Model):
    """Modelo intermedio (Through) que define la relación muchos a muchos entre TV y Componentes."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='bom_relations')
    component = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='product_relations')
    quantity = models.PositiveIntegerField(
        verbose_name="Cantidad Requerida",
        default=1,
        validators=[MinValueValidator(1)]
    )

    class Meta:
        verbose_name = "Componente de BOM"
        verbose_name_plural = "Componentes de BOM"
        unique_together = ('product', 'component')  # Evita duplicar el mismo componente en un TV

    def __str__(self):
        return f"{self.quantity}x {self.component.part_number} para {self.product.sku}"


class Inventory(models.Model):
    """Control de inventario en tiempo real acoplado a cada componente."""
    component = models.OneToOneField(Component, on_delete=models.CASCADE, related_name='inventory')
    current_stock = models.PositiveIntegerField(default=0, verbose_name="Stock Físico Actual")
    in_transit_stock = models.PositiveIntegerField(default=0, verbose_name="Stock en Tránsito")
    warehouse_location = models.CharField(max_length=50, verbose_name="Ubicación en Almacén (Rack/Bin)")

    class Meta:
        verbose_name = "Inventario de Componente"
        verbose_name_plural = "Inventarios de Componentes"

    def __str__(self):
        return f"Inventario de {self.component.part_number}: Físico={self.current_stock}"
    
    @property
    def is_under_safety_stock(self) -> bool:
        """Determina de forma reactiva si el componente está en riesgo de desabasto."""
        return self.current_stock < self.component.safety_stock
