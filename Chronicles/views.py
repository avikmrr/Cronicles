from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.encoding import smart_str
import os


def Dashboard(request):
    return render(request, 'index.html', {})


def downloadcv(request):
    print "Hello"
    file = open(settings.BASE_DIR + "/static/resume.docx").read()
    response = HttpResponse(file, content_type='application/x-itunes-ipa')
    response['Content-Disposition'] = 'attachment; filename=' + "Avinash(Resume).docx"
    return response

