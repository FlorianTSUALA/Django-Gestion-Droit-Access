from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from access_control.models import Gestionnaire
from access_control.forms import GestionnaireForm
from django.contrib.auth.decorators import login_required

def gestionnaire_metadata(key = None):

    model = 'gestionnaire'
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
    genre = 'M'
    data['title_modal_create'] = 'Creer ' +  ('une nouvelle', 'un nouveau')[ genre == 'F']  + f' {model}'

    if key is None:
        return data
    return data.get(key, '')

@login_required
def gestionnaire(request):
    items = Gestionnaire.objects.all()
    
    html_data = gestionnaire_metadata()
    html_data['data'] = items
    html_data['url_create_full'] = reverse(html_data['url_create'])
    
    return render(request, 'gestionnaire.html', html_data)

@login_required
def save_gestionnaire_form(request, form, template_name, template_data=None):
    data = gestionnaire_metadata()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            items = Gestionnaire.objects.all()
            data['html_gestionnaire_list'] = render_to_string(gestionnaire_metadata('path_table_body'), { 'data': items })
        else:
            data['form_is_valid'] = False
    template_data['form'] = form
    # html_data = gestionnaire_metadata()
    data['html_form'] = render_to_string(template_name, template_data, request=request)
    print("data", data)
    return JsonResponse(data)

@login_required
def gestionnaire_create(request):
    data = gestionnaire_metadata()
    
    print(data['title_modal_create'])
    if request.method == 'POST':
        form = GestionnaireForm(request.POST)
    else:
        form = GestionnaireForm()
    
    return save_gestionnaire_form(request, form, gestionnaire_metadata('path_form_create'), data)

@login_required
def gestionnaire_update(request, pk):
    gestionnaire = get_object_or_404(gestionnaire, pk=pk)
    if request.method == 'POST':
        form = GestionnaireForm(request.POST, instance=gestionnaire)
    else:
        form = GestionnaireForm(instance=gestionnaire)
    return save_gestionnaire_form(request, form, gestionnaire_metadata('path_form_update'))

@login_required
def gestionnaire_delete(request, pk):
    gestionnaire = get_object_or_404(gestionnaire, pk=pk)
    data = gestionnaire_metadata()
    if request.method == 'POST':
        gestionnaire.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        items = Gestionnaire.objects.all()
        data['html_gestionnaire_list'] = render_to_string(gestionnaire_metadata('path_table_body'), { 'data': items })
    else:
        context = {'gestionnaire': gestionnaire}
        data['html_form'] = render_to_string(gestionnaire_metadata('path_form_delete'), context, request=request, )
    return JsonResponse(data)
