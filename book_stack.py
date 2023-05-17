def tambah_buku(nama ,penulis, stack):
    stack.append((nama, penulis))

def print_top_book(stack):
    if stack:
        print(stack[-1])
    else:
        print("Stack kosong.")
        
stack = []

while True:
    buku = input("Masukan nama buku: ")
    if not buku:
        break
    penulis = input("Masukan nama penulis: ")
    if not penulis:
        break
    if penulis not in stack:
        print_top_book(stack)
        tambah_buku(buku, penulis, stack)
        print_top_book(stack)

if stack:
    print_top_book(stack)
else:
    print("Stack Kosong.")
