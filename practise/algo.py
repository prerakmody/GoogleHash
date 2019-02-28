import read
import sys
import numpy as np 

def get_candidate_shapes(L):    
    shapes = []
    for cols in range(1, 2 * L + 1):
        if (2 * L % cols == 0):
            rows = 2 * L / cols
            shapes.append([rows, cols])
    return shapes

def fit_shape_in_map(shape, pizza, slices_map, i, j, L):
    shape_fitting = True

    shape_row = shape[0]
    shape_column = shape[1]
    
    t_count = 0
    m_count = 0
    
    for r in range(0,shape[0]):  #row Check
        for c in range(0,shape[1]):  #col Check
            if i+r >= len(pizza) or j+c >= len(pizza[0]) or slices_map[i+r][j+c] != 0: # Check out of bounds and pre-occupy
                shape_fitting = False
                break
            else:
                if pizza[i+r][j+c] == 'M':
                    m_count = m_count + 1
                else:
                    t_count = t_count + 1
    
    return shape_fitting and t_count >= L and m_count >= L

def create_slice(shape, slices_map, row, col, slice_id):
    for i in range(0, shape[0]):
        for j in range(0, shape[1]):
            slices_map[row+i][col+j] = slice_id

    top_left = [row, col]
    bottom_right = [row + shape[0] - 1, col + shape[1] - 1]
    return [top_left, bottom_right]

def get_sub_maps_available():
    return []

def solve(rows, cols, L, H, pizza):   #[pizza = [t, m]]
    slices = []    
    slices_map = np.zeros((rows,cols))

    # loop over all cells
    for i in range(0, rows):
        for j in range(0, cols):
            shapes = get_candidate_shapes(L)
            #print(shapes)
            for shape in shapes:                
                if (fit_shape_in_map(shape, pizza, slices_map, i, j, L)):
                    slice_id = len(slices) + 1
                    pizza_slice = create_slice(shape, slices_map, i, j, slice_id)
                    slices.append(pizza_slice)
                    break

    #print(slices_map)
    # TODO: postprocessing

    return len(slices), slices

######################################################
                    # POSTPROCESSING
######################################################

def postprocessFindSlicesAroundCell(pizza_slicemap, x, y):
    # Go N.E.W.S
    
    rows, cols = np.shape(np.array(pizza_slicemap))

    # North
    news = []
    north_flag = -1
    for i in range(x, 0, -1):
        if (pizza_slicemap[i][y] != 0):
            news.append([i,y])
            north_flag = 1 
            break
    if north_flag == -1:
        news.append(-1)
    
    # East
    east_flag = 1
    for j in range(y, 0):
        if pizza_slicemap[x][j] != 0:
            news.append([x, j])
            east_flag = 1
            break
    if east_flag == 1:
        news.append(-1)
    
    # West
    west_flag = 1
    for j in range(y,cols,1):
        if pizza_slicemap[x][j] !=0:
            news.append(-1)
            west_flag = -1
            break
    if west_flag == 1:
        news.append([x,j])
    
    # South
    south_flag = 1
    for i in range(x, rows, 1):
        if pizza_slicemap[i][y] != 0:
            news.append(-1)
            south_flag = -1
            break
    if south_flag == 1:
        news.append([i,y])
    
    return news



filename = sys.argv[1]
rows, cols, L, H, pizza = read.read(filename)

#print(rows, cols, L, H)
#print(pizza)

S, slices = solve(rows, cols, L, H, pizza)

print(S)

for pizza_slice in slices:
    print ("%d %d %d %d" % (pizza_slice[0][0], pizza_slice[0][1], 
        pizza_slice[1][0], pizza_slice[1][1]))
