from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template
from searchFiles.forms import  SearchForms
from searchFiles.models import FileTable, PathTable
from django_tables2 import RequestConfig
from django.db.models import Q
import json
from app_cmp.models import TempTable

from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

import app_cmp.word_finder as getData

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
        args = list(args.strip().split(" "))
        if len(args) < 1:
            
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
            table = getData.getResult(args).getValues()
            #print(json.dumps(table, indent = 4))

            def insertDB(_list):
                import django
                django.setup()
                print("*************************************************************")
                TempTable.objects.all().delete()

                for i in _list:
                    c = TempTable.objects.get_or_create(SearchTerm = i[0],RootPath=i[1], FileName=i[2], lineNumber=i[3])[0]
                    print(c)
                    c.save()


            def initial_letter_filter(text, line,  autoescape=True):
                result ="<a href=\"displayFile/" + str(text) + "\">"+ str(line) + "</a>"
                return mark_safe(result)

            i = []
            a = []
            for x in table:
                for _i in table[x]:
                    a.append(x)
                    for c in _i :
                        a.append(c)
                    i.append(a)
                    a= []
            insertDB(i)

            table = TempTable.objects.all()

            i = []
            a = []
            for x in table:
                a.append(x.SearchTerm)
                a.append(x.RootPath)
                a.append(x.FileName)
                a.append(initial_letter_filter(x.FileID, x.lineNumber))
                i.append(a)
                a = []

                
            return render(request,'app_cmp/fileList.1.html', {'files': i})

    else:
        print(form.errors)
    
    return render(request, 'app_cmp/index.1.html', {'form' : form})
 
def displayFile(request, value):
    vals = TempTable.objects.filter(FileID = value)
    path = str(vals[0].RootPath) + "//" + str(vals[0].FileName)
    lineNumber = vals[0].lineNumber
    context_val = []
    i = 1
    with open(path) as fp:  
        line = fp.readline()
        if i == int(lineNumber):
            context_val.append("$" + str(i) +". " + line.replace('\n', ""))
        else:
            context_val.append(str(i) +". " + line.replace('\n', ""))
        while line:
            i+= 1
            line = fp.readline()
            if i == int(lineNumber):
                context_val.append("$" + str(i) +". " + line.replace('\n', ""))
            else:
                context_val.append(str(i) +". " +  line.replace('\n', ""))
    return render(request, 'app_cmp/files.1.html', {'code' : context_val})
