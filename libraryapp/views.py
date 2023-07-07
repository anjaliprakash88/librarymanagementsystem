from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book


def helloview(request):
    books = Book.objects.all()
    return render(request, 'viewbook.html', {'books': books})


def addbookview(request):

    return render(request, 'addbook.html')


def addbook(request):
    if request.method == 'POST':
        t = request.POST['title']
        p = request.POST['price']
        print(t, p)
        book = Book()

        book.title = t
        book.price = p
        book.save()
        return HttpResponseRedirect('/')


def editbook(request):
    if request.method == 'POST':
        t = request.POST['title']
        p = request.POST['price']

        book = Book.objects.get(id=request.POST['bookid'])

        book.title = t
        book.price = p
        book.save()
        return HttpResponseRedirect('/')


def editbookview(request):
    book = Book.objects.get(id=request.GET['bookid'])
    return render(request, 'editbook.html', {'book': book})

def deletebookview(request):
    book = Book.objects.get(id=request.GET['bookid'])
    book.delete()
    return HttpResponseRedirect('/')




