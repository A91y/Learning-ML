def prime(x):
    composite = False
    for _ in range(2,x):
        if x%_==0:
            composite = True
            break
    if composite:
        print("Composite he")
    else:
        print("Prime he")

prime(int(input()))

