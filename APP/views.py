from django.shortcuts import render,HttpResponse,redirect
from APP import models
from django.views import View
#############################################测试实例###################################################
class person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def dream(self):
        dream = '想要带你去浪漫的西二旗，然后一起去上地做笔试题，其实我特别喜欢去望京西'
        return dream

    def __str__(self):
        return self.name

def test(request):
    namelist = [['kevin','mike','Jenny','Lucks'],['lucy','liliy','vivan','mars','harry']]
    p1 = person('Kevin',34)
    p2 = person('Jenny',28)
    return render(request,'test.html',{'person1':p1,'person2':p2,'namelist':namelist})

#############################################用户登录简单实例###################################################
def userlogin(request):
    if request.method =='POST':
        error_msg = ''
        if request.POST['uname'] == 'kevin' and request.POST['upass'] == '88888888':
            username = request.POST['uname']
            upassword = request.POST['upass']
            print(request.POST)
            print(username, upassword)
            return redirect('http://google.com/')
        else:
            username = request.POST['uname']
            upassword = request.POST['upass']
            print(request.POST)
            print(username, upassword)
            error_msg = '用户名或者密码错误'
            return render(request,'login.html',{'error':error_msg})
    else:
        return render(request,'login.html')
#############################################主外键，多对多数据库操作实例################################################
def userlist(request):
    res = models.userinfo.objects.all()
    print(res)
    return render(request,'userlist.html',{'userlist':res})

#------------FBV=Function Base View--------------
def adduser(request):
    if request.method == 'POST':
        print(request.POST)
        models.userinfo.objects.create(uname=request.POST['username'],upassword=request.POST['userpass'])
        return redirect('/userlist/')
    return render(request,'adduser.html')
#------------CBV=Class Base View--------------
#CBV模式下调用类实现，里面的get,post方法名是固定写法，且需要导入整个文件，from APP import views
class CFVAdduser(View):
    def get(self,request):
        return render(request, 'adduser.html')

    def post(self,request):
        models.userinfo.objects.create(uname=request.POST['username'], upassword=request.POST['userpass'])
        return redirect('/userlist/')


def delectuser(request):
    if request.GET:
        print(request.GET)
        models.userinfo.objects.filter(uid=request.GET['uid']).delete()
        return redirect('/userlist/')
    return HttpResponse('The message did not find')

def edituser(request):
    if request.GET:
        print(request.GET)
        resnameobject = models.userinfo.objects.get(uid=request.GET['uid'])
        return render(request,'edituser.html',{'rename_object':resnameobject})
    if request.method == 'POST':
        print(request.POST)
        edituserobjet = models.userinfo.objects.get(uid = request.POST['usid'])
        edituserobjet.uname = request.POST['username']
        edituserobjet.upassword = request.POST['userpass']
        edituserobjet.save()
        return redirect('/userlist/')
    return render(request,'edituser.html')



def addtags(request):
    res = models.userinfo.objects.all()
    if request.method == 'POST':
        print(request.POST)
        models.usertags.objects.create(tag_name = request.POST['tagename'],userinfo_id = request.POST['username'])
        return redirect('/taglist/')
    return render(request,'addtags.html',{'userinfo':res})



def taglist(request):
    tagslist = models.usertags.objects.all()
    userlist = models.userinfo.objects.all()
    return render(request,'taglist.html',{'taglist':tagslist,'userlist':userlist})

def deltag(request):
    print(request.GET['did'])
    models.usertags.objects.filter(tag_id=request.GET['did']).delete()
    return redirect('/taglist/')

def edittag(request):
    if request.GET:
        edit_tag = models.usertags.objects.get(tag_id=request.GET['eid'])
        username = models.userinfo.objects.all()
        return render(request, 'edittag.html', {'edit_tag': edit_tag, 'username': username})
    if request.method == 'POST':
        tag_edit = models.usertags.objects.get(tag_id=request.POST['tid'])
        print(tag_edit)
        tag_edit.tag_name = request.POST['tagname']
        tag_edit.userinfo_id = request.POST['userid']
        tag_edit.save()
        return redirect('/taglist/')

def petlist(request):
    showpetlist = models.Pet.objects.all()
    #print(showpetlist[0],models.Pet.objects.get(pet_id=1).uname.all())
    return render(request,'petlist.html',{'petlist':showpetlist})

def deletepet(request):
    models.Pet.objects.get(pet_id=request.GET['pid']).delete()
    return redirect('/petlist/')

def addpet(request):
    if request.method == 'POST':
        new_pet = request.POST.get('addpetname')
        owner = request.POST.getlist('allowers')
        print(owner)
        newpet_object = models.Pet.objects.create(pet_name=new_pet)
        newpet_object.uname.set(owner)
        return redirect('/petlist/')
    return render(request,'addpet.html',{'owner':models.userinfo.objects.all()})

def editpet(request):
    if request.method == 'POST':
        # edit_pet_object = models.Pet.objects.get(pet_id=request.POST.get('editpetid'))
        edit_pet_object = models.Pet.objects.get(pet_id=request.POST['editpetid'])
        edit_pet_object.pet_name = request.POST['editpetname']
        edit_pet_object.uname.set(request.POST.getlist('allowers'))
        edit_pet_object.save()
        return  redirect('/petlist/')
    ownerlist = models.userinfo.objects.all()
    peteditlist = models.Pet.objects.get(pet_id=request.GET['editid'])
    return render(request,'editpet.html',{'owner':ownerlist,'editpet':peteditlist})