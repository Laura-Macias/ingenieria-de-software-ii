# **Documentacion Frontend**
Este archivo contiene la documentación relacionada con la implementación del Frontend. En esta implementación se detalla lo siguiente:

1. [Template de inspiracion](##Template-de-inspiracion)
2. [Estructura HTML](#Estructura-HTML)
3. [Implementacion visual con CSS](#Implementacion-visual-con-CSS)
4. [Funcionalidades JavaScrip](#Funcionalidades-JavaScrip)
5. [Implementacion responsive](#Implementacion-responsive)
6. [Correcion de errores](#Correcion-de-errores)
7. [ajustes de diseño y funciones](#ajustes-de-diseño-y-funciones)
8. [implementacion Sing up y Login](#implementacion-Sing-up-y-Login)

# **Documentacion Frontend V 0.1**
## Lista de Ítems

## **Template de inspiracion**
En esta fase inicial del proyecto, para la parte del frontend, nos dedicamos a buscar inspiración en diferentes templates de varios negocios; sin embargo, no nos convenció ninguno, así que decidimos crear un template desde cero, usando detalles similares que encontramos en otros templates.

<img src="https://cdn.dribbble.com/users/359023/screenshots/3142624/57574_drib.png?resize=400x0" alt="Template" width="300">

## **Estructura HTML**
En esta fase se creó una estructura HTML que incluye toda la página principal, con diferentes secciones como menú, inicio, mapa, información y precios. Los enlaces al CSS se ubican en la parte del head, y los enlaces a los scripts de JavaScript están en el body.

## **Implementacion visual con CSS**
En esta fase se diseñó toda la estructura HTML. Se utilizó una paleta de colores pastel combinada con colores oscuros para resaltar los botones principales. También se diseñó un fondo con una imagen de un diseño de uñas realizado en el spa. En la sección de "Ubicación" se añadió un mapa extraído de la API de Google Maps. En la sección de "Precios" se decoraron dos listados con diferentes combos, los cuales tienen una animación al apuntar el cursor sobre ellos.

## **Funcionalidades JavaScrip**
En esta fase se implementó la interacción que tendrá la página con el usuario. Se añadió una funcionalidad para que el mapa pueda usarse directamente desde la página, sin necesidad de redirigir al usuario a Google Maps.

# **Documentacion Frontend V 0.2**
Con la estructura, el diseño y las funcionalidades básicas ya implementadas, nos dedicamos a la implementación responsiva, corrección de errores, ajustes de diseño, e implementación de los formularios de registro (Sign Up) y acceso (Login).

## **Implementacion responsive**
Se añadió a la estructura y diseño CSS, en combinación con una función JavaScript, para que a cierta resolución de pantalla la página se adapte completamente. El menú se cambia por un menú desplegable activado mediante un ícono, que expande una barra mostrando el menú.

## **Correcion de errores**
Se corrigió un error que ocurría al aplicar el estilo responsive, el cual no se ajustaba a toda la pantalla. Para solucionarlo, se ajustó el ancho (width) de todas las secciones, permitiendo que se adapten automáticamente a la resolución cambiante.

## **ajustes de diseño y funciones**
Se ajustó el diseño CSS del menú, la sección del mapa y los precios. En el menú, se rediseñó para que permanezca fijo en la parte superior de la pantalla (top). En la sección de mapa, se reorganizó para que el mapa esté a la izquierda y se implementaron imágenes del local en la parte derecha. Al hacer clic en estas imágenes, el cliente es redirigido a la ubicación del local. En la sección de precios, se ajustaron los botones de agenda y se modificó el tamaño de las tarjetas donde se encuentran los dos combos.

## **implementacion Sing up y Login**
Se implementó una estructura de formulario tanto para el login como para el Sign Up. En ambos formularios, se utilizó un diseño simple y minimalista, que sigue la paleta de colores pastel combinados con colores oscuros.
