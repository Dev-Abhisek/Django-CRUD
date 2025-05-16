from book_store.models import Book
from .serializer import BookSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])

def get_books(request):
    if request.method == "POST":
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    if request.method == "GET":
        books = Book.objects.all()
        if not books.exists():
            return Response({"message": "No books found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET','PUT','DELETE'])

def get_book(request, pk):
    try:
        book = Book.objects.get(pk = pk)
    except Book.DoesNotExist:
        return Response({"Message": "Book not found"}, status= 404)
    
    if request.method == "GET":
        serializer = BookSerializer(book)
        return Response(serializer.data, status=200)
    
    if request.method == "PUT":
        serializer = BookSerializer(book, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    if request.method == "DELETE": 
        book.delete()
        return Response({"Message": "Book deleted"}, status=204)
    