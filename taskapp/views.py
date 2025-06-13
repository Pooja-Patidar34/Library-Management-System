from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Author,Book,Borrow_Record
from .forms import add_author,add_book,borrow_record
from django.contrib import messages
from django.core.paginator import Paginator
import pandas as pd

def home(request):
    return render(request,'taskapp/home.html')

def AddAuthorDetails(request):
    if request.method=="POST":
        form=add_author(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get('name')
            email=form.cleaned_data.get('email')
            bio=form.cleaned_data.get('bio')
            Author.objects.create(
                name=name,
                email=email,
                bio=bio
            )
            messages.success(request,"New author added successfully")
            return redirect('/')
        else:
            messages.error(request,'Please complete all required fields.')
    else:
        form=add_author()
    return render(request,"taskapp/addauthor.html",{"form":form})


def AddBookDetails(request):
    if request.method=='POST':
        form=add_book(request.POST)
        if form.is_valid():
            title=form.cleaned_data.get('title')
            genre=form.cleaned_data.get('genre')
            published_date=form.cleaned_data.get('published_date')
            author_id=form.cleaned_data['author']
            print (author_id)
            if author_id:
                try:
                    author=Author.objects.get(id=author_id)

                    Book.objects.create(
                    title=title,
                    genre=genre,
                    published_date=published_date,
                    author=author
                    )
                except Author.DoesNotExist:
                    messages.error(request,"Author does not Exist")
            messages.success(request,'New Book Added Successfully!')
            return redirect('/')
        else:
            messages.error(request,'Please complete all required fields.')
    else:
        form=add_book()
        return render(request,'taskapp/addbook.html',{'form':form})
    
def AddBorrowDetails(request):
    if request.method=='POST':
        form=borrow_record(request.POST)
        if form.is_valid():
            user_name=form.cleaned_data.get('user_name')
            book_id=form.cleaned_data.get('book')
            borrow_date=form.cleaned_data.get('borrow_date')
            return_date=form.cleaned_data.get('return_date')
            if book_id:
                try:
                    book=Book.objects.get(id=book_id)
                    Borrow_Record.objects.create(
                    user_name=user_name,
                    book=book,
                    borrow_date=borrow_date,
                    return_date=return_date
                    )
                except Book.DoesNotExist:
                    messages.error(request,"Book is not Available")
            messages.success(request,'Borrow Record Added Successfully!')
            return redirect('/')
        else:
            messages.error(request,'Please complete all required fields.')
    else:  
        form=borrow_record()  
        return render(request, 'taskapp/addborrowrecord.html', {"form":form})    


def AuthorRecord(request):
    all_author=Author.objects.all().order_by('id')
    paginator=Paginator(all_author,2)
    page_number=request.GET.get('page')
    authors=paginator.get_page(page_number)
    all_pages=authors.paginator.num_pages
    page_range=[n+1 for n in range(all_pages)]
    return render(request,'taskapp/authorrecord.html',{'authors':authors,'page_range':page_range})


def BookRecord(request):
    all_books=Book.objects.all().order_by('id')
    paginator=Paginator(all_books,2)
    page_number=request.GET.get('page')
    books=paginator.get_page(page_number)
    all_pages=books.paginator.num_pages
    page_range=[n+1 for n in range(all_pages)]
    return render(request,'taskapp/bookrecord.html',{'books':books,"page_range":page_range})

def BorrowRecord(request):
    all_borrow_records=Borrow_Record.objects.all().order_by('id')
    paginator=Paginator(all_borrow_records,2)
    page_number=request.GET.get('page')
    borrow_records=paginator.get_page(page_number)
    all_pages=borrow_records.paginator.num_pages
    page_range=[n+1 for n in range(all_pages)]
    return render(request,'taskapp/borrowrecord.html',{'borrow_records':borrow_records,'page_range':page_range})


def ExportBookRecords(request):
    books=Book.objects.all()

    data=[]
    for book in books:
        data.append({
            'Id':book.id,
            'Title':book.title,
            'Genre':book.genre,
            'Author':book.author.name
        })
    df = pd.DataFrame(data)
    response=HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition']='attachment;filename="Books_Records.xlsx"'
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Author_Records', index=False)

    return response


        
def ExportAuthorRecords(request):
    authors=Author.objects.all()

    data=[]
    for author in authors:
        data.append({
            'Id':author.id,
            'Name':author.name,
            'Email':author.email,
            'Bio':author.bio
        })
    df = pd.DataFrame(data)
    response=HttpResponse(content_type='application/vnd.openxmlformats-officedocuments.spreadsheet.sheet')
    response['Content-Disposition']='attachment;filename="AuthorRecords.xlsx"'
    with pd.ExcelWriter(response,engine='openpyxl') as writer:
        df.to_excel(writer,sheet_name='AuthorRecords,index=false')
    return response


def ExportBorrowRecords(request):
    borrow_rec=Borrow_Record.objects.all()
    data=[]
    for borrow in borrow_rec:
        data.append({
            'Id':borrow.id,
            'UserName':borrow.user_name,
            'Book':borrow.book.title,
            'Borrow Date':borrow.borrow_date,
            'Return Date':borrow.return_date
        })
    df = pd.DataFrame(data)
    response=HttpResponse(content_type='application/vnd.openxmlformats-officedocuments.spreadsheet.sheet')
    response['Content-Disposition']='attachment;filename="BorrowRecords.xlsx"'
    with pd.ExcelWriter(response,engine='openpyxl') as writer:
        df.to_excel(writer,sheet_name='BorrowRecords,index=false')
    return response
