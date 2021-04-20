
if __name__ == '__main__':
    try:
        x, y, z, n = map(int,
                         input("enter x and y and z and n add space between theme (must be a number) ").split(" "))
    except ValueError:
        print(f"please enter valid input must be only numbers")
    else:
        print([[i, j, k] for i in iter(range(x + 1)) for j in iter(range(y+1)) for k in iter(range(z+1)) if i+j+k != n])