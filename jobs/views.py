from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import JobForm, NoteForm

def jobs(request, pk):
  company = request.GET.get("company")
  role = request.GET.get("role")
  status = request.GET.get("status")
  jobs = Job.objects.all().order_by("-date_applied")
  if company:
    jobs = jobs.filter(company=company)
  if role:
    jobs = jobs.filter(role=role)
  if status:
    jobs = jobs.filter(status=status)
  context = {"jobs": jobs, "count": jobs.count()}
  return render(request, "jobs/jobs.html", context)

def job(request, pk):
  job = Job.objects.get(id=pk)
  notes = job.note_set.all().order_by("-date_created")
  context = {"jobs": [job], "count": 1 if job else 0, "notesFlag": True, "notes": notes}
  return render(request, "jobs/jobs.html", context)

def createJob(request):
  form = JobForm()
  if(request.method.upper() == "POST"):
    form = JobForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("jobs")
  context = {"form": form}
  return render(request, "jobs/form.html", context)

def updateJob(request, pk):
  job = Job.objects.get(id=pk)
  form = JobForm(instance=job)
  if request.method.upper() == "POST":
    form = JobForm(request.POST, instance=job)
    if form.is_valid():
      form.save()
      return redirect(f'/jobs/{pk}')
  context = {"form": form}
  return render(request, "jobs/form.html", context)

def deleteJob(request, pk):
  job = Job.objects.get(id=pk)
  if request.method.upper() == "POST":
    job.delete()
    return redirect("jobs")
  context = {"job": job}
  return render(request, "jobs/deleteJob.html", context)
  
def createNote(request, jobId, noteId):
    form = None
    if noteId != None:
      note = Note.objects.get(id=noteId)
      form = NoteForm(instance=note)
    else:
      job = Job.objects.get(id=jobId)
      form = NoteForm(initial={'job': job})
    if request.method.upper() == "POST":
      form = NoteForm(request.POST)
      if noteId != None:
        form.instance = Note.objects.get(id=noteId)
      if form.is_valid():
        form.save()
        return redirect(f'/jobs/{jobId}')
    context = {"form": form}
    return render(request, "jobs/form.html", context)

def deleteNote(request, pk):
  note = Note.objects.get(id=pk)
  if request.method.upper() == "POST":
    note.delete()
    return redirect(f'/jobs/{note.job.id}')
  context = {"note": note}
  return render(request, "jobs/deleteNote.html", context)