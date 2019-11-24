from django import template   #自定义Tag和自定义Filter一样，只是Filter 只能传一个参数，Filter可以传无数参数
register = template.Library()

@register.simple_tag(name="tagone")
def sum(arg1,arg2,arg3):
    return "{}{}{}".format(arg1,arg2,arg3)
