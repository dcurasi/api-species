import utils
from specie import Specie
import random

print("Load Regions...\n")
regions = utils.getRegions()

if(not(regions)):
    exit()

print("Regions:")
for region in regions.get('results'):
    print(region.get('name'))
	
print("\n")

print("Select random Region...\n")
n = random.randint(0, regions.get('count') - 1)
selectedRegion = regions.get('results')[n]
print("Region selected are: " + selectedRegion.get('name') + "\n")

print("Load Species in " + selectedRegion.get('name') + "...\n")
speciesFromApi = utils.getSpeciesFromRegion(selectedRegion.get("identifier"))
if(not(speciesFromApi)):
    exit()

print("Create array of Species...\n")
species = []
for specie in speciesFromApi.get('result'):
    species.append(Specie(specie))
print("Species are " + str(len(species)) + "\n")

print("Filter for Critically Endangered...\n")
speciesCR = list(filter(lambda specie: specie.category == "CR", species))
print("Species with Critically Endangered are " + str(len(speciesCR)) + "\n")

for specie in speciesCR:
    conservationMeasures = utils.getConservationMeasures(specie.taxonid, selectedRegion.get('identifier'))
    if(not(conservationMeasures)):
        exit()
    specie.setConservationMeasures(conservationMeasures.get("result"))
    print("Name: " + specie.scientific_name + "\nCategory: " + specie.category + "\nConservation Measures: " + specie.conservation_measures + "\n")


print("Filter for Mammal Class...\n")
speciesMammal = list(filter(lambda specie: specie.class_name == "MAMMALIA", species))
print("Species with Mammal Class are " + str(len(speciesMammal)) + "\n")
for specie in speciesMammal:
    print("Name: " + specie.scientific_name + "\nClass: " + specie.class_name + "\n")
