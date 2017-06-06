from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseRedirect
import json
from .models import Image

# Create your views here.

def index(request):
    '''
    图片上传
    :param request:
    :return:
    '''
    return render(request, 'picture/index.html')

def upload(request):
    '''
    图片上传
    :param request:
    :return:
    '''
    if len(request.FILES) == 0:
        raise Exception('无上传文件')
    file_obj = request.FILES.get('file_upload', None)
    img = Image(name=file_obj.name, size=file_obj.size, extension=file_obj.name.split('.')[-1], img=file_obj)
    img.content_type = request.content_type
    img.host = request.get_host()
    img.save()
    res = {
        'code': 200,
        'content': {
            'name': img.img.name,
            'path': img.img.path,
            'url': img.img.url
        }
    }
    return HttpResponse(json.dumps(res), content_type="application/json")
