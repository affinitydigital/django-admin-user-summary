from django.contrib.auth import get_user_model

django_user_model = get_user_model()


class UserSummary(django_user_model):
    class Meta:
        proxy = True
        verbose_name = 'User Summary'
        verbose_name_plural = 'Users Summary'
