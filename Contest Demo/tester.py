import pickle
import os

def check(s):
    model = pickle.load(open(os.path.join(s+".pkl"), 'rb'))
    data = []
    label = []
    for line in open('data_train.txt', 'r'):
        words = line.strip().split()
        label.append(float(words[0]))
        text = []
        for i in range(1,len(words)):
            text.append(float(words[i]))
        data.append(text)
    for line in open('data_test.txt', 'r'):
        words = line.strip().split()
        label.append(float(words[0]))
        text = []
        for i in range(1,len(words)):
            text.append(float(words[i]))
        data.append(text)
    test = model.predict(data)
    count=0
    for i in range(len(test)):
        if test[i] == label[i]:
            count +=1
    return str(count/len(test)*100)+"%"

# x=input()
# check(x)