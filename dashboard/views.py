from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status, response
from .serializers import FileSerializer
from .models import FileModel


# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')



def manage(request):
    return render(request, 'dashboard/manage.html')



def feed(request):
    return render(request, 'dashboard/feed.html')



def scan_info(request):
    alert_data = FileModel.objects.filter(message_type="ALERT")
    good_data = FileModel.objects.exclude(message_type="ALERT")
    return render(request, "dashboard/scan_info.html", context={
        "alerts":alert_data,
        "alert_count": len(alert_data),
        "goods": good_data,
        "good_count": len(good_data)
    })

@api_view(['POST'])
def file_post(request):
    serializer = FileSerializer(data = request.data)
    if(serializer.is_valid()):
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def file_delete(request):
    FileModel.objects.all().delete()
    return response.Response(data={"message":"Data deleted"}, status=status.HTTP_200_OK)



