from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from main.models import State, City, StateCapital
from django.template import RequestContext

#list views
#detail views
#create view
#edit view
#delete view
#make the view --> make the url


def city_create(request):

    request_context = RequestContext(request)
    context = { }

    if request.method == 'POST':
        form = CreateCityForm(request.POST)
        context["form"] = form

        if form.is_valid():
            form.save()

            context['valid'] = "is valid"
            return render_to_response( "city_create.html", context, context_instance=request_context )

        else:
            context['valid'] = form.errors

            return render_to_response( "city_create.html", context, context_instance=request_context )

    else:
        form = CreateCityForm()
        context["form"] = form

        return render_to_response( "city_create.html", context, context_instance=request_context )


def city_search(request):

        request_context = RequestContext(request)

        context ={}

            if request.method == 'POST':
                form = CitySearchForm(request.POST)
                context['form'] = form

            if form.is_valid():
                name =  "%s" %
        form.cleaned_data['name'] state = form.cleaned_data['state']

        context['city_list'] = City.objects.filter(name__startswith=name, state__name__startswith=state)

                context['valid'] = "is valid"
                    return render_to_response( "city_search.html", context, context_instance=request_context )

                else:
                    context['valid'] = form.errors



                return render_to_response( "city_search.html", context, context_instance=request_context )

            else:
                form = CitySearchForm()
                context["form"] = form

                return render_to_response( "city_search.html", context, context_instance=request_context )

def state_list(request):

    context = {}

    states = State.objects.all()

    context['states'] = states

    #template --> context dictionary --> context_instance variable
    return render_to_response('state_list.html', context, context_instance=RequestContext(request))

    



def state_detail(request, pk):
    context = {}

    state = State.objects.get(pk=pk)

    context['state'] = state

    return render_to_response('state_detail.html', context, context_instance=RequestContext(request))





def state_search(request):

    context = {}

    context['request'] = request

    # context['get_vars'] = request.GET['a']

    #context['get_vars'] = request.GET.get('a', None)

    state = request.GET.get('state', None)

    #tate = request.POST.get('state', None)

    #states = State.objects.filter(name__icontains=state)



    if state != None:
        states = State.objects.filter(name__icontains=state)
    else:
        states = State.objects.all()

#    states.State.objects.all()

#    context['states'] = states

    context['state'] = states

    return render_to_response('state_search.html', context, context_instance=RequestContext(request))


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


def city_detail(request, pk):
    context = {}

    city = City.objects.get(pk=pk)

    context['crazy_steve'] = city  

    return render_to_response('city_detail.html', context, context_instance=RequestContext(request))


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



def stateCapital_detail(request, pk):

    context = {}

    state_capital = StateCapital.objects.get(pk=pk)

    context['stateCapital'] = state_capital 

    return render_to_response('stateCapital_detail.html', context, context_instance=RequestContext(request))

    

#def state_search(request):

#    context = {}
 #   context =['request']= request

    #var1 = '%s' % dir(request)
 #   var1=str(request)

#    string="<pre>%s %s</pre>" %(request.GET, request.POST)

 #   return HttpResponse(string)   

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


