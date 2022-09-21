from dotenv import load_dotenv
import os


class ProfilePage:
    # Import environment variables
    load_dotenv()

    @staticmethod
    def assert_being_on_the_profile_page(sb):
        page_title = "h1.title"
        current_url = sb.get_current_url()
        sb.assert_equal(f"{os.getenv('STAGING_URL')}/Client/Profile/", current_url)
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
        profile_photo = "div.imgs>div>img"
        profile_name = "section.photo>h2"
        work_experience = "section.photo>div.box>p.experience"
        profile_age = "section.photo>div.box>p.age"
        session_info = "section.photo>div.price-box"
        session_price_value = "section.photo>div.price-box>span.price-value"
        session_duration_time = "section.photo>div.price-box>p>span.duration-value"
        sb.assert_elements_present(profile_photo, profile_name, profile_age,
                                   work_experience, session_info,
                                   session_duration_time, session_price_value)
        sb.assert_not_equal(session_price_value, "undefined")
        sb.assert_not_equal(session_duration_time, "null")

    @staticmethod
    def assert_calendar_widget_to_be_present(sb):
        calendar_widget = "div.calendar-small"
        calendar_info_text = "p.calendar-text"
        calendar_dates_wheel = "div.calendar-small>div.header"
        calendar_items_body = "div.calendar-small>div.body"
        sb.assert_elements_present(calendar_widget, calendar_info_text, calendar_dates_wheel, calendar_items_body)
        sb.assert_text("Ваши текущие записи на этой неделе:", calendar_info_text)

    @staticmethod
    def assert_article_section_to_render(sb):
        articles_block = "div.box>div.wrapper"
        articles_header = "div.box>div.wrapper>h2"
        articles_box = "div.box>div.wrapper>div.articles"
        sb.assert_elements_present(articles_block, articles_header, articles_box)
        sb.assert_text("Материалы специалиста", articles_header)

    @staticmethod
    def navigate_to_profile_edit_page(sb):
        profile_edit_button = "div.edit-btn>button"
        sb.click(profile_edit_button)
        sb.assert_equal(f"{os.getenv('STAGING_URL')}/Client/Profile/edit", sb.get_current_url())
        sb.assert_text("Редактирование страницы", "h1.title")




