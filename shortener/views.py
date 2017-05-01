from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import KirrURL
from .forms import SubmitUrlForm

from analytics.models import ClickEvent
# Create your views here.


class HomeView(View):
    def get (self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        bg_image = ""
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
            new_url = form.cleaned_data.get("url")
            obj, created = KirrURL.objects.get_or_create(url=new_url)
            context = {
                "object" : obj,
                "created" : created
            }
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already_exists.html"


        return render (request, template, context)

class URLRedirectView(View):
    def get (self, request, shortcode=None, *args, **kwargs):
        print ("REQUEST= ", request)
        qs = KirrURL.objects.filter(shortcode__iexact=shortcode)
        if qs.count()!=1 and not qs.exists():
            raise Http404
        obj = qs.first()
        return HttpResponseRedirect(obj.url)




    def post (self, request, *args, **kwargs):
        return HttpResponse()
