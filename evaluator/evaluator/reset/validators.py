from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

def email_exist(email):
    try:
        user = User.objects.get(email=email)
    except:
        raise ValidationError("User with this email does not exist")
    return email