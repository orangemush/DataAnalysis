from django.shortcuts import render

from django.template  import RequestContext
from django.http      import HttpResponse, JsonResponse

from django.views import View
from django.db.models  import Q

import json
from .models import Searchword, Movie


class MovieView(View):
    def get(request):
        if request.method == "GET":
            print("get")

        return render(request, 'prediction/index.html')

    def post(request):
        movie_name = request.POST["movieName"]
        if Movie.objects.filter(movieNm=movie_name).exists():
            movie_data = Movie.objects.filter(movieNm=movie_name).values()[0]
            movie_data["status"] = True
            print(movie_data)
            return render(request, 'prediction/index.html', movie_data)

        return render(request, 'prediction/index.html')

    # def index(request):
    #     # print(request.POST["movieName"])

        # try:
        #     movie_name = request.POST["movieName"]
        # except:
        #     pass

        # print(Movie.objects.filter(movieNm=movie_name))
        # print(movie_name)    

        
        # list(ShopProduct.objects.all().values())
        # list(CategoryProduct.objects.filter(category_id = 2).values())
        # search_shop = list(ShopProduct.objects.filter(
        #         Q(outer_tag__icontains = item) | 
        #         Q(inner_description__icontains = item) | 
        #         Q(inner_details__icontains = item)
        #         ).values()
        #     )

