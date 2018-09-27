# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# -*- coding: utf_8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.encoding import smart_str
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import resolve_url
from django.template.response import TemplateResponse
from django.utils.deprecation import RemovedInDjango20Warning
from django.utils.translation import ugettext as _
import warnings
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests
from config import *
from googleplay import GooglePlayAPI
from helpers import sizeof_fmt
import os
from forms import UploadApkViaUrlForm


# Create your views here.
def download_apk_via_url(apk):
    GOOGLE_LOGIN = "digital.sec.devs@gmail.com"
    GOOGLE_PASSWORD = "dev@6395"
    AUTH_TOKEN = "aAX_7XGsaT4B5hIDvtdh8oM-R7B5iidTCgHxXOKQXXFDFdmdzPcXKslTr6SX0YpiDMIORA."
    f = 0
    head, sep, tail = apk.partition('&')
    apk = head
    msg = ""
    if "." in apk:
        if (apk.startswith('http')):
            if "play.google.com/store/apps/details?id=" in apk:
                print "Link:" + apk
                link, packagename = apk.split("=")
            else:
                message = "Wrong URL!"
                return message
        else:
            packagename = apk
    else:
        message = "Invalid Package Name"
        return message

    if (len(sys.argv) == 3):
        filename = sys.argv[2]
    else:
        filename = packagename + ".apk"
    print ("Package Name: " + packagename)
    # Connect
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    api = GooglePlayAPI(ANDROID_ID)
    api.login(GOOGLE_LOGIN, GOOGLE_PASSWORD, AUTH_TOKEN)
    try:
        # Get the version code and the offer type from the app details
        m = api.details(packagename)
        doc = m.docV2
        vc = doc.details.appDetails.versionCode
        ot = doc.offer[0].offerType
        size = sizeof_fmt(doc.details.appDetails.installationSize)
        l = len(size)
        ext = size[(l-2):l]
        size = size[:-2]
        if ext == "MB":
            f = float(size)
        if ext == "GB":
            f =float(size) * 1024
        if f > float(200):
            message = "App Size is Greater than 200MB. Please Enter a Different URL or Package Name"
            return message

        # Download
        print "Downloading %s..." % sizeof_fmt(doc.details.appDetails.installationSize),
        data, msg = api.download(packagename, vc, ot)
        DIR = settings.BASE_DIR
        ANAL_DIR = os.path.join(DIR)
        fullpath = ANAL_DIR+'/uploads/'+packagename + ".apk"
        open(fullpath, "wb").write(data)
        print "APK Downloaded!"
        return fullpath

    except Exception as e:
        print "Not able to fetch the apk: {}".format(e)
        if "Google Play purchases are not supported in your country" in msg:
            message = """App region isn't supported by the platform."""
        elif "does not support this purchase." in msg:
            message = """The platform doesn't support paid app download."""
        else:
            message = "Sorry! We are not able to fetch the APK at this moment. Please upload the APK."
        return message

def upload_apk_via_url(request):
    try:
        if request.method == 'POST':
            form = UploadApkViaUrlForm(request.POST)
            if form.is_valid():
                url = request.POST.get("url", "")
                filename = download_apk_via_url(url)
                fullpath = filename
                DIR = settings.BASE_DIR
                ANAL_DIR = os.path.join(DIR)
                URL = "file://" + filename
                if URL:
                    import pdb
                    pdb.set_trace()
                    file = open(filename).read()
                    response = HttpResponse(file, content_type='application/vnd.android.package-archive')
                    response['Content-Disposition'] = 'attachment; filename=' + filename
                    return response
                mime = MimeTypes()
                mime_type = mime.guess_type(URL, strict=True)
                path = urlparse.urlsplit(URL).path
                filename = posixpath.basename(path)
                if fullpath == """App region isn't supported by the platform.""":
                    return render(request, 'gpapi.html',
                                  {'filename': fullpath})
                if fullpath == """The platform doesn't support paid app download.""":
                    return render(request, 'gpapi.html',
                                  {'filename': fullpath})
                if fullpath == "Invalid Package Name":
                    return render(request, 'gpapi.html',
                                  {'filename': fullpath})
                if fullpath == "App Size is Greater than 200MB. Please Enter a Different URL or Package Name":
                    return render(request, 'gpapi.html',
                                  {'filename': fullpath})
                if fullpath == "Wrong URL!" or "Sorry!" in fullpath:
                    return render(request, 'gpapi.html',
                                  {'filename': fullpath})


    except Exception, e:
        return HttpResponseRedirect('/GooglePlay')


def GooglePlay(request):
    return render(request, 'gpapi.html',{})