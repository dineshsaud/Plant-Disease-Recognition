from django.shortcuts import render
from django.http import HttpResponse 
from .models import testImage
from .models import DiseaseDes
import pickle
import numpy as np
from PIL import Image
from keras.preprocessing.image import img_to_array
from keras.models import load_model 
import keras 

from image_processing import image_converter

def index(request):
    return render(request,'home.html')


def uploadImage(request):
    caughtImage = request.FILES["myImage"]
    outgoingImage = testImage(image = caughtImage)
    outgoingImage.save()
    plant = testImage.objects.all()
    p =  plant[len(plant)-1].image
    # print(p.url)
    # return render(request,'classify1.html', {'pic':p.url})
    classifer_model = load_model('mymodel.h5')
    label_binarizer = pickle.load(open("label_transform.pkl",'rb'))
    image_array = image_converter.convert_image_to_array(p.url)
    prediction = classifer_model.predict(image_array)
    label_pridected = label_binarizer.inverse_transform(prediction)[0]
    keras.backend.clear_session()
    return render(request,'home.html',{'output':label_pridected})


    
# def get_img_url():
#     plant = testImage.objects.all()
#     p =  plant[len(plant)-1].image
#     image_url = p.url
#     return image_url


# def predict_disease(request):
#     # image_data = get_img_url()
#     # classifer_model = pickle.load(open("cnn_model.pkl",'rb'))
#     classifer_model = load_model('mymodel.h5')
#     label_binarizer = pickle.load(open("label_transform.pkl",'rb'))
#     image_array = image_converter.convert_image_to_array(image_data)
#     prediction = classifer_model.predict(image_array)
#     label_pridected = label_binarizer.inverse_transform(prediction)[0]
#     return render(request,'home.html',{'output':label_pridected})


def test_url(request):
    url=get_img_url()
    return render(request,'about.html',{'url':url})


def help(request):
    return render(request,'help.html')

def getDetails(request):
    Diseasename = request.GET['name']
    # print('name=',name)
    print(Diseasename)
    obj=DiseaseDes.objects.filter(name=Diseasename)
    # Disease = obj[Name=Diseasename]
    print(obj)
    return render(request,'result.html',{'Details':obj})

def aboutus(request):
    return render(request,'aboutus.html')