import os
from apps.blog.models import Post
from django.dispatch import receiver
from django.db.models.signals import post_delete, pre_delete


@receiver(post_delete, sender=Post)
def image_post_delete(sender, instance, **kwargs):
    print(f"Post {instance.title} has been deleted!")

    if os.path.exists(instance.image.path):
        os.remove(instance.image.path)
        print(f"Post image {instance.image.path} has been removed successfully.")


@receiver(pre_delete, sender=Post)
def image_pre_delete(sender, instance, **kwargs):
    print(f"Preparing to delete post {instance.title} | {instance.author}.")


