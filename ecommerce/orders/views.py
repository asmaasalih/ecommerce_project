from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .forms import OrderCreateForm
from .models import OrderItem,order
from cart.cart import Cart


# Create your views here.
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
				order=order,
				product=item['product'],
				price=item['price'],
				quantity=item['quantity'])
            cart.clear()
            context = {
                'order':order,
            }
            request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))

    else:
        form = OrderCreateForm()
    context = {
        'cart':cart,
        'form':form,
    }
    return render(request,'order/create.html',context)              
