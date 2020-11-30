from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views import View
import traceback


class ListProductView(View):
    template_name = "words/index.html"

    def get(self, request):
        context = {"products": {}}
        try:
            return render(request, self.template_name, context)

        except Exception as err:
            print(traceback.format_exc())
            return HttpResponseNotFound(
                '<h1>Failed to reder template [%s] </h1><br><p>%s</p><br><p>%s</p>' % (
                    self.template_name, err, traceback.format_exc()))
