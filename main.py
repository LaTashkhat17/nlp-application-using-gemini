import google.generativeai as genai


class NLPModel:
    try:
        def get_model(self):
            GOOGLE_API_KEY = "AIzaSyAZwDV4ELT5trTDBJ54ks3pyY6UtAWTmfA"
            genai.configure(api_key=GOOGLE_API_KEY)
            model = genai.GenerativeModel("gemini-2.0-flash")
            return model
    except Exception as e:
        print(f"Error configuring the model: {e}")
    
class NLPApp(NLPModel):
    def __init__(self):
        self.__database = {}
        self.__main_menu()

    def __main_menu(self):
        first_input = input("""
        Welcome to the NLP Application!
        Please choose an option:
                            1.Not Registered User?Register Here
                            2.Registered User?Login Here
                            3.Exit
                            
        """)

        if first_input == '1':
            self.__register_user()
        elif first_input == '2':
            self.__login_user()
        elif first_input == '3':
            print("Exiting the application. Goodbye!")
            exit()

    def __second_menu(self):
        second_input = input("""
        Please choose an NLP task:
                            1.Language Translation
                            2.Sentiment Analysis
                            3.Language Detection
                            3.Exit
        """)

        if second_input == '1':
            self.__language_translation()   
        elif second_input == '2':
            self.__sentiment_analysis()
        elif second_input == '3':
            self.__language_detection() 
        elif second_input == '4':
            print("Exiting the application. Goodbye!")
            exit()

    def __register_user(self):
        username = input("Enter a username for registration: ")

        # Check username
        if username in self.__database:
            print("Username already exists. Please try logging in.")
            self.__login_user()
            return

        email = input("Enter your email for registration: ")

        # Check email
        for user, info in self.__database.items():
            if info["email"] == email:
                print("Email already registered. Please try logging in.")
                self.__login_user()
                return

        # Register new user
        password = input("Enter a password for registration: ")
        self.__database[username] = {'email': email, 'password': password}
        print("Registration successful! You can now log in.")
        self.__second_menu()

    def __login_user(self):
        username = input("Enter your username to login: ")
        password = input("Enter your password to login: ")

        # Validate credentials
        if username in self.__database and self.__database[username]['password'] == password:
            print(f"Login successful! Welcome back, {username}.")
            self.__nlp_menu()
        else:
            print("Invalid username or password. Please try again.")
            self.__main_menu()
    
    def __sentiment_analysis(self):
        user = input("Enter the text you want to translate: ")
        model = super().get_model()
        response = model.generate_content(
            f"Analyze the sentiment of the following text: {user}",)
        results = response.text
        print(f"Sentiment Analysis Result: {results}")
        self.__second_menu()

    def __language_translation(self):
        user = input("Enter the text you want to translate: ")
        model = super().get_model()
        response = model.generate_content(
            f"Translate the following text to Bangla: {user}",)
        results = response.text
        print(f"Translation Result: {results}") 
        self.__second_menu()
    
    def __language_detection(self):
        user = input("Enter the text for language detection: ")
        model = super().get_model()
        response = model.generate_content(
            f"Detect the language of the following text: {user}",)
        results = response.text
        print(f"Language Detection Result: {results}")
        self.__second_menu()



if __name__ == "__main__":
    app = NLPApp()