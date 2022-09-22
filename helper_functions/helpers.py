from pages.psychologist_pages.psychologist_login_page import PsychologistLoginPage
from pages.client_pages.client_login_page import ClientLoginPage
from common.common_actions import CommonActions
from dotenv import load_dotenv
from pathlib import Path
import os
import random


class HelperFunctions:
    # Import environment variables
    load_dotenv()

    @staticmethod
    def perform_client_login(sb):
        login_page = ClientLoginPage()
        common_actions = CommonActions()
        sb.get(f"{os.getenv('STAGING_URL')}/Client/RegistrationLoginPage")
        login_page.type_client_login_credentials(sb)
        common_actions.accept_privacy_policy_and_submit_login_form(sb)
        login_page.type_otp_code_and_proceed_further(sb)

    @staticmethod
    def perform_psychologist_login(sb):
        login_page = PsychologistLoginPage()
        common_actions = CommonActions()
        sb.get(f"{os.getenv('STAGING_URL')}/Client/LoginPage")
        login_page.type_email_in_the_login_field(sb)
        login_page.type_password_in_the_input_field(sb)
        common_actions.accept_privacy_policy_and_submit_login_form(sb)

    # Assertion will probably fail when multiple files are uploaded.
    # There's need to either refactor the method later :preferable
    # Or write a new method to handle multiple upload & assert name correctly
    # Upload file to file input & verify name after upload
    @staticmethod
    def upload_test_file_to_input(sb, input_selector):
        # Get project root directory to upload files form
        project_root = Path(__file__).parent.parent

        # List of currently used test files in test_files folder
        test_file_names = ["annapurna.jpg", "forest.jpg", "session.jpeg"]

        # Choose file from test files folder to use in uploads
        upload_file_name = random.choice(test_file_names)

        # Define path to randomly chosen file to use in input uploads
        file_path = os.path.join(project_root, f"test_files\\{upload_file_name}")

        # Upload file to the chosen file input
        sb.choose_file(input_selector, file_path)

        # Selector for file name element after upload has been completed
        uploaded_file_name_value = "div>div>div.file-info>p>span.file-name"

        # Assert that displayed file name is identical to uploaded file name
        sb.assert_text(upload_file_name, uploaded_file_name_value)
