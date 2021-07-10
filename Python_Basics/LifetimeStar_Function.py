#Lab 6: Task 1: Lifetime of a star using Mass in solar masses

def lifetime(M):
    '''
    Input:
        M: Mass of star in solar masses
    Output:
        lt: Lifetime of stars in years
    '''
    p=0.
    
    if(M>=30):
        p=3.
    elif(M<=10):
        p=4.
    else:
        p=3.5
    
    lt=(1./(M**(p-1)))*(10**10)
    return lt
    

M=1

print(lifetime(M))

    
    