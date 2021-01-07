import os
import random

directory = os.path.abspath(os.curdir)+"/obj/"
images = []
train_filename = 'train_animals.txt'
test_filename = 'test_animals.txt'
for i in os.listdir(directory):
    if '.txt' not in i:
      images.append(i)
random.shuffle(images)  
print(len(images))
separation = int((len(images)/100)*80)
print(separation)
train = images[:separation]
test = images[separation:]

print(len(test)+len(train))

t = open(train_filename, 'w')
for i in train:
    t.write(directory+str(i)+'\n')
te = open(test_filename, 'w')
for i in test:
    te.write(directory+str(i)+'\n')
