from django.shortcuts import render,redirect
from .models import Restaurant,Place,Event
from django.views.generic import ListView
from django.views.generic import DetailView , CreateView
from .Forms import search


from django.db.models import Q
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = search(request.POST)
        if form.is_valid():
            ville = form.cleaned_data['ville']
            cat = form.cleaned_data['categorie']

            if cat==1:
                rests = Restaurant.objects.all().filter(ville__icontains=ville)
                print(rests)
                return render(request, 'Restaurant.html', {'rests': rests})
            elif cat==2:
                places = Place.objects.all().filter(ville__icontains=ville)
                return render(request, 'Place.html', {'places': places})
            else:
                events = Event.objects.all().filter(ville__icontains=ville)
                return render(request, 'event.html', {'events': events})
    context = {
        'Restaurant': Restaurant.objects.all(),
        'form':search
    }
    return render(request,'index.html',context)










class RestaurantListView(ListView):
    model = Restaurant
    context_object_name = 'rests'
    template_name = 'Restaurant.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(ville__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list

class RestaurantDetail(DetailView):
    model = Restaurant
    template_name = 'Restau.html'




class PlacecListView(ListView):
    model = Place
    context_object_name = 'places'
    template_name = 'Place.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(ville__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list

class PlaceDetail(DetailView):
    model = Place
    template_name = 'Place.html'





class EventListView(ListView):
    model = Event
    template_name = 'event.html'
    context_object_name = 'events'
    ordering = ['price']

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(ville__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list



class EventDetail(DetailView):
    model = Event
    template_name = 'eve.html'
