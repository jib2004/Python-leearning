def main():
    x = input("Whats x?: ")
    print("x squared is",square(x))

def square(x):
    return x * x

if __name__ == "__main__": #To  make sure main is not always called when not in this file
    main()