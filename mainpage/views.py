from django.shortcuts import render,HttpResponse
from . SVM import getStrength
# from getStrength import testingSaala,parseData,realGame
# Create your views here.
def enterpass(request):
	if request.method=='POST':
		enterpassword=request.POST.get('password')
		getStrength.testingSaala(enterpassword)
		predicted=getStrength.realGame()
		noOfTrains=predicted[1]
		predicted=predicted[0]
		print(predicted)
		return render(request,'indexfinal.html',{'predicted':predicted,'value':enterpassword,'noOfTrains':noOfTrains})
	else:
		return render(request,'index.html')