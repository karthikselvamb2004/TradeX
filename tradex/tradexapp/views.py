from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')
def adminhome(request):
    return render(request,'admin.html')

def userindex(request):
    return render(request,'userindex.html')
def regis(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        forms = LoginForm(request.POST)
        if form.is_valid() and forms.is_valid():
        
            a=forms.save(commit=False)
            a.user_type='user'
            a.save()

            b=form.save(commit=False)
            b.loginid=a
            b.save()
        
     
            messages.success(request, 'User data saved successfully!')
            return redirect('signin')
    else:
        form=UserForm()
        forms=LoginForm()
    return render(request,'signup.html',{'form':form,'forms':forms})
def tablecontent(request):
    users=user.objects.all()
    return render(request,'table.html',{'users':users})

def loginform(request):
    if request.method == 'POST':
        logform = LoginCheck(request.POST)
        if logform.is_valid():
            email = logform.cleaned_data['email']
            password = logform.cleaned_data['password']
            try:
                user_login = login.objects.get(email=email)
                
                if user_login.password == password:
                    # Check if the user exists in the 'user' table and is approved
                    try:
                        user_data = user.objects.get(loginid=user_login)
                        if user_data.status == 1:  # Only allow login if approved
                            if user_login.user_type == 'user':
                                request.session['user_id'] = user_login.id
                                return redirect('userindex')
                        else:
                            messages.error(request, 'Your account is not approved yet.')
                    except user.DoesNotExist:
                        messages.error(request, 'User profile not found.')
                else:
                    messages.error(request, 'Invalid password')
            except login.DoesNotExist:
                messages.error(request, 'User does not exist')
    else:
        logform = LoginCheck()
        
    return render(request, 'signin.html', {'loginform': logform})



def userprofile(request):
    id=request.session.get('user_id')
    print('id')
    log=login.objects.get(id=id)
    userv=user.objects.get(loginid=log)
    if request.method=='POST':
        form=UserForm(request.POST, instance=userv)
        loginform=LoginForm(request.POST, instance=log)
        if form.is_valid() and loginform.is_valid():
            form.save()
            loginform.save()
            return redirect('userindex')
    else:
        form=UserForm(instance=userv)
        loginform=LoginForm(instance=log)
    return render(request,'userprofile.html',{'form':form,'loginform':loginform}) 

def datatable(request):
    users=user.objects.all()
    return render(request,'datatable.html',{'users':users})

def news_list(request):
    news = StockMarketNews.objects.all().order_by('-published_at')
    return render(request, 'news_list.html', {'news': news})

def add_news(request):
    if request.method == 'POST':
        form = StockMarketNewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = StockMarketNewsForm()
    return render(request, 'add_news.html', {'form': form})

def delete_news(request, news_id):
    news_item = get_object_or_404(StockMarketNews, id=news_id)
    news_item.delete()
    return redirect('news_list')

def edit_news(request, news_id):
    news_item = get_object_or_404(StockMarketNews, id=news_id)
    
    if request.method == "POST":
        form = StockMarketNewsForm(request.POST, instance=news_item)
        if form.is_valid():
            form.save()
            return redirect("news_list")  # Redirect to the news list page

    else:
        form = StockMarketNewsForm(instance=news_item)

    return render(request, "edit_news.html", {"form": form, "news_item": news_item})

def user_news_view(request):
    news = StockMarketNews.objects.all().order_by('-published_at')  # Fetch latest news
    return render(request, "user_news.html", {"news": news})


def approve_user(request,id):
    data = get_object_or_404(user, id=id)
    data.status=1
    data.save()
    return redirect('datatable')
def unapprove_user(request, id):
    data = get_object_or_404(user, id=id)
    data.status = 0  # Set status to 0 (Unapproved)
    data.save()
    return redirect('datatable')

def profile(request):
    return render(request,'profile.html')

def community(request):
    return render(request,'k.html')

def chat(request):
    return render(request,'chat.html')















        