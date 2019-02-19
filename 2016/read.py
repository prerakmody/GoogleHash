import numpy as np

def to_int_list(str_list):
    return [int(item) for item in str_list]

def read(ip_file):
    file = open(ip_file, 'rb')
    each = file.readline()
    map_rows   = int(each.split(' ')[0])
    map_cols   = int(each.split(' ')[1])
    total_drones = int(each.split(' ')[2])
    total_turns  = int(each.split(' ')[3])
    drone_cap      = int(each.split(' ')[4])
    
    product_types  = int(file.readline())

    each = file.readline()
    product_weights  = to_int_list(each.split(' '))
    
    total_warehouses = int(file.readline())

    warehouse_data = []

    for i in range(total_warehouses):
        data = {}
        data["id"] = i
        data["location"] = to_int_list(file.readline().split(' '))
        data["product_available"] = to_int_list(file.readline().split(' '))

        warehouse_data.append(data)
        
    total_orders = int(file.readline())

    order_data = []
    for i in range(total_orders):
        data = {}
        data["id"] = i
        data["location"] = to_int_list(file.readline().split(' '))
        data["product_quantity"] = int(file.readline())
        data["product_ids"] = to_int_list(file.readline().split(' '))

        order_data.append(data)
        
    
    print ('Rows : ', map_rows, ' || Cols : ', map_cols)
    print ('Drones : ', total_drones)
    print ('TotalTurns : ', total_turns)
    print ('DroneCapacity : ', drone_cap)
    print ('Product Types : ', product_types)
    print ('Product Weights : ', product_weights)
    print ('Total Warehouses : ', total_warehouses)
    print ('Warehouses Data: ', warehouse_data)
    print ('Orders Data: ', order_data)

    
    return [map_rows, map_cols], total_drones, total_turns, warehouse_data, order_data



if __name__ == "__main__":
    warehouses, orders = read('data/busy_day.in')
