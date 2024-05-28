
"""
Esta función calcula el número máximo de paneles que se pueden colocar en un techo rectangular.

Args:
    x: El largo del techo.
    y: El ancho del techo.
    a: El largo del panel.
    b: El ancho del panel.

Returns:
    El número máximo de paneles que se pueden colocar en el techo.
"""
def max_panels(x, y, a, b):


    def count_panels(largo, ancho, panel_largo, panel_ancho):
        """
        Esta función calcula la cantidad de paneles que se pueden colocar en una superficie rectangular.

        Args:
            largo: El largo del techo.
            ancho: El ancho del techo.
            panel_largo: El largo del panel.
            panel_ancho: El ancho del panel.

        Returns:
            El número de paneles que se pueden colocar en la superficie.
        """
        return (largo // panel_largo) * (ancho // panel_ancho)

    # contar la cantidad de paneles y sumar en el caso que sobre espacio
    count1 = count_panels(x, y, a, b) + count_panels(x % a, y, b, a)
    # contar de igual forma los paneles pero con orientacion rotada
    count2 = count_panels(x, y, b, a) + count_panels(x % b, y, a, b)

    return max(count1, count2)


a = 1
b = 2
x = 3
y = 5
print(f"Con paneles de {a} x {b} en un techo rectangular de {x} x {y}")
print("Número máximo de paneles: ", max_panels(x, y, a, b))


