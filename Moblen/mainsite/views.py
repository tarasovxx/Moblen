import hashlib
import uuid
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from .models import Tutor


# Create your views here.

@csrf_protect
def registry(request):
    if request.method == 'POST':
        username = request.POST['username']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']

        # Генерируем случайную соль
        salt = str(uuid.uuid4())

        # Создаем хеш пароля с использованием соли
        password_with_salt = (password + salt).encode('utf-8')
        password_hash = hashlib.sha256(password_with_salt).hexdigest()

        # Создаем нового преподавателя в базе данных
        tutor = Tutor.objects.create(
            tutor_name=username,
            phone_number=phone,
            email=email,
            password_hash=password_hash,
            salt=salt
        )

        # Дополнительная обработка, например, редирект на другую страницу
        return redirect('registration_success')

    return render(request, "mainsite/registry.html")


def registration_success(request):
    return render(request, "mainsite/registry_success.html")
