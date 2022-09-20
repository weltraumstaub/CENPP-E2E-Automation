from dotenv import load_dotenv
import os


class ClientLoginPage:
    # Import environment variables
    load_dotenv()

    # User types his phone number to the phone input field
    @staticmethod
    def type_client_login_credentials(sb):
        test_phone_number = os.getenv("CLIENT_FAKE_PHONE_NUMBER")
        sb.focus("input[type='phone']")
        sb.type("input[type='phone']", test_phone_number)

    # User enters one time password received by sms and proceeds further to office page
    @staticmethod
    def type_otp_code_and_proceed_further(sb):
        test_otp_code = os.getenv("CLIENT_FAKE_PHONE_OTP_CODE")
        sb.focus("input.input[required]")
        sb.type('input[required]', test_otp_code)
        sb.click('button.size-55')
