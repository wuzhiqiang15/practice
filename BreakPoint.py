def SayHello(name):
    print("I want say hello with you,{0}".format(name))
    print("hello")
    print("Done............")

if __name__ == "__main__":
    name_1 = input("Please inter your name:")
    print(SayHello(name=name_1))
    print("###" * 10)
