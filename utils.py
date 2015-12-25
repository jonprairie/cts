def ExtractToDict(object_list, key_method):
    """utility function that takes a list of objects, each with a 0-parameter method: key_method.
    Iterates over the list calling key_method on each object, then builds a dict using the results
    of each key_method call as the key and the original object as the value"""
    
    temp_list = []
    for o in object_list:
        k = key_method(o)
        temp_list.append((k,o))
    return dict(temp_list)