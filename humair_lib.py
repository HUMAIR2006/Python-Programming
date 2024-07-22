# Author : Humair Munir  , email:humairmunirawan@gmail.com  Date : July 21 , 2024  , loc : Mandal , Lipa , AJK, Pakistan.
#Activity : Fun with Functions , Time : 12:19



"""
Let suppose a problem where we have to find the income of employees where we know income_per-hour , numbers_of hours , .
 we also have to find income after tax . So solution is:
"""
def income_after_tax(income_per_hour , numbers_of_hours , tax_percentage):
    #Finding total daily income without excluding taxes
    total_income = income_per_hour * numbers_of_hours
     #Finding total daily income with excluding taxes
    income_after_taxes = total_income *(1 - tax_percentage)
    #returning value
    return income_after_taxes
"""
   Let  suppose we have a problem that we have to predict the house price , there is a condition that while predicting
 we have to take care  some  conditions such as there is a condition that the price of only house with no bed ,bath room 
 is dummy_house-price .While the price increase as per bath or bed room increase in certain  amount let say per_bed_increase ....
 So , solution is :
"""
def house_predict_problem(dummy_house_price , numbers_of_beds , per_bed_increase, numbers_of_bath , per_bath_increase):
    #Findind house price on basis of given values 
    house_price = dummy_house_price + numbers_of_beds * per_bed_increase + numbers_of_bath * per_bath_increase
    #Feturning value
    return house_price
"""
Let  suppose a problem where we have to find the income of  person as we know the basic income and income increase percentage .
So solution is here :

"""
def per_year_income_increase(basic_income , increase_percentage):
    # First we find only increased amount 
    increase_income= basic_income*increase_percentage
     # Now findind  neew total income
    total_new_basic_income = basic_income + increase_income
    #Returning variables values 
    return increase_income , total_new_basic_income

"""
Let suppose we have a problem that we have to find the extra_income of employee when we know only his/her daily income.
So solution is below:
"""

#W declare two variable for value storing inside the function parameter 
def extra_work_income(eight_hours_income , num_extra_hours):
    #finding per hour income of employee
    per_hours_income = eight_hours_income / 8
    extra_work_income = per_hours_income * num_extra_hours
    #Returning the value of extra work income 
    return extra_work_income

