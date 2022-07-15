from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Link
from .serializers import LinkSerializer
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
import uuid

@api_view(['GET', 'POST'])
def Link_list(request, custom_name=''):

    if request.method == 'GET':
        links = Link.objects.all()
        serializer = LinkSerializer(links, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        request.data['short_url'] = str(uuid.uuid4())[:10] if custom_name == '' else custom_name
        print(request.data['long_url'])
        try:
            URLValidator(request.data['long_url'])
        except ValidationError:
            return Response('This url is invalid', status=status.HTTP_400_BAD_REQUEST)# Check if the initial url is valid

        if len(request.data['long_url']) > 250: # Check if the initial url has more than 250 symbols
            return Response("This url is longer than 250 symbols", status=status.HTTP_400_BAD_REQUEST)
        elif len(request.data['short_url']) > 10: # Check if the url of a premium member is above the maximum limit or not
            return Response('Your specified link is too long, please make it shorter', status=status.HTTP_400_BAD_REQUEST)
        elif len(request.data['short_url']) < 4: # Check if the url of a premium member is shorter than 24 symbols.
            return Response('Your specified link is too short, please make it longer', status=status.HTTP_400_BAD_REQUEST)
        

        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def redirect_to_url(request, url_short_name):
    short_url = get_object_or_404(Link, short_url=url_short_name)
    Link.visit_count_increment(short_url)
    
    return HttpResponseRedirect(short_url.long_url)
