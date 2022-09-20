from dotenv import load_dotenv
import os


class LandingPage:
    # Import environment variables
    load_dotenv()

    @staticmethod
    def open_landing_page(sb):
        landing_url = os.getenv("STAGING_URL")
        sb.goto(landing_url)

    # User accepts site's cookie policy by clicking Modal Window's "Accept" button
    @staticmethod
    def accept_cookie_policy(sb):
        cookie_acceptance_button = "div.cookie>div>button"
        sb.click(cookie_acceptance_button)

    # User clicks arrow down button to scroll down
    @staticmethod
    def click_away_from_welcome_page(sb):
        arrow_down_button = "div.wrapper>button.btn"
        sb.click(arrow_down_button)

    @staticmethod
    def scroll_to_the_first_section(sb):
        description_section_login_button = "a[href='/Client/RegistrationLoginPage']>button.size-55"
        sb.scroll_to(description_section_login_button)
        sb.assert_element(description_section_login_button)

    # User sees header menu & able to use it
    @staticmethod
    def assert_header_menu_to_be_visible(sb):
        header_menu = "div.wrapper-menu"
        sb.assert_element(header_menu)
        sb.is_attribute_present(header_menu, "[class='is-visible']")

    # User chooses link for client login in the header menu and proceeds to login form
    @staticmethod
    def click_the_header_client_login_link(sb):
        client_login_button = "//span[text()='Вход клиентам']"
        sb.click(client_login_button)

    # User types his phone number to the phone input field
    @staticmethod
    def type_client_login_credentials(sb):
        test_phone_number = os.getenv("CLIENT_FAKE_PHONE_NUMBER")
        sb.focus("input[type='phone']")
        sb.type("input[type='phone']", test_phone_number)

    # User check the site's privacy policy checkbox and clicks the login submission button
    @staticmethod
    def accept_privacy_policy_and_submit(sb):
        sb.select_if_unselected("input[type='checkbox']")
        sb.click('button.btn-enter')

    # User enters one time password received by sms and proceeds further to office page
    @staticmethod
    def type_otp_code_and_proceed_further(sb):
        test_otp_code = os.getenv("CLIENT_FAKE_PHONE_OTP_CODE")
        sb.focus("input.input[required]")
        sb.type('input[required]', test_otp_code)
        sb.click('button.size-55')


