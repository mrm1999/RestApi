from mongoengine import * 
import jsonify

try:
    connect( host='mongodb+srv://mohit:mohit1234@mohit.yaoax.mongodb.net/testdatabase?retryWrites=true&w=majority')
    print('Database Connected')
except Exception as err:
    print("Database Connection error\n")
    print(err)


class Address(EmbeddedDocument):
    location = StringField(required=True)
    pinCode = StringField(required=True)
    city = StringField(required=True)
    
class Transaction(EmbeddedDocument):
    item = ListField(StringField(required=True))
    quantity = ListField(StringField(required=True))
    total_amount = IntField(required=True)

#Registration id is called as buyer_id   
class Registration(Document):
    email = StringField(required=True)
    name = StringField(required=True)
    mobileNumber = IntField(required=True)
    password = StringField(required=True)
    address = ListField(EmbeddedDocumentField(Address))
    meta = {"allow_inheritance": True}


#This will be seller id
class Seller(Document):
    name = StringField(required=True)
    mobileNumber = IntField(required=True)
    email = StringField(required=True)
    shopName = StringField(required=True)
    shop_address = ListField(EmbeddedDocumentField(Address))
    meta = {"allow_inheritance": True}


class Transaction_Details(Document):
    buyer_id = StringField(required=True)
    seller_id = StringField(required=True)
    transaction = ListField(EmbeddedDocumentField(Transaction))
    meta = {"allow_inheritance": True}

#This will be the product ID;
class Product(Document):
    product_name = StringField(required= True)
    seller_id = StringField(required=True)
    img_url = StringField(required= True)
    product_amount = IntField(required=True)
    product_quantity = StringField(required=True)
    
class Rating(Document):
    product_id = StringField(required = True)
    rating = IntField(required= True)

class Feedback(Document):
    product_id = StringField(required=True)
    comment = StringField(required=True)    

def dummy():
    
    # trans = Transaction(item = {"Pickle" , "Spices"} , quantity = {"5" , "4"} , total_amount = 500 )
    registration = Registration(email = "mohitrajmunot1999@gmail.com" , name = "Mohit" , mobileNumber = 6376270113 , password = "Mohit@123" )
    registration.address.location = "Kot Ka Mohalla"
    registration.address.pinCode = "306104" 
    registration.address.city = "Sojat City"
    registration.save()
    seller = Seller(email = "mohitrajmunot1999@gmail.com" , name = "Mohit" , mobileNumber = 6376270113 ,shopName = "DesiMart" )
    seller.shop_address.location = "Kot Ka Mohalla"
    seller.shop_address.pinCode = "306104" 
    seller.shop_address.city = "Sojat City"
    seller.save()
    transaction_details = Transaction_Details(buyer_id = '1234' , seller_id = '2345')
    transaction_details.transaction.item = ("Pickle" , "Spices")
    transaction_details.transaction.quantity = ("5" , "4")
    transaction_details.transaction.total_amount = 500
    transaction_details.save()
    prod = Product(product_name = "Pickle", seller_id = "2345" , img_url = "google.com" , product_amount = 50 , product_quantity = "Per kg")
    prod.save()
    rat = Rating(product_id = '12' , rating = -5)
    rat.save()
    feed = Feedback(product_id = '12' , comment = "Good Product")
    feed.save()
    print("Great Success")

# # for i in range(5):
#     dummy()


user_id = []
for user in Registration.objects:
    user_id.append(user.id)
    
    


print(user_id)