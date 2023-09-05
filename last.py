from tkinter import *
import pandas as pd
import pickle
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
#
# data = pd.read_csv('heart2.csv')
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
# filename = 'heart-model1234.sav'
# pickle.dump(logisticRegression, open(filename, 'wb'))
# loadBM = pickle.load(open('heart-model1234.sav', 'rb'))
# print(loadBM)
# print(loadBM)
root = Tk()
root.title('heart PredictionIO')
root.geometry('1500x800')
root.resizable(width=True, height=True)

def condition():
    user_input = Gender.get("1.0","end-1c"), age.get("1.0","end-1c"), education.get("1.0","end-1c"), currentSmoker.get("1.0","end-1c"), cigsPerDay.get(
        "1.0","end-1c"), BPMeds.get("1.0","end-1c"), prevalentStroke.get("1.0","end-1c"), prevalentHyp.get("1.0","end-1c"), diabetes.get(
        "1.0","end-1c"), totChol.get("1.0","end-1c"), sysBP.get("1.0","end-1c")
    print(user_input)
    #user_input =pd.DataFrame(user_input1)
    #print(user_input)
    type(user_input)
    if user_input[0] == "male" or user_input[0] == "Male":
        user_input[0] = 1
    elif user_input[0] == "female" or user_input[0] == "Female":
        user_input[0] = 0
    if user_input[3] == "no" or user_input[3] == "No":
        user_input[3] = 0
    elif user_input[3] == "yes" or user_input[3] == "Yes":
        user_input[3] = 1
    if user_input[5] == "no" or user_input[5] == "No":
        user_input[5] = 0
    elif user_input[5] == "yes" or user_input[5] == "Yes":
        user_input[5] = 1
    if user_input[6] == "no" or user_input[6] == "No":
        user_input[6] = 0
    elif user_input[6] == "yes" or user_input[6] == "Yes":
        user_input[6] = 1
    if user_input[7] == "no" or user_input[7] == "No":
        user_input[7] = 0
    elif user_input[7] == "yes" or user_input[7] == "Yes":
        user_input[7] = 1
    if user_input[8] == "no" or user_input[8] == "No":
        user_input[8] = 0
    elif user_input[8] == "yes" or user_input[8] == "Yes":
        user_input[8] = 1
    encodeNewdf = pd.DataFrame(
        {"Gender": user_input[0], "Age": user_input[1], "Education": user_input[2], "CurrentSmoker": user_input[3], "CigsPerDay": user_input[4],
         "BP_Meds": user_input[5], "PrevalentStroke": user_input[6], "PrevalentHyp": user_input[7], "Diabetes": user_input[8],
         "total_Col": user_input[9], "sys_BP": user_input[10]},index=[0])

    print(encodeNewdf)

    answer.config(text=make_Prediction(load_Model))


label1 = Label(root, text='Please enter your gender: ', font=("Palatine", 14), padx=10)
label1.pack()

Gender = Text(root, height=0.1, width=40)
Gender.pack()

label2 = Label(root, text='Please enter your age here: ', font=("Palatine", 14), padx=10)
label2.pack()

age = Text(root, height=0.1, width=40)
age.pack()

label3 = Label(root, text='Please enter your education(1-4) ', font=("Palatine", 14), padx=10)
label3.pack()

education = Text(root, height=0.1, width=40)
education.pack()

label4 = Label(root, text='Are you currentSmoker (yes/no) ', font=("Palatine", 14), padx=10)
label4.pack()

currentSmoker = Text(root, height=0.1, width=40)
currentSmoker.pack()

label5 = Label(root, text='your cigsPerDay:', font=("Palatine", 14), padx=10)
label5.pack()

cigsPerDay = Text(root, height=0.1, width=40)
cigsPerDay.pack()

label6 = Label(root, text='do you take BPMeds(yes/no) ', font=("Palatine", 14), padx=10)
label6.pack()

BPMeds = Text(root, height=0.1, width=40)
BPMeds.pack()

label7 = Label(root, text='ever have prevalentStroke (yes/no)', font=("Palatine", 14), padx=10)
label7.pack()

prevalentStroke = Text(root, height=0.1, width=40)
prevalentStroke.pack()

label8 = Label(root, text='ever have prevalentHyp(yes/no)', font=("Palatine", 14), padx=10)
label8.pack()

prevalentHyp = Text(root, height=0.1, width=40)
prevalentHyp.pack()

label9 = Label(root, text='ever have diabetes(yes/no)', font=("Palatine", 14), padx=10)
label9.pack()

diabetes = Text(root, height=0.1, width=40)
diabetes.pack()

label10 = Label(root, text='total Cholesterol', font=("Palatine", 14), padx=10)
label10.pack()

totChol = Text(root, height=0.1, width=40)
totChol.pack()

label11 = Label(root, text='sys Blood Pressure:', font=("Palatine", 14), padx=10)
label11.pack()

sysBP = Text(root, height=0.1, width=40)
sysBP.pack()
button1 = Button(root, text='Detect', command=condition, height=2, width=25, bd=4)
button1.pack()

answer = Label(root, text='', font=("palatine", 12))
answer.pack()




# def process_Email(Gender,age, education, currentSmoker,cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes,totChol,sysBP):
#     if Gender == "male" or Gender == "Male":
#         Gender = 1
#     elif Gender == "female" or Gender == "Female":
#         Gender = 0
#     if currentSmoker == "no" or currentSmoker == "No":
#         currentSmoker = 0
#     elif currentSmoker == "yes" or currentSmoker == "Yes":
#         currentSmoker = 1
#     if BPMeds == "no" or BPMeds == "No":
#         BPMeds = 0
#     elif BPMeds == "yes" or BPMeds == "Yes":
#         BPMeds = 1
#     if prevalentStroke == "no" or prevalentStroke == "No":
#         prevalentStroke = 0
#     elif prevalentStroke == "yes" or prevalentStroke == "Yes":
#         prevalentStroke = 1
#     if prevalentHyp == "no" or prevalentHyp == "No":
#         prevalentHyp = 0
#     elif prevalentHyp == "yes" or prevalentHyp == "Yes":
#         prevalentHyp = 1
#     if diabetes == "no" or diabetes == "No":
#         diabetes = 0
#     elif diabetes == "yes" or diabetes == "Yes":
#         diabetes = 1
#     encodeNewdf = pd.DataFrame(
#         {"Gender": Gender, "Age": age, "Education": education, "CurrentSmoker": currentSmoker, "CigsPerDay": cigsPerDay,
#          "BP_Meds": BPMeds, "PrevalentStroke": prevalentStroke, "PrevalentHyp": prevalentHyp, "Diabetes": diabetes,
#          "total_Col": totChol, "sys_BP": sysBP})
#     return encodeNewdf
#     print(encodeNewdf)


# Load trained model
def load_Model(encodeNewdf):
    loadBM = pickle.load(open('heart-model1234.sav', 'rb'))
    outputPrediction = loadBM.predict(encodeNewdf)
    return outputPrediction


def make_Prediction(outputPrediction):
    #outputPredictionBM = loadBM.predict(encodeNewdf)
    #outputPredictionBM = outputPrediction;
    if outputPrediction == 0:
        TenYearCHD = "NO risk of coronary heart disease"

    elif outputPrediction == 1:
        TenYearCHD = " Risk of coronary heart disease"
    return TenYearCHD


root.mainloop()
