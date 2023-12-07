from django.shortcuts import render,get_object_or_404,redirect
from .models import Products,Event
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import ContactForm  # Import your contact form if you have one defined
from .models import ContactMessage
from django.contrib import messages
# Create your views here. # Import your contact form if you have one defined

def send_message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Create and save the message in the database
            ContactMessage.objects.create(subject=subject, message=message)
            
            # Add success message using Django's messages framework
            messages.success(request, 'Message saved successfully!')
            return redirect('home')  # Replace 'your_template' with your desired URL name or path
    
    form = ContactForm()
    return render(request, 'home.html', {'form': form})

def home(request):
    data=Products.objects.all()
    return render(request,'home.html',{'data':data})

def Create(request):
    if request.method=='POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        availability = request.POST.get('availability')
        obj=Products.objects.create(name=name,price=price,description=description,availability=availability)
        return redirect('home')
    return render(request,'create.html')


def Search(request):
    query=request.GET['query']
    data1=Products.objects.filter(name__icontains=query)
    data2=Products.objects.filter(description__icontains=query)
    data=data1.union(data2)
    if not data:  # Check if no products are found
        message = f"No products found for '{query}'."
        return render(request, 'search.html', {'message': message})
    return render(request,'search.html',{'data':data})

def Delete(request,id):
    data=Products.objects.get(id=id)
    data.delete()
    return redirect(home)

def Update(request,id):
    data=Products.objects.get(id=id)
    if request.method=="POST":
        data.name=request.POST['name']
        data.price=request.POST['price']
        data.description=request.POST['description']
        data.availability=request.POST['availability']
        data.save()
        return redirect('home')
    return render(request,'update.html',{'data':data})


def event_calendar(request):
    events = Event.objects.all()
    return render(request, 'event_calendar.html', {'events': events})

def event_details(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event_details.html', {'event': event})

def book_event(request, event_id):
    # Handle booking process for the selected event
    event = get_object_or_404(Event, pk=event_id)
    # Implement your booking logic here
    return render(request, 'booking_confirmation.html', {'event': event})

    