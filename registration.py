'''READ ME!!!
Welcome to the algorithm to registrate products, employees, customers and sales.
The registers are stored in dictionaries, you can access by the numeric key displayed when the program is running.
For sales, when the customer is an employee, there´s a 10% of discount applied to this person
The discount is calculate directly by: (1-10%)=0.9, so the discount just multiplies by 0.9 at the price*quantity
The script it´s in the initial fase. Some next steps could be encapsulating classes attributes and implementing
a search mechanism to alter incorrect sales, by searching via sales Id.
For advices and complains, feel free to send an email to: emanuelgoulartf@gmail.com
Thank´s for reading!'''

#Creating classes for the program
class Users():
    def __init__(self, Id_int, Name_Varchar, Age, Address_Varchar):
        self.Id_int = Id_int
        self.Name_Varchar = Name_Varchar
        self.Age = Age
        self.Address_Varchar = Address_Varchar


class Customers(Users):
    def __init__(self, Id_int, Name_Varchar, Age, Address_Varchar):
        super().__init__(Id_int, Name_Varchar, Age, Address_Varchar)

    def retornar_dados(self):
        return {'Id_customer':self.Id_int,'Name_customer':self.Name_Varchar,
                'Age_customer':self.Age,'Address_customer':self.Address_Varchar}


class Employees(Users):
    def __init__(self, Id_int, Name_Varchar, Age, Address_Varchar, Wage_Double):
        super().__init__(Id_int, Name_Varchar, Age, Address_Varchar)
        self.Wage_Double = Wage_Double

    def retornar_dados(self):
        return {'Id':self.Id_int,'Name':self.Name_Varchar,
                'Age':self.Age,'Adress':self.Address_Varchar,'Wage':self.Wage_Double}


class Products():
    def __init__(self,Id_int, Name_Varchar, Price_Double, stock_quant):
        self.Id_int = Id_int
        self.Name_Varchar = Name_Varchar
        self.Price_Double = Price_Double
        self.stock_quant = stock_quant

    def retornar_dados(self):
        return {'Id':self.Id_int,'Name':self.Name_Varchar,
                'Price':self.Price_Double,'Stock':self.stock_quant}


class Sales():
    def __init__(self,Id_sales, Id_product, Id_customer, Quantity, Final_Price):
        self.Id_Sales = Id_sales
        self.Id_product = Id_product
        self.Id_customer = Id_customer
        self.Quantity = Quantity
        self.Final_Price = Final_Price

    def retornar_dados(self):
        return {'Id_sale':self.Id_Sales,'Id_product':self.Id_product,
                'Id_customer':self.Id_customer,'Quantity':self.Quantity,
                'Final_price':self.Final_Price}


def escreva(msg):
    tam = len(msg)
    print('~'*tam)
    print(msg)
    print('~'*tam)
escreva('Welcome to our registration algorithm!')


#Creating lists to store data
lista_products = []
lista_employees = []
lista_customer = []
lista_sales = []


while True:
    print('''
    Type 1 to create a new product
    Type 2 to show registered products
    Type 3 to create new employee
    Type 4 to show registered employees
    Type 5 to create new customer
    Type 6 to show registered customers
    Type 7 to create new sale
    Type 8 to show registered sales
    Type 9 to exit from the program''')
    choice = int(input('Type your selection: ').strip())


    if choice == 1:
        Id_product = int(input('Enter with the Id of the product:'))
        nome_product = input('Enter with the name of the product:')
        price = float(input('Enter with price of the product:'))
        stock = int(input('Number of products in stock: '))
        generic_class = Products(Id_product, nome_product,price,stock)
        lista_products.append(generic_class.retornar_dados())

    if choice == 2:
        for lista in lista_products:
            print(lista)

    if choice == 3:
        Id_employee = str(input('Id of employee: '))
        Name_employee = str(input('Name of employee: '))
        Age_employee = int(input('Age of employee: '))
        Adress_employee = str(input('Adress of employee: '))
        Wage_employee = float(input('Wage employee: '))
        generic_employee = Employees(Id_employee,Name_employee,Age_employee,Adress_employee,Wage_employee)
        lista_employees.append(generic_employee.retornar_dados())

    if choice == 4:
        print(lista_employees)

    if choice == 5:
        Id_customer = str(input('Id customer: '))
        Name_customer = str(input('Name customer: '))
        Age_customer = int(input('Age customer: '))
        Adress_customer = str(input('Adress customer: '))
        generic_customer = Customers(Id_customer, Name_customer, Age_customer, Adress_customer)
        lista_customer.append(generic_customer.retornar_dados())

    if choice == 6:
        print(lista_customer)

    if choice == 7:
        Id_Product = int(input('Id product: '))
        for lista in lista_products: #Verifying if the Id_product exists in the product's list
            if lista['Id'] == Id_Product:
                price_sales = lista['Price']
                product_name = lista['Name']
                Id_sales = int(input('Id sale: '))
                Id_customer = int(input('Id customer: '))
                Quantity = int(input('Type quantity: '))

                for lista in lista_products: #Iterating the list to check if it exists
                    if lista['Id'] == Id_Product:
                        if Quantity>lista['Stock']:
                            print(f'''There are currently not enough products on the stock.
The current amount is {lista['Stock']}''')
                        else: #In case there's enough products in the stock, the script keeps going on
                            final_price = price_sales*Quantity
                            for lista in lista_employees: #Verifying if the employee exist in the employee's list
                                if lista['Id'] == Id_customer:
                                    final_price = price_sales*0.9*Quantity #Discount of 10% for employees
                            generic_sales = Sales(Id_sales,Id_Product,Id_customer,Quantity,final_price)
                            lista_sales.append(generic_sales.retornar_dados())

                            for lista in lista_products: #Reduce the quantity of product in stock
                                if lista['Id'] == Id_Product:
                                    lista['Stock'] = lista['Stock'] - Quantity

                            print(f'''Sale registered sucessfully! 
                            Id Customer : {Id_customer}
                            Product's name: {product_name}
                            Quantity: {Quantity}
                            Final price: {final_price}
                            ''')
            else:
                print("Error, this product's Id is not registered yet! Please verify!")

    if choice == 8:
        print(lista_sales)

    if choice == 9:
        escreva('Thank you! See you later! ')
        break