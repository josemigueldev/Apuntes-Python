"""
+  suma
-  resta
*  multiplicacion
** exponente
/  division
// division entera
%  modulo
"""
bruto = 175
tasa_interes = 12.5
interes = bruto * tasa_interes / 100
tasa_bonificacion = 5.0
bonificacion = bruto * tasa_bonificacion / 100
neto = (bruto - bonificacion) + interes

print(neto)
