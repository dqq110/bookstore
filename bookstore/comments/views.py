from django.shortcuts import render
from utils.decorators import login_required
from comments.models import Comments
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from books.models import Books
from order.models import OrderGoods,OrderInfo
from users.models import Passport
# Create your views here.

@login_required
def comment_add(request):
    passport_id = request.session.get('passport_id')
    passport = Passport.objects.filter(id=passport_id)[0]
    if passport:
            content = request.POST.get('comment','')
            books_id = request.POST.get('books_id','')
            print('books_id================',books_id)
            book = Books.objects.get_books_by_id(books_id=books_id)
            book_li = Books.objects.get_books_type(type_id=book.type_id,limit=2,sort='default')
            bookname = book.name
            comments = Comments()
            comments.comment_man = passport
            comments.comment_book = book
            comments.comment_content = content
            comments.save()
            context = {
                'bookname' : bookname,
                'content' : content,
                'books' : book,
                'books_li': book_li
            }
            return render(request,'books/detail.html',context)




