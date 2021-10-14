import utils
import Specie

print("Load Regions...\n")
regions = utils.getRegions()

if(not(regions)):
    exit()

print("Regions:")
for region in regions.get('results'):
    print(region.get('name'))
	