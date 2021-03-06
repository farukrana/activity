#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
import json data from API
IMPORTANT!! you must turn off pagination for this to work from a URL
and get all country records
Install module django-extensions
Runs twice via function calls at bottom once
"""
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.db import connection

cursor = connection.cursor()


def run():
    print("Setting Tokens")


for user in User.objects.all():
    Token.objects.get_or_create(user=user)
