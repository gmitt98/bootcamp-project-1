def zip_correct(zip):
    zip_str = str(zip)
    while len(zip_str) < 5:
        zip_str= "0" + zip_str
    return zip_str

test1 = zip_correct(1)
test2 = zip_correct(97405)
test3 = zip_correct(405)

print(test1, test2, test3)