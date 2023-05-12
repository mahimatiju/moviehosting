from django.shortcuts import render ,redirect
from .models import Movie
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from. forms import movieform

def add(request):
    a = Movie.objects.all()
    return render(request, 'movie.html',{'a':a})

def detail(request, movie_id):
        movie = Movie.objects.get(id= movie_id)
        return render(request, 'detail.html',{'o':movie})

def add_movies(request):
    if request.method == "POST":
        img = request.FILES['image']
        name = request.POST.get("name",)
        year = request.POST.get("year", )
        discription = request.POST.get("details", )
        m = Movie(image=img, discription=discription, year=year, name=name) 
        m.save()
        return redirect('demo_app:mem')
    return render(request, "add.html") 
    
def update(request, id):
    c = Movie.objects.get(id=id)
    form = movieform(request.POST or None, request.FILES, instance=c)
    if form.is_valid():
        form.save()
        return redirect('demo_app:mem')
    else:
        form = movieform(instance=c)
    return render(request, "update.html", {'form': form})


def delete(request, id):
    if request.method == 'POST':
        d = Movie.objects.get(id=id)
        d.delete()
        return redirect('demo_app:mem')
    else:
        return render(request, "delete.html")
        

class MOVIEListView(ListView):
    model = Movie
    template_name = "movie.html"
    context_object_name ="a"
    

class MOVIEdetailView(DetailView):
    model = Movie
    template_name = "detail.html"
    context_object_name ="o"

class MOVIEupdatelView(UpdateView):
    model = Movie
    template_name = "edit.html"
    context_object_name ="form"
    fields = ['name', 'discription', 'year', 'image']
    
    def get_success_url(self):
        return reverse_lazy('demo_app:cbvdetails', kwargs={"pk":self.object.id})

class MOVIEdeleteView(DeleteView):
    model = Movie
    template_name = "delete.html"
    sucesss_url = reverse_lazy('demo_app:cbvhome')
