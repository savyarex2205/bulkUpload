from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.parsers import MultiPartParser, FileUploadParser


from django.http import Http404
import pandas as pd


from .models import userModel
from .serializers import userSerializers

class userList(APIView):
    def get(self, request, format=None):
        users = userModel.objects.all()
        userSerialize = userSerializers(users, many=True)
        return Response(userSerialize.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        print(request.data)
        userData = userSerializers(data = request.data)
        if userData.is_valid():
            userData.save()
            return Response(userData.data, status=status.HTTP_201_CREATED)
        return Response(userData.errors, status=status.HTTP_400_BAD_REQUEST)

class fileUpload(APIView):
    parser_classes = [MultiPartParser, FileUploadParser, ]

    def post(self, request, format=None):
        file = request.FILES.get('file')
        allData = []
        df1 = pd.read_excel(file, 'Sheet1')
        toJson = df1.to_csv()
        data = toJson.split(',')[4:]
        for i in range(len(data)):
            data[i] = data[i].split('\n')[0]
        # print(data)
        fileRange = int(len(data)/3)
        for i in range(fileRange):
            userData = {}
            userData["username"] = data[i]
            userData["password"] = data[i+2]
            userData["Name"] = data[i+3] 
            allData.append(userData)
            user = userSerializers(data = userData)
            if user.is_valid():
                user.save()
            else:
                return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(allData, status=status.HTTP_201_CREATED)
