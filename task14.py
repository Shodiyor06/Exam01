fayl_k = input("fayl nomi: ")
fayl = ".pdf" , ".docx", ".txt"
if fayl_k.endswith(".txt"):
    print("bu txt fayl")
elif fayl_k.endswith(".pdf"):
    print("bu pdf fayl")
elif fayl_k.endswith(".docx"):
    print("bu docx fayl")
else:
    print("bu turdagi fayl yuq")
