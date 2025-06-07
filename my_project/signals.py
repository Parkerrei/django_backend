from django.db.models.signals import post_delete , post_save
from django.dispatch import receiver
from .models import Book, Author
from django.contrib.auth.models import User


@receiver(post_delete, sender=Book)
def delete_book_file(sender, instance, **kwargs):
    if instance.content:
        print(f'deleting file {instance.content.name} from {instance.content.name}')
        instance.content.delete(False)


@receiver(post_save, sender=Book)
def save_book_file(sender, instance, **kwargs):
    if instance.content:
        print(f'saving file {instance.content.name} to {instance.content.name}')

        
@receiver(post_save, sender=Author)
def save_author(sender, instance, **kwargs):
    if instance.name:
        print(f'author {instance.name} has been saved  ')
    else:
        print(f'author {instance.name} is not created yet')


@receiver(post_save, sender=User)
def save_user(sender, instance, **kwargs):
    if instance.username:
        print(f' user {instance.username} has been saved')
    else:
        print(f' user {instance.username} is not created yet')


@receiver(post_save, sender=User)
def send_email(sender, instance, created, **kwargs):
    if created:
        print(f' email sent to {instance.email} for user {instance.username}')

 