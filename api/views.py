from django.http import HttpResponse,JsonResponse
import datetime



def homepage(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    friends = [
        'mihir', 'not mihir', 'also not mihir',
    ]
    return JsonResponse(friends,safe=False)