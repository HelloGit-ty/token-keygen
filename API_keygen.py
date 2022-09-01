import string
import random
nof_keys = int(input("Enter the no.of api keys or auth tokens you want to generate--> "))
i = 0
while i < nof_keys:
    sos = random.randint(10, 128)
    res = ''.join(random.choices(string.ascii_letters + string.digits + '_' + '.' + '-', k=sos))
    #print("The generated random string : " + str(res))
    try:
        with open("train_data.txt", 'a') as file:
            file.write(str(res) + '\n')
    except IOError:
        print("Could not read/open file")
        exit(-1)
    i = i + 1
print("Done!!")
