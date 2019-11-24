'''
自定义Filter
第一，在APP目录下，新建一个Python包，包名固定为   =   templatetags
第二，在templatetags下面新建一个Python文件，可自定义命名
第三，新建的Python文件中导入 所需要的包  语法 = from django import template
第四，实例化一个Filter的类 register = template.Library()
第五，编辑方法函数，并且用装饰器导入到之前定义的Filter类，且为自定义Filter命名：
'''
#第三步
from django import template
#第四步
register = template.Library()
#第五步
@register.filter(name="secondfilter")
def func(arg):
    return "{} {}.".format(arg,"就是愣")




