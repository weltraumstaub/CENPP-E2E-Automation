from dotenv import load_dotenv
import os


class PsychologistLoginPage:
    # Import environment variables
    load_dotenv()

    @staticmethod
    def type_email_in_the_login_field(sb):
        test_psychologist_email = os.getenv("PSYCHOLOGIST_TEST_LOGIN")
        login_input_field = "input[type='email']"
        sb.focus(login_input_field)
        sb.type(login_input_field, test_psychologist_email)

    @staticmethod
    def type_password_in_the_input_field(sb):
        test_psychologist_password = os.getenv("PSYCHOLOGIST_TEST_PASSWORD")
        password_input_field = "input[type='password']"
        sb.focus(password_input_field)
        sb.type(password_input_field, test_psychologist_password)







