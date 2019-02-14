import read

"""
0. Loop over all drones
    <find closest warehouse and traverse>
        1. Loop over all satisfiable order in the warehouse of the drone
            2 Do a knapsack for that drone
                3. Find the best PC of orders so that cost is minimized
                    4. Deploy drone
"""

if __name__ == "__main__":
    mapsize, total_drones, total_turns, warehouses, orders = read.read('data/busy_day.in')
    
    drones = [{'id': i, 'location': warehouses[0]['location']} for i in range(total_drones)]

    for drone in drones:

        drone_id = drone['id']

        order_cost_list = []
        for order in orders: 

            order_id = order['id']

            order_cost_drone, commandList = findOrderCostForDrone(order_id, drone_id)
            order_dependancy, order_cost_list = order_cost_list.append(order_cost_drone)
        
        order_dependancy_list, to_dispatch_order_ids = calculateKnapsack(order_dependancy, order_cost_list)
                
        # ------ Knapsack Problem Dispatch Order 
        dispatchDroneCommands(order_dependancy_list, to_dispatch_order_ids, drone_id)
        # Remove Order from List
        removeOrdersFromList(to_dispatch_order_ids)
        
            #warehouse             = findClosestWarehouse(drone)
            #drone_possible_orders = findSatisfiableOrders(warehouse.id)
            #drone_knapsack_order  = findKnapsackOrders(drone_possible_orders, drone.maxWeight)
            #drone_final_order     = findLowestCostOrder(drone_knapsack_order, warehouse.id)

    def findOrderCostForDrone(orderId, droneId):
        
        #Get productList from Order
        order = orders[orderId]
        missing_items = order['product_ids']        
        
        warehouse_distances = [distance(warehouse['location'], drone['location']) + 
            distance(warehouse['location'], order['location']) for warehouse in warehouses]

        # todo: sort
        warehouses_by_distance = warehouses

        used_warehouses = []

        while len(missing_items) > 0:
            for warehouse in warehouses_by_distance:
                if (warehouse['product_available'][missing_items[0]] > 0):                    
                    missing_items.pop(0)
                    warehouse['product_available'][missing_items[0]] = warehouse['product_available'][missing_items[0]] - 1
                    used_warehouses.append(warehouse['id'])

        return used_warehouses, 10


    def distance(orgin, dest):
        # √|ra − rb|2 + |ca − cb|2 
        origin_x = orgin[0]
        origin_y = orgin[0]
        dest_x = orgin[0]
        origin_x = orgin[0]

        print("test")

    def removeOrdersFromList(to_dispatch_order_ids):
        print("test")

    def removeProductFromWarehouse (warehouse_id, product_id):
        print("test")
    
    def calculateKnapsack(order_dependancy, order_cost_list):
        print("test")

    def dispatchDroneCommands(order_dependancy_list, to_dispatch_order_ids, drone_id):
        print("test")