class Specie:
  def __init__(self, obj):
    self.taxonid = obj.taxonid
    self.kingdom_name = obj.kingdom_name
    self.phylum_name = obj.phylum_name
    self.class_name = obj.class_name
    self.order_name = obj.order_name
    self.family_name = obj.family_name
    self.genus_name = obj.genus_name
    self.scientific_name = obj.scientific_name
    self.taxonomic_authority = obj.taxonomic_authority
    self.infra_rank = obj.infra_rank
    self.infra_name = obj.infra_name
    self.population = obj.population
    self.category = obj.category
    self.main_common_name = obj.main_common_name
    self.conservation_measures = ""

  def setConservationMeasures(self, conservation_measures):
    cm_size = len(conservation_measures)
    for key, cm in conservation_measures:
        if(key == (cm_size - 1)):
            self.conservation_measures += cm.title
        else:
            self.conservation_measures += cm.title + ", "