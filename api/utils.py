from django.db.models import F, Avg

from api.models import Shop, Review


def get_shop(self, domain):
    shop, _ = Shop.objects.get_or_create(domain=domain)
    if self.action == 'create':
        shop.reviews = F('reviews') + 1
    if self.action == 'destroy':
        shop.reviews = F('reviews') - 1
        self.perform_destroy(self.get_object())
    shop.avg_rate = Review.objects.filter(shop_link__contains=shop.domain).aggregate(Avg('rating'))['rating__avg']
    shop.save()