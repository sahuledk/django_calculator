from django import forms

class OperationForm(forms.Form):
    num1=forms.CharField()
    num2=forms.CharField()

class CubeForm(forms.Form):
    num=forms.CharField()

class EbillForm(forms.Form):
    consumer_number=forms.CharField()
    email=forms.EmailField()
    date=forms.DateField()
    previous_reading=forms.CharField()
    current_reading=forms.CharField()

class DonationForm(forms.Form):
    Full_Name=forms.CharField()
    Email=forms.EmailField()
    Donation_Amount=forms.CharField()
    Credit_Card_Number=forms.CharField()
    First_Name=forms.CharField()
    Last_Name=forms.CharField()
    Security_Code=forms.CharField()
    Expiration_Date=forms.DateField()

class ParkingForm(forms.Form):
    Date=forms.DateField()
    Starting_Time=forms.TimeField()
    Vehicle_Number=forms.CharField()
    Phone_Number=forms.CharField()