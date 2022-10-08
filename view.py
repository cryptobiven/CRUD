import json
import datetime

# [
#     {
#         "id": 1,
#         "name": "cocain",
#         "price": 500,
#         "time": "2022-10-08 12:10:32.311231",
#         "description": "white, fresh, good",
#         "status": "sell"
#     },
#     {
#         "id": 2,
#         "name": "mephedrone",
#         "price": 200,
#         "time": "2022-10-08 12:10:32.311231",
#         "description": "blue, fresh, good",
#         "status": "sales"
#     }
# ]

def get_obj(ge_price = None, le_price = None,data = None, status = None):
    with open('candyshop.json') as file:
        s = json.load(file)
    if ge_price:
        s2 = [i for i in s if i['price'] >= ge_price]
        print(s2)
        return s2
    if le_price:
        s2 = [i for i in s if i['price'] <= le_price]
        return s2
    if data:
        s2 =[i for i in s if str(data) in i['time']]
        return s2
    if status:
        s2 =[i for i in s if i['status'] == status]
        if status == 'sell':
            return s2
        elif status == 'sales':
            return s2

    return s

def get_one_obj(id):
    s = get_obj()
    one_obj = [i for i in s if i['id'] == id]
    if one_obj:
        return one_obj[0]

    return 'нет такого товара'
    
def update_obj(id):
    s = get_obj()
    s2 = [ i for i in s if i['id'] == id]
    if s2:
        s2[0]['name'] = input('New name: ')
        s2[0]['price'] = float(input('New price: '))
        s2[0]['time_update'] = f'{datetime.datetime.today()}'
        s2[0]['description'] = input('New description: ')
        s2[0]['status'] = input('New status: ')
        json.dump(s, open('candyshop.json', 'w'))
        return s
    
    return 'нет такого товара'

def delete_obj(id):
    s = get_obj()
    s2 = [i for i in s if i['id'] == id]
    if s2:
        s.remove(s2[0])
    with open('candyshop.json', 'w') as file:
        json.dump(s, file)
        
    return 'нет такого товара'

def post_obj():
    s = get_obj()
    max_i = max(i['id'] for i in s)
    s.append({
        'id': max_i + 1, 
        'name': input('Name: '),
        'price': float(input('Price: ')), 
        "time": f'{datetime.datetime.today()}', 
        "time_update": None,  
        "description": input('Description: '), 
        "status": input('Status: ')})
    with open('candyshop.json', 'w') as file:
        json.dump(s, file)
        return s