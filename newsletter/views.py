from django.contrib.auth.models import User, Group, Permission
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404, redirect
from .models import Newsletter
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate, login, logout
from trending.models import Trending
from django.contrib.contenttypes.models import ContentType

# Create your views here.
