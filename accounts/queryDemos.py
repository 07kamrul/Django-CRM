#****(1)Return All customer from customer table
from .models import *

customers = Customer.objects.all()

#****(2) Return first customer in table
firstCustomer = Customer.objects.first()

#****(3) Return last customer in table
lastCustomer = Customer.objects.last()

#****(4) Return single customer by name in table
customerByNmae = Customer.objects.get(name='Kamrul Hasan')

#****(5) Return single customer by id in table
customerById = Customer.objects.get(id=4)

#****(6) Return all orders related to customer (firsCustomer veriable set aove) in table
firstCustomer.order_set.all()

#****(7) Return order customer name: (Query parent model values) in table
order = Order.objects.first()
parentName = order.customer.name

#****(8) Return products customer in table with values of "Out Door" in category attribute
products = Product.objects.filter(category="Out Door")

#****(9) Order/Sort objects by id in table
lastToGreatest = Product.objects.all().order_by('id')
greaterToLeast = Product.objects.all().order_by('-id')

#****(10) Return all product with tag of "sports" :(Query Many to Many  Fields) in table
productsFiltered = Product.objects.filter(tag__name="sports")

#**** Return the total count for number of time a "Ball"
ballOrders = firstCustomer.order_set.filter(product_name="MI")

#****Return total count for each product orderd
allOrders = {}
for order in firstCustomer.order_set.all():
    if order.product.name in allOrders:
        allOrders[order.product.name] += 1
    else:
        allOrders[order.product.name] = 1

#Returns: allOrder:{'Ball':2,'BBQ Grill':1}

#Related Set Example
class ParentModel(models.Model):
    name = models.CharField(max_length=200,null=True)

class ChildModel(models.Model):
    parent = models.ForeignKey(ParentModel)
    name = models.CharField
parent = ParentModel.objects.first()
#Return all child models related to parent
parent.childmodel_set.all()



