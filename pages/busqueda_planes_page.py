from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BusquedaPlanesPage(BasePage):
    URL = "https://queplan.cl/buscar"

    INPUT_BUSQUEDA = (By.XPATH, "//input[@placeholder='Plan a buscar...']")
    BTN_BUSCAR = (By.XPATH, "//button[@type='button']//fa-icon[@class='ng-fa-icon']//*[name()='svg']")
    RESULTADO_LOCATOR = (By.CSS_SELECTOR, "h3.title-insurance-movil")

    def abrir(self):
        self.driver.get(self.URL)

    def buscar_plan(self, plan):
        self.write(*self.INPUT_BUSQUEDA, plan)
        self.click(*self.BTN_BUSCAR)

        # Esperar a que aparezca algún resultado de la búsqueda
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.RESULTADO_LOCATOR)
        )