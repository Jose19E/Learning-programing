Algoritmo geometric_areas
		// Declaración de constantes
		PI_VALUE <- 3.1416
		
		// Declaración de variables
		lado <- 0
		baseRect <- 0
		alturaRect <- 0
		baseTri <- 0
		alturaTri <- 0
		radio <- 0
		areaCuadrado <- 0
		areaRectangulo <- 0
		areaTriangulo <- 0
		areaCirculo <- 0
		totalAreas <- 0
		
		// Solicitar valores al usuario para cada figura
		Escribir "Ingrese el valor del lado del cuadrado:"
		Leer lado
		
		Escribir "Ingrese el valor de la base del rectángulo:"
		Leer baseRect
		
		Escribir "Ingrese el valor de la altura del rectángulo:"
		Leer alturaRect
		
		Escribir "Ingrese el valor de la base del triángulo:"
		Leer baseTri
		
		Escribir "Ingrese el valor de la altura del triángulo:"
		Leer alturaTri
		
		Escribir "Ingrese el valor del radio del círculo:"
		Leer radio
		
		// Cálculo de áreas
		areaCuadrado <- lado * lado
		areaRectangulo <- baseRect * alturaRect
		areaTriangulo <- (baseTri * alturaTri) / 2
		areaCirculo <- PI_VALUE * (radio * radio)  // Actualizamos PI a PI_VALUE
		
		// Calcular el total de áreas
		totalAreas <- areaCuadrado + areaRectangulo + areaTriangulo + areaCirculo
		
		// Mostrar resultados
		Escribir "El área del cuadrado es: ", areaCuadrado
		Escribir "El área del rectángulo es: ", areaRectangulo
		Escribir "El área del triángulo es: ", areaTriangulo
		Escribir "El área del círculo es: ", areaCirculo
		Escribir "El total de todas las áreas es: ", totalAreas
FinAlgoritmo
