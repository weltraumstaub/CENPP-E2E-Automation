from seleniumbase import BaseCase
from pages.landing_page import LandingPage


class HomePage(BaseCase):

    def test_client_login(self):

        # Given user opens the landing page
        self.goto("https://stage.psyedge.ru/")

        # Then reads and accepts the site's cookie policy
        LandingPage().accept_cookie_policy(self)

        # Then clicks away from the welcoming section using arrow button
        LandingPage().click_away_from_welcome_page(self)

        # Then clicks at client login form link in header
        LandingPage().click_the_header_client_login_link(self)

        # Then types phone number into the input field
        LandingPage().type_client_login_credentials(self)

        # Then user accepts site's privacy policy and presses login button
        LandingPage().accept_privacy_policy_and_submit(self)

        # Then user enters received by sms one time password and proceeds to login by clicking submit button
        LandingPage().type_otp_code_and_proceed_further(self)

        self.assert_text('Личный кабинет', 'h1')


