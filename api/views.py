from itertools import count
from .models import *
import json
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import JsonResponse
from django.db import models


@api_view(['GET'])
def index(request):
    return JsonResponse({"status": 200})


@api_view(['POST', 'PUT'])
def user_actions(request):
    """
        "first_name": "value",
        "last_name":"value",
        "age", value,
        "address_no":value,
        "address_street":"value",
        "address_city":"value",
        "address_country":"value",
    """
    if request.method == "POST":
        json_data = json.loads(request.body)
        first_name = json_data['first_name']
        last_name = json_data['last_name']
        age = json_data['age']
        address_no = json_data['address_no']
        address_street = json_data['address_street']
        address_city = json_data['address_city']
        address_country = json_data['address_country']
        n_user = User(f_name=first_name, l_name=last_name, age=age, address_no=address_no,
                      address_street=address_street, address_city=address_city, address_country=address_country)
        n_user.save()
        return JsonResponse({"success": True})
    elif request.method == "PUT":
        json_data = json.loads(request.body)
        keys = json_data.items()
        user_id = json_data.get('user_id') or None
        if user_id == None:
            return JsonResponse({"success": False, "error": "user_id is required"})
        try:
            filteredObject = User.objects.get(u_id=user_id)
        except User.DoesNotExist:
            return JsonResponse({"success": False, "error": "user_id does not exist"})

        for key, value in keys:
            if key == "first_name":
                filteredObject.f_name = value
            elif key == "last_name":
                filteredObject.l_name = value
            elif key == "age":
                filteredObject.age = value
            elif key == "address_no":
                filteredObject.address_no = value
            elif key == "address_street":
                filteredObject.address_street = value
            elif key == "address_city":
                filteredObject.address_city = value
            elif key == "address_country":
                filteredObject.address_country = value

        filteredObject.save()
        return JsonResponse({"success": True})

    return JsonResponse({
        "message": "Method Not Allowed"
    })


@api_view(['GET'])
def specific_user_actions(request, user_id):
    try:
        user_object = User.objects.get(u_id=user_id)
    except User.DoesNotExist:
        return JsonResponse({"success": False, "error": "user_id does not exist"})
    return JsonResponse({
        "user_id": user_object.u_id,
        "first_name": user_object.f_name,
        "last_name": user_object.l_name,
        "age": user_object.age,
        "address": {
            "no": user_object.address_no,
            "street": user_object.address_street,
            "city": user_object.address_city,
            "country": user_object.address_country
        }
    })


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def ad_actions(request):
    if request.method == "GET":
        # this would've been used with a serializer which I forgot ..
        add_json = []
        all_ads = Ad.objects.all()
        for ad in all_ads:
            add_json.append({
                "ad_id": ad.a_id,
                "title": ad.title,
                "description": ad.description,
                "price": ad.price_per_km,
                "posted_time": ad.posted_time,
                "user": {
                    "id": ad.user.u_id,
                    "name": ad.user.f_name + " " + ad.user.l_name,
                },
                "car": {
                    "id": ad.car.c_id,
                    "model": ad.car.model,
                    "brand": ad.car.brand,
                    "car_plate": ad.car.number_plate,
                }
            })
        return JsonResponse(add_json, safe=False)
    # for creating a new ad
    elif request.method == "POST":
        json_data = json.loads(request.body)
        title = json_data['title']
        description = json_data['description']
        price = json_data['price']
        user_id = json_data.get('user_id') or None
        car_id = json_data.get('car_id') or None
        if car_id == None:
            return JsonResponse({"success": False, "error": "car_id is required"})
        if user_id == None:
            return JsonResponse({"success": False, "error": "user_id is required"})
        try:
            user_object = User.objects.get(u_id=user_id)
        except User.DoesNotExist:
            return JsonResponse({"success": False, "error": "user_id does not exist"})

        try:
            car_object = Car.objects.get(c_id=car_id)
        except Car.DoesNotExist:
            return JsonResponse({"success": False, "error": "car_id does not exist"})

        n_ad = Ad(title=title, description=description,
                  price_per_km=price, car=car_object, user=user_object)
        n_ad.save()

        return JsonResponse({"success": True})

    # for updating a specific ad
    elif request.method == "PUT":
        json_data = json.loads(request.body)
        ad_id = json_data.get('ad_id') or None
        if (ad_id == None):
            return JsonResponse({"success": False, "error": "ad_id is required"})
        try:
            filteredObject = Ad.objects.get(a_id=ad_id)
        except Ad.DoesNotExist:
            return JsonResponse({"success": False, "error": "Ad does not exist"})

        keys = json_data.items()
        for key, value in keys:
            if key == "title":
                filteredObject.title = value
            elif key == "description":
                filteredObject.description = value
            elif key == "price":
                filteredObject.price_per_km = value
            elif key == "user_id":
                try:
                    user_object = User.objects.get(u_id=value)
                except User.DoesNotExist:
                    return JsonResponse({"success": False, "error": "user_id does not exist"})
                filteredObject.user = user_object
            elif key == "car_id":
                try:
                    car_object = Car.objects.get(c_id=value)
                except Car.DoesNotExist:
                    return JsonResponse({"success": False, "error": "car_id does not exist"})
                filteredObject.car = car_object

        filteredObject.save()
        return JsonResponse({"success": True})

    elif request.method == "DELETE":
        json_data = json.loads(request.body)
        ad_id = json_data.get('ad_id') or None
        if (ad_id == None):
            return JsonResponse({"success": False, "error": "ad_id is required"})
        try:
            filteredObject = Ad.objects.filter(a_id=ad_id)
        except Ad.DoesNotExist:
            return JsonResponse({"success": False, "error": "Ad does not exist"})

        filteredObject.delete()
        return JsonResponse({"success": True})

    return JsonResponse({
        "message": "Method Not Allowed"
    })


