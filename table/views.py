from djangoProject_Wargaming.settings import MEDIA_ROOT
from .models import Table, File, ResultTable

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
import math

FILES = []


def handle_uploaded_file(f, request):
    name_file = File.objects.all()
    names = []
    for text in name_file:
        names.append(str(text))
    filename = str(request.FILES["file"])

    if str(filename) not in names:
        n = File()
        n.name_file = filename
        n.save()

        FILES.append(str(filename))
        FILES_count = len(FILES)

        with open(f'{MEDIA_ROOT}/{filename}', 'wb') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

        with open(f'{MEDIA_ROOT}/{filename}', 'r') as f:

            # добавляем слова в локальный список слов, чтобы затем посчитать TF
            lst_words = f.read().replace('.', ' .').replace(',', ' ,').split()
            # print(lst_words)

            # cоздаем словарь слов со значением 0
            word_dict = {}
            for dct in lst_words:
                word_dict[dct] = 0

            # считаем сколько раз слово указано в тексте
            word_counter = {}
            for key in word_dict.keys():
                word_counter[key] = lst_words.count(key)

            sum_words = len(lst_words)

            # считаем TF в одном документе
            word_TF = {}
            for key, value in word_counter.items():
                word_TF[key] = (round(value / sum_words, 2))
            print(word_TF)

            # добавляем слово и его TF в БД.
            for k, v in word_TF.items():
                table = Table()
                table.word = k
                table.word_TF = v
                table.filename = filename
                table.save()

            # Таким образом, если «заяц» содержится в 1000 документах из 10 000 000 документов,
            # то IDF будет равной: log(10 000 000/1000) = 4.
            word_IDF = {}
            for key in word_counter.keys():
                q = Table.objects.filter(word=key).all().count()
                print(q)
                idf = round(math.log(FILES_count / q), 3)
                word_IDF[key] = idf

            # Добавляем word, TF, IDF в отдельную таблицу.
            for k, v in word_TF.items():
                for k1, v1 in word_IDF.items():
                    if k == k1:
                        result = ResultTable()
                        result.word = k
                        result.word_TF = v
                        result.word_IDF = str(v1)
                        result.filename = filename
                        result.save()


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'], request)
            return HttpResponseRedirect('/file_info')
    else:
        form = UploadFileForm()
    return render(request, 'table/index.html', {'form': form, 'title': 'Загрузить файл'})


def file_read(request):
    context = {
        'table': ResultTable.objects.all().order_by('-word_IDF')[:50],
        'title': 'Результат анализа',
    }

    return render(request, 'table/file_info.html', context)
