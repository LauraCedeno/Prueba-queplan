from behave import given, when, then
from pages.busqueda_planes_page import BusquedaPlanesPage
from utils.config import get_driver

@given("que el usuario está en la página de búsqueda de planes")
def step_open_busqueda_planes(context):
    context.driver = get_driver()
    context.page = BusquedaPlanesPage(context.driver)
    context.page.abrir()

@when('busca el plan "{plan}" de Masvida')
@when('busca el plan "{plan}" de Consalud')
def step_buscar_plan(context, plan):
    context.page.buscar_plan(plan)

@then("el sistema muestra los resultados para el plan buscado")
def step_verificar_resultado(context):
    pass

def after_scenario(context, scenario):
    context.driver.quit()