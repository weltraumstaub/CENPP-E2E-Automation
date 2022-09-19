from seleniumbase import BaseCase

class HomePage(BaseCase):


    def test_client_registration(self):

        self.open("https://stage.psyedge.ru/")

        self.click("button.primary.size-55")
        
        self.click("button[data-v-11dd0570]")

        self.scroll_to_bottom()

        self.assert_element_present("div.wrapper-menu")

        self.click("div.menu-login-link>a[href='/Client/RegistrationLoginPage']")
    
        self.assert_text("Вход в систему", "h1")

        self.focus("input[type='phone']")
        
        self.type("input[type='phone']", "9999999999")

        self.select_if_unselected("input[type='checkbox']")

        self.click('button.btn-enter')

        self.focus("input.input[required]")

        self.type('input[required]', '0000')

        self.click('button.size-55')

        self.assert_text('Личный кабинет', 'h1')
