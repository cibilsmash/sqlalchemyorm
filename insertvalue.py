from create import Customer, Item, Order, OrderLine, Base, Session

### Inserting data to database By  objects

# lets create two customer objects 

session = Session()

c1 = Customer(
            first_name = "John", 
            last_name = "Lara", 
            username = "johnlara", 
            email = "johnlara@mail.com"
)

c2 = Customer(          
            first_name = "Sarah", 
            last_name = "Tomlin", 
            username = "sarahtomlin", 
            email = "sarahtomlin@mail.com"        
)

c3 = Customer(first_name = 'Toby', 
              last_name = 'Miller', 
              username = 'tmiller', 
              email = 'tmiller@example.com'
             )

c4 = Customer(first_name = 'Scott', 
              last_name = 'Harvey', 
              username = 'scottharvey', 
              email = 'scottharvey@example.com'
             )



i1 = Item(name = 'Chair', cost_price = 9.21, selling_price = 10.81)
i2 = Item(name = 'Pen', cost_price = 3.45, selling_price = 4.51)
i3 = Item(name = 'Headphone', cost_price = 15.52, selling_price = 16.81)
i4 = Item(name = 'Travel Bag', cost_price = 20.1, selling_price = 24.21)


o1 = Order(customer = c1)
o2 = Order(customer = c1)

line_item1 = OrderLine(order = o1, item = i1, quantity =  3)
line_item2 = OrderLine(order = o1, item = i2, quantity =  2)
line_item3 = OrderLine(order = o2, item = i1, quantity =  1)
line_item3 = OrderLine(order = o2, item = i2, quantity =  4)


session.add_all([c1,c2,c3,c4])

session.add_all([i1,i2,i3,i4])

session.add_all([o1, o2])

session.new
session.commit()


