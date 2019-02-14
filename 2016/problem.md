

# Orders
    - it is not required to deliver all orders
# Drones
    - euclidean distance is rounded
    - max load = W
    - Actions = [load, deliver, unload](d + 1 turns), wait (w turns)
    - all unload before load 

# Input
    - 0:P-1 products
    - 0:W-1 warehouses
    - 0:C-1 orders
    - 




# Input Data 
    - 3 different i/p files to be simulated 
        * mother_of_all_warehouses (More no.of warehouses)
        * busy_day (more no.of orders)
        * redundancy (redundant routing)
        
    - File Format
        * line 1 - [map_row, map_column, no.of drones, total_turns, max_drone_load]
        * line 2 - no.of products
        * line 3... - product wgts. 
        * line 4 - no.of warehouses
            ~ warehouse location
            ~ avail product quantity (same order as line 3)
        * line 5 - no.of orders
            ~ delivery location
            ~ product counts (array) 
            ~ product ids (array) (id as per line 3 index)

# Target Output (Requirement)
    * line 1 - no.of commands/ drone task [c] (each command = certain turns)
    * c lines of commands (each command is as below) [each command - 5 or 3 items indicating todo]
        "Incase of Load or Delivery" - 5
        ~ c1 - drone id
        ~ c2 - drone task ('L' - load, 'D' - deliver)
        ~ c3 - warehouseId (If 'L' - load) or customerId (If 'D' - deliver)
        ~ c4 - productId
        ~ c5 - product quantity
        Incase of Wait" - 3
        ~ c1 - drone id
        ~ c2 - 'W'
        ~ c3 - no.of turns - to wait

# AIM - MAX ORDER DELIVERY IN GIVEN no.of turns
        