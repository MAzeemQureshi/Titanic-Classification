import pickle
import streamlit as st
import numpy as np

# Load the model
model_file = pickle.load(open('model.pkl', 'rb'))

# Function to make predictions
def pred_output(user_input):
    model_input = np.array(user_input).astype(np.float64)  # Convert input to float array
    ypred = model_file.predict(model_input.reshape(1, -1))
    return ypred[0]

def main():
    st.title("Titanic Classification - Azeem")

    # Input Variables
    passenger_class = st.text_input("Enter the passenger class: (1/2/3)")
    sex = st.text_input("Enter your sex (Male/Female): ").lower()
    age = st.text_input("Enter their age: ")
    sibsp = st.text_input("Enter their number of siblings: ")
    parch = st.text_input("Enter their number of parents/children: ")
    fare = st.text_input("Enter their ticket fare: ")
    embarked = st.text_input("Enter their Port of Embarked: (C=Cherbourg | Q=Queenstown | S=Southampton)").upper()

    # Convert inputs to appropriate types
    try:
        passenger_class = int(passenger_class)
        if sex == "male":
            sex = 0
        elif sex == "female":
            sex = 1
        else:
            sex = None

        age = float(age)
        sibsp = int(sibsp)
        parch = int(parch)
        fare = float(fare)

        if embarked == "C":
            embarked = 1
        elif embarked == "Q":
            embarked = 2
        elif embarked == "S":
            embarked = 0
        else:
            embarked = None

    except ValueError:
        st.error("Invalid input! Please enter valid numeric values for age, sibsp, parch, fare and choose from 'Male' or 'Female' for sex, and 'C', 'Q', 'S' for embarked.")
        return

    # Button to predict
    if st.button('Predict'):
        if None in [sex, embarked]:
            st.error("Invalid input! Please enter 'Male' or 'Female' for sex, and 'C', 'Q', 'S' for embarked.")
        else:
            user_input = [passenger_class, sex, age, sibsp, parch, fare, embarked]
            make_prediction = pred_output(user_input)

            if make_prediction == 0:
                make_prediction = "Not Survived :("
            elif make_prediction == 1:
                make_prediction = "Survived :)"

            st.success(make_prediction)

if __name__ == '__main__':
    main()
