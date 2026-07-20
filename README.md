# IA Generativa
## IA generativa orientado al analisis de datos e Inteligencia de Negocios

![image](https://github.com/jcromerohdz/IA_generativa/blob/main/presentaciones/IA_generica.png)

# Contenido
1. Configuración de equipo
2. Introducción a la programación con python
3. Presentación de Ingeniería de prompts
4. Practicas con Anatomía de prompts

# 1. Configuración de equipo
- Visita la [Sitio oficial lenguaje de programación Python](https://www.python.org/) para más detalles.
- Visita la [Sitio de Descarga de miniconda](https://www.anaconda.com/download) para más detalles.

# Comandos Basicos en CMD
Explorar Directorio
```batch
dir
```
Cambio de directorio
```batch
cd Documents
```
Crear Directorio
```batch
md Proyectos
```
Regresar al Directorio Anterior
```batch
cd ..
```

2. Introducción a la programación con python [link](https://github.com/jcromerohdz/IA_generativa/blob/main/codigo/Python_Intro.ipynb)

3. Simulación de un sistema de información

# Prompt 1 Inicio de pregutas para el analisis de este sistema
```batch
Actúa como un ingeniero en cadena de suministro en el contexto de la industria maquiladora de televisiones y explícame detalladamente los problemas más comunes de producción, por ejemplo, contéstame estas preguntas: ¿Por qué para la línea de producción? ¿Cuál es el tiempo estimado de producción si no tenemos las partes para ensamblar un producto? ¿Cómo contacto a proveedores cercanos para mitigar el impacto? 
```

## Respuesta
Vamos a desglosar detalladamente tus preguntas desde la perspectiva del piso de manufactura y los tableros de control de SCM.

1. ¿Por qué se para la línea de producción? (Causas Raíz en Televisores)
En el ensamble de televisiones, la línea no se detiene por capricho; se detiene porque falta sincronía. Las razones más comunes divididas por su origen son:

* Falta de Componentes Críticos (Material Shortage): Una televisión tiene una lista de materiales (BOM) muy estricta. Si falta el panel LCD/OLED, la tarjeta principal (Main Board), la fuente de poder (Power Board) o incluso los tornillos específicos para el pedestal, la línea se congela. No puedes avanzar un televisor a medias porque reintroducirlo a la línea después genera defectos de calidad.

* Problemas de Calidad del Proveedor (Defective Material): Imagina que llega el contenedor de biseles (marcos frontales), pero el plástico viene rayado o deforme por un mal proceso de moldeo. Aseguramiento de Calidad (QA) pone el lote en Hold (retención). Si no hay stock de seguridad (Safety Stock), la línea se para inmediatamente.

* Desfase en el "Just In Time" (JIT): Muchas maquiladoras operan con inventarios mínimos para no saturar el almacén. Si el camión que trae los empaques de cartón se retrasó en la aduana o en la carretera, la línea se llena de televisiones terminadas que no se pueden empacar, colapsando el área de Packaging y deteniendo la parte alta de la línea.

* Fallas en el Equipo de Inserción Automática (SMT): Antes del ensamble final, las tarjetas electrónicas se montan en la planta. Si una máquina SMT falla o se queda sin componentes (reels de microchips), se corta el suministro de cerebros para la televisión.

2. ¿Cuál es el tiempo estimado de producción si no tenemos las partes para ensamblar un producto?
Siendo fríos y realistas: El tiempo estimado de producción es INFINITO (o cero unidades por hora) hasta que la primera pieza faltante toque el piso de la planta.

En la industria maquiladora, el cálculo del impacto no se mide en "cuánto tardaremos en fabricarlo después", sino en Tiempo de Recuperación (Time to Recover - TTR) y Costo por Hora de Paro.

El cálculo del impacto real:
* Si falta un componente de Asia (Long Lead Time): Si dependes de un chip o un panel que viene de Corea, Taiwán o China y no viene en tránsito aéreo crítico, el tiempo de paro o retraso de ese modelo puede ser de 2 a 4 semanas.

* Costo de Línea Parada: En una maquiladora de televisiones, tener una línea detenida (con operadores cruzados de brazos) cuesta entre $10,000 y $50,000 USD por hora, dependiendo del volumen del modelo (no es lo mismo parar una línea de pantallas de 32" que una de 75" Premium).

* Estrategia de Mitigación Inmediata: Como Ingeniero de SCM, si veo que una parte va a tardar 3 días en llegar, no dejo la línea parada. Coordino con el departamento de Programación de la Producción (Production Scheduling) para hacer un Cambio de Modelo (Changeover). Desmontamos la línea actual y montamos la producción de otro modelo de televisión del cual sí tengamos el 100% de los materiales.

3. ¿Cómo contacto y activo a proveedores cercanos para mitigar el impacto? (Estrategia de Nearshoring y Fast Track)
Cuando el plan A falla, el equipo de SCM activa el plan de contingencia para localizar proveedores locales o regionales (en un radio de pocas horas de la planta) para hacer un bypass al desabasto. Este es el protocolo de acción rápida:

A. Activación del Directorio de Proveedores Desarrollados (Approved Vendor List - AVL)
En nuestro sistema ERP (como SAP o Oracle), filtramos a los proveedores aprobados por zona geográfica. Buscamos plantas locales que ya pasaron por el proceso de certificación pero que quizás no tienen el contrato principal porque sus precios son ligeramente más altos que los de Asia. En una crisis, el costo de la pieza pasa a segundo término; lo que importa es el costo de parar la línea.

B. El Proceso de Contacto y Negociación "Fast Track"
1. Llamada de Emergencia al Key Account Manager (KAM): No enviamos correos electrónicos informales. El Gerente de Compras o el Ingeniero de SCM llama directamente a los directivos del proveedor local para plantear la necesidad de capacidad inmediata (Spot Capacity).

2. Compartir el "Gage" y las Especificaciones Técnicas: Se envían los planos CAD, las tolerancias y las especificaciones de resina o componentes electrónicos de inmediato para que su equipo de ingeniería confirme si sus máquinas (por ejemplo, inyectoras de plástico de gran tonelaje para las carcasas) pueden correr nuestro molde.

3. Transferencia de Moldes/Herramental (Tooling Transfer): Si el proveedor local tiene la capacidad pero no el molde, mandamos un camión de nuestra planta a recoger el molde de respaldo de nuestro almacén (o retiramos el molde del proveedor original si es local) y se lo entregamos en su planta en cuestión de horas.

C. Alianzas con Clústeres Industriales y Canales de la Industria
Si no tenemos a nadie en el AVL que pueda ayudarnos, recurrimos a:

* Asociaciones de Maquiladoras (Index / Clústeres Electrónicos locales): Se lanza una alerta en la red del clúster industrial de la región: "Se busca proveedor con capacidad disponible para inyección de ABS de alta densidad o ensamble de arneses con entrega en 24 horas". La comunidad industrial maquiladora suele responder rápido para subcontrataciones de emergencia.

* Brokers de Componentes Electrónicos: Para microchips o capacitores, contactamos a distribuidores globales con almacenes regionales (como Avnet, Arrow, Digi-Key) que tienen stock de emergencia en zonas fronterizas o hubs logísticos importantes, listos para enviar por Hand Carrier (una persona que toma un avión con las piezas en una maleta) o flete dedicado esa misma noche.

Como puedes ver, mi trabajo aquí es evitar que la fábrica se convierta en un enorme y costoso almacén de televisiones incompletas. Todo se reduce a visibilidad, flexibilidad en la programación y tener excelentes relaciones con la proveeduría local para cuando el suministro global nos falle.

# Prompt 2 - Conexion con el analisis del sistema para genera estrategia de negocio
```batch
Ahora actúa como un analista de negocio y genérame una estrategia para un sistema de información para la gestión del problema que explicó el ingeniero de cadena de suministro, este sistema debe dividirse en 7 sprints (fases) y cada sprint debe ser explicado detalladamente para que un ingeniero en desarrollo de software pueda entender claramente las fases de cada sprint 
```

## Respuesta:
Para resolver el caos logístico y operativo que describió el ingeniero de cadena de suministro (paros de línea por falta de material, problemas de calidad, alertas JIT y activación tardía de proveedores), vamos a diseñar e implementar un sistema de información crítico: un SCM Cockpit & Emergency Mitigation System (SCM-CEMS).

Como analista, mi objetivo es traducir los dolores de la operación en requerimientos técnicos claros, estructurados bajo el marco de trabajo Scrum. El proyecto se dividirá en 7 Sprints de dos semanas cada uno, diseñados para entregar valor funcional incremental y mantener la arquitectura limpia y escalable para los desarrolladores.

Arquitectura General del Sistema (Para Contexto del Desarrollador)
* Backend: API RESTful (vía Python/Django o Node.js) para procesamiento pesado de datos de inventario.

* Frontend: Framework SPA (como Angular) orientado a páneles reactivos y de alta velocidad (WebSockets para alertas en tiempo real).

* Base de Datos: Base de datos relacional (SQL) para el manejo estricto de la lista de materiales (BOM) y relaciones de proveedores.

Estrategia de Desarrollo: Plan de 7 Sprints
- Sprint 1: Modelado de Datos de Producción y Núcleo de la BOM (Bill of Materials)
- Objetivo del Sprint: Crear las bases de datos funcionales y las API de lectura/escritura para gestionar los componentes críticos de los televisores. Si no entendemos la estructura de la televisión, no podemos predecir su desabasto.

- Entregables Técnicos para el Desarrollador:
    * Modelo de Base de Datos (Esquema SQL): Entidades fuertemente relacionadas: Product (TV Model), Component (Panel, Mainboard, etc.), BOM (Relación muchos a muchos con cantidad requerida) y Inventory (Stock físico, Stock de seguridad, En tránsito).

    * Endpoints API: GET /api/v1/products/{id}/bom para desglosar cada componente necesario por pantalla.

    * Interfaz Angular: Pantalla de consulta de la estructura del producto para los ingenieros de manufactura.

- Sprint 2: Integración de Inventario en Tiempo Real y Alertas de Punto de Reorden (JIT)
- Objetivo del Sprint: Desarrollar el motor que detecte cuándo un componente de televisión está cayendo por debajo del Safety Stock (Stock de seguridad), disparando alertas antes de que la línea se pare.

* Entregables Técnicos para el Desarrollador:
    Background Workers / Cron Jobs: Servicios en segundo plano que consulten o simulen la ingesta de datos del ERP principal para actualizar Inventory.current_stock.
    * Lógica de Negocio (Backend): Algoritmo que compare constantemente:
    $$\text{Stock Actual} + \text{En Tránsito} \le \text{Punto de Reorden}$$
    * Servicio WebSockets: Infraestructura de mensajería (ej. Django Channels o Socket.io) para enviar notificaciones Push inmediatas al frontend cuando un material clave (como el panel LCD) entre en zona de riesgo.

- Sprint 3: Módulo de Gestión de Calidad (QA) y Retención de Lotes (Material Hold)
- Objetivo del Sprint: Permitir a los inspectores de calidad bloquear lotes defectuosos en el sistema, recalculando automáticamente la disponibilidad de material para la línea.

- Entregables Técnicos para el Desarrollador:
    * Estado del Inventario (FSM): Implementar una Máquina de Estados Finitos para los lotes de material (Status: Available -> Inspection -> Quarantine / Approved).

    * Endpoint de Bloqueo: POST /api/v1/inventory/hold que descuente de inmediato el material defectuoso del inventario utilizable.

    * UI Dashboard: Un panel con estados visuales (Rojo/Amarillo/Verde) en Angular para que Control de Producción vea qué componentes fueron rechazados por QA.

- Sprint 4: Motor de Simulación de Producción y Planificación de Cambios de Modelo

- Objetivo del Sprint: Crear la herramienta que permita al programador de la producción simular un "Cambio de Modelo" (Changeover) si se entera de que una parte no llegará a tiempo.

- Entregables Técnicos para el Desarrollador:
    * Algoritmo de Simulación (Simulación de Escenarios): Un servicio de software que reciba un Model_ID y una Quantity_To_Produce, cruce la información con la BOM y el inventario disponible del Sprint 2, y devuelva un JSON con el diagnóstico: {"feasible": true/false, "missing_components": [...]}.

    * UI Drag-and-Drop: Pantalla interactiva en el frontend que permita reordenar la secuencia de producción de las líneas de ensamble para mitigar las horas de paro de forma visual.

Sprint 5: Módulo Geo-Localizado de Proveedores Alternos (AVL - Approved Vendor List)
- Objetivo del Sprint: Integrar el directorio de contingencia para localizar proveedores locales en caso de emergencia, ordenados por cercanía geográfica y capacidad técnica.

- Entregables Técnicos para el Desarrollador:
    * Modelos de Datos de Proveedores: Tablas Supplier, Supplier_Component_Capability (qué piezas pueden fabricar, su costo spot y su lead time local) y Supplier_Location (coordenadas geográficas).

    * Query de Cercanía: Implementación de consultas espaciales (utilizando extensiones como PostGIS o fórmulas de Haversine en backend) para ordenar a los proveedores según la distancia a la maquiladora.

    * Frontend Map: Integración de un mapa interactivo (Leaflet o Google Maps API) que muestre visualmente los proveedores locales capaces de salvar la producción de la pieza faltante.

Sprint 6: Módulo de Comunicación "Fast-Track" y Transferencia de Herramental
- Objetivo del Sprint: Automatizar el contacto con los proveedores aprobados y gestionar el flujo logístico para enviarles los moldes/planos de la pieza de televisión requerida.

- Entregables Técnicos para el Desarrollador:
    * Servicio de Notificación Automatizado: Integración con APIs de comunicación (como Twilio para SMS/WhatsApp o servicios SMTP para correo institucional) para disparar solicitudes de cotización de emergencia (Spot Quotes) con un solo clic.

    * Gestor de Documentos (Blob Storage): Repositorio seguro (como AWS S3 o Azure Blob) vinculado al sistema, donde el proveedor local pueda descargar instantáneamente los planos CAD y las especificaciones técnicas de la pieza asignada mediante URLs firmadas y temporales.

Sprint 7: Panel de Control Ejecutivo (SCM Cockpit) y Pruebas Extremo a Extremo
- Objetivo del Sprint: Centralizar todas las métricas críticas de la planta (Costo de línea parada, TTR, eficiencias) y asegurar la estabilidad del sistema mediante pruebas de integración.

- Entregables Técnicos para el Desarrollador:
    * Dashboard Consolidado: Gráficas en tiempo real en el frontend (usando librerías como Chart.js o Ngx-charts) que muestren las horas de paro evitadas y el estatus actual de las líneas.

    * Estrategia de Testing (QA Automatizado): * Backend: Pruebas unitarias para los algoritmos de suficiencia de la BOM.

    * Frontend / E2E: Pruebas de integración para asegurar que el flujo completo (Falta material -> Alerta WebSocket -> Activación de Proveedor Local) funcione sin fricciones.

    * Despliegue (Deployment): Configuración de los entornos de staging/producción (Dockerización de los servicios para facilitar el despliegue en la infraestructura local o nube de la maquiladora).

Nota para el Líder de Desarrollo: > Este roadmap está diseñado para que cada sprint entregue un componente de software funcional e independiente. Al terminar el Sprint 3, la planta ya tendrá visibilidad total de sus riesgos de inventario, dejando los sprints finales para la automatización de la mitigación y las herramientas de geolocalización.

¿Consideras que esta división por Sprints se adapta bien a la arquitectura actual de desarrollo que manejas, o prefieres profundizar en los requerimientos técnicos de algún módulo en específico?

# Prompt 3 - Modificacion del Sprint 1
```barch
En el Sprint 1: puedes cambiar el objetivo por crear el modelo de datos de forma tradicional el stack de tecnologias que quiero uses es Django en su maxima expresion no quiero hacer un API quiero la forma tradicional del modelo MVT es decir que quiero en el fronend Templates de django con Boostrap 5 como su framework de css. 
```

## Respuesta
Usaremos el ORM nativo de Django, vistas basadas en clases (CBVs) para acelerar el desarrollo, y renderizaremos directamente en el servidor utilizando el motor de Templates de Django combinado con Bootstrap 5 para una interfaz limpia, responsiva y ágil en el piso de la maquiladora.

Aquí tienes la reestructuración detallada del Sprint 1 diseñada específicamente para un ingeniero de software:

# Sprint 1: Modelo de Datos Relacional y Arquitectura MVT para el Núcleo de la BOM.
- Objetivo del Sprint: Diseñar y construir la base de datos relacional mediante el ORM de Django, implementando la estructura de la Lista de Materiales (BOM) y el inventario, junto con las interfaces tradicionales de visualización y administración utilizando Django Templates y Bootstrap 5.

1. Backend: Modelos del ORM de Django (models.py)
El desarrollador debe definir un diseño relacional sólido aprovechando las ventajas del ORM. Se implementarán los siguientes modelos:

* Product (Modelo de Televisor): Representa el producto final (ej. Smart TV 55" 4K). Campos clave: name, sku (único), description, created_at.

* Component (Componentes Individuales): Paneles, tarjetas principales, fuentes de poder, etc. Campos: name, part_number (único), category (Choices: PANEL, MAIN_BOARD, POWER, etc.), safety_stock (Stock mínimo de seguridad).

* BOM (Bill of Materials): Relación muchos a muchos intermedia (through en Django) para definir qué componentes y en qué cantidad exacta se necesitan para armar un modelo de televisión específico.

* Inventory (Inventario Físico): Relación uno a uno con Component. Campos: current_stock, in_transit_stock, location_in_warehouse.

2. Capa de Control: Vistas Basadas en Clases (views.py y urls.py)
Para mantener el código limpio y seguir las mejores prácticas de Django, utilizaremos las Class-Based Views (CBVs) nativas para resolver el CRUD de la BOM:
* ProductListView(ListView): Para listar todos los modelos de televisiones en producción.
* ProductDetailView(DetailView): La vista más importante de este sprint. Debe realizar un prefetch_related o select_related de la relación de la BOM para mitigar el problema de consultas $N+1$ en la base de datos y listar todos los componentes del televisor con sus cantidades.

3. Frontend: Django Templates + Bootstrap 5
Toda la interfaz se procesa en el servidor. El desarrollador creará las siguientes plantillas dentro del directorio templates/:

* base.html: El cascarón global del sistema. Incluirá el CDN o archivos locales de Bootstrap 5.3 (CSS y JS Bundle) y definirá los bloques {% block content %}. Contendrá una barra de navegación (Navbar) responsiva de Bootstrap.

* product_list.html: Una interfaz limpia que utilice las Tarjetas (Cards) o Tablas (Tables) de Bootstrap 5 con clases como table table-striped table-hover para mostrar los televisores disponibles.

* product_detail.html: Mostrará el perfil del televisor seleccionado y una tabla detallada con los componentes de su BOM. Utilizaremos los componentes Badge de Bootstrap 5 para categorizar visualmente los tipos de componentes (ej. paneles en azul, microchips en gris).

4. Admin de Django (admin.py)
Para acelerar las pruebas del negocio sin haber programado pantallas de inserción, se configurará el panel de administración nativo de Django:

* Utilizar InlineModelAdmin (TabularInline) para que al dar de alta o editar un televisor (Product), el usuario pueda agregar sus componentes de la BOM en la misma pantalla de forma tabular.

Entregables Técnicos Clave para el Cierre del Sprint:
1. Archivos de Migración (makemigrations y migrate): Scripts de base de datos ejecutados y validados.

2. Poblamiento Inicial (fixtures o seeders): Un archivo JSON o script de comandos con datos de prueba de al menos 3 modelos de televisión y sus componentes reales.

3. Vistas y Plantillas Funcionales: Navegación fluida entre la lista de televisiones y el desglose de su BOM, estilizada al 100% con Bootstrap 5 y renderizada nativamente por Django.

# Prompt 3 -  Dasarrollo del Sprint 1
```batch
Actúa como un ingeniero de software senior y comienza a desarrollar el primer sprint
```
Para un entorno de producción maquiladora, necesitamos un código robusto y tipado. Vamos a estructurar la aplicación central, configurar los modelos con el ORM, optimizar las consultas para evitar el cuello de botella de $N+1$, y diseñar los templates con Bootstrap 5.

# 🛠️ Paso 1: Configuración del Entorno y Estructura del Proyecto

Lo primero es estructurar el proyecto de forma limpia. Vamos a crear un entorno virtual, instalar Django e inicializar la aplicación de gestión de materiales que llamaremos materials.

```batch
# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar Django (versión LTS estable)
pip install django

# Crear proyecto y aplicación modular
django-admin startproject scm_cems .
python manage.py startapp materials
```
Agrega 'materials' a tu lista de INSTALLED_APPS en el archivo scm_cems/settings.py.

# 📑 Paso 2: El Modelo de Datos Avanzado (materials/models.py)
Como ingenieros senior, sabemos que la base de datos es el corazón del sistema. Usaremos relaciones explícitas, choices estructurados para legibilidad, y un modelo intermedio (through) para la BOM que nos permita guardar metadatos (como la cantidad de componentes por TV).
```python
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
```
Aplica las migraciones en tu terminal:
```batch
python manage.py makemigrations materials
python manage.py migrate
```

# 🎛️ Paso 3: Configuración del Admin con Inlines (materials/admin.py)
Para habilitar la carga de datos ágil en el piso sin requerir formularios complejos aún, implementamos un TabularInline. Esto permite mapear la BOM completa de una televisión desde la misma vista del producto.
```python
from django.contrib import admin
from .models import Product, Component, BillOfMaterials, Inventory

class BillOfMaterialsInline(admin.TabularInline):
    model = BillOfMaterials
    extra = 1  # Permite agregar filas dinámicamente en el admin

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'created_at')
    search_fields = ('sku', 'name')
    inlines = [BillOfMaterialsInline]

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ('part_number', 'name', 'category', 'safety_stock')
    list_filter = ('category',)
    search_fields = ('part_number', 'name')

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('get_part_number', 'current_stock', 'in_transit_stock', 'warehouse_location')
    
    def get_part_number(self, obj):
        return obj.component.part_number
    get_part_number.short_description = 'Número de Parte'
```
# 🧠 Paso 4: Capa de Control Optimizada (materials/views.py)
Aquí aplicamos seniority: al renderizar la relación Many-To-Many en los templates tradicionales de Django, corremos el riesgo latente de ejecutar una consulta SQL por cada iteración. Para solucionarlo, usamos prefetch_related con un objeto Prefetch personalizado para precargar los componentes y sus inventarios relacionados en un único query optimizado.

```python
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
```
Enruta las vistas creando el archivo materials/urls.py y vinculándolo al urls.py principal del proyecto:
```python
from django.urls import path
from .views import ProductListView, ProductDetailView

app_name = 'materials'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
```
# 🎨 Paso 5: Capa de Presentación con Django Templates y Bootstrap 5
Creamos una jerarquía limpia de templates dentro de materials/templates/materials/.

base.html (Estructura Global y Navbar)
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}SCM Cockpit{% endblock %}</title>
    <!-- Bootstrap 5.3 CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">

    <!-- Navbar Maquiladora Estilo Industrial -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark shadow-sm">
        <div class="container-fluid">
            <a class="navbar-brand fw-bold text-warning" href="{% url 'materials:product_list' %}">
                ⚙️ SCM-CEMS <span class="fs-6 fw-normal text-white">| TV Manufacturing</span>
            </a>
            <div class="navbar-nav ms-auto">
                <span class="nav-link text-light disabled">Planta de Ensamble Activa</span>
            </div>
        </div>
    </nav>

    <div class="container my-4">
        {% block content %}
        {% endblock %}
    </div>

    <!-- Bootstrap JS Bundle -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```
product_list.html (Listado de Modelos de Televisores)

```html
{% extends 'materials/base.html' %}

{% block title %}Modelos de Producción - SCM{% endblock %}

{% block content %}
<div class="row mb-4 align-items-center">
    <div class="col">
        <h1 class="h3 text-secondary m-0">Modelos de Televisores en Producción</h1>
        <p class="text-muted small m-0">Seleccione un modelo para auditar su Lista de Materiales (BOM) crítica.</p>
    </div>
</div>

<div class="row row-cols-1 row-cols-md-3 g-4">
    {% for product in products %}
    <div class="col">
        <div class="card h-100 shadow-sm border-0 border-top border-dark border-3">
            <div class="card-body d-flex flex-column">
                <div class="d-flex justify-content-between align-items-start mb-2">
                    <span class="badge bg-secondary font-monospace">{{ product.sku }}</span>
                    <small class="text-muted">{{ product.created_at|date:"d/M/Y" }}</small>
                </div>
                <h5 class="card-title fw-bold text-dark">{{ product.name }}</h5>
                <p class="card-text text-muted flex-grow-1 small">
                    {% if product.description %}{{ product.description }}{% else %}Sin descripción técnica registrada.{% endif %}
                </p>
                <div class="mt-3">
                    <a href="{% url 'materials:product_detail' product.pk %}" class="btn btn-outline-dark btn-sm w-100">
                        Ver Estructura de BOM →
                    </a>
                </div>
            </div>
        </div>
    </div>
    {% empty %}
    <div class="col-12 text-center py-5">
        <div class="alert alert-info shadow-sm">No hay modelos de televisión dados de alta en el sistema de producción.</div>
    </div>
    {% endfor %}
</div>
{% endblock %}
```
product_detail.html (Desglose de la BOM con Alertas de Stock)
```html
{% extends 'materials/base.html' %}

{% block title %}{{ product.sku }} - Detalle de BOM{% endblock %}

{% block content %}
<nav aria-label="breadcrumb" class="mb-4">
    <ol class="breadcrumb">
        <li class="breadcrumb-item"><a href="{% url 'materials:product_list' %}" class="text-dark">Inicio</a></li>
        <li class="breadcrumb-item active" aria-current="page">{{ product.sku }}</li>
    </ol>
</nav>

<div class="card shadow-sm border-0 p-4 mb-4 bg-white">
    <div class="row">
        <div class="col-md-8">
            <span class="text-uppercase text-muted font-monospace small">Especificación de Producto</span>
            <h2 class="fw-bold text-dark mb-2">{{ product.name }}</h2>
            <p class="text-muted">{{ product.description }}</p>
        </div>
        <div class="col-md-4 text-md-end border-start-md">
            <div class="p-2 bg-light rounded text-center">
                <span class="d-block text-muted small text-uppercase">Identificador Master</span>
                <span class="fs-4 fw-bold font-monospace text-dark">{{ product.sku }}</span>
            </div>
        </div>
    </div>
</div>

<h3 class="h4 text-secondary mb-3">Estructura de la Lista de Materiales (BOM)</h3>
<div class="card shadow-sm border-0 overflow-hidden">
    <div class="table-responsive">
        <table class="table table-hover align-middle mb-0">
            <thead class="table-dark">
                <tr>
                    <th>Categoría</th>
                    <th>No. Parte</th>
                    <th>Nombre de Componente</th>
                    <th class="text-center">Cant. Requerida</th>
                    <th class="text-center">Stock Físico</th>
                    <th class="text-center">Mínimo de Seguridad</th>
                    <th>Estado de Disponibilidad</th>
                </tr>
            </thead>
            <tbody>
                {% for item in product.bom_relations.all %}
                <tr {% if item.component.inventory.is_under_safety_stock %}class="table-danger-light" style="background-color: #fff0f1;"{% endif %}>
                    <td>
                        <span class="badge bg-secondary w-100">{{ item.component.get_category_display }}</span>
                    </td>
                    <td class="font-monospace fw-bold text-dark">{{ item.component.part_number }}</td>
                    <td>{{ item.component.name }}</td>
                    <td class="text-center fw-bold">{{ item.quantity }} pcs</td>
                    <td class="text-center">{{ item.component.inventory.current_stock }}</td>
                    <td class="text-center text-muted">{{ item.component.safety_stock }}</td>
                    <td>
                        {% if item.component.inventory.is_under_safety_stock %}
                            <span class="badge bg-danger text-white p-2 d-block text-center">
                                ⚠️ RIESGO PARO DE LÍNEA
                            </span>
                        {% else %}
                            <span class="badge bg-success text-white p-2 d-block text-center">
                                ✓ Abasto Conforme
                            </span>
                        {% endif %}
                    </td>
                </tr>
                {% empty %}
                <tr>
                    <td colspan="7" class="text-center py-4 text-muted">Este producto no cuenta con componentes asignados en su BOM.</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</div>

<div class="mt-4">
    <a href="{% url 'materials:product_list' %}" class="btn btn-secondary">← Volver al Panel Base</a>
</div>
{% endblock %}
```
# 🚀 Conclusión del Sprint 1

El código está listo para ser desplegado localmente. Hemos implementado:
1. Un modelo relacional con integridad referencial robusta (unique_together, validators).

2. Una vista de Django optimizada a nivel de base de datos (prefetch_related) para asegurar tiempos de respuesta mínimos en consultas pesadas.

3. El frontend acoplado usando Django Templates dinámicos estilizados de forma limpia y profesional con Bootstrap 5.

El esqueleto técnico de nuestro SCM Cockpit está firme. Quedo a la espera de tus comentarios para pasar formalmente al Sprint 2, donde implementaremos los disparadores automáticos del punto de reorden y el control de inventario en tránsito.