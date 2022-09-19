class LandingPage:

    # User accepts site's cookie policy by clicking Modal Window's "Accept" button
    def accept_cookie_policy(self, sb):
        cookie_acceptance_button = "div.cookie>div>button"
        sb.click(cookie_acceptance_button)

    # User clicks arrow down button to scroll down
    def click_away_from_welcome_page(self, sb):
        arrow_down_button = "div.wrapper>button.btn"
        sb.click(arrow_down_button)

    def click_the_header_client_login_link(self, sb):
        client_login_button = "//span[text()='Вход клиентам']"
        sb.click(client_login_button)

    def type_client_login_credentials(self, sb):
        sb.focus("input[type='phone']")
        sb.type("input[type='phone']", "9999999999")

    def accept_privacy_policy_and_submit(self, sb):
        sb.select_if_unselected("input[type='checkbox']")
        sb.click('button.btn-enter')

    def type_otp_code_and_proceed_further(self, sb):
        sb.focus("input.input[required]")
        sb.type('input[required]', '0000')
        sb.click('button.size-55')


