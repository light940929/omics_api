from django.db.models.signals import post_save
from oauth2_provider.models import Application

def create_auth_client(sender, instance=None, created=False, **kwargs):
    """
    Intended to be used as a receiver function for a `post_save` signal on a custom User model
    Creates client_id and client_secret for authenicated users
    """
    if created:
        Application.objects.create(user=instance, client_type=Application.CLIENT_CONFIDENTIAL,
                                   authorization_grant_type=Application.GRANT_PASSWORD)

post_save.connect(create_auth_client, sender=User)
