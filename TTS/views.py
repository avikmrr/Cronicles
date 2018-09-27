from django.shortcuts import render
from django.http import HttpResponse
from gtts import gTTS
from django.conf import settings
from django.utils.encoding import smart_str
import os


def gtts(request):
    if request.method == "POST":
        txt = request.POST.get("text", "")
        lang = request.POST.get("language", "")
        filename = request.POST.get("filename", "")
        tts = gTTS(text=txt, lang=lang)
        str1 = filename + ".mp3"
        str2 = settings.BASE_DIR
        tts.save(str1)
        file = open(str2 + "/" + str1, "rb").read()
        response = HttpResponse(file, content_type='audio/mpeg')
        response['Content-Disposition'] = 'attachment; filename=' + str1
        # response.write(tts.save(str1))
        return response
    else:
        return render(request, 'tts.html', {})
