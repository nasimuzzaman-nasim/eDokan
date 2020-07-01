from django.db import models
from jsonfield import JSONField
from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.contrib.auth.models import User


def get_uplaod_file_name(product, filename):
    return u'product/%s/%s' % (product.title, filename)


class Product(models.Model):
    # added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)

    image = models.ImageField(upload_to=get_uplaod_file_name, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    brand = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=55, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    other_feature = JSONField(null=True, blank=True)
    in_stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    discounted_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    approved = models.BooleanField(default=False)


    slug = models.SlugField(allow_unicode=True, null=True, blank=True, max_length=2055, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_updated']


@receiver(post_save, sender=Product)
def generate_slug(instance, sender, **kwargs):
    if not instance.slug:
        instance.slug = slugify(str(instance.id) + '_' + instance.title)
        instance.save()

