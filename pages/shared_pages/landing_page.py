from dotenv import load_dotenv
import os


class LandingPage:
    # Import environment variables
    load_dotenv()

    # User opens the URL and lands on the welcoming screen of the landing page
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

    # User chooses link for client login in the header menu and proceeds to client login form
    @staticmethod
    def click_the_header_client_login_link(sb):
        client_login_button = "//span[text()='Вход клиентам']"
        sb.click(client_login_button)

    # User chooses link for psychologist login in the header menu and proceeds to psychologist login form
    @staticmethod
    def click_the_header_psychologist_login_link(sb):
        client_login_button = "//span[text()='Вход специалистам']"
        sb.click(client_login_button)

