from django.shortcuts import render
from .models import Categories, Services,ServiceProviders,Comment
from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from .forms import UserRegistrationForm,ServiceProviderForm,AddServiceForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import User
# from django.contrib.sessions.models import Session
# Create your views here.
def Home(request):
    Data=Services.objects.all()[:3]
    return render(request,'community/home.html',{'list':Data})
    # return render(request,'community/home.html')

def AboutUs(request):
    return render(request,'community/about.html')

def Service_list(request):
    Data=Services.objects.all()
    return render(request,'community/services_list.html',{'list':Data})
  


def Service_Category(request,id):
      Data=Categories.objects.filter(Service_id=id)
      return render(request,'community/Category.html',{'data':Data})
    
@login_required
def Service_provider(request,id):
     provider=ServiceProviders.objects.filter(Category_id=id)
     return render(request,'community/service_provider.html',{'info':provider})


def ServiceDetail(request,pk):
        post_data=get_object_or_404(ServiceProviders,pk=pk) 
    # if request.method=="POST":
    #     form=CommentForm(request.POST)
    #     form.save()
    #     return  HttpResponse('going well')
    # Form_data=CommentForm()
        return render(request,'community/service_detail.html',{'data':post_data})

   

@login_required
def postComment(request,pk):
    if request.method == 'POST':
            data=ServiceProviders.objects.get(pk=pk)
            # print(f'Data is {data}')
            # username = request.user.username
            # print(f'User name is {username}')
            if request.POST.get('comment'):
                comment=Comment()
                comment.comment= request.POST.get('comment')
                comment.User=request.user.id
                Service_provider.username=data
                comment.save()
                return redirect('ServiceDetail',pk=pk)  
            else:
                return render(request,'community/service_detail.html',data)
    return render(request,'community/service_detail.html')


# def comment(request):

#     Data=Comment.objects.all()
#     return render(request,'community/comment.html',{'list':Data})

# showed code
# def add_comment(request,pk):
#     data=ServiceProviders.objects.get(id=pk)
#     username = User.objects.get(username=request.user.username)
#     # print(username)
#     form = CommentForm(request.POST)
#     if form.is_valid():
#         cmt = form.save(commit=False)
#         cmt.User = username
#         cmt.Service_provider = data
#         cmt.save()
#         return redirect('ServiceDetail',pk=pk)
#     else:
#         form = CommentForm()
#     return render(request,'community/add_comment.html',{'form':form})




    # form=CommentForm(instance=data)
    # if request.method=="POST":
    #     form=CommentForm(request.POST,instance=data)
    #     if form.is_valid():
    #         username=request.user.username
    #         # print(f'UserName is {username}')
    #         my_Comment=form.cleaned_data['Comment']
    #         # print(f'Comment {Comment}')
    #         comment_data = form.save(commit=False)
    #         comment_data.User = username
    #         print(comment_data.save())
    #         # c=Comment(User=username,Comment=my_Comment)
    #         # c.save()
    #         return redirect('ServiceDetail',pk=pk)
    #     else:
    #         print('invalid form')
    # else:
    #     form=CommentForm   
    # context={
    #     'form':form
    # }

    # return render(request,'community/add_comment.html',context)



#def Comment(request,pk):
#     if request.method=="POST":
#         Comment=request.POST.get("Comment")
#         User=request.user
#         id=request.POST.get("id")
#         Service_provider=ServiceProviders.objects.get(sno=id)
#         Comments=Comment(Comment=Comment,User=User,Service_provider=Service_provider)
#         Comments.save()
#         messages.success(request,"Your comment has been posted successfully ")
#     # return redirect(f"/community/{ServiceProviders.pk}")
#     return redirect("/")






  



# def Queries_answer(request):
#       Data=QueryAnswer.objects.all()
#       return render(request,'community/query_ans.html',{'list':Data})   



def NewServiceProvider(request):
    if request.method=='POST':
        form_data=ServiceProviderForm(request.POST) #capturing the form data
        if form_data.is_valid():
            post_data=form_data.save()
            return redirect('ServiceList') #redirect to our post_list url
    else:
        form_data=ServiceProviderForm()
    return render(request,'community/service_new.html',{'form_data':form_data})    
  
    

   





def register_user(request):
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account Created Successfully for {username}')
            return redirect('ServiceList')
    else:
        form=UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})
 

def ContactUs(request):
   return render(request,'community/Contact.html')

def SignIn(request):
    return render(request,'community/SignIn.html')


def AddNewService(request):
    if request.method=='POST':
        ServiceForm=AddServiceForm(request.POST)
        if ServiceForm.is_valid():
            Service=ServiceForm.object.get('service ')
            service=ServiceProviders.object.get('Service')
            # if Service==service:
            #     message.error("service already exist")
            # else:
                
            # return redirect('ServiceList')

    else:
        ServiceForm=AddServiceForm()
    return render(request,'community/AddNewService.html',{'ServiceForm':ServiceForm})    

