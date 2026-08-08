from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Employee
from .serializer import EmployeeModelSerializer


class EmployeeAPIView(APIView):
    def get(self, request):
        employee = Employee.objects.all()
        print("Employee", employee)
        serializer = EmployeeModelSerializer(employee, many=True)
        print("serializer", serializer.data)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetailedAPIView(APIView):
    def get(self, request, employee_id):
        # employee = Employee.objects.get(id=employee_id)
        employee = get_object_or_404(Employee, id=employee_id)
        serializer = EmployeeModelSerializer(employee)
        return Response(serializer.data)

    def put(self, request, employee_id):
        employee = get_object_or_404(Employee, id=employee_id)
        serializer = EmployeeModelSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, employee_id):
        employee = get_object_or_404(Employee, id=employee_id)
        serializer = EmployeeModelSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, employee_id):
        employee = get_object_or_404(Employee, id=employee_id)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
