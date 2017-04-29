from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item
from .forms import ItemForm
from django.shortcuts import render
from django.utils import timezone
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy

# Create your views here.
def index(request):
    latest_list = Item.objects.order_by('pub_date')
    context = {'latest_list': latest_list}
    return render(request, 'to_do/index.html', context)
    
def add(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            query = Item(item_content = content, pub_date = timezone.now())
            query.save()
            return HttpResponseRedirect('/to_do')
    else:
        form = ItemForm()
    return render(request, 'to_do/add.html', {'form':form})
    
class NoteDelete(DeleteView):
    model = Item
    success_url = reverse_lazy('index')
    template_name = 'to_do/delete.html'