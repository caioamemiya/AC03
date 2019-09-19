from django.contrib import admin
from .models import Produto, Orcamento, ItemOrcamento

# Register your models here.

admin.site.register(Produto)
admin.site.register(Orcamento)
admin.site.register(ItemOrcamento)