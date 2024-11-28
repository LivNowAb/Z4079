# svoje jmeno, gen post. vraci editace jmena
# Albert - program si pamatuje -bert
# pred ni davame "Al", "Ro", "Hu", "Nor", "Gil"

def GeneratorJmen(cast1, cast2):
    for item in cast1:
        yield item + cast2

cast1 = ["Li", "Oli", "A", "In"]
cast2 = "via"

for jmeno in GeneratorJmen(cast1, cast2):
    print(f"Tve jmeno je {jmeno}.")