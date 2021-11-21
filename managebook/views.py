from django.shortcuts import render
from django.http.request import HttpRequest
from rest_framework import renderers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

# Create your views here.
import requests
import json

# def error_view(request, exception):
#     data = {"exception": "Server Side Exception. Method failed to proceed!"}
#     # return render(request,"managebook/error_500.html", data)
#     return Response(data, 404)

# def error_500_view(request):
#     data = {"exception": "Server Side Exception. Method failed to proceed!"}
#     # return render(request,"managebook/error_500.html", data)
#     return Response(data, 500)


class ExternalView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            bookname = request.GET["name"]

            if(len(bookname.strip())==0):
                responseJson = {
                    'status_code': 200,
                    'status': 'success',
                    'data': []
                }
                return Response(responseJson)

            # response = requests.get('https://anapioficeandfire.com/api/books?name=A Game of Thrones')
            response = requests.get('https://anapioficeandfire.com/api/books?name='+bookname)
            books_from_ext = response.json()

            json_data = json.dumps(response.json())
            item_dict = json.loads(json_data)
            books_no = len(item_dict)
            bookdata={}
            booklist = []
            for book in books_from_ext:
                bookdata["name"]=book["name"]
                bookdata["isbn"]=book["isbn"]
                bookdata["authors"]=book["authors"]
                bookdata["number_of_pages"]=book["numberOfPages"]
                bookdata["publisher"]=book["publisher"]
                bookdata["country"]=book["country"]
                bookdata["release_date"]=book["released"][:10] # clipping timestamp to date part
                # print(bookdata)
                booklist.append(bookdata)

            # print(booklist)
            responseJson = {
                'status_code': 200,
                'status': 'success',
                'data': booklist
            }
            return Response(responseJson, status=200)
        
        except:
            responseJson = {
                'status_code': 500,
                'status': 'failed',
                'data': []
            }
            return Response(responseJson, status=500)

# class DbOpView(APIView):
#     @api_view(('POST',))
#     @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
#     def post(self, request:HttpRequest, *args, **kwargs):
#         try:
#             bookname = request.GET["name"]
#             # print("Bookname "+bookname);
#             if(len(bookname.strip())==0):
#                 responseJson = {
#                     'status_code': 200,
#                     'status': 'success',
#                     'data': []
#                 }
#                 return Response(responseJson)

#             json_data = json.dumps([])
#             item_dict = json.loads(json_data)
#             books_no = len(item_dict)
#             bookdata={}
#             booklist = []
#             # for book in books_from_ext:
#             #     bookdata["name"]=book["name"]
#             #     bookdata["isbn"]=book["isbn"]
#             #     bookdata["authors"]=book["authors"]
#             #     bookdata["number_of_pages"]=book["numberOfPages"]
#             #     bookdata["publisher"]=book["publisher"]
#             #     bookdata["country"]=book["country"]
#             #     bookdata["release_date"]=book["released"][:10] # clipping timestamp to date part
#             #     # print(bookdata)
#             #     booklist.append(bookdata)

#             # print(booklist)
#             responseJson = {
#                 'status_code': 200,
#                 'status': 'success',
#                 'data': booklist
#             }
#             return Response(responseJson, status=200)
        
#         except:
#             responseJson = {
#                 'status_code': 500,
#                 'status': 'failed',
#                 'data': []
#             }
#             return Response(responseJson, status=500)