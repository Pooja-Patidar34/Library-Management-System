from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('AddAuthor/',views.AddAuthorDetails,name='AddAuthor'),
    path('AddBook',views.AddBookDetails,name='AddBook'),
    path('AddBorrowRecord',views.AddBorrowDetails,name="AddBorrowRecord"),
    path('AutherRecord',views.AuthorRecord,name='AuthorRecord'),
    path('BookRecord',views.BookRecord,name='BookRecord'),
    path('BorrowRecord',views.BorrowRecord,name='BorrowRecord'),
    path('Export_BookRecords',views.ExportBookRecords,name='Export_BookRecords'),
    path('Export_AuthorRecords',views.ExportAuthorRecords,name='Export_AuthorRecords'),
    path('Export_BorrowRecords',views.ExportBorrowRecords,name='Export_BorrowRecords'),

]