from __future__ import print_function

def submit(solution):            
    # Submission File
    print(len(solution))
    for slide in solution:
        picIds = [str(pic.id) for pic in slide]
        print(" ".join(picIds))

"""
with open(filename, 'w') as fp:
    for slide in solution:
        picIds = [str(pic.id) for pic in slide]
            fp.writeline(" ".join(picIds))
    
"""