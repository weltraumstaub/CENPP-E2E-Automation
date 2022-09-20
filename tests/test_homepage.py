from seleniumbase import BaseCase
from pages.client_pages.landing_page import LandingPage


class HomePage(BaseCase):

    def test_client_login(self):
        # Initiating Landing Page
        landing_page = LandingPage()

        # Given user opens the landing page
        landing_page.open_landing_page(self)

        # Then reads and accepts the site's cookie policy
        landing_page.accept_cookie_policy(self)

        # Then clicks away from the welcoming section using arrow button
        landing_page.click_away_from_welcome_page(self)

        # Then users scrolls to read the description section content and sees button to login
        landing_page.scroll_to_the_first_section(self)

        # And header menu appears to be visible
        landing_page.assert_header_menu_to_be_visible(self)

        # Then clicks at client login form link in header
        landing_page.click_the_header_client_login_link(self)

        # Then types phone number into the input field
        landing_page.type_client_login_credentials(self)

        # Then user accepts site's privacy policy and presses login button
        landing_page.accept_privacy_policy_and_submit(self)

        # Then user enters received by sms one time password and proceeds to login by clicking submit button
        landing_page.type_otp_code_and_proceed_further(self)

        self.assert_text('Личный кабинет', 'h1')


