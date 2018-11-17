from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('sample/index.html')
    context = {
        'key': 'value',
    }
    return HttpResponse(template.render(context, request))