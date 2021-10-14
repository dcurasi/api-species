class Specie:
  def __init__(self, obj):
    self.taxonid = obj.get("taxonid")
    self.kingdom_name = obj.get("kingdom_name")
    self.phylum_name = obj.get("phylum_name")
    self.class_name = obj.get("class_name")
    self.order_name = obj.get("order_name")
    self.family_name = obj.get("family_name")
    self.genus_name = obj.get("genus_name")
    self.scientific_name = obj.get("scientific_name")
    self.taxonomic_authority = obj.get("taxonomic_authority")
    self.infra_rank = obj.get("infra_rank")
    self.infra_name = obj.get("infra_name")
    self.population = obj.get("population")
    self.category = obj.get("category")
    self.main_common_name = obj.get("main_common_name")
    self.conservation_measures = ""

  def setConservationMeasures(self, conservation_measures):
    for cm in conservation_measures:
      self.conservation_measures += cm.get("title") + ", "