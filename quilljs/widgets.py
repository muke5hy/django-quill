from django import forms
from django.apps import apps
from django.forms.utils import flatatt
from django.template.loader import render_to_string
from django.templatetags.static import static
from django.utils.safestring import mark_safe


class QuillEditorWidget(forms.Textarea):

    """Widget used to render a QuillJS WYSIWYG."""

    class Media:
        css = {
            'all': (
                static('quilljs/css/quilljs.snow.min.css'),
                static('quilljs/css/quilljs.core.css'),
                static('quilljs/css/quilljs.css'),
            )
        }

        js = (
            static('quilljs/js/vendor/SimpleAjaxUploader-1a6f62289d.min.js'),
            static('quilljs/js/build/quilljs-django.min.js'),
        )

    def __init__(self, config='default', *args, **kwargs):
        """Create a new Quill WYSIWYG Widget.

        :param str config: The QuillJS config to use (from :py:class:`quilljs.apps.QuilljsConfig`)

        """
        self.config = config
        super(QuillEditorWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None, renderer=None):
        """Render the Quill WYSIWYG."""
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, {'name': name})
        quilljs_app = apps.get_app_config('quilljs')
        quilljs_config = getattr(quilljs_app, self.config)

        return mark_safe(render_to_string(quilljs_config['template'], {
            'final_attrs': flatatt(final_attrs),
            'value': value,
            'id': final_attrs['id'],
            'config': self.config,
        }))
