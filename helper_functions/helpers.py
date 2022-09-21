from pages.psychologist_pages.psychologist_login_page import PsychologistLoginPage
from pages.client_pages.client_login_page import ClientLoginPage
from common.common_actions import CommonActions
from dotenv import load_dotenv
import os


class HelperFunctions:
    # Import environment variables
    load_dotenv()

    @staticmethod
    def perform_client_login(sb):
        login_page = ClientLoginPage()
        common_actions = CommonActions()
        sb.get(os.getenv("CLIENT_LOGIN_URL"))
        login_page.type_client_login_credentials(sb)
        common_actions.accept_privacy_policy_and_submit_login_form(sb)
        login_page.type_otp_code_and_proceed_further(sb)

    @staticmethod
    def perform_psychologist_login(sb):
        login_page = PsychologistLoginPage()
        common_actions = CommonActions()
        sb.get(os.getenv("PSYCHOLOGIST_LOGIN_URL"))
        login_page.type_email_in_the_login_field(sb)
        login_page.type_password_in_the_input_field(sb)
        common_actions.accept_privacy_policy_and_submit_login_form(sb)

