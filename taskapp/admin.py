from django.contrib import admin
from .models import Author,Book,Borrow_Record

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Borrow_Record)
