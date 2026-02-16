def main():
    yield("Hello from env-uv-solution!")
    yield("Hello again!")
    return("Bye")
    return("Bye again - not shown")


if __name__ == "__main__":
    gen = main()
    try:
         while True:
             print(next(gen))
#        for item in  main():
#            print(item)
    except StopIteration as e:
        print(e.value)
#        print(e.value)
