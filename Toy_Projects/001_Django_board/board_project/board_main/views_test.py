from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from .models import test
# Create your views here.

#get 요청시 html파일 그대로 return
def test_html(request):
    return render(request,'test/test.html')

#get 요청시 html+data return 일단 하드코딩으로 배우고~
def test_html_multidata(request):
    JS_data={
        'name' : "LEE",
        'age' :  28
    }
    #render : 웹개발에서 화면을 return 해줄때 사용하는 용어
    # return render(request,'test/test.html',JS_data)
    return render(request, 'test/test.html', {'data':JS_data})

# #get 요청시 data만  return 
def test_html_JSdata(request):
    JS_data={
        'name' : "LEE",
        'age' :  28
    }
    return JsonResponse(JS_data) 

#get 요청시 html+data return(단일)
def test_html_data(request):
    name='Lee'
    #render : 웹개발에서 화면을 return 해줄때 사용하는 용어
    return render(request,'test/test.html',{'name':name})

#사용자가 get요청으로 quary parameter 방식으로 데이터 넣을떄
#방식1 : 쿼리 파라미터 방식(quary parameter) localhost:8000/author?id=10&name=Lee
#방식2 : path variable방식(rest api 규격 방식) localhost:8000/author/10
def test_html_userget(request):
    name=request.GET.get('name')
    age=request.GET.get('age')
    email=request.GET.get('email')
    password=request.GET.get('password')
    data={'name':name,"age":age,'email':email,'password':password}
    print(name,email,password)
    return render(request,'test/test.html',{"data":data})

#pathvalue 방식
def test_html_pathvalue(request,my_id):
    print(my_id)
    return render(request,'test/test.html',{"data":data})

#post방식(form 태그를 활용한)
#먼저 화면을 rendering 하는 method이 필요함
# def test_post_form(request):
#     return render(request,'test/test_post_form.html')

def test_post_new(request):
    if request.method=="POST":
        # data={"name":request.POST.get('my_name',False),
        # 'email':request.POST.get('my_email',False),
        # 'password':request.POST.get('my_password',False)}
        
        data2={"name":request.POST['my_name'],
        'email':request.POST['my_email'],
        'password':request.POST['my_password']}
        #DB에 insert -> save함수 사용
        #DB의 테이블과 sync가 맞는 test객체를 만들어 save
        t1=test()
        t1.name=data2['name']
        t1.email=data2['email']
        t1.password=data2['password']
        t1.save()
        print(data2)
        # return HttpResponse("성공!!")
        return redirect("/")
    else:
        return render(request,'test/test_post_form.html')

    '''
    post 요청의 경우에는 보안상 서버에 치명적인 영향을 미칠 수 있다.
    csrf토큰이라는 것을 django에서 사용한다.
    '''

def test_select_one(request, my_id):
    #단건만 조회할땐 get()함수
    t1=test.objects.get(id=my_id)
    print(t1.name,t1.email,t1.password)
    return render(request,'test/test_select_one.html',{"data":t1})


def test_select_all(request):
    #모든 data조회시 select *from xxxx : all()함수 사용
    tests=test.objects.all()
    # for x in tests:
    #     print(x.id,x.name,x.email,x.password)
    return render(request,'test/test_select_all.html',{'datas':tests})

# #where 조건으로 다건을 조회할때 filter()함수를 사용
# def test_select_filter(request,my_name):
#     ftests=test.objects.filter(name=my_name)
#     return render(request,'test/test_select_filter.html',{'datas':ftests})

#get방식
def test_select_filter(request):
    my_name=request.GET.get('name')
    ftests=test.objects.filter(name=my_name)
    return render(request,'test/test_select_filter.html',{'datas':ftests})

#update를 하기 위해서는 해당건을 사전에 조회하기 위한 id값이 필요
#method는 등록과 동일하게 save()함수
def test_update(request):
    if request.method=="POST":
        data2={"name":request.POST['my_name'],
        'email':request.POST['my_email'],
        'password':request.POST['my_password'],
        'id':int(request.POST['my_id'])}
        # print(type(data2['id']))
        t1=test.objects.get(id=data2['id'])
        t1.name=data2['name']
        t1.email=data2['email']
        t1.password=data2['password']
        t1.save()
        # print(data2)
        return redirect("/")
    else:
        return render(request,'test/test_update.html')
    
#삭제는 delete()사용. update와 마찬가지로 기존객체 탐색 후 delete


 