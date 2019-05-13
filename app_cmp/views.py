from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template
from searchFiles.forms import  SearchForms
from searchFiles.models import FileTable, PathTable
from searchFiles.tables import PTable
from django_tables2 import RequestConfig
from django.db.models import Q

from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

# Create your views here.
def index(request):
    form = SearchForms()
    return render(request, 'app_cmp/index.1.html', {'form' : form})
    
def fileList(request):

    form = SearchForms()
    if request.method == "POST":
        form = SearchForms(request.POST)
        data = request.POST.get('search')
        args = request.POST.get('search1')
        args = list(args.split(" "))
        if len(args) < 5:
            
            table = FileTable.objects.filter(Q(FileName__contains = str(data)))

            def initial_letter_filter(text, autoescape=True):
                result ="<a href=\"displayFile/" + str(text) + "\">Visit File</a>"
                return mark_safe(result)

            i = []
            a = []
            for x in table:
                a.append(x.RootPath)
                a.append(x.FileName)
                a.append(x.Extension)
                a.append(initial_letter_filter(x.FileID))
                i.append(a)
                a = []

                
            return render(request,'app_cmp/fileList.1.html', {'files': i})
        else:
            table = FileTable.objects.filter(Q(FileName__contains = str(arg[0])))

            def initial_letter_filter(text, autoescape=True):
                result ="<a href=\"displayFile/" + str(text) + "\">Visit File</a>"
                return mark_safe(result)

            i = []
            a = []
            for x in table:
                a.append(x.RootPath)
                a.append(x.FileName)
                a.append(x.Extension)
                a.append(initial_letter_filter(x.FileID))
                i.append(a)
                a = []

                
            return render(request,'app_cmp/fileList.1.html', {'files': i})

    else:
        print(form.errors)
    
    return render(request, 'app_cmp/index.1.html', {'form' : form})
 
def displayFile(request, file_id):
    vals = FileTable.objects.filter(FileID = file_id)
    path = str(vals[0].RootPath) + "//" + str(vals[0].FileName) +  str(vals[0].Extension)
    context_val = []
    i = 1
    with open(path) as fp:  
        line = fp.readline()
        context_val.append(str(i) +". " + line.replace('\n', ""))
        while line:
            i+= 1
            line = fp.readline()
            context_val.append(str(i) +". " +  line.replace('\n', ""))
    return render(request, 'app_cmp/files.1.html', {'code' : context_val})
