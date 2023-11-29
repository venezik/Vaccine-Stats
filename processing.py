#Must find and return the largest value associated with the second parameter.
def max_value(data, dates):
    ans = ""
    for dit in data:
        for keys in dit:
            if keys == dates:
                if dit[dates] > ans:
                    ans = dit[dates]
    return ans

#should use the accumulator pattern to create and return a new dictionary
def init_dictionary(data, loc):
    ans = {}
    for dit in data:
        for locs in dit:
            if locs == loc:
                 ans[dit[loc]] = 0
    return ans
 #hould use the accumulator pattern to calculate and return a float. It should initialize the accumulator variable to 0.           
def sum_matches(lod,k,v,tgt):
    ans = 0.0
    for dit in lod:
        if k in dit:
            if dit[k] == v:
                ans = ans + dit[tgt]
    return ans
#Should use the accumulator pattern to calculate and return a new list.
def copy_matching(lod, k, v):
    lst = []
    for dit in lod:
        if k in dit:
            if dit[k] == v:
                lst.append(dit)
    return lst