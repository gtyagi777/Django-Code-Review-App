from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, Template
from app_cmp.forms import SearchForms
from app_cmp.models import FileTable, PathTable
from django_tables2 import RequestConfig
from django.db.models import Q

from app_cmp.models import TempTable

from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

import app_cmp.word_finder as getData
from app_cmp.searchInFiles import searchHandler
import app_cmp.populate as pop

def index(request):
    return render(request, 'api/filelist.html', {})

def get_files(request):

    form = SearchForms()
    if request.method == "POST":
        form = SearchForms(request.POST)
        data = request.POST.get('search')
        args = request.POST.get('search1')
        args = list(args.strip().split())
        return render(request, 'api/filelist.html', {'fname': data,'args':args})
        if len(args) < 1 and len(str(data)) < 1:
            pass
 
        elif len(args) < 1:
            table = FileTable.objects.filter(Q(FileName__contains=str(data)))
            xX = list(table.values("FileID","RootPath__Path","FileName","Extension"))

            i = []
            a = []
            for x in table:
                a.append(x.RootPath)
                a.append(x.FileName)
                a.append(x.Extension)
                a.append(x.FileID)
                i.append(a)
                a = []
            
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
    
    pk = request.GET.get('pk')
    data = FileTable.objects.filter(Q(FileName__contains=str(pk)))
    data = list(data.values("FileID", "RootPath__Path","FileName","Extension"))
    return JsonResponse(data, safe=False)