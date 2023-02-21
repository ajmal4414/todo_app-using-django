from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import RegisterForm,LoginForm
from .models import Tasks,Register,Login

from django.contrib.auth.views import LoginView
# Create your views here.

# def login_fun(request):

# def signup_fun(request):
#     context={}
#     form=Signupform(request.POST)
#     if form.is_valid():
#         form.save()
#     context['form']=form
#     return render(request,'signup.html',context)
#
# def login_fun(request):
#     context={}
#     form=Loginform(request.POST)
#     if form.is_valid():
#         form.save()
#     context['form']=form
#     return render(request,'Login.html',context)





class Tasklist(ListView):
    model= Tasks
    context_object_name = 'Tasks'
    template_name = 'tasklist.html'

class TaskCreate(CreateView):
    model= Tasks
    fields = '__all__'
    success_url = reverse_lazy('Tasks')
    template_name = 'taskcreate.html'

class TaskUpdate(UpdateView):
    model=Tasks
    fields='__all__'
    success_url = reverse_lazy('Tasks')
    template_name = 'taskcreate.html'

class TaskDelete(DeleteView):
    model=Tasks
    context_object_name = 'Tasks'
    success_url = reverse_lazy('Tasks')
    template_name = 'taskdelete.html'

class TaskDetailView(DetailView):
    model=Tasks
    context_object_name = 'Tasks'
    success_url= reverse_lazy('Tasks')
    template_name = 'taskdetails.html'
#
def register_fun(request):
    register=Register.objects.all()
    form=RegisterForm()

    if request.method=='POST':
        form =RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    context={'register':register,'form':form}
    return render(request,'register.html',context)

def login_fun(request):
    login=Login.objects.all()
    form=LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Tasks')
    context = {'login': login, 'form': form}
    return render(request,'login.html', context)




# class CustomLoginView(LoginView):
#     template_name = 'login.html'
#     fields ='__all__'
#     redirect_authenticated_user = True
#     success_url = reverse_lazy('Login')

# class CustomSignupView( CreateView):
#     template_name='signup.html'
#     fields='__all__'
#     redirect_authenticated_user =True
#     success_url =reverse_lazy('Tasks')


