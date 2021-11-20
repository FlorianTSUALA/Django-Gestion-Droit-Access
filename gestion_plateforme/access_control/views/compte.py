from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from reservation.models import Compagnie
from dashboard.forms import CompagnieForm
# Create your views here.

def compagnie_metadata(key = None):

    model = 'compagnie'
    data = {
        'model': model,
        'genre': 'F',
        'url_create': model + '_create',
        'url_update': model + '_update',
        'url_delete': model + '_delete',
        'path_script': 'custom/js/entity.js',
        'path_table_body': 'partials/entity/table_body.html',
        'path_form_update': 'partials/entity/form_update.html',
        'path_form_create': 'partials/entity/form_create.html',
        'path_form_delete': 'partials/entity/form_delete.html',
    }
    genre = 'F'
    print(genre)
    data['title_modal_create'] = 'Creer ' +  ('une nouvelle', 'un nouveau')[ genre == 'F']  + f' {model}'

    if key is None:
        return data
    return data.get(key, '')

def compagnie(request):
    
    items = Compagnie.objects.all()
    
    html_data = compagnie_metadata()
    html_data['data'] = items
    html_data['url_create_full'] = reverse(html_data['url_create'])
    
    return render(request, 'compagnie.html', html_data)


def save_compagnie_form(request, form, template_name, template_data=None):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            items = Compagnie.objects.all()
            data['html_compagnie_list'] = render_to_string(compagnie_metadata('path_table_body'), { 'data': items })
        else:
            data['form_is_valid'] = False
    template_data['form'] = form
    data['html_form'] = render_to_string(template_name, template_data, request=request)
    return JsonResponse(data)

def compagnie_create(request):
    data = compagnie_metadata()
    
    print(data['title_modal_create'])
    if request.method == 'POST':
        form = CompagnieForm(request.POST)
    else:
        form = CompagnieForm()
    
    return save_compagnie_form(request, form, compagnie_metadata('path_form_create'), data)

def compagnie_update(request, pk):
    compagnie = get_object_or_404(Compagnie, pk=pk)
    if request.method == 'POST':
        form = CompagnieForm(request.POST, instance=compagnie)
    else:
        form = CompagnieForm(instance=compagnie)
    return save_compagnie_form(request, form, compagnie_metadata('path_form_update'))

def compagnie_delete(request, pk):
    compagnie = get_object_or_404(Compagnie, pk=pk)
    data = dict()
    if request.method == 'POST':
        compagnie.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        items = Compagnie.objects.all()
        data['html_compagnie_list'] = render_to_string(compagnie_metadata('path_table_body'), { 'data': items })
    else:
        context = {'compagnie': compagnie}
        data['html_form'] = render_to_string(compagnie_metadata('path_form_delete'), context, request=request, )
    return JsonResponse(data)
