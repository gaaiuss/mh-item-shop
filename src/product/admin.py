from typing import TYPE_CHECKING

from django.contrib import admin

from product.models import Product, Variation

if TYPE_CHECKING:
    VariationInLineModelAdmin = admin.TabularInline[Variation]
    ProductModelAdmin = admin.ModelAdmin[Product]
    VariationModelAdmin = admin.ModelAdmin[Variation]
else:
    VariationInLineModelAdmin = admin.TabularInline
    ProductModelAdmin = admin.ModelAdmin
    VariationModelAdmin = admin.ModelAdmin


class VariationInLine(VariationInLineModelAdmin):
    model = Variation
    extra = 1


@admin.register(Product)
class ProductAdmin(ProductModelAdmin):
    def __init__(self, model: type[Product], admin_site: admin.AdminSite) -> None:
        super().__init__(model, admin_site)
        self.inlines = [VariationInLine]
        self.list_display = [
            "name",
            "short_description",
            "get_fomatted_market_price",
            "get_fomatted_promo_market_price",
        ]


@admin.register(Variation)
class VariationAdmin(VariationModelAdmin): ...
