from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, Template
from app_cmp.forms import SearchForms
from coreapi.models import FileTable, PathTable
from django_tables2 import RequestConfig
from django.db.models import Q

from coreapi.models import TempTable

from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

import app_cmp.word_finder as getData
from app_cmp.searchInFiles import searchHandler
import app_cmp.populate as pop

def index(request):
    return render(request, 'api/filelist.html', {})


def getDataBasedOnFileName(table):
    def insertDB(_list):
        import django
        django.setup()
        TempTable.objects.all().delete()
        print(len(_list))
        for i in _list:
            c = TempTable.objects.get_or_create(SearchTerm=i[0], RootPath=i[1],
                                                FileName=i[2], lineNumber=i[3], CodeLine=i[4])[0]
            c.save()

    i = []
    a = []
    for x in table:
        for _i in table[x]:
            a.append(x)
            for c in _i:
                a.append(c)
            i.append(a)
            a = []
    insertDB(i)

    table = TempTable.objects.all()
    data = list(table.values("FileID","SearchTerm","RootPath","FileName","lineNumber","CodeLine",))

    return data

def get_files(request):

    form = SearchForms()
    if request.method == "POST":
        form = SearchForms(request.POST)
        data = request.POST.get('search')
        args = request.POST.get('search1')
        print(args)
        args = list(args.split())
        return render(request, 'api/filelist.html', {'fname': data,'args':args})
        if len(args) < 1 and len(str(data)) < 1:
            pass
 
        elif len(args) < 1:
            table = FileTable.objects.filter(Q(FileName__contains=str(data)))
           
            return render(request, 'api/filelist.html', {'files': xX})

        elif len(args) > 0 and len(data.strip()) > 0:
            table = FileTable.objects.filter(Q(FileName__contains=str(data)))
            i = []
            for x in table:
               #print(str(x.RootPath) + "\\" + str(x.FileName))
                i.append(str(x.RootPath) + "\\" + str(x.FileName))
            table = searchHandler(args, i).getValues()
            #print(table)
            i = getDataBasedOnFileName(table)

            return render(request, 'app_cmp/fileList.1.html', {'files': i})

        else:
            table = getData.getResult(args).getValues()
            i = getDataBasedOnFileName(table)

            return render(request, 'app_cmp/fileList.1.html', {'files': i})

    else:
        print(form.errors)

    return render(request, 'app_cmp/index.1.html', {'form': form})





def get_data(request):
    data = request.GET.get('pk')
    args = request.GET.getlist('args[]')
    if  len(data) < 1 and len(args) < 1:
        pass

    elif len(args) > 0 and len(data.strip()) > 0:
        table = FileTable.objects.filter(Q(FileName__contains=str(data)))
        i = []
        for x in table:
            i.append(str(x.RootPath) + "\\" + str(x.FileName))

        table = searchHandler(args, i).getValues()
        #print(table)
        i = getDataBasedOnFileName(table)
        return JsonResponse(i, safe=False)
    
    elif len(args) < 1:
        data = FileTable.objects.filter(Q(FileName__contains=str(data)))
        data = list(data.values("FileID", "RootPath__Path","FileName",))
        return JsonResponse(data, safe=False)
        