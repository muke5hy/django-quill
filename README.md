# django-quilljs

[![Build Status](https://img.shields.io/travis/muke5hy/django-quilljs/master.svg?style=flat)](https://travis-ci.org/muke5hy/django-quilljs)
[![Latest Version](https://img.shields.io/pypi/v/django-quilljs.svg?style=flat)](https://pypi.python.org/pypi/django-quilljs/)

Easily use [Quill.js](http://quilljs.com/) in your django admin.

This project forked from [django-quill](https://github.com/coremke/django-quill).

Requires django 2.1.5

![Admin Preview](/.screenshots/admin.png?raw=true)

## Quick start

1. Install the package from pypi

    ```bash
    pip install django-quilljs
    ```

2. Add "quilljs" to your INSTALLED_APPS setting like this:

    ```python
    INSTALLED_APPS = (
        ...
        'quilljs',
    )
    ```

## Usage

```python
from django.db import models
from quilljs.fields import RichTextField


class MyModel(models.Model):
    content = RichTextField()
    content2 = RichTextField(config='basic')
```


If you want to support image uploads, your admin needs to extend from `quilljs.admin.QuillAdmin`:

```python
from quilljs.admin import QuillAdmin

class MyAdmin(QuilljsAdmin):
    pass
```

If you don't want to touch your models and enable the editor for all text fields in the admin page,
 you can do as well:

```python
from quilljs.widgets import QuillEditorWidget
from quilljs.admin import QuillAdmin


class MyAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': QuillEditorWidget},
    }
```

### Customizing

To customize this app, extend ``apps.QuilljsConfig`` and modify whatever you need. For example, to add a new toolbar:

```python
from quill.apps import QuilljsConfig


class MyQuilljsConfig(QuilljsConfig):
    my_toolbar = dict(full, toolbar_template='quill/toolbars/my_toolbar.html')
```

To customize the extensions of the images that can be uploaded:

```python
from quill.apps import QuilljsConfig


class MyQuilljsConfig(QuilljsConfig):
    allowed_image_extensions = ['jpeg', 'gif']
```

If you need to call other methods or perform additional actions on the quill editors, they will be available in ``window.DjangoQuillEditors``.

### Provided Toolbars

There are two toolbars that come with this package:

1. Full (default): Provides basic font style and size selection, bold, italics, underline, strikethrough, text color, background color, lists, links, and images.
2. Basic: Provides bold, italic, underline, lists, and links.

## Development

There are several dependencies on npm that are required before building django-quilljs:

```bash
$ npm install
```

### Auto Compile JS

```bash
$ make watch
```

### Running Tests

```bash
$ make test
```

### Building JS

```bash
$ make build
```


# TODO

1. Better documentation.
2. More tests.
3. Better support for using outside of the admin.
