


salary= float(input("Ingrese el salario:"))

transport_aid = 162000

rate_healt_discount = 0.04

rate_pension_discount = 0.04

minimum_legal_salary = 1300000



def calcalate_healt_discount(salary, rate_healt_discount):
    healt_discount = salary * rate_healt_discount
    return healt_discount

def calculate_pension_discount(salary, rate_pension_discount):
    pension_discount = salary * rate_pension_discount
    return pension_discount


discount_per_healt = calcalate_healt_discount(salary, rate_healt_discount)
discount_per_pension = calculate_pension_discount(salary, rate_pension_discount)


def calculate_net_salary(salary, discount_per_healt, discount_per_pension):


    if salary < (minimum_legal_salary* 2):
       net_salary = salary - discount_per_healt - discount_per_pension + transport_aid
       
    else:   
        net_salary = salary - discount_per_healt - discount_per_pension
        
    return net_salary



emp_net_salary = calculate_net_salary(salary, discount_per_healt, discount_per_pension)

print(f"Salario Neto{emp_net_salary}")