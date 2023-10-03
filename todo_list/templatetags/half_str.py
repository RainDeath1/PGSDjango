from django import template

register = template.Library()


@register.filter
def half_str(value):
    return value[:len(value) // 2]


@register.tag(name='split_string')
def split_string(parser, token):
    try:
        tag_name, value, separator, _, variable_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("Тег %r требует два аргумента (строку и разделитель) и переменную для "
                                           "хранения результата"
                                           % token.contents.split()[0])
    return SplitStringNode(value, separator, variable_name)


class SplitStringNode(template.Node):
    def __init__(self, value, separator, variable_name):
        self.value = template.Variable(value)
        self.separator = template.Variable(separator)
        self.variable_name = variable_name

    def render(self, context):
        value = self.value.resolve(context)
        separator = self.separator.resolve(context)
        context[self.variable_name] = value.split(separator)
        return ''


