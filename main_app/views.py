from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.http import JsonResponse
from django.views.generic import ListView, View, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy

from main_app.models import *
from main_app.forms import LoginUserForm, RegisterUserForm
from blog.models import Article


def index(request):
    title = "Добро пожаловать!"
    sliders = Slider.objects.filter(is_active=True)
    features = Feature.objects.filter(is_active=True)[:3]
    chefs = Chef.objects.filter(is_active=True)[:4]
    blog_list = Article.objects.filter(is_active=True)[:3]
    pizzas = Products.objects.filter(is_active=True, category_slug="Пиццы")[:9]
    desserts = Products.objects.filter(is_active=True, category_slug="Десерты")[:9]

    return render(request, "main_app/index.html", {
        "sliders": sliders,
        "features": features,
        "chefs": chefs,
        "blog_list": blog_list,
        "desserts": desserts,
        "pizzas": pizzas,
        "title": title
    })


class About(ListView):
    model = Chef
    template_name = "main_app/about-us.html"
    context_object_name = "chefs"
    queryset = model.objects.filter(is_active=True)[:4]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "О нас"
        
        return context

    
class Menu(ListView):
    model = Products
    template_name = "main_app/menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Меню"
        context["breakfast_list"] = self.model.objects.filter(is_active=True, category_slug="Завтраки")
        context["pizzas_list"] = self.model.objects.filter(is_active=True, category_slug="Пиццы")
        context["desserts_list"] = self.model.objects.filter(is_active=True, category_slug="Десерты")
        context["drinks_list"] = self.model.objects.filter(is_active=True, category_slug="Напитки")
        
        return context


class Gallery(ListView):
    model = GalleryFood
    template_name = "main_app/gallery.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Галлерея"
        context["food_photo_main"] = GalleryFood.objects.filter(is_active=True)[0]
        context["foods_photo_list"] = GalleryFood.objects.filter(is_active=True)[1:]
        
        context["restaurant_photo_main"] = GalleryRestaurant.objects.filter(is_active=True)[0]
        context["restaurant_photo_list"] = GalleryRestaurant.objects.filter(is_active=True)[1:]

        return context


class Registration(CreateView):
    form_class = RegisterUserForm
    template_name = "main_app/registration.html"
    success_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Авторизация на сайте"
        return context
    

class Login(LoginView):
    form_class = LoginUserForm
    template_name = "main_app/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Логин на сайте"
        return context
    
    def get_success_url(self):
        return reverse_lazy("home")


def order_table(request):
    if request.method == "GET":
        output = "Method GET"

        if request.GET["user_id"] != "":
            id_p = request.GET["user_id"]
            if Client.objects.filter(person_id=id_p).exists():
                return HttpResponse(output)
            else:
                client = Client()
                client.person_id = id_p
                # client.telephone_number = request.GET["user_number"]
                client.save()
                return HttpResponse(output)

        if request.GET["user_number"] != "":
            pass

    output = "No data"
    return HttpResponse(output)


def order_products(request):

    if request.method == "GET":
        longitude = request.GET["longitude"]
        latitude = request.GET["latitude"]

        data = OrderProducts()
        data.user_id = request.GET["id"]
        data.phone = request.GET["tel"]
        data.order = request.GET["order"]
        data.location = f"longitude: {longitude}, latitude: {latitude}"

        data.save()

        return HttpResponse(status=200)

    output = "No data"
    return HttpResponse(output)


class ProductsCategoryView(View):

    def get(self, request):
        categories = ProductsCategory.objects.filter(is_active=True)
        if categories is None:
            return

        serialized_data = []
        for category in categories:
            serialized_data.append({
                "name": category.name,
            })

        data = {
            'data': serialized_data,
        }
        return JsonResponse(data)


class ProductsView(View):

    def get(self, request):
        products = Products.objects.filter(is_active=True)
        if products is None:
            return

        serialized_data = []
        for product in products:
            serialized_data.append({
                'name': product.name,
                'description': product.description,
                'category': product.category.name,
                'price': product.price,
                'size': product.size,
                'is_active': product.is_active,
            })

        data = {
            'data': serialized_data,
        }
        return JsonResponse(data)
