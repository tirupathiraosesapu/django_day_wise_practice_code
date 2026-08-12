from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)



from .models import Employee
from .serializer import EmployeeModelSerializer
from .permissions import IsAdminUser, IsAdminOrManager


# Normal API Views
class EmployeeAPIView(APIView):
    # permission_classes = [IsAuthenticated]
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

# Generic API Views
class EmployeeGenericAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class EmployeeDeleteAPIView(APIView):
    permission_classes = [IsAdminOrManager  ]
    def delete(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeeDetailedGenericAPIView(
    RetrieveModelMixin, UpdateModelMixin,DestroyModelMixin, GenericAPIView
):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer

    def get(self, request, pk):
        return self.retrieve(request)

    def put(self, request, pk):
        return self.update(request)

    def patch(self, request, pk):
        return self.partial_update(request)

    def delete(self, request, pk):
        return self.destroy(request)

# Concrete generic API Views
class EmployeeListCreateAPIView(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer

class EmployeeDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer
