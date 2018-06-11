import random


def cash_flow(monthly_income_min, monthly_income_max, number_of_courses, number_of_months):
    cash = 0
    for _ in range(0, number_of_courses):
        cash += random.randint(monthly_income_min, monthly_income_max) * number_of_months
        number_of_months -= 1  # we are taking 1 month out because there are courses that are yet not created.
    return "The money that will be made is about: ${0}".format(cash)


print(cash_flow(50, 150, 20, 20))





















