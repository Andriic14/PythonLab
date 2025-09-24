def product  (N):
    dob=1
    if N<=0:
        print("N повинно бути невід'ємним числом")
        return None
    elif N % 2==1:
        for i in range(1,N+1,2):
            dob*=i
        return dob
    elif N % 2 == 0:
        for i in range(2,N+1,2):
            dob*=i
        return dob