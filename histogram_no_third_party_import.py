sales = {
  'google': 20,
  'facebook': 42,
  'twitter': 10,
  'offline': 12,
}

def histogram(sales_data):
  for company, sales in sales_data.items():
    print(company[0], sales * '$')


histogram(sales)