def getMismatchIndex(of: str, on: str) -> int:
    
    index = 0

    while index < len(of) and index < len(on):

        if of[index] != on[index]: 
            return index
    return -1