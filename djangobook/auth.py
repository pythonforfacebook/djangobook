from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


class FacebookBackend(ModelBackend):
    def authenticate(self, facebook_id=None):
        """ We rely on the middleware to call authenticate() with a valid facebook_id. """
        print facebook_id
        if facebook_id:
            user, created = User.objects.get_or_create(username=facebook_id)
            return user
        return None
