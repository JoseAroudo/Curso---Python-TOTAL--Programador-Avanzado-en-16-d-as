def describir_persona(name, **kwargs):
    print(f"Caracteristicas de {name}:")
    for i in kwargs:
        print(f"{i}: {kwargs[i]}")#i recorre en las keys "kwargs" en las values

describir_persona("Jose",color_ojos="azules", color_pelo="rubio", pene = 28)