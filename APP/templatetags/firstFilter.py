from django import template
register = template.Library() #Library首字母一定是大写的

@register.filter(name = "firstfilter") # 定义filter名字的时候一定要是双引号""
def addname(arg,arg2): #第一个参数永远是管道符|前面的内容，第二个参数才是冒号：后面的参数
    return "{} {}.".format(arg,arg2) #主要标点的中英文，和漏掉符号点   .