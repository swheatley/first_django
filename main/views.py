from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, JsonResponse
from main.models import State, City, StateCapital
from main.forms import ContactForm, CityEditForm, CityEditForm
from django.template import RequestContext
from django.core.mail import send_mail
from django.conf import settings



#list views
#detail views
#create view
#edit view
#delete view
#make the view --> make the url

def ajax_search(request):
    context = {}
    return render_to_response('ajax_search.html', context, context_instance=RequestContext(request))


def json_response(request):
    search_string = request.GET.get('search', '')
    objects = State.objects.filter(name__icontains=search_string)

    object_list = []

    for obj in objects:
        object_list.append(obj.name)

    return JsonResponse(object_list, safe=False)


# STATE VIEWS:

def state_list(request):

    context = {}

    states = State.objects.all()

    context['states'] = states

    #template --> context dictionary --> context_instance variable
    return render_to_response('state_list.html', context, context_instance=RequestContext(request))

    

def state_search(request):

    context = {}

    context['request'] = request

    # context['get_vars'] = request.GET['a']

    #context['get_vars'] = request.GET.get('a', None)

    state = request.GET.get('state', None)

    #tate = request.POST.get('state', None)

    #states = State.objects.filter(name__icontains=state)


    print state
    if state != None:
        states = State.objects.filter(name__icontains=state)
    else:
        states = State.objects.all()

#    states.State.objects.all()

#    context['states'] = states
    print states
    context['states'] = states

    return render_to_response('state_search.html', context, context_instance=RequestContext(request))


def state_create(request):

    context = {}

    return render_to_response('state_create.html', context, context_instance=RequestContext(request))


def state_detail(request, pk):
    context = {}

    state = State.objects.get(pk=pk)
    
    context['state'] = state

    return render_to_response('state_detail.html', context, context_instance=RequestContext(request))


# #def state_edit(request):
#     context = {}

    return render_to_response('state_edit.html', context, context_instance=RequestContext(request))


def state_delete(request):
    context = {}

    return render_to_response('state_delete.html', context, context_instance=RequestContext(request))



#  CITY VIEWS:

def city_list(request):

    context = {}

    cities = City.objects.all()

    context['cities'] = cities

    return render_to_response('city_list.html', context, context_instance=RequestContext(request))   


def city_search(request):
    
    context = {}

    context['request'] = request

    city = request.GET.get('city', None)

    if city != None:
        cities = City.objects.filter(name__icontains=city)
    else:
        cities = City.objects.all() 

    context['cities'] = cities

    return render_to_response('city_search.html', context, context_instance=RequestContext(request))


def city_create(request):

    context = {}

    context['request'] = request.method

    context['states'] = State.objects.all()

    if request.method == "POST":
        name = request.GET.get('name', None)
        county = request.GET.get('county', None)
        latitude = request.GET.get('latitude', None)
        longitude = request.GET.get('longitude', None)
        state_id = request.POST.get('state', None)

        if state_id != None:
            state = State.objects.get(pk=state_id)
        else:
            state = State.objects.get(name="Texas")

        the_city, created = City.objects.get_or_create(name=name)

        the_city.county = county
        the_city.latitude = latitude
        the_city.longitude = longitude


        the_city.save()

        context['created'] = "Operation Successful"

    elif request.method == 'GET':
        pass

    return render_to_response('city_create.html', context, context_instance=RequestContext(request))


# #def city_create(request):

#     request_context = RequestContext(request)
#     context = { }

#     if request.method == 'POST':
#         form = CreateCityForm(request.POST)
#         context["form"] = form

#         if form.is_valid():
#             form.save()

#             context['valid'] = "is valid"
#             return render_to_response( "city_create.html", context, context_instance=request_context )

#         else:
#             context['valid'] = form.errors

#             return render_to_response( "city_create.html", context, context_instance=request_context )

#     else:
#         form = CreateCityForm()
#         context["form"] = form

#         return render_to_response( "city_create.html", context, context_instance=request_context )

def city_detail(request, pk):
    context = {}

    city = City.objects.get(pk=pk)

    context['city'] = city  

    return render_to_response('city_detail.html', context, context_instance=RequestContext(request))


def city_edit(request, pk):

    context = {}

    city = City.objects.get(pk=pk)

    form = CityEditForm(request.POST or None, instance=city)

    context['city'] = city

    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('/state_list')


    return render_to_response('city_edit.html', context, context_instance=RequestContext(request))


def city_delete(request):
    context = {}

    return render_to_response('city_delete.html', context, context_instance=RequestContext(request))



# STATE CAPITAL VIEWS:


def stateCapital_list(request):
    context = {}

    statecapitals = StateCapital.objects.all()

    context['statecapitals'] = statecapitals

    #template --> context dictionary --> context_instance variable
    return render_to_response('StateCapital_list.html', context, context_instance=RequestContext(request))


# # #def stateCapital_search(request):
# #   context = {}

#     return render_to_response('StateCapital_search.html', context, context_instance=RequestContext(request))



def stateCapital_detail(request, pk):

    context = {}

    state_capital = StateCapital.objects.get(pk=pk)

    context['statecapital'] = state_capital 

    return render_to_response('StateCapital_detail.html', context, context_instance=RequestContext(request))


def stateCapital_create(request):

    context = {}

    context['request'] = request.method

    context['stateCapital'] = StateCapital.objects.all()


    if request.method == "POST":
        name = request.GET.get('name', None)
        state_id = request.POST.get('state', None)

        if state_id != None:
            state = StateCapital.objects.get(pk=state_id)
        else:
            state = StateCapital.objects.get(name="Texas")

        the_capital, created = StateCapital.objects.get_or_create(name=name)
        the_capital.save()

        context['created'] = "Operation Successful"

    elif request.method == 'GET':
        pass


    return render_to_response('StateCapital_create.html', context, context_instance=RequestContext(request))


def stateCapital_edit(request):

    context = {}

    stateCapital = StateCapital.objects.get(pk=pk)

    form = StateCapitalEditForm(request.POST or None, instance=city)

    context['stateCapital'] = stateCapital

    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('/StateCapital_list')



    return render_to_response('StateCapital_edit.html', context, context_instance=RequestContext(request))

# CONTACT VIEW:

def contact_view(request):
    
    context = {}
    
    form = ContactForm()

    context['form'] = form

    if request.method == 'POST':
        form = ContactForm(request.POST)
        context['form'] = form
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            send_mail('STATES SITE MESSAGE FROM %s' % name,
                      message,
                      email,
                      [settings.EMAIL_HOST_USER],
                      fail_silently=False
                      )
            context['message'] = "email sent"
        else:
            context['message'] = form.errors
    elif request.method == 'GET':
        form = ContactForm()
        context['form'] = form

    return render_to_response('contact_view.html', context, context_instance=RequestContext(request))
  

#def get_post(request):

  #  get_state = request.GET.get('state', None)

  #  get_city = request.GET.get('city', None)

  # city_state_string = ""

   # states = State.object.filter(name__startswith="%s" % get_state)

   # for state in states:
        #cities = state.city_set.filter(name__startswith="%s" % get_city)

       # for city in cities:
        #    city_state_string+= "<b>%s</b> %s <br>" % (state, city.name)

            #response = city_state_string

            #return HttpResponse(response)
    #a = request.GET.get('a', None)
    #b = request.GET.get('b', None)
    
    #response = "a: %s, b: %s" % (a, b)

    

    #return HttpResponse(escape(response))

    #@csrf_exempt
    #def get_post(request):


