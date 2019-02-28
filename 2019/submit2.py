from __future__ import print_function

def submit(solution, filename):                
    with open(filename, 'w') as fp:
        fp.write(str(len(solution)) + "\n")
        for slide in solution:
            picIds = [str(pic.id) for pic in slide]
            fp.write(" ".join(picIds) + '\n')
        