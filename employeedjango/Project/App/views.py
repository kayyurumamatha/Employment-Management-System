from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import staff
from .forms import newstaffform,searchform,deleteform,updateform

def home(request):
    return render(request,'home.html')

def newstaff(request):
    if(request.method=='POST'):
        form=newstaffform(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponse('successfully added')
        else:
             return HttpResponse('check ur fields')
    form=newstaffform()
    return render(request,'newstaff.html',{'form':form})

def search(request):
    person = None
    if request.method == "GET":
        form = searchform(request.GET)
        if form.is_valid():
            sna= form.cleaned_data.get('name')
            sdep=form.cleaned_data.get('dept')
            if sna and sdep:
                try:
                    person = staff.objects.get(name=sna,dept=sdep)
                except staff.DoesNotExist:
                    return HttpResponse('No staff found with that ID')
            return render(request, 'search.html', {'form': form, 'res': person})
    else:
        form = searchform()
    
    return render(request, 'search.html', {'form': form})



def delete(request):
    if request.method == 'POST':
        form = deleteform(request.POST)
        if form.is_valid():
            sid = form.cleaned_data.get('staffid')
            try:
                obj = staff.objects.get(staffid=sid)
                obj.delete()
                return HttpResponse('Successfully deleted')
            except staff.DoesNotExist:
                return HttpResponse('No staff exists with that ID')
    else:
        form = deleteform()
    return render(request, 'delete.html', {'form': form})



def update(request):
    if(request.method=='POST'):
        form=updateform(request.POST)
        if(form.is_valid()):
            sid=form.cleaned_data.get('staffid')
            newmail=form.cleaned_data.get('emailid')
            newph=form.cleaned_data.get('mobno')
            obj=staff.objects(staff,staffid=sid)
            obj.emailid=newmail
            obj.mobno=newph
            obj.save()
            return HttpResponse('updates saved')
        else:
            return HttpResponse('check values')
    
    else:
         
         form=updateform()
    return render(request,'update.html',{'form':form})
def display(request):
    obj=staff.objects.all().order_by('staffid')
    return render(request,'display.html',{'sta':obj})



  

    

            
            
        
    



