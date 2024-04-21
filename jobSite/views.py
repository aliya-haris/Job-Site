from django.shortcuts import render
from requests import post
from .models import job_data
from jobList.settings import BASE_DIR
# Create your views here.

def index(request):
    jobs = job_data.objects.all()
    return render(request, 'index.html', {'jobs':jobs, 'BASE_DIR':BASE_DIR})
 

def admin1(request):
    if request.method == 'POST':
        job = job_data()
        job.job_name = request.POST.get("job_name", False)
        job.job_title = request.POST.get("job_title", False)
        job.job_desc = request.POST.get("job_desc", False)
        job.job_photo = request.FILES.get("job_photo", False)
        job.save()

    return render(request, 'upload.html')