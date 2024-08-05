class MySequence:
    def __getitem__(self, index):
        return index

def log(msg):
    print("\n")
    print("=="*30)
    print(f"{msg:^50}")
    print("=="*30)
    print("\n")


myseq = MySequence()
log("Getting an index")
print(myseq[1])


log("Slice 1:4")
print(myseq[1:4])

log("Slice 1:4:2")
print(myseq[1:4:2])


log("Slice 1:4:2, 7:9. Returns a tuple!")
print(myseq[1:4:2, 7:9])


log("Slice is a class, therefore we can inspect it")

print(dir(slice))

log("Let's read the help of indices attribute of slice")

print(help(slice.indices))


log("Let's assume we have a sequence of 5 elements [1, 2, 3, 4, 5]. This is what indices returns")
slice(None, 10, 2).indices(5)

slice(-3, None, None).indices(5)

log("In other words, slice encapsulates the logic that allows us in Python to give negative integers as indexes for slicing")
