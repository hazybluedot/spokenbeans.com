from django.shortcuts import render_to_response
from SnB.records.models import Subscription, Order
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date, timedelta
from SnB.invoice.orders import OrderForm
from SnB.coffee.models import Origin
from django.template import RequestContext, loader
# Create your views here.

def current_roast_order(request):
    subscriptions = active_subscriptions(request)
    order_list = roast_orders(request)
    return render_to_response('records/current_roast_order.html', {'active_subscriptions_list': subscriptions, 'upcoming_orders_list': order_list})

def active_subscriptions(request):
    active_subscriptions_list = Subscription.objects.filter(status='A')
    return active_subscriptions_list


def roast_orders(request):
    next_delivery_date = get_next_delivery_date()
    orders_list = Order.objects.filter(date_fulfilled__exact=None)
    orders_list = orders_list.filter(date_placed__lte=next_delivery_date)
    return orders_list

def get_next_delivery_date():
    delivery_date = date.today()
    one_day = timedelta(days=1)
    while (delivery_date.weekday() != 6): # find next Sunday starting from today
        delivery_data = delivery_date + one_day

    return delivery_date

def thanks(request):
    # TODO: check that this was the result of a order, if not redirect to order form.
    c = { 'order': None }
    return render_to_response('thanks.html', c)

def order_form(request):
    origin_list = Origin.objects.all()
    if request.method == 'POST': # if the form has been submitted
        form = OrderForm(request.POST) # a form bound to the post data
        if form.is_valid(): # all validation rules pass
            #process data in form.cleaned_data
            name = form.cleaned_data['name']
            subject = "New Order from %s" % name
            amount = form.cleaned_data['amount']
            origin = form.cleaned_data['origin']
            roast = form.cleaned_data['roast']
            frequency = form.cleaned_data['frequency']
            address = form.cleaned_data['address']
            cycles = form.cleaned_data['cycles']
            sender = form.cleaned_data['email']
            notes = form.cleaned_data['notes'] 
            office = form.cleaned_data['office']
            message = """
Name: %s
Address: %s
Office: %s
Cycles: %s
Frequency: %s
Amount: %s
Roast: %s
Origin: %s
Notes: %s
""" % (name, address, office, cycles, frequency, amount, roast, origin, notes)

            recipients = ['orders@spokenbeans.com']
            from django.core.mail import send_mail
            send_mail(subject, message, sender, recipients)

            return HttpResponseRedirect('/thanks.html') #redirect after POST

    else:
        form = OrderForm(initial={'cycles': '1', 'delivery_day': '1'}) # an unbound form

    from django.core.context_processors import csrf
    #t = loader.get_template('records/order_form.html')
    #c = RequestContext(request, {'form': form})
    #return HttpResponse(t.render(c))
    c = {'form': form, 'origin_list': origin_list}
    c.update(csrf(request))
    return render_to_response('records/order_form.html', c)
    #return render_to_response('records/order_form.html',
    #                           locals(),
    #                           context_instance=RequestContext(request))
    #return render_to_response('records/order_form.html', {'form': form })
