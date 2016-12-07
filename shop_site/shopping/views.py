# from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse

from .forms import RegisterForm, LoginForm,BankForm,BankDetail
#registering a user
from django.contrib.auth import authenticate,login,logout
from .models import Customer, Cart, BankDetail, Items
from django.contrib.auth.models import User


# Create your views here.


def index(request):
    return HttpResponse("<h1>working</h1>")


def car(request):
    return render(request, "shopping/car.html")


def laptop(request):
    laptop_names = request.POST.getlist('laptop')
    laptops_db_name = Items.objects.filter(item_type="Laptops")

    context = {"laptop_names": laptop_names, "laptops_db_name": laptops_db_name,}

    if context:
        for lappy in laptop_names:
            item = Cart()
            item.total = Items.objects.get(code=lappy).price
            item.name = lappy
            item.cart_cust = request.user
            item.save()
    return render(request, "shopping/laptop.html",context)


def men(request):
    return render(request, "shopping/men.html")


def mobile(request):
    mobile_names = request.POST.getlist('mobile')
    phones_db_name = Items.objects.filter(item_type="Phones")

    context = {"mobile_names":mobile_names,"phones_name":phones_db_name,}

    if context:
        for phones in mobile_names:
            item = Cart()
            item.total = Items.objects.get(code=phones).price
            item.name = phones
            item.cart_cust = request.user
            item.save()

    return render(request, "shopping/mobile1.html",context)


def netbank(request):
    return render(request, "shopping/netbank.html")


def register(request):  #registers and logges the user
    #user_id = request.POST.get('userId', '')
    if request.user.is_staff or request.user.is_superuser:
        raise Http404
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()   #user registered

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #albums = Customer.objects.filter(user=request.user)
                # saving bank details
                bank_detail_model = BankDetail()
                #bank_detail_model.id = request.user.id
                bank_detail_model.bank_cust = request.user
                bank_detail_model.name = request.user.first_name
                bank_detail_model.card_no = 0
                bank_detail_model.save()
                return render(request, 'shopping/mobile.html', {})

    context = {"form": form, }

    return render(request, "shopping/Register_form.html", context)


def watches(request):
    #return redirect(reverse('shopping:women'))  #works
    return redirect('shopping:women')
    #return render(request, "shopping/watches.html")


def women(request):
    return render(request, "shopping/women.html")


def welcome(request):
    return render(request, "shopping/welcome.html", {})


def logout_view(request):
    logout(request)
    return render(request,'shopping/welcome.html',{"msg":"you logged out"})


#authenticate the user and log them in
def auth_login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # albums = Album.objects.filter(user=request.user)
            return render(request, 'shopping/welcome.html', {'msg': username, })
        else:
            return render(request, 'shopping/login.html', {'msg': 'Your account has been disabled'})
    else:
        return render(request, 'shopping/car.html', {'msg': 'Invalid login'})


#url goes through it    see the base.html hyperlink
def logme(request):

    form = LoginForm(request.POST or None)
    return render(request, 'shopping/login.html', {"form":form,})


def profile(request):

    if not request.user.is_authenticated():
        raise Http404
    user = request.user
    form = BankForm(request.POST or None)
    instance = BankDetail.objects.get(bank_cust=request.user)
    bank = instance.card_no

    #showing cart details
    #if you want to recieve more than one object, use filter() instead of get()
    cart = Cart.objects.filter(cart_cust=request.user)
    total = 0
    for cart_items in cart:
        total = total + cart_items.total

    return render(request, 'shopping/profile.html', {"user":user, "form":form, "bank":bank, "cart":cart, "total":total})


def profile_edited(request):

    #get instance of BankDetail which has bank_cust=request.user... bank_cust is ForeignKey on User
    instance = BankDetail.objects.get(bank_cust=request.user)
    form = BankForm(request.POST or None, instance=instance)

    if form.is_valid():
        user = form.save(commit=False)
        name= request.POST.get('name', '')
        card_no = request.POST.get('card_no', '')
        user.save()
        bank = instance.card_no

        return render(request, 'shopping/profile.html', {"user":user, "form":form, "bank":bank})
    return render(request, 'shopping/car.html', {})


def delete_cart(request):
    cart = Cart.objects.filter(cart_cust=request.user)
    del_cart_items = request.POST.getlist('cartitems')

    if del_cart_items:
        for cart_items in del_cart_items:
            cart.filter(name=cart_items).delete()

    return render(request, 'shopping/profile.html', {})
    #return redirect('women')   #not working

def item_detail(request, item_type, item_code):
    try:
        product = Items.objects.get(code=item_code) # get() raise exception
    except Items.DoesNotExist:
        raise Http404("No MyModel matches the given query.")


    # define dictionary for item_type
    item_dict = {"mobile":"Phones",}

    try:
        phones_db_name = Items.objects.filter(item_type=item_dict[item_type])  # filter() doesnt raise exception but dictionary does
    except:
        raise Http404("fsfd.")

    #phones_db_name = Items.objects.filter(item_type=item_dict[item_type])
    if not len(phones_db_name):
        raise Http404("no requested item type found")

    context = {"product":product,"phone_db_name":phones_db_name,}

    return render(request,'shopping/item_details.html', context)


