from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import KirrURL
# Create your views here.


class HomeView(View):
    def get (self, request, *args, **kwargs):
        return render (request, "shortener/home.html", {})

    def post (self, request, *args, **kwargs):
        some_dict = {}
        # some_dict['url']
        some_dict.get('url', 'http>//joincfe.com')
        print (request.POST)
        print (request.POST.get("url"))
        return render (request, "shortener/home.html", {})

class KirrCBView(View):
    def get (self, request,shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)

    def post (self, request, *args, **kwargs):
        return HttpResponse()

'''
def kirr_redirect_view(request,shortcode=None, *args, **kwargs):
    # obj = KirrURL.objects.get(shortcode=shortcode)
    # try:
    #     obj = KirrURL.objects.get(shortcode=shortcode)
    # except:
    #     obj = KirrURL.objects.all().first()
    obj = get_object_or_404(KirrURL, shortcode=shortcode)

    # qs = KirrURL.objects.filter(shortcode__iexact=shortcode)
    # if qs.exists() and qs.count()==1:
    #     obj = qs.first()
    #     obj_url=obj.url
    return HttpResponse("Hello {sc}".format(sc=obj.url))

def kirr_redirect_view(request,shortcode=None, *args, **kwargs):
    print (shortcode)
    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    print(obj.shortcode)
    return HttpResponseRedirect(obj.url)

 '''
