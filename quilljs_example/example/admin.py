from django.contrib import admin
from quilljs.admin import QuillAdmin

from .models import ExampleModel

admin.site.register(ExampleModel, QuillAdmin)
