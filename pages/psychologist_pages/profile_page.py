class ProfilePage:

    @staticmethod
    def assert_to_be_on_the_profile_page(sb):
        page_title = "h1.title"
        current_url = sb.get_current_url()
        sb.assertEqual("https://stage.psyedge.ru/Client/Profile/", current_url)
        sb.assert_text("Моя страница", page_title)

    @staticmethod
    def assert_about_section_elements(sb):
        section_header = "section.about>h2.title"
        about_myself = "section.about>h3"
        work_experience = "//div[@class='info']/h3[text()='Опыт работы']"
        education = "//div[@class='info']/h3[text()='Образование']"
        qualification = "//div[@class='info']/h3[text()='квалификация']"
        sb.assert_elements_present(section_header, about_myself, work_experience, education, qualification)

    @staticmethod
    def assert_personal_info_section_elements(sb):
        pass

    @staticmethod
    def assert_calendar_widget_to_be_present(sb):
        pass

    @staticmethod
    def assert_article_section_to_render(sb):
        pass

