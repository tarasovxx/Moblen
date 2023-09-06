import hashlib
import uuid
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from .models import Tutor
