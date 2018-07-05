from django.db import models
from django.urls import reverse

# Create your models here.
class Page(models.Model):
	title= models.CharField(max_length=200)
	content= models.TextField()
	last_update= models.DateTimeField(auto_now_add= True)

	def __str__(self):
		return self.title

	def absolute_url_view(request):
		return reverse('pages.views.details', args=str[(self.id)])


