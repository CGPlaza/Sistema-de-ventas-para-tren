Sistema de Gestión de Ventas de Trenes

![Python](https://img.shields.io/badge/python-3.x-blue.svg) ![Status](https://img.shields.io/badge/status-terminado-green.svg) ![POO](https://img.shields.io/badge/diseño-POO-orange.svg)

Sistema para la administración de ventas en transporte ferroviario, emisión de boletos y control financiero, desarrollado bajo estándares de **Programación Orientada a Objetos**.


**Documentación Técnica**
Puedes ver el informe completo de diseño y diagrama UML aquí:
 [Ver Informe PDF](documentacion%20tecnica/informe.pdf)


**Características Principales**
El sistema simula un entorno de producción real implementando lógica de negocio compleja:
 Integridad de Datos:
    * **Identificadores Únicos:** Emisión de boletos con UUID para garantizar unicidad y trazabilidad.
    * **Validaciones Regionales:** Algoritmo de verificación de **RUT Chileno** y formato de correo electrónico.
 Gestión de Flotas:
    * Administración de múltiples categorías (Primera Clase, Salón, Económica).
    * Control de stock y disponibilidad de asientos en tiempo real.
 Módulo Financiero:
    * Cierre de caja automatizado.
    * Reportes de ventas totales y desglosados por categoría.
    * Cálculo de recaudación total.
