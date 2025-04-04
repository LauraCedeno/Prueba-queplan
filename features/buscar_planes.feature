Feature: Busqueda de planes de Isapre

  Scenario: Buscar un plan específico en QuePlan.cl
    Given que el usuario está en la página de búsqueda de planes
    When busca el plan "JEMH08" de Masvida
    Then el sistema muestra los resultados para el plan buscado

  Scenario: Buscar otro plan de Isapre
    Given que el usuario está en la página de búsqueda de planes
    When busca el plan "13-FPO300-17" de Consalud
    Then el sistema muestra los resultados para el plan buscado
