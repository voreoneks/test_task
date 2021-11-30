import sys 

n = int(sys.argv[1])
m = int(sys.argv[2])

def searchroute(n, m):
    arr = []
    counter = 0
    route = ''
    while(True):
        for i in range(1, n + 1):
            arr.append(i)
            counter += 1
            if counter == m:
                route += str(arr[0])
                if arr[-1] == 1:
                    return print(route)
                else:
                    arr.clear()
                    arr.append(i)
                    counter = 1

searchroute(n, m)