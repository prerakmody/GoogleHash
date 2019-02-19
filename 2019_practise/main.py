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
    bottom_right = [row + shape[0], col + shape[1]]
    return [top_left, bottom_right]

def get_sub_maps_available():
    return []

def solve(rows, cols, L, H, pizza):   #[pizza = [t, m]]
    slices = []
    print(rows)
    print(cols)
    slices_map = np.zeros((rows,cols))

    # loop over all cells
    for i in range(0, rows):
        for j in range(0, cols):
            shapes = get_candidate_shapes(L)
            print(shapes)
            for shape in shapes:                
                if (fit_shape_in_map(shape, pizza, slices_map, i, j, L)):
                    slice_id = len(slices) + 1
                    pizza_slice = create_slice(shape, slices_map, i, j, slice_id)
                    slices.append(pizza_slice)
                    break

    print(slices_map)
    # TODO: postprocessing

    postprocess(slices_map, pizza, H)

    return len(slices), slices

######################################################
                    # POSTPROCESSING
######################################################

def postprocessFindSlicesAroundCell(pizza_slicemap, row, col):
    # Go N.E.W.S
    
    totalRows, totalCols = np.shape(np.array(pizza_slicemap))
    
    news = []

    # north, east, west, south
    dirs = [[row, 0, -1], [col, totalCols, 1], [col, 0, -1], [row, totalRows, 1]]

    for dir_id, direction in enumerate(dirs):
        flag = 0
        for i in range (direction[0], direction[1], direction[2]):
            switch (dir_id):
            if (dir_id == 1):
                item = [i, col]
            if (dir_id == 2):
                item = [row, i]
            if (dir_id == 3)
            if (pizza_slicemap[i][col] != 0):
                news.append([i, col])
                flag = 1
                break
        if (flag == 0):
            news.append (-1)

    # North
    flag = 0
    for i in range (row, 0, -1):
        if (pizza_slicemap[i][col] != 0):
            news.append([i, col])
            flag = 1
            break
    if (flag == 0):
        news.append (-1)
        
    # East
    flag = 0
    for i in range (col, totalCols):
        if (pizza_slicemap[row][i] != 0):
            news.append([row, i])
            flag = 1
            break
    if (flag == 0):
        news.append (-1)
    
    # West
    flag = 0
    for i in range (col, 0, -1):
        if (pizza_slicemap[row][i] != 0):
            news.append([row, i])
            flag = 1
            break
    if (flag == 0):
        news.append (-1)
    
    # South
    flag = 0
    for i in range (y, totalRows):
        if (pizza_slicemap[i][y] != 0):
            news.append([x, i])
            flag = 1
            break
    if (flag == 0):
        news.append (-1)
    return news

def postprocessFindSliceCorners(pizza_slicemap, news_dir_cell):
    slice_topleft = [-1, -1]
    slice_bottom_right = [-1, -1]

    pizza_rows, pizza_cols = np.shape(np.array(pizza_slicemap))
    
    cell_rowid, cell_colid = np.array(news_dir_cell)
    slice_idx = pizza_slicemap[news_dir_cell[0]][news_dir_cell[1]]

    # North
    for rowid in range(cell_rowid, 0, -1):
        if pizza_slicemap[rowid][cell_colid] != slice_idx:
            break
    slice_topleft[0] = rowid

    # East
    for colid in range(cell_colid, pizza_cols,1):
        if pizza_slicemap[cell_rowid][colid] != slice_idx:
            break
    slice_bottom_right[1] = colid

    # West
    for colid in range(cell_colid, 0, -1):
        if pizza_slicemap[cell_rowid][colid] != slice_idx:
            break
    slice_topleft[1] = colid

    # South
    for rowid in range(cell_rowid, pizza_rows, 1):
        if pizza_slicemap[rowid][cell_colid] != slice_idx:
            break
    slice_bottom_right[0] = rowid

    return slice_topleft, slice_bottom_right    

def postprocessCheckSliceExpansion(pizza_slicemap, slice_coords, cell_check, news_dir):

    rows, cols = np.shape(np.array(pizza_slicemap))
    topleft, bottomright = slice_coords
    slice_idx  = pizza_slicemap[topleft[0]][topleft[1]]


    if news_dir == 0: # slice is in North, so go south
        fill_flag = 1
        for rowid in range(bottomright[0]+1, cell_check[0], 1):
            for colid in range(topleft[1], bottomright[1]):
                if pizza_slicemap[rowid][colid] != slice_idx:
                    fill_flag = -1
                    break
    if fill_flag == 1:
        for rowid in range(bottomright[0]+1, cell_check[0], 1):
            for colid in range(topleft[1], bottomright[1]):
                pizza_slicemap[rowid][colid] = slice_idx
        
    if news_dir == 1: # slice is in East, so go West
        fill_flag = 1
        for colid in range(bottomright[1] + 1, cell_check[1]):
            for rowid in range(topleft[0], bottomright[0]):
                if pizza_slicemap[rowid][colid] != slice_idx:
                    fill_flag = -1
                    break
    if fill_flag == 1:
        
    
    if news_dir == 2: # West
        pass
    if news_dir == 3: # South
        pass

def postprocess(pizza_slicemap, pizza_map, H):
    pizza_rows, pizza_cols = np.shape(np.array(pizza_slicemap))
    for i in range(pizza_rows):
        for j in range(pizza_cols):
            if pizza_slicemap[i][j] == 0:
                news = postprocessFindSlicesAroundCell(pizza_slicemap, i, j)
                for news_dir, news_dir_cell in enumerate(news):
                    
                    if news_dir_cell != -1:
                        slice_topleft, slice_bottom_right = postprocessFindSliceCorners(pizza_slicemap, news_dir_cell)
                        postprocessCheckSliceExpansion(pizza_slicemap, [slice_topleft, slice_bottom_right], [i, j], news_dir)
    return True


filename = sys.argv[1]
rows, cols, L, H, pizza = read.read(filename)

#print(rows, cols, L, H)
#print(pizza)

S, slices = solve(rows, cols, L, H, pizza)

#print(S)

for pizza_slice in slices:
    print ("%d %d %d %d" % (pizza_slice[0][0], pizza_slice[0][1], 
        pizza_slice[1][0], pizza_slice[1][1]))
