from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from pages.base_page import BasePage

class MejorPlanPage(BasePage):
    URL = "https://queplan.cl/Tu-Mejor-Plan"

    SELECT_PLAN_ACTUAL = (By.XPATH, "//mat-select[contains(@id, 'mat-select')]")
    CODIGO_PLAN = (By.XPATH, "//input[@id='mat-input-4']")
    COD = (By.XPATH, "//span[@class='text-capitaliz name']")
    INPUT_UF = (By.XPATH, "//input[@id='mat-input-21']")
    SELECT_REGION = (By.ID, "region")
    SELECT_PRESTADOR = (By.ID, "prestador")
    INPUT_EDAD = (By.ID, "edad")
    INPUT_INGRESO = (By.ID, "ingreso")
    INPUT_EMAIL = (By.ID, "email")
    BTN_ENVIAR = (By.ID, "btn-enviar")

    def abrir(self):
        """Abre la página de 'Tu Mejor Plan'."""
        self.driver.get(self.URL)

    def completar_datos(self, plan, codigo, uf, region, prestador, edad, ingreso, email):

        # Click en el dropdown del plan
        self.wait.until(EC.element_to_be_clickable(self.SELECT_PLAN_ACTUAL)).click()
        time.sleep(1)  # Breve pausa para que carguen las opciones
        plan_xpath = f"//mat-option//span[contains(text(), '{plan}')]"

        # Esperar a que la opción del plan sea visible e interactuable
        plan_element = self.wait.until(EC.presence_of_element_located((By.XPATH, plan_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView();", plan_element)
        time.sleep(1)  # Espera para que el scroll se complete

        try:
            plan_element.click()
        except:
            self.driver.execute_script("arguments[0].click();", plan_element)  # Click con JS si el normal falla

        # Completar los otros campos del formulario
        self.write(*self.CODIGO_PLAN, codigo)
        self.click(*self.COD)
        time.sleep(3)
        self.click(*self.INPUT_UF, uf)
        self.write(*self.INPUT_EDAD, edad)
        self.write(*self.INPUT_INGRESO, ingreso)
        self.write(*self.INPUT_EMAIL, email)

        # Seleccionar región
        self.click(*self.SELECT_REGION)
        region_xpath = (By.XPATH, f"//option[contains(text(), '{region}')]")
        self.wait.until(EC.element_to_be_clickable(region_xpath)).click()

        # Seleccionar prestador
        self.click(*self.SELECT_PRESTADOR)
        prestador_xpath = (By.XPATH, f"//option[contains(text(), '{prestador}')]")
        self.wait.until(EC.element_to_be_clickable(prestador_xpath)).click()

        # Enviar formulario
        self.click(*self.BTN_ENVIAR)

