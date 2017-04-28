from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import KirrURL
from .forms import SubmitUrlForm
# Create your views here.


class HomeView(View):
    def get (self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title" : "KIRR.CO",
            "form" : the_form,

        }
        return render (request, "shortener/home.html", context)

    def post (self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "form" : form,
            "title" : "KIRR.CO",

        }
        template = "shortener/home.html"
        if form.is_valid():
            print (form.cleaned_data)
            new_url = form.cleaned_data.get("url")
            obj, created = KirrURL.objects.get_or_create(url=new_url)
            print (created)
            new_context = {
                "object" : obj,
                "created" : created
            }
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already_exists.html"


        return render (request, template, new_context)

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