@api_view(['GET'])
def specific_ad_actions(request, ad_id):
    try:
        ad = Ad.objects.get(a_id=ad_id)
    except Ad.DoesNotExist:
        return JsonResponse({"success": False, "error": "ad_id does not exist"})

    return JsonResponse({
        "ad_id": ad.a_id,
        "title": ad.title,
        "description": ad.description,
        "price": ad.price_per_km,
        "posted_time": ad.posted_time,
        "user": {
            "id": ad.user.u_id,
            "name": ad.user.f_name + " " + ad.user.l_name,
        },
        "car": {
            "id": ad.car.c_id,
            "model": ad.car.model,
            "brand": ad.car.brand,
            "car_plate": ad.car.number_plate,
        }
    })


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def car_actions(request):
    if request.method == "GET":
        car_json = []
        all_cars = Car.objects.all()
        for car in all_cars:
            car_json.append({
                "car_id": car.c_id,
                "model": car.model,
                "brand": car.brand,
                "number_plate": car.number_plate,
                "user": {
                    "id": car.user.u_id,
                    "name": car.user.f_name + " " + car.user.l_name,
                }
            })
        return JsonResponse(car_json, safe=False)

    elif request.method == "POST":
        json_data = json.loads(request.body)
        model = json_data['model']
        brand = json_data['brand']
        number_plate = json_data['number_plate']
        user_id = json_data.get('user_id') or None
        if user_id == None:
            return JsonResponse({"success": False, "error": "user_id is required"})
        try:
            user_object = User.objects.get(u_id=user_id)
        except User.DoesNotExist:
            return JsonResponse({"success": False, "error": "user_id does not exist"})

        n_car = Car(model=model,
                    brand=brand, number_plate=number_plate, user=user_object)
        n_car.save()
        return JsonResponse({"success": True})

    elif request.method == "PUT":
        json_data = json.loads(request.body)
        car_id = json_data.get('car_id') or None
        if (car_id == None):
            return JsonResponse({"success": False, "error": "car_id is required"})
        try:
            filteredObject = Car.objects.get(c_id=car_id)
        except Car.DoesNotExist:
            return JsonResponse({"success": False, "error": "Car does not exist"})

        keys = json_data.items()
        for key, value in keys:
            if key == "model":
                filteredObject.model = value
            elif key == "brand":
                filteredObject.brand = value
            elif key == "number_plate":
                filteredObject.number_plate = value
            elif key == "user_id":
                try:
                    user_object = User.objects.get(u_id=value)
                except User.DoesNotExist:
                    return JsonResponse({"success": False, "error": "user_id does not exist"})
                filteredObject.user = user_object

        filteredObject.save()
        return JsonResponse({"success": True})
    elif request.method == "DELETE":
        json_data = json.loads(request.body)
        car_id = json_data.get('car_id') or None
        if (car_id == None):
            return JsonResponse({"success": False, "error": "car_id is required"})
        try:
            filteredObject = Car.objects.filter(c_id=car_id)
        except Car.DoesNotExist:
            return JsonResponse({"success": False, "error": "Car does not exist"})

        filteredObject.delete()
        return JsonResponse({"success": True})


@api_view(['GET'])
def specific_car_actions(request, car_id):
    try:
        car = Car.objects.get(c_id=car_id)
    except Car.DoesNotExist:
        return JsonResponse({"success": False, "error": "car_id does not exist"})
    return JsonResponse({
        "car_id": car.c_id,
        "model": car.model,
        "brand": car.brand,
        "number_plate": car.number_plate,
        "user": {
            "id": car.user.u_id,
            "name": car.user.f_name + " " + car.user.l_name,
        }
    })
