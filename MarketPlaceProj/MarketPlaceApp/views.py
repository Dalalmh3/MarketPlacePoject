from django.shortcuts import render,redirect, HttpResponse
# Create your views here.

# def index(request):
#     return HttpResponse("this is the equivalent of @app.route('/')!")

#     from django.shortcuts import render, redirect
def index(request):
    return render(request, "MarketPlaceApp/index.html" ) 
    # if request.method == "POST":
    #     val_from_field_one = request.POST["one"]
    # 	val_from_field_two = request.POST["two"]