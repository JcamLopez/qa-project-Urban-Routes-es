import data
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    phone = (By.ID, 'phone')
    number_card = (By.ID, 'number')
    call_taxi = (By.CSS_SELECTOR, 'button.button.round')
    comfort = (By.CSS_SELECTOR, 'img[alt="Comfort"]')
    button_open_phone = (By.XPATH, '//div[text()="Número de teléfono"]')
    next_button_phone = (By.CSS_SELECTOR, 'button.button.full')
    code_input = (By.ID, 'code')
    button_confirm_phone = (By.XPATH, '//button[text()="Confirmar"]')
    code_card = (By.CSS_SELECTOR, '.card-code-input input')
    button_method_pay = (By.CLASS_NAME, 'pp-text')
    form_card = (By.CLASS_NAME,'card-wrapper')
    select_card = (By.XPATH, '//div[text()="Agregar tarjeta"]')
    button_add_card_submit = (By.XPATH, '//button[text()="Agregar"]')
    button_close_modal = (By.CSS_SELECTOR, '.payment-picker .close-button')
    comment_field_driver = (By.ID, 'comment')
    counter_plus_button_ice = (By.CSS_SELECTOR, '.counter-plus')
    blanket_tissues_switch = (By.CSS_SELECTOR, '.slider.round')
    send_button = (By.CSS_SELECTOR, 'button.smart-button')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.from_field)
        )
        self.driver.find_element(*self.from_field).send_keys(from_address)
        time.sleep(2)

    def set_to(self, to_address):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.to_field)
        )
        self.driver.find_element(*self.to_field).send_keys(to_address)
        time.sleep(2)

    def clic_to_call_taxi(self):
        taxi = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.call_taxi)
        )
        taxi.click()
        time.sleep(2)

    def select_comfort(self):
        com = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.comfort)
        )
        com.click()
        time.sleep(2)

    def add_phone_number(self, number_phone):
        open_win_phone = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_open_phone)
        )
        open_win_phone.click()
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.phone)
        )
        self.driver.find_element(*self.phone).send_keys(number_phone)
        time.sleep(2)
        next = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.next_button_phone)
        )
        next.click()
        time.sleep(2)

    def confirm_phone_code(self):
        sms_code = retrieve_phone_code(self.driver)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.code_input)
        )
        self.driver.find_element(*self.code_input).send_keys(sms_code)
        confirm = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_confirm_phone)
        )
        confirm.click()
        time.sleep(2)

    def add_card(self, card_num, card_cod):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_method_pay)
        )
        button.click()
        time.sleep(2)

        card = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.select_card)
        )
        card.click()
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.number_card)
        )
        self.driver.find_element(*self.number_card).send_keys(card_num)
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.code_card)
        )
        self.driver.find_element(*self.code_card).send_keys(card_cod)
        time.sleep(2)
        form = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.form_card)
        )
        form.click()
        time.sleep(2)

        add = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_add_card_submit)
        )
        add.click()
        time.sleep(2)

        close = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_close_modal)
        )
        close.click()


    def comment_driver(self, comment):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.comment_field_driver)
        )
        self.driver.find_element(*self.comment_field_driver).send_keys(comment)
        time.sleep(2)

    def select_blanket_and_tissues(self):
        switch = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.blanket_tissues_switch)
        )
        switch.click()
        time.sleep(3)

    def select_ice(self):
        for i in range(2):
            ice = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.counter_plus_button_ice)
            )
            ice.click()
            time.sleep(2)

    def search_driver(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.send_button)
        )
        button.click()
        time.sleep(15)

    def set_route(self, from_address, to_address, number_phone, card_number, code_card,comment):
        self.set_from(from_address)
        self.set_to(to_address)
        self.clic_to_call_taxi()
        self.select_comfort()
        self.add_phone_number(number_phone)
        self.confirm_phone_code()
        self.add_card(card_number, code_card)
        self.comment_driver(comment)
        self.select_blanket_and_tissues()
        self.select_ice()
        self.search_driver()

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = webdriver.ChromeOptions()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        number_phone = data.phone_number
        card_number = data.card_number
        card_code = data.card_code
        comment_driver = data.message_for_driver
        routes_page.set_route(address_from, address_to, number_phone, card_number, card_code,comment_driver)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
