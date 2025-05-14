from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

CustomUser = get_user_model()


class Category(models.Model):
    title = models.CharField('Title', max_length=256)
    slug = models.SlugField('Slug', unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def save(
            self,
            *args,
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None,
    ):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(
            *args,
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )


class Post(models.Model):
    title = models.CharField("Title", max_length=256)
    slug = models.SlugField("Slug", unique=True)
    content = models.TextField('Content')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Category")
    image = models.ImageField("Image", upload_to="images/", )
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

    def save(
            self,
            *args,
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None,
    ):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(
            *args,
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )


