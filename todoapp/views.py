# from django.views import generic
# from .models import Task
#
# class IndexView(generic.ListView):
#     template_name = 'todoapp/index.html'
#
#     def get_queryset(self):
#         return Task.objects.all()
#
#
# class DetailView(generic.DetailView):
#     model = Task
#     template_name = 'todoapp/detail.html'
#


from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Task
from django.template import loader
from django.db.models import Q


# Create your views here.

def index(request):
    task_list = Task.objects.all()
    #output = ','.join([q.task_name for q in task_list])
    #template = loader.get_template('todoapp/index.html')
    context = {
        'task_list':task_list
    }
    return render(request, 'todoapp/index.html', context)


def addTodo(request):
    new_item = Task(task_name = request.POST['task_name'], task_priority = request.POST['task_priority'], task_description = request.POST['task_description'])
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def deleteTodo(request, task_id):
    delete_item = Task.objects.get(id=task_id)
    delete_item.delete()
    return HttpResponseRedirect('/todoapp/')


def detail(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404('Task does not exist')
    context = {
        'task':task,
    }
    return render(request, 'todoapp/detail.html', context)


def search(request):
    #template = ''
    query = request.GET.get('q')
    results = Task.objects.filter(Q(task_name__icontains=query) |  Q(task_description__icontains=query))
    print(len(results))
    context = {
        'task_list': results,
    }
    return render(request, 'todoapp/index.html', context)
