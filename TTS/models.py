from django.db import models


# Create your models here.
class TextSpeech(models.Model):
	text = models.CharField(max_length=20000)
	language = models.CharField(max_length=10)
	filename = models.CharField(max_length=10)

	def __unicode__(self):
		return self.text
