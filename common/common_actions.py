

class CommonActions:

    # User check the site's privacy policy checkbox and clicks the login submission button
    @staticmethod
    def accept_privacy_policy_and_submit_login_form(sb):
        sb.select_if_unselected("input[type='checkbox']")
        sb.click('button.btn-enter')
        sb.wait_for_ready_state_complete()

    # After initial authorization, user checks for side menu to appear & all its elements to be present
    @staticmethod
    def assert_side_menu_to_be_interaction_ready(sb):
        side_menu = "div.side-menu"
        menu_items = "ul.menu-list>li"
        sb.assert_element_present(side_menu)
        sb.assert_elements(menu_items)



