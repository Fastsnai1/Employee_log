from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import *
from .models import *
import psycopg2
from mysite.settings import DATABASES
from psycopg2.extras import RealDictCursor


def db_answer(query):
    try:
        connection = psycopg2.connect(
            database=DATABASES['default']['NAME'],
            user=DATABASES['default']['USER'],
            host=DATABASES['default']['HOST'],
            port=DATABASES['default']['PORT'],
            password=DATABASES['default']['PASSWORD']
        )
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as err:
        print(err)
        print('ЧТо то пошло не так!')
    finally:
        cursor.close()
        connection.close()


def index(request):
    query1 = """SELECT * FROM employees_worker;"""
    all_workers = db_answer(query1)
    query2 = """SELECT * FROM employees_category;"""
    all_cat = db_answer(query2)
    query3 = """SELECT * FROM employees_position;"""
    all_pos = db_answer(query3)
    context = {
        'workers': all_workers,
        'cats': all_cat,
        'positoin': all_pos,
        'title': 'Главная страница',
    }
    return render(request, 'employees/index.html', context=context)


def adduser(request):
    if request.method == 'POST': # проверка валиднасти данных, если данные не верны вернёться заполненная форма
        form = AddWorkerForm(request.POST)
        if form.is_valid():
            try:
                Worker.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, "Ошибка добавления поста!")
    else:
        form = AddWorkerForm()
    query2 = """SELECT * FROM employees_category;"""
    all_cat = db_answer(query2)
    context = {
        'cats': all_cat,
        'form': form,
        'title': 'Добавление сотрудника',
    }

    return render(request, 'employees/adduser.html', context=context)


def create_user(request):

    return render(request, 'employees/create_user.html')


def add_position(request):
    workers = Worker.objects.all()
    context = {
        'workers': workers,
        'title': 'Добавление сотрудника',
    }
    return render(request, 'employees/add_position.html', context=context)


def show_worker(request, pos_id):
    query1 = f"SELECT * FROM employees_worker WHERE cat_id = {pos_id};"
    all_workers = db_answer(query1)
    query2 = """SELECT * FROM employees_category;"""
    all_cat = db_answer(query2)
    query3 = f"SELECT * FROM employees_position WHERE cat_id = {pos_id};"
    all_pos = db_answer(query3)
    context = {
        'workers': all_workers,
        'cats': all_cat,
        'positoin': all_pos,
        'title': 'Главная страница',
    }
    return render(request, 'employees/show_worker.html', context=context)


def show_cats(request, cat_id):
    # Выводит все должности в категории
    query2 = """SELECT * FROM employees_category;"""
    all_cat = db_answer(query2)
    query3 = f"SELECT * FROM employees_position WHERE cat_id = {cat_id};"
    all_pos = db_answer(query3)
    context = {
        'cats': all_cat,
        'positoin': all_pos,
        'title': 'Главная страница',
    }
    return render(request, 'employees/show_cats.html', context=context)
