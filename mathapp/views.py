from django.shortcuts import render
from mathapp.forms import OperationForm,CubeForm,EbillForm,DonationForm,ParkingForm
from django.views.generic import View

# Create your views here.
class AddView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,'add.html',{'form':form})
    def post(self,request):
        print(request.POST)
        num1 = request.POST["num1"]
        num2 = request.POST["num2"]
        res = (int(num1) + int(num2))
        return render(request, 'add.html', {'result': res})
def add(request):
    if request.method=="GET":
        form=OperationForm()
        return render(request,'add.html',{'form':form})
    else:
        print(request.POST)
        num1=request.POST["num1"]
        num2=request.POST["num2"]
        res=(int(num1)+int(num2))
        return render(request,'add.html',{'result':res})

class SubView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,'sub.html',{'form':form})
    def post(self,request):
        print(request.POST)
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        res = (int(num1) - int(num2))
        return render(request, 'sub.html', {'result': res})
def sub(request):
    if request.method=="GET":
        form=OperationForm()
        return render(request,'sub.html',{'form':form})
    else:
        print(request.POST)
        num1=request.POST['num1']
        num2=request.POST['num2']
        res=(int(num1)-int(num2))
        return render(request,'sub.html',{'result':res})
def mul(request):
    if request.method=="GET":
        form=OperationForm()
        return render(request,'mul.html',{'form':form})
    else:
        print(request.POST)
        num1=request.POST['num1']
        num2=request.POST['num2']
        res=(int(num1)*int(num2))
        return render(request,'mul.html',{'result':res})
def divi(request):
    if request.method == "GET":
        form = OperationForm()
        return render(request, 'mul.html', {'form': form})
    else:
        print(request.POST)
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        res = (int(num1) / int(num2))
        return render(request, 'mul.html', {'result': res})

def cube(request):
    if request.method=="GET":
        form=CubeForm()
        return render(request,'cube.html',{'form':form})
def square(request):
    if request.method=='GET':
        form=CubeForm()
        return render(request,'square.html',{'form':form})

def home(request):
    return render(request,'home.html')

def ebill(request):
    form=EbillForm()
    return render(request,'ebill.html',{'form':form})

def donation(request):
    form=DonationForm()
    return render(request,'donation.html',{'form':form})

def parking(request):
    if request.method=='GET':
        form=ParkingForm()
        return render(request,'parking.html',{'form':form})
    else:
        print(request.POST)
        form=ParkingForm()
        return render(request,'parking.html',{'form':form})
