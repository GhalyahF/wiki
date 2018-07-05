from django.shortcuts import render, get_object_or_404
from .models import Page

# Create your views here.
def list(request):
	context={
			"pages": Page.objects.all(),
	}
	return render (request,'list.html',context)

def detail(request,page_id):
	context={
			"page": Page.objects.get(id=page_id),

	}
	return render (request,'detail.html',context)



