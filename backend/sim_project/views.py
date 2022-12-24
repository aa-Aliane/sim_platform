from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .core.query import search, index, model
import os, json


@api_view(["POST"])
@permission_classes([AllowAny])
def get_context(request):
    print("aminneeeee")
    print(request.data["query_text"])
    results = search(request.data["query_text"], 5, index, model)
    data = results

    return Response(status=status.HTTP_200_OK, data=data)
