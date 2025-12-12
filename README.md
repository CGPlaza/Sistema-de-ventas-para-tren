Sistema de Gestión de Ventas de Trenes

![Python](https://img.shields.io/badge/python-3.x-blue.svg) ![Status](https://img.shields.io/badge/versión-1.0_(extensible)-blue.svg) ![POO](https://img.shields.io/badge/diseño-POO-orange.svg)

Sistema para la administración de ventas en transporte ferroviario, emisión de boletos y control financiero, desarrollado bajo estándares de **Programación Orientada a Objetos**.


**Documentación Técnica**
Puedes ver el informe completo de diseño y diagrama UML aquí:
 [Ver Informe PDF](documentacion%20tecnica/informe.pdf)


**Características Principales**
El sistema gestiona el ciclo completo del servicio de transporte, aplicando validaciones específicas para asegurar el orden operativo:

* **Integridad de Datos:**
  * **Identificadores Únicos:** Emisión de tickets asignando un identificador exclusivo a cada pasajero.
  * **Validaciones Regionales:** Algoritmo de verificación **RUT Chileno** y formato de correo electrónico.

* **Gestión de Flotas:**
  * Administración de viajes en múltiples categorías (Primera Clase, Salón, Económica).
  * Control y registro de capacidad y disponibilidad de asientos en tiempo real.

* **Módulo Financiero:**
  * Cierre de caja automatizado.
  * Reportes de recaudación total y ventas desglosadas por categoría de servicio.
