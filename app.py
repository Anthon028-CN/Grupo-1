import streamlit as st

Título de la aplicación
st.title("Software Libre y Privativo: Historia y Ejemplos")

Sección: Introducción
st.header("Introducción")
st.write("""
El software se puede clasificar en dos grandes categorías: software libre y software privativo.
En esta aplicación, exploraremos la historia y ejemplos de cada uno.
""")

Sección: Software Libre
st.header("Software Libre")
st.write("""
El software libre es aquel que permite a los usuarios ejecutar, estudiar, modificar y distribuir el software.
Esto fomenta la colaboración y la transparencia en el desarrollo de software.
""")

Ejemplos de Software Libre
st.subheader("Ejemplos de Software Libre")
libre_ejemplos = ["Linux", "Apache", "Mozilla Firefox", "LibreOffice"]
st.write(", ".join(libre_ejemplos))

Sección: Software Privativo
st.header("Software Privativo")
st.write("""
El software privativo, por otro lado, es aquel que restringe el acceso al código fuente y limita la capacidad de los usuarios para modificarlo o compartirlo.
""")

Ejemplos de Software Privativo
st.subheader("Ejemplos de Software Privativo")
privativo_ejemplos = ["Microsoft Windows", "Adobe Photoshop", "Oracle Database"]
st.write(", ".join(privativo_ejemplos))

Sección: Conclusión
st.header("Conclusión")
st.write("""
La elección entre software libre y privativo depende de las necesidades y valores de los usuarios.
Ambas categorías tienen sus ventajas y desventajas, y es importante considerar cuál se adapta mejor a cada situación.
""")

Pie de página
st.write("Fuente: Wikipedia")


