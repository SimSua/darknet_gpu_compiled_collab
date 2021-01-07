import os
import random

directory = os.path.abspath(os.curdir)+"/obj/"
images = []
for i in os.listdir(directory):
    if '.txt' not in i:
      images.append(i)
random.shuffle(images)  
print(len(images))
separation = (len(images)/100)*80
print(separation)
train = images[:separation]
test = images[separation:]

print(len(test)+len(train))

t = open('train.txt', 'w')
for i in train:
    t.write(str(i)+'\n')
te = open('test.txt', 'w')
for i in test:
    te.write(str(i)+'\n')
