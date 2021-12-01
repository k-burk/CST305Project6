#recurrence formula found from solving on paper
def recurrence(n, a):
    an = (a*(-n*(n-1)-1))/(4*(n+2)*(n+1))
    return an

# function so it can run from main
def run():

    arr = [1, 1] #set to 1 to not mess with the a0 and a1 values

    for i in range(10):
        arr.append(recurrence(i, arr[i]))
        if(i == 0 or i == 1):
            print("")
        else:
            #the an+2 alternate between a0 on even n values and a1 on odd n values
            if i%2==0:
                print("a"+str(i) +"= "+str(arr[i])+" * a0")
            else:
                print("a"+str(i) +"= "+str(arr[i])+" * a1")

