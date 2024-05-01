from django.http import HttpResponse

def helloworldfunc(request):
    responseobject = HttpResponse('<h1>hello world</h1>')
    return responseobject