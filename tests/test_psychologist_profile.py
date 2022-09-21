from helper_functions.helpers import HelperFunctions
from pages.psychologist_pages.profile_page import ProfilePage
from common.common_actions import CommonActions
from seleniumbase import BaseCase


class PsychologistProfilePage(BaseCase):

    def test_all_profile_sections(self):
        helper_functions = HelperFunctions()
        profile_page = ProfilePage()
        common_actions = CommonActions()

        # Given psychologist authorized in system
        helper_functions.perform_psychologist_login(self)

        # Then psychologists checks side menu elements to make sure page is fully loaded
        common_actions.assert_side_menu_to_be_interaction_ready(self)

        # Then psychologist makes sure he ended up in personal profile page
        profile_page.assert_being_on_the_profile_page(self)

        # Then psychologist makes sure the information in about section is rendered
        profile_page.assert_about_section_elements(self)

        # Then psychologist checks his profile photo and personal info in the card info
        profile_page.assert_personal_info_section_elements(self)

        # Then psychologist looks at his calendar to make sure it has been rendered correctly
        profile_page.assert_calendar_widget_to_be_present(self)

        # Finally psychologist makes sure all of his articles and article images are visible
        profile_page.assert_article_section_to_render(self)

    def test_basic_profile_edit(self):
        pass
