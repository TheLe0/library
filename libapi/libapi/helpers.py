from django.contrib.auth.models import User

def create_super_user():
    superuser = User()
    superuser.is_active = True
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.username = 'admin'
    superuser.email = 'admin@admin.com.br'
    superuser.set_password('admin')
    superuser.save()
