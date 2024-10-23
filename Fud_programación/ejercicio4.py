ingreso_total = float(input("¿Cual es su ingreso total?:"))
nº_hijos = float(input("¿Cuantos hijos tiene usted?:"))
Ingreso_imponible = ingreso_total - (600 + (nº_hijos * 60))
impuesto = Ingreso_imponible / 3
dinero_restante = impuesto * 2
print("dinero a pagar por el impuesto:" , impuesto)
print("dinero restante tras deducciones y dinero:" , dinero_restante)