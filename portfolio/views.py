from django.shortcuts import render
from .models import Portfolio


# Create your views here.
#모든객체내용을 portfolio html에 띄워주세요!
def portfolio(request):
    portfolios = Portfolio.objects
    return render(request,'portfolio/portfolio.html',{'portfolios':portfolios})
