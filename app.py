import streamlit as st
import random
import json

# Define the path for the data file
FILE_PATH = './data.json'

class Quiz:
    def __init__(self):
        # Initialize user and quiz data from session state or defaults
        self.__users = st.session_state.get('users', {})
        self.__current_user = st.session_state.get('current_user', None)
        self.__quiz_list = {}
        self.load_data()

    def user_registration(self, name, username, email, user_class, password):
        if username in self.__users:
            st.error('User Already Exists')
            return

        # Load data from JSON file
        with open(FILE_PATH, "r") as json_file:
            data = json.load(json_file)

        # Update users in the file and session state
        data["users"][username] = {
            "name": name,
            "email": email,
            "class": user_class,
            "pwd": password
        }

        self.__users = data["users"]
        st.session_state.users = self.__users

        with open(FILE_PATH, "w") as json_file:
            json.dump(data, json_file, indent=4)

        st.success('User Successfully Registered')

    def user_login(self, username, password):
        if username in self.__users and self.__users[username]['pwd'] == password:
            st.session_state["Logged"] = True
            st.session_state["current_user"] = username
            st.success(f'Login Successful. Welcome, {username}!')
        else:
            st.error('Invalid Credentials')

    def user_logout(self):
        st.session_state["Logged"] = False
        st.session_state["current_user"] = None
        st.info('Logged out successfully.')

    def load_data(self):
        # Load user and quiz data from the JSON file
        with open(FILE_PATH, "r") as json_file:
            data = json.load(json_file)

        st.session_state['users'] = data['users']
        self.__quiz_list = data['questions']

    def start_quiz(self):
        st.success('Quiz Started')

        col1, col2 = st.columns(2)
        with col1:
            subj = st.radio(
                "Select Subject",
                ["DSA", "DBMS", "PYTHON"],
                captions=["Data Structures and Algorithms", "Database Management Systems", "Python Programming Language"]
            )

            if 'ques' not in st.session_state:
                st.session_state['ques'] = random.sample(list(self.__quiz_list[subj]), 5)

            if st.button("Randomize Questions", use_container_width=True):
                st.session_state['ques'] = random.sample(list(self.__quiz_list[subj]), 5)

            st.button("Logout", on_click=self.user_logout, use_container_width=True)

        with col2:
            self.list_questions(subj, st.session_state['ques'])

    def list_questions(self, subj, questions):
        score = 0
        answers = []

        for question in questions:
            selected_answer = st.radio(
                self.__quiz_list[subj][question]['ques'],
                self.__quiz_list[subj][question]['opt'],
                # index=-1,
                key=f"question_{question}"
            )
            answers.append((selected_answer, self.__quiz_list[subj][question]['ans']))

        if st.button("Submit", use_container_width=True):
            score = sum(1 for user_ans, correct_ans in answers if user_ans == correct_ans)
            st.write(f"Your Total Score is: {score}")

if __name__ == "__main__":
    st.markdown("""
    # 🌌 **Welcome to Galactic Quiz!** 🚀

    ✨ **Unleash Your Knowledge Across the Universe!** ✨  
    Are you ready to challenge your mind and explore diverse galaxies of trivia?  
    Whether it's science, history, or pop culture, **Galactic Quiz** takes you on an interstellar journey through knowledge.  

    > 🌠 **Galactic Quiz - Your Ultimate Journey Through Knowledge!**
    """)

    quiz_app = Quiz()

    # Show login or quiz interface based on user session state
    if st.session_state.get("Logged", False):
        quiz_app.start_quiz()
    else:
        st.header("Login or Registration")
        col1, col2 = st.columns(2)

        with col1:
            user_opt = st.radio(
                "Choose one",
                ["Login", "Registration"],
                key="login_radio"
            )

        with col2:
            if user_opt == "Login":
                username = st.text_input(label='Username', key="login_username")
                password = st.text_input(label='Password', type='password', key="login_password")
                st.button("Login", on_click=quiz_app.user_login, args=(username, password))

            elif user_opt == "Registration":
                name = st.text_input(label='Name', key="register_name")
                username = st.text_input(label='Username', key="register_username")
                email = st.text_input(label='Email', key="register_email")
                user_class = st.text_input(label='Class', key="register_class")
                password = st.text_input(label='Password', type='password', key="register_password")
                st.button("Register", on_click=quiz_app.user_registration, args=(name, username, email, user_class, password))
