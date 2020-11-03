from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Item


# Create your views here.
def index(request):
    print("********")
    print(Item.objects.all())
    print("********")

    context = {
        "allItems": Item.objects.all()
    }

    return render(request, "items.html", context)


def createItem(request):
    #this is the post request function that handles the information from the form and has access to info from the form with the keyword "request.POST"
    print("THE THANGGG BELOW IS REQUEST.POST")
    print(request.POST) # REQUEST.POST IS A DICTIONARY
    # <QueryDict: {'csrfmiddlewaretoken': ['BbqhOX3x9BsypJ6U5Z1JsYQsOmIrk7TfzK8kOHbogkv7sQRQSazaAmGUbuTnwXsN'], 'itemName': ['macbook'], 'itemDescription': ['to avoid getting annoying windows issuess']}>
    # ClassName.objects.create(field1="value for field1", field2="value for field2", etc.)

    #sending the information from the form (request.post) to the validator in models so that the validatoer can tell us if its filld out based on a certain criteria
    errors = Item.objects.itemValidator(request.POST)
    
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")

    else:
        newItem = Item.objects.create(name = request.POST['itemName'], desc = request.POST['itemDescription'])


    #ALWAYS REDIRECT ON A POST REQUEST
    return redirect("/")

def showItem(request, itemid):
    print("!!!!!!!!")
    print(Item.objects.get(id = itemid))
    context = {
        'iteminfo': Item.objects.get(id = itemid),
        'allusers': User.objects.all()
    }

    return render(request, 'specificitem.html', context)

def addUserToItem(request, itemid):
    print("printing the info from the from, aka request.POST HERE:", request.POST)
    # this_book = Book.objects.get(id=4)	# retrieve an instance of a book
    # this_publisher = Publisher.objects.get(id=2)
    this_item = Item.objects.get(id=itemid)
    this_user = User.objects.get(id= request.POST['userinfo'])
    # this_user.fav_items.add(this_item)
    this_item.favoriters.add(this_user)

    #am i going to render or redirect? hint: if its a form submition (post request) then its redirect
    return redirect(f"/items/{itemid}")

def deleteItem(request, itemid):
    # c = ClassName.objects.get(id=1)
    # c.delete()
    itemToRemove = Item.objects.get(id=itemid)
    itemToRemove.delete()
    return redirect("/")

def editItem(request, itemid):
    itemToEdit = Item.objects.get(id= itemid)
    print(f"item to edit is this: {itemToEdit} ")
    context = {
        'itemObj': itemToEdit
    }
    return render(request, "editItem.html", context)


def updateItem(request, itemid):
    # c = ClassName.objects.get(id=1)
    # c.field_name = "some new value for field_name"
    # c.save()
    print("in the update item function")
    print(request.POST) # <QueryDict: {'csrfmiddlewaretoken': ['ynaAzKQ76p2jGPZxkpHGhRXiAEmGy6K4wWSDzuYYd85SJWKt7Af7pfNKXMxCKWjC'], 'itemName': ['polo hat'], 'itemdescription': ['hat squad']}>

    itemToUpdate = Item.objects.get(id= itemid)
    itemToUpdate.name = request.POST['itemName']
    itemToUpdate.desc = request.POST['itemdescription']
    itemToUpdate.save()
    return redirect("/")