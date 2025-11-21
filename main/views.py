from django.shortcuts import render,redirect,get_object_or_404
from .models import Product

def home(request):
    data={
        "products":Product.objects.filter(is_active=True)
    }
    return render(request,"index.html",context=data)

def create(request):
    if request.method=="POST":
        if request.POST.get("is_active"):
                is_active=True
        else:
            is_active=False
        Product.objects.create(
            is_active=is_active,
            title=request.POST.get("title"),
            price=request.POST.get("price"),
            image=request.FILES.get("image"),
            desc=request.POST.get("desc"),  
        )
        return redirect("home")
    
    return render(request,"create.html")

def detail(request,pk):
    product=get_object_or_404(Product,pk=pk)
    product={
        "product":product
    }
    return render(request,"detail.html",context=product)


def update(request,pk):
    product=get_object_or_404(Product,pk=pk)
    
    if request.method=="POST":
        if request.POST.get("is_active"):
            product.is_active=True
        else:
            product.is_active=False
            
        product.title=request.POST.get("title")
        product.price=request.POST.get("price")
        product.desc=request.POST.get("desc")
        product.image=request.FILES.get("image")
        product.save()
        return redirect("home")
        
    
    
    
    return render(request,"update.html",context={"product":product})
    
    
def delete(request,pk):
    product=get_object_or_404(Product,pk=pk)
    
    if request.method=="POST":
        product.delete()
        return redirect("home")
    
    return render(request,"delete.html",context={"product":product})
