Feature: Verificación del mejor plan de Isapre

  Scenario: Completar el formulario de mejor plan
    Given que el usuario está en la página "Tu Mejor Plan"
    When completa el formulario con sus datos:
      |Plan          | Codigo Plan | Pago Actual | Region        | Prestador         | Edad | Ingreso  | Email                 |
      |Nueva Masvida | JEMH08        | 4 UF      | Metropolitana | Redsalud Vitacura | 37   | 1500000  | prueba@queplan.cl     |
    Then el sistema recomienda el mejor plan disponible
