from django.http import HttpResponse
from django.template import loader

from .models import Paper


def index(request):
    return HttpResponse("Hello, world!")



def list_index(request):
    latest_paper_list = Paper.objects.order_by('-pub_dater')[:5]
    template = loader.get_template('approval/index.html')

    context = {
        'latest_paper_list' : latest_paper_list,
    }
    return HttpResponse(template.render(context, request))