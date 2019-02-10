import json

from django import template
from django.apps import apps


register = template.Library()
quilljs_app = apps.get_app_config('quilljs')


@register.filter()
def quilljs_conf(name):
    """Get a value from the configuration app."""
    return getattr(quilljs_app, name)
quilljs_conf.is_safe = True


@register.filter()
def quilljs_conf_json(name):
    """Get a value from the configuration app as JSON."""
    return json.dumps(getattr(quilljs_app, name))
quilljs_conf_json.is_safe = True


@register.simple_tag(takes_context=True)
def render_toolbar(context, config):
    """Render the toolbar for the given config."""
    quilljs_config = getattr(quilljs_app, config)
    t = template.loader.get_template(quilljs_config['toolbar_template'])
    return t.render(context.flatten())


@register.simple_tag(takes_context=True)
def render_editor(context, config):
    """Render the editor for the given config."""
    quilljs_config = getattr(quilljs_app, config)
    t = template.loader.get_template(quilljs_config['editor_template'])
    return t.render(context.flatten())
