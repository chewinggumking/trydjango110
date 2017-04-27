from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import KirrURL
# Create your views here.
def kirr_redirect_view(request,shortcode=None, *args, **kwargs):
    # obj = KirrURL.objects.get(shortcode=shortcode)
    # try:
    #     obj = KirrURL.objects.get(shortcode=shortcode)
    # except:
    #     obj = KirrURL.objects.all().first()
    obj_url = None
    qs = KirrURL.objects.filter(shortcode__iexact=shortcode)
    if qs.exists() and qs.count()==1:
        obj = qs.first()
        obj_url=obj.url
    return HttpResponse("Hello {sc}".format(sc=obj_url))



class KirrCBView(View):
    def get (self, request,shortcode=None, *args, **kwargs):
        print (shortcode)
        return HttpResponse("Hello CBV {sc}".format(sc=shortcode))
