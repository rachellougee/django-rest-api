from django.shortcuts import render
#from django.http import JsonResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#from rest_framework.decorators import api_view
from book_api.models import Book
from book_api.serializer import BookSerializer

# class based view
class BookList(APIView):
    def get(self, request, format=None):
         books = Book.objects.all()
         serializer = BookSerializer(books, many=True)
         return Response(serializer.data)

    def post(self, request, format=None):     
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)



class BookDetail(APIView):

     def get_book_by_id(self, id):
        try:
           return Book.objects.get(pk=id)  
        except Book.DoesNotExist:
            raise Http404
        

     def get(self, request, id, format=None):
         book = self.get_book_by_id(id)
         serializer = BookSerializer(book)
         return Response(serializer.data)


     def put(self, request, id, format=None):
         book = self.get_book_by_id(id)
         serializer = BookSerializer(book, data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


     def delete(self, request, id, format=None):
        book = self.get_book_by_id(id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# function based view
# @api_view(['GET', 'POST'])
# def book_list(request, format=None):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         # bookList = list(books.values())
#         # return JsonResponse({
#         #    'books': bookList
#         # })
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


# @api_view(['GET', 'PUT', 'DELETE'])
# def book_detail(request, id):
#     try:
#         book = Book.objects.get(pk=id)
#     except Book.DoesNotExist:
#         return Response({
#             'error': "Book doesn't exist"
#         }, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
        
#     elif request.method == 'PUT':
#          serializer = BookSerializer(book, data=request.data)
#          if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
 
#     elif request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
