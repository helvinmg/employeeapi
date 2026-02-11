#from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
# Create your views here.
@api_view(['GET'])
def emp_all(request):#/api/employees/
    records=Employee.objects.all()
    serializer=EmployeeSerializer(records,many=True)
    return Response(serializer.data)
    #return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def emp_one(request,id):#/api/employees/1/
    record=Employee.objects.get(id=id)
    serializer=EmployeeSerializer(record)
    return Response(serializer.data)

@api_view(['POST'])
def emp_create(request):
    serializer=EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Successfully Created")
    else:
        return Response("Data missing or Invalid")
