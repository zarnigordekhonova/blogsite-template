from django.db import models
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    ico_code = models.CharField(_('ICO code'), max_length=3, unique=True)
    name = models.CharField(_('Name'), max_length=128)
    icon = models.ImageField(_('Image'), upload_to='countries', null=True, blank=True)

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
