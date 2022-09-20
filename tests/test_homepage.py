from seleniumbase import BaseCase

from pages.psychologist_pages.profile_page import ProfilePage
from pages.shared_pages.landing_page import LandingPage
from pages.client_pages.client_login_page import ClientLoginPage
from pages.psychologist_pages.psychologist_login_page import PsychologistLoginPage
from common.common_actions import CommonActions


class HomePage(BaseCase):

    def test_client_login(self):
        # Initiating Landing & Client Login Pages. Making Common Actions Available
        landing_page = LandingPage()
        login_page = ClientLoginPage()
        common_actions = CommonActions()

        # Given client opens the landing page
        landing_page.open_landing_page(self)

        # Then reads and accepts the site's cookie policy
        landing_page.accept_cookie_policy(self)

        # Then clicks away from the welcoming section using arrow button
        landing_page.click_away_from_welcome_page(self)

        # Then client scrolls to read the description section content and sees button to login
        landing_page.scroll_to_the_first_section(self)

        # And header menu appears to be visible
        landing_page.assert_header_menu_to_be_visible(self)

        # Then clicks at client login form link in header and ends up at the client authorization page
        landing_page.click_the_header_client_login_link(self)

        # Then types phone number into the input field
        login_page.type_client_login_credentials(self)

        # Then client accepts site's privacy policy and presses login button
        common_actions.accept_privacy_policy_and_submit_login_form(self)

        # Then user enters received by sms one time password and proceeds to login by clicking submit button
        login_page.type_otp_code_and_proceed_further(self)

        self.assert_text('Личный кабинет', 'h1')

    def test_psychologist_login(self):

        # Initiating Common Landing Page & Psychologist Login Page, as well as Common Actions
        landing_page = LandingPage()
        login_page = PsychologistLoginPage()
        common_actions = CommonActions()
        profile_page = ProfilePage()

        # Given psychologist opens the landing page
        landing_page.open_landing_page(self)

        # Then reads and accepts the site's cookie policy
        landing_page.accept_cookie_policy(self)

        # Then clicks away from the welcoming section using arrow button
        landing_page.click_away_from_welcome_page(self)

        # Then psychologist scrolls to read the description section content and sees button to login
        landing_page.scroll_to_the_first_section(self)

        # And header menu appears to be visible
        landing_page.assert_header_menu_to_be_visible(self)

        # Then clicks at psychologist login link in the header and navigates to psychologist login form
        landing_page.click_the_header_psychologist_login_link(self)

        # Then psychologist types email into the login input field
        login_page.type_email_in_the_login_field(self)

        # Then psychologist types password into the password input field
        login_page.type_password_in_the_input_field(self)

        # Then psychologist marks site's policy checkbox and submits login form
        common_actions.accept_privacy_policy_and_submit_login_form(self)

        # Then assert side menu to appear after logging in
        common_actions.assert_side_menu_to_be_interaction_ready(self)

        # Finally assert to be on the personal profile page
        profile_page.assert_to_be_on_the_profile_page(self)






