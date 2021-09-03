from django.contrib import messages
from django.shortcuts import render

from djangoProject_Wargaming.settings import MEDIA_ROOT
from .models import Table

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ModelDataForm, UploadFileForm
import time
import sys
import os


def handle_uploaded_file(f,request):
    with open(f'{MEDIA_ROOT}/{request.FILES["file"]}', 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# def upload_file(request):
#     if request.method == 'POST':
#         form = ModelDataForm(request.POST, request.FILES)
#         if form.is_valid():
#             # handle_uploaded_file(request.FILES['file'])
#             form.save()
#             return HttpResponseRedirect('/file_info')
#     else:
#         form = ModelDataForm()
#     return render(request, 'table/index.html', {'form': form})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES['file'])
            handle_uploaded_file(request.FILES['file'],request)
            # file_read(request)
            return HttpResponseRedirect('/file_info')
    else:
        form = UploadFileForm()
    return render(request, 'table/index.html', {'form': form})


def file_read(request):
    # with open(f'{MEDIA_ROOT}/file.txt', 'r') as f:
    #     file = f.readlines()

    # for city in lst:
    #     table = Table()
    #     table.city = city
    #     table.save()

    # lst = []
    #
    # new_city = Table.objects
    # lst.append(new_city)
    #
    # city = Table.objects.all()
    #
    # print(lst)

    with open(f'{MEDIA_ROOT}/file.txt', 'r') as f_1:
        f = f_1.read()
        lst = f.replace(',', ' ,').replace('.', ' .').split()

        # cоздаем словарь слов со значением 0
        word_dict = {}
        for dct in lst:
            word_dict[dct] = 0

        # считаем сколько раз слово указано в тексте
        result = {}
        count = 0
        for key in word_dict.keys():
            result[key] = lst.count(key)
            count += 1
        sum_words = len(lst)

        # считаем TF в одном документе
        word_TF = {}
        for key, value in result.items():
            word_TF[key] = round(value / sum_words, 2)
        # print(word_TF)




        # word_IDF =
    # word = Table.objects.all()
    context = {
        # 'word': word,
        'word_TF': word_TF,
        # 'word_IDF': word_IDF,
    }
    return render(request, 'table/file_info.html', context)
