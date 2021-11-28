from django.shortcuts import render
from MedicalApp.models import MedicalData
from MedicalApp import inserttodb,forms

# Create your views here.
def medicinedetails(request):
    e=MedicalData.objects.all()
    if not e:
        data=inserttodb.insertData()
        for i in data:
            MedicalData.objects.create(sku_id=i[0],
            product_id=i[1],
            sku_name=i[2],
            price=i[3],
            manufacturer_name=i[4],
            salt_name=i[5],
            drug_form=i[6],
            Pack_size=i[7],
            strength=i[8],
            product_banned_flag=i[9],
            unit=i[10],
            price_per_unit=i[11])

    return render(request,'MedicalApp/index.html',{'e':MedicalData.objects.all()})

def medicineName(request):
    form=forms.medNameForm()
    if request.method=="POST":
        form=forms.medNameForm(request.POST)
        if form.is_valid():
            med=form.cleaned_data['name']
            e=MedicalData.objects.filter(sku_name__icontains=med)
        return render(request,'MedicalApp/index.html',{'e':e})
    return render(request,'MedicalApp/medsearch.html',{'form':form})
