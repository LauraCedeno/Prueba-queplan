from behave import given, when, then
from pages.mejor_plan_page import MejorPlanPage
from utils.config import get_driver

@given('que el usuario está en la página "Tu Mejor Plan"')
def step_open_mejor_plan(context):
    context.driver = get_driver()
    context.page = MejorPlanPage(context.driver)
    context.page.abrir()

@when("completa el formulario con sus datos")
def step_completar_formulario(context):
    for row in context.table:
        context.page.completar_datos(
            row["Plan"], row["Codigo Plan"], row["Pago Actual"], row["Region"],
            row["Prestador"], row["Edad"], row["Ingreso"], row["Email"]
        )

@then("el sistema recomienda el mejor plan disponible")
def step_verificar_recomendacion(context):
    # Aquí puedes agregar validaciones
    pass

def after_scenario(context, scenario):
    context.driver.quit()
