from django.shortcuts import render ,redirect
from .models import Todo
from .forms import AddTodoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.utils.timezone import datetime

# Create your views here.
@login_required(login_url="/accounts/login/")
def dashboard(request):

    form = AddTodoForm()
    if request.method =='POST':
        form = AddTodoForm(request.POST)
        #check whether form is valid
        if form.is_valid():
            fs = form.save(commit=False)
            fs.user = request.user
            fs.save()
            messages.success(request, "your todo added Successfully.")
            return redirect('/dashboard')
        else:
            messages.error(request, 'The form is not Valid')
            return redirect('/dashboard')
    else:
        todo_list = Todo.objects.filter(user = request.user).order_by('-id')
        paginator = Paginator(todo_list , 10 ) #Show 10 data per page

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        get_completed_todo = Todo.objects.filter(user=request.user,status=False)
        get_completed_todo = get_completed_todo.count()


        get_pending_todo = Todo.objects.filter(user=request.user, status=True)
        get_pending_todo = get_pending_todo.count()

        context = {'form': form, 'page_obj': page_obj ,'todo_list':todo_list,
                   'get_completed_todo':get_completed_todo,
                   'get_pending_todo':get_pending_todo}

        return render(request,'todo/dashboard.html', context)


def home(request):
    return render(request, 'todo/home.html')

@login_required(login_url="/accounts/login/")
def delete_todo(request,pk):
    if request.method =='POST':
        deleted_todo = get_object_or_404(Todo,pk=pk,user=request.user)
        deleted_todo.delete()
        messages.success(request, "your todo delete Successfully.")
        return redirect('/dashboard')
    else:
        return redirect('/dashboard')

@login_required(login_url="/accounts/login/")
def complete_todo(request, pk):
    edit_todo = get_object_or_404(Todo, pk=pk)
    print(edit_todo)
    if request.method =="POST":
        edit_todo.status = False
        edit_todo.completed_at = datetime.now()
        messages.info(request, "your todo marked as completed.")
        edit_todo.save()
        return redirect('/dashboard')
    else:
        return redirect('/dashboard')