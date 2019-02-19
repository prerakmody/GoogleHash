
def read(filename):
    pizza_rows_data = []
    for rowid, row in enumerate(open(filename, 'r')):
        if rowid == 0:
            pizza_rows = int(row.split(' ')[0])
            pizza_cols = int(row.split(' ')[1])
            pizza_low    = int(row.split(' ')[2])
            pizza_high    = int(row.split(' ')[3])

            #print ('Rows : ', pizza_rows, ' || Cols : ', pizza_cols)
            #print ('Min cells of any ingredient: ', pizza_low)
            #print ('Max cells of any ingredient : ', pizza_high)
        else:
            pizza_rows_data.append(list([ingred for ingred in row])[:-1])

    #print ('\nIngredients on each row : ')
    #for rowid, row in enumerate(pizza_rows_data):
        #print ('Row : ', rowid, ' || ', row)
            
    return pizza_rows, pizza_cols, pizza_low, pizza_high, pizza_rows_data

if __name__ == "__main__":
    # data = read('data/a_example.in')
    data = read('data/b_small.in')