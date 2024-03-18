from django.core.cache import cache

from config import settings
from main_app.models import Category


def get_cached_categories_for_product(product_id: int):
    if settings.CACHE_ENABLED:
        key = f'categories_list_{product_id}'
        categories_list = cache.get(key)
        if categories_list is None:
            categories_list = Category.objects.filter(product_id=product_id)
            cache.set(key, categories_list)
    else:
        categories_list = Category.objects.filter(product_id=product_id)
    return categories_list
