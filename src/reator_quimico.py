def principal():
    print("Bem-vindo ao Reator Químico! Vamos formar novos compostos a partir de dois íons!")
    primeiro_ion = input("Digite o primeiro íon: ")
    segundo_ion = input("Digite o segundo íon: ")
    primeira_carga = descobre_carga(primeiro_ion)
    segunda_carga = descobre_carga(segundo_ion)
    tipo_de_composto = define_tipo(primeiro_ion, segundo_ion)

    carga_oposta = segunda_carga * (-1)
    
    if primeira_carga == 0 or segunda_carga == 0 or (primeira_carga > 0 and segunda_carga > 0) or (primeira_carga < 0 and segunda_carga < 0):
        print("Impossível formar esse composto!!!")
    
    elif primeira_carga > segunda_carga and primeira_carga != carga_oposta:
        segunda_carga = str(segunda_carga * (-1))
        primeira_carga = str(primeira_carga)
        if primeira_carga == "1":
            primeira_carga = ""
        if segunda_carga == "1":
            segunda_carga = ""
        resultado = tipo_de_composto + " resultante é: " + primeiro_ion + segunda_carga + segundo_ion + primeira_carga
        print(resultado)
    
    elif primeira_carga < segunda_carga and primeira_carga != carga_oposta:
        segunda_carga = str(segunda_carga)
        primeira_carga = str(primeira_carga * (-1))
        if primeira_carga == "1":
            primeira_carga = ""
        if segunda_carga == "1":
            segunda_carga = ""
        resultado = tipo_de_composto + " resultante é: " + segundo_ion + primeira_carga + primeiro_ion + segunda_carga
        print(resultado)
        
    elif primeira_carga > 0:
        resultado = tipo_de_composto + " resultante é: " + primeiro_ion + segundo_ion
        print(resultado)
    
    else:
        resultado = tipo_de_composto + " resultante é: " + segundo_ion + primeiro_ion
        print(resultado)
    
    
def descobre_carga(ion_um):
    nox_um = ["H", "Li", "Na", "K", "Rb", "Cs", "Fr", "Ag", "(NH4)"]
    nox_dois = ["Be", "Mg", "Ca", "Sr", "Ba", "Ra", "Zn"]
    nox_tres = ["Al"]
    ametal_um = ["(OH)", "F", "Cl", "Br", "I", "At", "Ts", "(NO3)", "(ClO3)"]
    ametal_dois = ["O", "S", "Se", "Te", "(CO3)", "(SO4)"]
    ametal_tres = ["N", "P", "As", "PO4"]
    
    if ion_um in nox_um:
        carga = 1
    elif ion_um in nox_dois:
        carga = 2
    elif ion_um in nox_tres:
        carga = 3
    elif ion_um in ametal_um:
        carga = -1
    elif ion_um in ametal_dois:
        carga = -2
    elif ion_um in ametal_tres:
        carga = -3
    else:
        carga = 0
    return carga
    
    
def define_tipo(ion_um, ion_dois):
    tipo = "Sal"
    if ion_um == "O" or ion_dois == "O":
        tipo = "Óxido"
    elif (ion_um == "H" and ion_dois == "(OH)") or (ion_um == "(OH)" and ion_dois == "H"):
        tipo = "Água"
    elif ion_um == "(OH)" or ion_dois == "(OH)":
        tipo = "Base"
    elif ion_um == "H" or ion_dois == "H":    
        tipo = "Ácido"    
    return tipo
    
    
principal()
