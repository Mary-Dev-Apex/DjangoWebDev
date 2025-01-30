from django.contrib import admin

# Register your models here.


from .models import Topic, Entry
admin.site.register(Topic)
admin.site.register(Entry)

# Topic here is just a Class name we created int he models.py
# The dot in front of models tells Django to look for models.py in the same directory as admin.py.