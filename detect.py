import pickle
import spam
from tkinter import *


with open('linearSVCTrainedModel.sav', 'rb') as f:
    loadedSVC = pickle.load(f)

def detect():
    user_input = input1.get("1.0","end-1c")
    answer.config(text=spam.make_Prediction(spam.load_Model(user_input)))

root = Tk()
root.title('Spam detector')
root.geometry('500x400')
root.resizable(width=True, height=True)

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

label1 = Label(topFrame, text='Enter the Email: ',font=("Palatino",14), padx=10)
label1.pack()

input1 = Text(topFrame, height=8, width=40)
input1.pack()

button1 = Button(topFrame, text='Detect', command=detect, height=2,width=25, bd=4)
button1.pack()

button2 = Button(bottomFrame, text='Quit',fg='red', height=2,width=25, bd=4, command=quit)
button2.pack()

answer = Label(topFrame, text='' ,font=("palatino",12))
answer.pack()

root.mainloop()


























































# data = pd.read_csv('heart.csv')
# data.columns.name = "index"
# print("Train Dataset:")
# print(data)
#
# print("Train Data Set Columns:")
# trainDatadf = pd.DataFrame(data)
# trainDataIndex = trainDatadf.columns
# print(trainDataIndex)
#
# print("\n")
# print("Number of instances in Train Dataset")
# print("Train Instances: %s" % (len(trainDatadf.index)))
#
# preprocessed_dataset = data.fillna('0')
#
# print("Train dataset before pre-processing:")
# print("=========================================\n")
# print(data)
#
# print("\n\n\nTrain dataset after pre-processing:")
# print("=========================================\n")
# print(preprocessed_dataset)
#
# preprocessed_dataset.head()
#
# x = preprocessed_dataset.iloc[:, :-1].values
# y = preprocessed_dataset.iloc[:, -1:].values
#
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
#
# logisticRegression = LogisticRegression()
# logisticRegression.fit(x_train, y_train)
# LR = logisticRegression.predict(x_test)
#
# filename = 'heart-model.sav'
# pickle.dump(logisticRegression, open(filename, 'wb'))
