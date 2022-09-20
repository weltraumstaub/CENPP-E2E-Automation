class CommonActions:

    # User check the site's privacy policy checkbox and clicks the login submission button
    @staticmethod
    def accept_privacy_policy_and_submit_login_form(sb):
        sb.select_if_unselected("input[type='checkbox']")
        sb.click('button.btn-enter')
