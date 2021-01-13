# django imports
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
# restricts page if not logged in
from django.contrib.auth.decorators import login_required

# Class imports
from .filters import OrderFilter, ProductFilter
from .models import *
from .forms import OrderForm, createUserForm, CustomerForm
from .decorators import unauth_user, allowed_users, admin_only


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders = request.user.customer.order_set.all()

    total_orders = orders.count()

    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {'orders': orders,
               'total_orders': total_orders,
               'delivered': delivered, 'pending': pending}
    return render(request, 'account/user.html', context)


def logoutuser(request):
    logout(request)
    return redirect('login')


@unauth_user
def resgisterPage(request):
    form = createUserForm()
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, 'Account has been created for' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'account/register.html', context)


@unauth_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username OR password is Incorrect')
    context = {}
    return render(request, 'account/login.html', context)


@login_required(login_url='login')
@admin_only
def home(request):
    orders = Order.objects.all()  # returns all orders
    customers = Customer.objects.all()  # returns all customers
    total_customers = customers.count()
    total_orders = orders.count()

    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders,
               'customers': customers,
               'total_customers': total_customers,
               'total_orders': total_orders,
               'delivered': delivered, 'pending': pending}
    return render(request, 'account/home.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    product = Product.objects.all()
    myFilter_p = ProductFilter(request.GET, queryset=product)
    product = myFilter_p.qs

    context = {'products': product, 'filter': myFilter_p}
    return render(request, 'account/products.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):

    customer = Customer.objects.get(id=pk)
    # return all orders related to a customer ID
    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'customer': customer,
               'orders': orders, 'order_count': order_count, 'myFilter': myFilter}
    return render(request, 'account/customer.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request, pk):
    orderFormSet = inlineformset_factory(
        Customer, Order, fields=('product', 'status'), extra=5)  # (Parent, Child) ; # make this dynamic
    customer = Customer.objects.get(id=pk)
    formset = orderFormSet(queryset=Order.objects.none(), instance=customer)

    if request.method == 'POST':
        formset = orderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset': formset, 'customer': customer}

    return render(request, 'account/orderform.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        # senidng new data into a pre exisitng field.
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()  # save the form into the database
            return redirect('/')  # redirect to home page

    context = {'formset': form}
    return render(request, 'account/orderform.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)  # returns order with specific id

    if request.method == 'POST':
        order.delete()
        return redirect('/')  # redirect to

    context = {'item': order}
    return render(request, 'account/delete.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def account_settings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()  # save the form into the database
            return redirect('/')

    context = {'form': form}
    return render(request, 'account/user_account.html', context)
