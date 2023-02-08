import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportActionModelAdmin

GENDER = (
    ('MALE', "MALE"),
    ('FEMALE', "FEMALE"),
    ('UNSPECIFIED', "UNSPECIFIED"),
)
class ValidManager(models.Manager):
    def get_queryset(self):
        return super(ValidManager, self).get_queryset().filter(is_deleted=False)



class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    is_deleted = models.BooleanField(default=False)
    date_deleted = models.DateTimeField(blank=True, null=True)

    objects = models.Manager()
    valid_objects = ValidManager()

    class Meta:
        abstract = True


class SurveyUser(BaseModel):
    full_name = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=225)
    occupation = models.CharField(max_length=225)
    education_level = models.CharField(max_length=225)
    
    class Meta:
        verbose_name = _('Survey User')
        verbose_name_plural = _('Survey Users')
        ordering = ('-id', )

    def __str__(self):
        return f'{self.email}'
    

# Create your models here.
# Section A Model
class IntroSurveyDataA(models.Model):
    
    Correspondent_Email = models.OneToOneField(SurveyUser, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200)
    # Political Section
    pol_landuse = models.CharField(max_length=200)
    pol_landuse_rating = models.PositiveIntegerField()
    
    pol_Geographic = models.CharField(max_length=200)
    pol_Geographic_rating = models.PositiveIntegerField()
    pol_Economic = models.CharField(max_length=200)
    pol_Economic_rating = models.PositiveIntegerField()
    pol_Technological = models.CharField(max_length=200)
    pol_Technological_rating = models.PositiveIntegerField()
    pol_Social = models.CharField(max_length=200)
    pol_Social_rating = models.PositiveIntegerField()
    pol_Environmental = models.CharField(max_length=200)
    pol_Environmental_rating = models.PositiveIntegerField()

        
    landuse_geographic = models.CharField(max_length=200)
    landuse_geograhpic_rating = models.PositiveIntegerField()
    landuse_Economic = models.CharField(max_length=200)
    landuse_Economic_rating = models.PositiveIntegerField()
    landuse_Technological = models.CharField(max_length=200)
    landuse_Technological_rating = models.PositiveIntegerField()
    landuse_Social = models.CharField(max_length=200)
    landuse_Social_rating = models.PositiveIntegerField()
    landuse_Environmental = models.CharField(max_length=200)
    landuse_Environmental_rating = models.PositiveIntegerField()


    geographic_Economic = models.CharField(max_length=200)
    geographic_Economic_rating = models.PositiveIntegerField()
    geographic_Technological = models.CharField(max_length=200)
    geographic_Technological_rating = models.PositiveIntegerField()
    geographic_Social = models.CharField(max_length=200)
    geographic_Social_rating = models.PositiveIntegerField()
    geographic_Environmental = models.CharField(max_length=200)
    geographic_Environmental_rating = models.PositiveIntegerField()
    
    
    economic_Technological = models.CharField(max_length=200)
    economic_Technological_rating = models.PositiveIntegerField()
    economic_Social = models.CharField(max_length=200)
    economic_Social_rating = models.PositiveIntegerField()
    economic_Environmental = models.CharField(max_length=200)
    economic_Environmental_rating = models.PositiveIntegerField()
    
    
    technological_Social = models.CharField(max_length=200)
    technological_Social_rating = models.PositiveIntegerField()
    technological_Environmental = models.CharField(max_length=200)
    technological_Environmental_rating = models.PositiveIntegerField()
    
    
    social_Environmental = models.CharField(max_length=200)
    social_Environmental_rating = models.PositiveIntegerField()

    

    class Meta:
        verbose_name = _('Survey Data')
        verbose_name_plural = _('Survey Data')
        ordering = ('-pk',)

    def __str__(self):
        return f'{self.Correspondent_Email.email}'
    
    
    
    
    
class PoliticalFactorDataA(models.Model):
    
    Correspondent_Email = models.OneToOneField(SurveyUser, on_delete=models.CASCADE, blank=True, null=True)
    fullname = models.CharField(max_length=200, blank=True, null=True)
   
    p1_Insecurity_instability_Border_Check = models.CharField(max_length=200)
    p1_Insecurity_instability_Border_Check_rating = models.PositiveIntegerField()
    p1_Insecurity_instability_Policy_nonalignment = models.CharField(max_length=200)
    p1_Insecurity_instability_Policy_nonalignment_rating = models.PositiveIntegerField()
    p1_Insecurity_instability_weak_institutions = models.CharField(max_length=200)
    p1_Insecurity_instability_weak_institutions_rating = models.PositiveIntegerField()
    p1_Insecurity_instability_disimilar_regulation = models.CharField(max_length=200)
    p1_Insecurity_instability_disimilar_regulation_rating = models.PositiveIntegerField()
    p1_Insecurity_instability_inability_to_observe = models.CharField(max_length=200)
    p1_Insecurity_instability_inability_to_observe_rating = models.PositiveIntegerField()
    p1_Insecurity_instability_corruption_impact = models.CharField(max_length=200)
    p1_Insecurity_instability_corruption_impact_rating = models.PositiveIntegerField()
    p1_Insecurity_instability_realignment_design = models.CharField(max_length=200)
    p1_Insecurity_instability_realignment_design_rating = models.PositiveIntegerField()
    p1_Insecurity_instability_commitment_fluctuation = models.CharField(max_length=200)
    p1_Insecurity_instability_commitment_fluctuation_rating = models.PositiveIntegerField()

        
   
    p2_Border_Check_Policy_nonalignment = models.CharField(max_length=200)
    p2_Border_Check_Policy_nonalignment_rating = models.PositiveIntegerField()
    p2_Border_Check_weak_institutions = models.CharField(max_length=200)
    p2_Border_Check_weak_institutions_rating = models.PositiveIntegerField()
    p2_Border_Check_disimilar_regulation = models.CharField(max_length=200)
    p2_Border_Check_disimilar_regulation_rating = models.PositiveIntegerField()
    p2_Border_Check_inability_to_observe = models.CharField(max_length=200)
    p2_Border_Check_inability_to_observe_rating = models.PositiveIntegerField()
    p2_Border_Check_corruption_impact = models.CharField(max_length=200)
    p2_Border_Check_corruption_impact_rating = models.PositiveIntegerField()
    p2_Border_Check_realignment_design = models.CharField(max_length=200)
    p2_Border_Check_realignment_design_rating = models.PositiveIntegerField()
    p2_Border_Check_commitment_fluctuation = models.CharField(max_length=200)
    p2_Border_Check_commitment_fluctuation_rating = models.PositiveIntegerField()
    
    
    
    p3_Policy_nonalignment_weak_institutions = models.CharField(max_length=200)
    p3_Policy_nonalignment_weak_institutions_rating = models.PositiveIntegerField()
    p3_Policy_nonalignment_disimilar_regulation = models.CharField(max_length=200)
    p3_Policy_nonalignment_disimilar_regulation_rating = models.PositiveIntegerField()
    p3_Policy_nonalignment_inability_to_observe = models.CharField(max_length=200)
    p3_Policy_nonalignment_inability_to_observe_rating = models.PositiveIntegerField()
    p3_Policy_nonalignment_corruption_impact = models.CharField(max_length=200)
    p3_Policy_nonalignment_corruption_impact_rating = models.PositiveIntegerField()
    p3_Policy_nonalignment_realignment_design = models.CharField(max_length=200)
    p3_Policy_nonalignment_realignment_design_rating = models.PositiveIntegerField()
    p3_Policy_nonalignment_commitment_fluctuation = models.CharField(max_length=200)
    p3_Policy_nonalignment_commitment_fluctuation_rating = models.PositiveIntegerField()
    
    
    
    p4_weak_institutions_disimilar_regulation = models.CharField(max_length=200)
    p4_weak_institutions_disimilar_regulation_rating = models.PositiveIntegerField()
    p4_weak_institutions_inability_to_observe = models.CharField(max_length=200)
    p4_weak_institutions_inability_to_observe_rating = models.PositiveIntegerField()
    p4_weak_institutions_corruption_impact = models.CharField(max_length=200)
    p4_weak_institutions_corruption_impact_rating = models.PositiveIntegerField()
    p4_weak_institutions_realignment_design = models.CharField(max_length=200)
    p4_weak_institutions_realignment_design_rating = models.PositiveIntegerField()
    p4_weak_institutions_commitment_fluctuation = models.CharField(max_length=200)
    p4_weak_institutions_commitment_fluctuation_rating = models.PositiveIntegerField()
    
    
    p5_disimilar_regulation_inability_to_observe = models.CharField(max_length=200)
    p5_disimilar_regulation_inability_to_observe_rating = models.PositiveIntegerField()
    p5_disimilar_regulation_corruption_impact = models.CharField(max_length=200)
    p5_disimilar_regulation_corruption_impact_rating = models.PositiveIntegerField()
    p5_disimilar_regulation_realignment_design = models.CharField(max_length=200)
    p5_disimilar_regulation_realignment_design_rating = models.PositiveIntegerField()
    p5_disimilar_regulation_commitment_fluctuation = models.CharField(max_length=200)
    p5_disimilar_regulation_commitment_fluctuation_rating = models.PositiveIntegerField()
    
    
    p6_inability_to_observe_corruption_impact = models.CharField(max_length=200)
    p6_inability_to_observe_corruption_impact_rating = models.PositiveIntegerField()
    p6_inability_to_observe_realignment_design = models.CharField(max_length=200)
    p6_inability_to_observe_realignment_design_rating = models.PositiveIntegerField()
    p6_inability_to_observe_commitment_fluctuation = models.CharField(max_length=200)
    p6_inability_to_observe_commitment_fluctuation_rating = models.PositiveIntegerField()
    
    
    p7_corruption_impact_realignment_design = models.CharField(max_length=200)
    p7_corruption_impact_realignment_design_rating = models.PositiveIntegerField()
    p7_corruption_impact_commitment_fluctuation = models.CharField(max_length=200)
    p7_corruption_impact_commitment_fluctuation_rating = models.PositiveIntegerField()
    
    
    p8_realignment_design_commitment_fluctuation = models.CharField(max_length=200)
    p8_realignment_design_commitment_fluctuation_rating = models.PositiveIntegerField()

    class Meta:
        verbose_name = _('Political Data')
        verbose_name_plural = _('Political Data')
        ordering = ('-pk',)

    def __str__(self):
        return f'{self.Correspondent_Email.email}'
    
    
    

    
class LandUseFactorDataA(models.Model):
    
    Correspondent_Email = models.OneToOneField(SurveyUser, on_delete=models.CASCADE, blank=True, null=True)
    fullname = models.CharField(max_length=200, blank=True, null=True)
   
  
    L1_Speculative_land_Likely_split = models.CharField(max_length=200)
    L1_Speculative_land_Likely_split_rating = models.PositiveIntegerField()
    L1_Speculative_land_Hard_to_determine = models.CharField(max_length=200)
    L1_Speculative_land_Hard_to_determine_rating = models.PositiveIntegerField()
    L1_Speculative_land_Perception_project = models.CharField(max_length=200)
    L1_Speculative_land_Perception_project_rating = models.PositiveIntegerField()
    L1_Speculative_land_Corridor_efficiency = models.CharField(max_length=200)
    L1_Speculative_land_Corridor_efficiency_rating = models.PositiveIntegerField()
    L1_Speculative_land_Perception_Land = models.CharField(max_length=200)
    L1_Speculative_land_Perception_Land_rating = models.PositiveIntegerField()
    L1_Speculative_land_limited_access = models.CharField(max_length=200)
    L1_Speculative_land_limited_access_rating = models.PositiveIntegerField()
    L1_Speculative_land_communal_informal = models.CharField(max_length=200)
    L1_Speculative_land_communal_informal_rating = models.PositiveIntegerField()
    L1_Speculative_land_weak_land = models.CharField(max_length=200)
    L1_Speculative_land_weak_land_rating = models.PositiveIntegerField()
    
    
    L2_Likely_split_Hard_to_determine = models.CharField(max_length=200)
    L2_Likely_split_Hard_to_determine_rating = models.PositiveIntegerField()
    L2_Likely_split_Perception_project = models.CharField(max_length=200)
    L2_Likely_split_Perception_project_rating = models.PositiveIntegerField()
    L2_Likely_split_Corridor_efficiency = models.CharField(max_length=200)
    L2_Likely_split_Corridor_efficiency_rating = models.PositiveIntegerField()
    L2_Likely_split_Perception_Land = models.CharField(max_length=200)
    L2_Likely_split_Perception_Land_rating = models.PositiveIntegerField()
    L2_Likely_split_limited_access = models.CharField(max_length=200)
    L2_Likely_split_limited_access_rating = models.PositiveIntegerField()
    L2_Likely_split_communal_informal = models.CharField(max_length=200)
    L2_Likely_split_communal_informal_rating = models.PositiveIntegerField()
    L2_Likely_split_weak_land = models.CharField(max_length=200)
    L2_Likely_split_weak_land_rating = models.PositiveIntegerField()
    

    L3_Hard_to_determine_Perception_project = models.CharField(max_length=200)
    L3_Hard_to_determine_Perception_project_rating = models.PositiveIntegerField()
    L3_Hard_to_determine_Corridor_efficiency = models.CharField(max_length=200)
    L3_Hard_to_determine_Corridor_efficiency_rating = models.PositiveIntegerField()
    L3_Hard_to_determine_Perception_Land = models.CharField(max_length=200)
    L3_Hard_to_determine_Perception_Land_rating = models.PositiveIntegerField()
    L3_Hard_to_determine_limited_access = models.CharField(max_length=200)
    L3_Hard_to_determine_limited_access_rating = models.PositiveIntegerField()
    L3_Hard_to_determine_communal_informal = models.CharField(max_length=200)
    L3_Hard_to_determine_communal_informal_rating = models.PositiveIntegerField()
    L3_Hard_to_determine_weak_land = models.CharField(max_length=200)
    L3_Hard_to_determine_weak_land_rating = models.PositiveIntegerField()
    
    
    
    L4_Perception_project_Corridor_efficiency = models.CharField(max_length=200)
    L4_Perception_project_Corridor_efficiency_rating = models.PositiveIntegerField()
    L4_Perception_project_Perception_Land = models.CharField(max_length=200)
    L4_Perception_project_Perception_Land_rating = models.PositiveIntegerField()
    L4_Perception_project_limited_access = models.CharField(max_length=200)
    L4_Perception_project_limited_access_rating = models.PositiveIntegerField()
    L4_Perception_project_communal_informal = models.CharField(max_length=200)
    L4_Perception_project_communal_informal_rating = models.PositiveIntegerField()
    L4_Perception_project_weak_land = models.CharField(max_length=200)
    L4_Perception_project_weak_land_rating = models.PositiveIntegerField()
    
    
    L5_Corridor_efficiency_Perception_Land = models.CharField(max_length=200)
    L5_Corridor_efficiency_Perception_Land_rating = models.PositiveIntegerField()
    L5_Corridor_efficiency_limited_access = models.CharField(max_length=200)
    L5_Corridor_efficiency_limited_access_rating = models.PositiveIntegerField()
    L5_Corridor_efficiency_communal_informal = models.CharField(max_length=200)
    L5_Corridor_efficiency_communal_informal_rating = models.PositiveIntegerField()
    L5_Corridor_efficiency_weak_land = models.CharField(max_length=200)
    L5_Corridor_efficiency_weak_land_rating = models.PositiveIntegerField()
    
    
    L6_Perception_Land_limited_access = models.CharField(max_length=200)
    L6_Perception_Land_limited_access_rating = models.PositiveIntegerField()
    L6_Perception_Land_communal_informal = models.CharField(max_length=200)
    L6_Perception_Land_communal_informal_rating = models.PositiveIntegerField()
    L6_Perception_Land_weak_land = models.CharField(max_length=200)
    L6_Perception_Land_weak_land_rating = models.PositiveIntegerField()
  
    
    L7_limited_access_communal_informal = models.CharField(max_length=200)
    L7_limited_access_communal_informal_rating = models.PositiveIntegerField()
    L7_limited_access_weak_land = models.CharField(max_length=200)
    L7_limited_access_weak_land_rating = models.PositiveIntegerField()
    
    
    L8_communal_informal_weak_land = models.CharField(max_length=200)
    L8_communal_informal_weak_land_rating = models.PositiveIntegerField()
      
        
        
    class Meta:
        verbose_name = _('Land Use Data')
        verbose_name_plural = _('Land Use Data')
        ordering = ('-pk',)

    def __str__(self):
        return f'{self.Correspondent_Email.email}'
    
    
    
class GeographicFactorDataA(models.Model):
    
    Correspondent_Email = models.OneToOneField(SurveyUser, on_delete=models.CASCADE, blank=True, null=True)
    fullname = models.CharField(max_length=200, blank=True, null=True)
   
  
    G1_Lateritic_soft_Flood_prone_water =  models.CharField(max_length=200)
    G1_Lateritic_soft_Flood_prone_water_rating = models.PositiveIntegerField()
    G1_Lateritic_soft_Diverse_terrain =  models.CharField(max_length=200)
    G1_Lateritic_soft_Diverse_terrain_rating = models.PositiveIntegerField()
    G1_Lateritic_soft_Crossing_seismic =  models.CharField(max_length=200)
    G1_Lateritic_soft_Crossing_seismic_rating = models.PositiveIntegerField()
    G1_Lateritic_soft_Landslide_flooding =  models.CharField(max_length=200)
    G1_Lateritic_soft_Landslide_flooding_rating = models.PositiveIntegerField()
    G1_Lateritic_soft_Traversing_mining =  models.CharField(max_length=200)
    G1_Lateritic_soft_Traversing_mining_rating = models.PositiveIntegerField()
    G1_Lateritic_soft_Sparse_detached =  models.CharField(max_length=200)
    G1_Lateritic_soft_Sparse_detached_rating = models.PositiveIntegerField()
    G1_Lateritic_soft_undocumented_geological =  models.CharField(max_length=200)
    G1_Lateritic_soft_undocumented_geological_rating = models.PositiveIntegerField()
    G1_Lateritic_soft_Geopolitical_consideration =  models.CharField(max_length=200)
    G1_Lateritic_soft_Geopolitical_consideration_rating = models.PositiveIntegerField()


   #Flood-prone/water logged areas necessitating costly foundation design 


    G2_Flood_prone_water_Diverse_terrain =  models.CharField(max_length=200)
    G2_Flood_prone_water_Diverse_terrain_rating = models.PositiveIntegerField()
    G2_Flood_prone_water_Crossing_seismic =  models.CharField(max_length=200)
    G2_Flood_prone_water_Crossing_seismic_rating = models.PositiveIntegerField()
    G2_Flood_prone_water_Landslide_flooding =  models.CharField(max_length=200)
    G2_Flood_prone_water_Landslide_flooding_rating = models.PositiveIntegerField()
    G2_Flood_prone_water_Traversing_mining =  models.CharField(max_length=200)
    G2_Flood_prone_water_Traversing_mining_rating = models.PositiveIntegerField()
    G2_Flood_prone_water_Sparse_detached =  models.CharField(max_length=200)
    G2_Flood_prone_water_Sparse_detached_rating = models.PositiveIntegerField()
    G2_Flood_prone_water_undocumented_geological =  models.CharField(max_length=200)
    G2_Flood_prone_water_undocumented_geological_rating = models.PositiveIntegerField()
    G2_Flood_prone_water_Geopolitical_consideration =  models.CharField(max_length=200)
    G2_Flood_prone_water_Geopolitical_consideration_rating = models.PositiveIntegerField()



   #Diverse terrain (flat/ rolling/mountain/escarpments) increase design and technology complexity 


    G3_Diverse_terrain_Crossing_seismic =  models.CharField(max_length=200)
    G3_Diverse_terrain_Crossing_seismic_rating = models.PositiveIntegerField()
    G3_Diverse_terrain_Landslide_flooding =  models.CharField(max_length=200)
    G3_Diverse_terrain_Landslide_flooding_rating = models.PositiveIntegerField()
    G3_Diverse_terrain_Traversing_mining =  models.CharField(max_length=200)
    G3_Diverse_terrain_Traversing_mining_rating = models.PositiveIntegerField()
    G3_Diverse_terrain_Sparse_detached =  models.CharField(max_length=200)
    G3_Diverse_terrain_Sparse_detached_rating = models.PositiveIntegerField()
    G3_Diverse_terrain_undocumented_geological =  models.CharField(max_length=200)
    G3_Diverse_terrain_undocumented_geological_rating = models.PositiveIntegerField()
    G3_Diverse_terrain_Geopolitical_consideration =  models.CharField(max_length=200)
    G3_Diverse_terrain_Geopolitical_consideration_rating = models.PositiveIntegerField()



   #Crossing seismic active Great Rift Valley 


    G4_Crossing_seismic_Landslide_flooding =  models.CharField(max_length=200)
    G4_Crossing_seismic_Landslide_flooding_rating = models.PositiveIntegerField()
    G4_Crossing_seismic_Traversing_mining =  models.CharField(max_length=200)
    G4_Crossing_seismic_Traversing_mining_rating = models.PositiveIntegerField()
    G4_Crossing_seismic_Sparse_detached =  models.CharField(max_length=200)
    G4_Crossing_seismic_Sparse_detached_rating = models.PositiveIntegerField()
    G4_Crossing_seismic_undocumented_geological =  models.CharField(max_length=200)
    G4_Crossing_seismic_undocumented_geological_rating = models.PositiveIntegerField()
    G4_Crossing_seismic_Geopolitical_consideration =  models.CharField(max_length=200)
    G4_Crossing_seismic_Geopolitical_consideration_rating = models.PositiveIntegerField()

   #Landslide,flooding, erosion events could potentially delay project schedule and disrupt operations


    G5_Landslide_flooding_Traversing_mining =  models.CharField(max_length=200)
    G5_Landslide_flooding_Traversing_mining_rating = models.PositiveIntegerField()
    G5_Landslide_flooding_Sparse_detached =  models.CharField(max_length=200)
    G5_Landslide_flooding_Sparse_detached_rating = models.PositiveIntegerField()
    G5_Landslide_flooding_undocumented_geological =  models.CharField(max_length=200)
    G5_Landslide_flooding_undocumented_geological_rating = models.PositiveIntegerField()
    G5_Landslide_flooding_Geopolitical_consideration =  models.CharField(max_length=200)
    G5_Landslide_flooding_Geopolitical_consideration_rating = models.PositiveIntegerField()

   #Traversing mining areas with active blasting/ explosions


    G6_Traversing_mining_Sparse_detached =  models.CharField(max_length=200)
    G6_Traversing_mining_Sparse_detached_rating = models.PositiveIntegerField()
    G6_Traversing_mining_undocumented_geological =  models.CharField(max_length=200)
    G6_Traversing_mining_undocumented_geological_rating = models.PositiveIntegerField()
    G6_Traversing_mining_Geopolitical_consideration =  models.CharField(max_length=200)
    G6_Traversing_mining_Geopolitical_consideration_rating = models.PositiveIntegerField()



   #Sparse/detached settlement pattern unfeasible to link with GELB

    G7_Sparse_detached_undocumented_geological =  models.CharField(max_length=200)
    G7_Sparse_detached_undocumented_geological_rating = models.PositiveIntegerField()
    G7_Sparse_detached_Geopolitical_consideration =  models.CharField(max_length=200)
    G7_Sparse_detached_Geopolitical_consideration_rating = models.PositiveIntegerField()


    ##undocumented geological/subsurface condition

    G8_undocumented_geological_Geopolitical_consideration =  models.CharField(max_length=200)
    G8_undocumented_geological_Geopolitical_consideration_rating = models.PositiveIntegerField()

        
        
    class Meta:
        verbose_name = _('Geographic Data')
        verbose_name_plural = _('Geographic Data')
        ordering = ('-pk',)

    def __str__(self):
        return f'{self.Correspondent_Email.email}'
    
    
class EconomicFactorDataA(models.Model):
    
    Correspondent_Email = models.OneToOneField(SurveyUser, on_delete=models.CASCADE, blank=True, null=True)
    fullname = models.CharField(max_length=200, blank=True, null=True)
    
    
    #  Dependance on scarce govt finance with few alternatives
    
    Ec1_Dependance_Fiscally_strong =  models.CharField(max_length=200)
    Ec1_Dependance_Fiscally_strong_rating = models.PositiveIntegerField()
    Ec1_Dependance_Forex_loss =  models.CharField(max_length=200)
    Ec1_Dependance_Forex_loss_rating = models.PositiveIntegerField()
    Ec1_Dependance_inability_to_agree =  models.CharField(max_length=200)
    Ec1_Dependance_inability_to_agree_rating = models.PositiveIntegerField()
    Ec1_Dependance_user_fees =  models.CharField(max_length=200)
    Ec1_Dependance_user_fees_rating = models.PositiveIntegerField()
    Ec1_Dependance_budgetary_focus =  models.CharField(max_length=200)
    Ec1_Dependance_budgetary_focus_rating = models.PositiveIntegerField()
    Ec1_Dependance_fluctuation_of_exchange =  models.CharField(max_length=200)
    Ec1_Dependance_fluctuation_of_exchange_rating = models.PositiveIntegerField()
    Ec1_Dependance_Economic_vulnerability =  models.CharField(max_length=200)
    Ec1_Dependance_Economic_vulnerability_rating = models.PositiveIntegerField()

#  Fiscally strong states emasculating economically weak


    Ec2_Fiscally_strong_Forex_loss =  models.CharField(max_length=200)
    Ec2_Fiscally_strong_Forex_loss_rating = models.PositiveIntegerField()
    Ec2_Fiscally_strong_inability_to_agree =  models.CharField(max_length=200)
    Ec2_Fiscally_strong_inability_to_agree_rating = models.PositiveIntegerField()
    Ec2_Fiscally_strong_user_fees =  models.CharField(max_length=200)
    Ec2_Fiscally_strong_user_fees_rating = models.PositiveIntegerField()
    Ec2_Fiscally_strong_budgetary_focus =  models.CharField(max_length=200)
    Ec2_Fiscally_strong_budgetary_focus_rating = models.PositiveIntegerField()
    Ec2_Fiscally_strong_fluctuation_of_exchange =  models.CharField(max_length=200)
    Ec2_Fiscally_strong_fluctuation_of_exchange_rating = models.PositiveIntegerField()
    Ec2_Fiscally_strong_Economic_vulnerability =  models.CharField(max_length=200)
    Ec2_Fiscally_strong_Economic_vulnerability_rating = models.PositiveIntegerField()

#  Forex loss through import of project inputs/labour


    Ec3_Forex_loss_inability_to_agree =  models.CharField(max_length=200)
    Ec3_Forex_loss_inability_to_agree_rating = models.PositiveIntegerField()
    Ec3_Forex_loss_user_fees =  models.CharField(max_length=200)
    Ec3_Forex_loss_user_fees_rating = models.PositiveIntegerField()
    Ec3_Forex_loss_budgetary_focus =  models.CharField(max_length=200)
    Ec3_Forex_loss_budgetary_focus_rating = models.PositiveIntegerField()
    Ec3_Forex_loss_fluctuation_of_exchange =  models.CharField(max_length=200)
    Ec3_Forex_loss_fluctuation_of_exchange_rating = models.PositiveIntegerField()
    Ec3_Forex_loss_Economic_vulnerability =  models.CharField(max_length=200)
    Ec3_Forex_loss_Economic_vulnerability_rating = models.PositiveIntegerField()

#  inability to agree on benefit/cost sharing related to common facility


    Ec4_inability_to_agree_user_fees =  models.CharField(max_length=200)
    Ec4_inability_to_agree_user_fees_rating = models.PositiveIntegerField()
    Ec4_inability_to_agree_budgetary_focus =  models.CharField(max_length=200)
    Ec4_inability_to_agree_budgetary_focus_rating = models.PositiveIntegerField()
    Ec4_inability_to_agree_fluctuation_of_exchange =  models.CharField(max_length=200)
    Ec4_inability_to_agree_fluctuation_of_exchange_rating = models.PositiveIntegerField()
    Ec4_inability_to_agree_Economic_vulnerability =  models.CharField(max_length=200)
    Ec4_inability_to_agree_Economic_vulnerability_rating = models.PositiveIntegerField()

#  user-fees to limit access if community/users if unable/unwilling to pay



    Ec5_user_fees_budgetary_focus =  models.CharField(max_length=200)
    Ec5_user_fees_budgetary_focus_rating = models.PositiveIntegerField()
    Ec5_user_fees_fluctuation_of_exchange =  models.CharField(max_length=200)
    Ec5_user_fees_fluctuation_of_exchange_rating = models.PositiveIntegerField()
    Ec5_user_fees_Economic_vulnerability =  models.CharField(max_length=200)
    Ec5_user_fees_Economic_vulnerability_rating = models.PositiveIntegerField()


#  budgetary focus inclined to expansion and new roads than maintainance, 


    Ec6_budgetary_focus_fluctuation_of_exchange =  models.CharField(max_length=200)
    Ec6_budgetary_focus_fluctuation_of_exchange_rating = models.PositiveIntegerField()
    Ec6_budgetary_focus_Economic_vulnerability =  models.CharField(max_length=200)
    Ec6_budgetary_focus_Economic_vulnerability_rating = models.PositiveIntegerField()


#  fluctuation of exchange rate and construction material prices


    Ec7_fluctuation_of_exchange_Economic_vulnerability =  models.CharField(max_length=200)
    Ec7_fluctuation_of_exchange_Economic_vulnerability_rating = models.PositiveIntegerField()

   
   
    class Meta:
        verbose_name = _('Economic Data')
        verbose_name_plural = _('Economic Data')
        ordering = ('-pk',)

    def __str__(self):
        return f'{self.Correspondent_Email.email}'
    
    
    
class TechnologicalFactorDataA(models.Model):
    
    Correspondent_Email = models.OneToOneField(SurveyUser, on_delete=models.CASCADE, blank=True, null=True)
    fullname = models.CharField(max_length=200, blank=True, null=True)
    
    
    # Variation among states in highway classification by purpose & capacity
    
    Tc1_Variation_among_Telecommuting_technology =  models.CharField(max_length=200)
    Tc1_Variation_among_Telecommuting_technology_rating = models.PositiveIntegerField()
    Tc1_Variation_among_Evolving_technology =  models.CharField(max_length=200)
    Tc1_Variation_among_Evolving_technology_rating = models.PositiveIntegerField()
    Tc1_Variation_among_necesstiy_of_tunnels =  models.CharField(max_length=200)
    Tc1_Variation_among_necesstiy_of_tunnels_rating = models.PositiveIntegerField()
    Tc1_Variation_among_use_of_monopolistic =  models.CharField(max_length=200)
    Tc1_Variation_among_use_of_monopolistic_rating = models.PositiveIntegerField()
    Tc1_Variation_among_Favoring_politically_popular =  models.CharField(max_length=200)
    Tc1_Variation_among_Favoring_politically_popular_rating = models.PositiveIntegerField()
    Tc1_Variation_among_Delays_downtime =  models.CharField(max_length=200)
    Tc1_Variation_among_Delays_downtime_rating = models.PositiveIntegerField()
    Tc1_Variation_among_Equipment_parts =  models.CharField(max_length=200)
    Tc1_Variation_among_Equipment_parts_rating = models.PositiveIntegerField()
    Tc1_Variation_among_construction_preceding =  models.CharField(max_length=200)
    Tc1_Variation_among_construction_preceding_rating = models.PositiveIntegerField()


# Telecommuting technology making redundant human movement


    Tc2_Telecommuting_technology_Evolving_technology =  models.CharField(max_length=200)
    Tc2_Telecommuting_technology_Evolving_technology_rating = models.PositiveIntegerField()
    Tc2_Telecommuting_technology_necesstiy_of_tunnels =  models.CharField(max_length=200)
    Tc2_Telecommuting_technology_necesstiy_of_tunnels_rating = models.PositiveIntegerField()
    Tc2_Telecommuting_technology_use_of_monopolistic =  models.CharField(max_length=200)
    Tc2_Telecommuting_technology_use_of_monopolistic_rating = models.PositiveIntegerField()
    Tc2_Telecommuting_technology_Favoring_politically_popular =  models.CharField(max_length=200)
    Tc2_Telecommuting_technology_Favoring_politically_popular_rating = models.PositiveIntegerField(db_column='tc2_telecommuting_tech_favoring_politically_pop_rating')
    Tc2_Telecommuting_technology_Delays_downtime =  models.CharField(max_length=200)
    Tc2_Telecommuting_technology_Delays_downtime_rating = models.PositiveIntegerField()
    Tc2_Telecommuting_technology_Equipment_parts =  models.CharField(max_length=200)
    Tc2_Telecommuting_technology_Equipment_parts_rating = models.PositiveIntegerField()
    Tc2_Telecommuting_technology_construction_preceding =  models.CharField(max_length=200)
    Tc2_Telecommuting_technology_construction_preceding_rating = models.PositiveIntegerField()


# Evolving technology rendering obsolete construction/ maintainance/operation equipment


    Tc3_Evolving_technology_necesstiy_of_tunnels =  models.CharField(max_length=200)
    Tc3_Evolving_technology_necesstiy_of_tunnels_rating = models.PositiveIntegerField()
    Tc3_Evolving_technology_use_of_monopolistic =  models.CharField(max_length=200)
    Tc3_Evolving_technology_use_of_monopolistic_rating = models.PositiveIntegerField()
    Tc3_Evolving_technology_Favoring_politically_popular =  models.CharField(max_length=200)
    Tc3_Evolving_technology_Favoring_politically_popular_rating = models.PositiveIntegerField()
    Tc3_Evolving_technology_Delays_downtime =  models.CharField(max_length=200)
    Tc3_Evolving_technology_Delays_downtime_rating = models.PositiveIntegerField()
    Tc3_Evolving_technology_Equipment_parts =  models.CharField(max_length=200)
    Tc3_Evolving_technology_Equipment_parts_rating = models.PositiveIntegerField()
    Tc3_Evolving_technology_construction_preceding =  models.CharField(max_length=200)
    Tc3_Evolving_technology_construction_preceding_rating = models.PositiveIntegerField()


# necesstiy of tunnels, overpasses, barriers in areas with flora/fauna/water-bodies/settlements 


    Tc4_necesstiy_of_tunnels_use_of_monopolistic =  models.CharField(max_length=200)
    Tc4_necesstiy_of_tunnels_use_of_monopolistic_rating = models.PositiveIntegerField()
    Tc4_necesstiy_of_tunnels_Favoring_politically_popular =  models.CharField(max_length=200)
    Tc4_necesstiy_of_tunnels_Favoring_politically_popular_rating = models.PositiveIntegerField()
    Tc4_necesstiy_of_tunnels_Delays_downtime =  models.CharField(max_length=200)
    Tc4_necesstiy_of_tunnels_Delays_downtime_rating = models.PositiveIntegerField()
    Tc4_necesstiy_of_tunnels_Equipment_parts =  models.CharField(max_length=200)
    Tc4_necesstiy_of_tunnels_Equipment_parts_rating = models.PositiveIntegerField()
    Tc4_necesstiy_of_tunnels_construction_preceding =  models.CharField(max_length=200)
    Tc4_necesstiy_of_tunnels_construction_preceding_rating = models.PositiveIntegerField()


# use of monopolistic foreign contractor limiting technology transfer to local firms/citizens 



    Tc5_use_of_monopolistic_Favoring_politically_popular =  models.CharField(max_length=200)
    Tc5_use_of_monopolistic_Favoring_politically_popular_rating = models.PositiveIntegerField()
    Tc5_use_of_monopolistic_Delays_downtime =  models.CharField(max_length=200)
    Tc5_use_of_monopolistic_Delays_downtime_rating = models.PositiveIntegerField()
    Tc5_use_of_monopolistic_Equipment_parts =  models.CharField(max_length=200)
    Tc5_use_of_monopolistic_Equipment_parts_rating = models.PositiveIntegerField()
    Tc5_use_of_monopolistic_construction_preceding =  models.CharField(max_length=200)
    Tc5_use_of_monopolistic_construction_preceding_rating = models.PositiveIntegerField()


# Favoring politically-popular but inefficient labor intensive technology


    Tc6_Favoring_politically_popular_Delays_downtime =  models.CharField(max_length=200)
    Tc6_Favoring_politically_popular_Delays_downtime_rating = models.PositiveIntegerField()
    Tc6_Favoring_politically_popular_Equipment_parts =  models.CharField(max_length=200)
    Tc6_Favoring_politically_popular_Equipment_parts_rating = models.PositiveIntegerField()
    Tc6_Favoring_politically_popular_construction_preceding =  models.CharField(max_length=200)
    Tc6_Favoring_politically_popular_construction_preceding_rating = models.PositiveIntegerField()


# Delays/downtime due to low-utilization of efficient border clearance technology


    Tc7_Delays_downtime_Equipment_parts =  models.CharField(max_length=200)
    Tc7_Delays_downtime_Equipment_parts_rating = models.PositiveIntegerField()
    Tc7_Delays_downtime_construction_preceding =  models.CharField(max_length=200)
    Tc7_Delays_downtime_construction_preceding_rating = models.PositiveIntegerField()


# Equipment/parts supply disruption by pandemics and local unavailability of equipment dealers

    Tc8_Equipment_parts_construction_preceding =  models.CharField(max_length=200)
    Tc8_Equipment_parts_construction_preceding_rating = models.PositiveIntegerField()

   
   
    class Meta:
        verbose_name = _('Technology Data')
        verbose_name_plural = _('Technology Data')
        ordering = ('-pk',)

    def __str__(self):
        return f'{self.Correspondent_Email.email}'
    
    
    
class SocialFactorDataA(models.Model):
    
    Correspondent_Email = models.OneToOneField(SurveyUser, on_delete=models.CASCADE, blank=True, null=True)
    fullname = models.CharField(max_length=200, blank=True, null=True)
    
    
    # Disrupted social interaction by settlement split/displacement


    So1_Disrupted_social_Benefits_unlikely=  models.CharField(max_length=200)
    So1_Disrupted_social_Benefits_unlikely_rating = models.PositiveIntegerField()
    So1_Disrupted_social_loss_of_work=  models.CharField(max_length=200)
    So1_Disrupted_social_loss_of_work_rating = models.PositiveIntegerField()
    So1_Disrupted_social_Hard_to_identify=  models.CharField(max_length=200)
    So1_Disrupted_social_Hard_to_identify_rating = models.PositiveIntegerField()
    So1_Disrupted_social_High_speed=  models.CharField(max_length=200)
    So1_Disrupted_social_High_speed_rating = models.PositiveIntegerField()
    So1_Disrupted_social_Crowding=  models.CharField(max_length=200)
    So1_Disrupted_social_Crowding_rating = models.PositiveIntegerField()
    So1_Disrupted_social_low_per_capita=  models.CharField(max_length=200)
    So1_Disrupted_social_low_per_capita_rating = models.PositiveIntegerField()
    So1_Disrupted_social_Food_security=  models.CharField(max_length=200)
    So1_Disrupted_social_Food_security_rating = models.PositiveIntegerField()
    So1_Disrupted_social_Community_resistance=  models.CharField(max_length=200)
    So1_Disrupted_social_Community_resistance_rating = models.PositiveIntegerField()


# Benefits unlikely to trickle to local communities


    So2_Benefits_unlikely_loss_of_work=  models.CharField(max_length=200)
    So2_Benefits_unlikely_loss_of_work_rating = models.PositiveIntegerField()
    So2_Benefits_unlikely_Hard_to_identify=  models.CharField(max_length=200)
    So2_Benefits_unlikely_Hard_to_identify_rating = models.PositiveIntegerField()
    So2_Benefits_unlikely_High_speed=  models.CharField(max_length=200)
    So2_Benefits_unlikely_High_speed_rating = models.PositiveIntegerField()
    So2_Benefits_unlikely_Crowding=  models.CharField(max_length=200)
    So2_Benefits_unlikely_Crowding_rating = models.PositiveIntegerField()
    So2_Benefits_unlikely_low_per_capita=  models.CharField(max_length=200)
    So2_Benefits_unlikely_low_per_capita_rating = models.PositiveIntegerField()
    So2_Benefits_unlikely_Food_security=  models.CharField(max_length=200)
    So2_Benefits_unlikely_Food_security_rating = models.PositiveIntegerField()
    So2_Benefits_unlikely_Community_resistance=  models.CharField(max_length=200)
    So2_Benefits_unlikely_Community_resistance_rating = models.PositiveIntegerField()


# loss of work/opportunity to immigrants due to inadequate skill and language barrier



    So3_loss_of_work_Hard_to_identify=  models.CharField(max_length=200)
    So3_loss_of_work_Hard_to_identify_rating = models.PositiveIntegerField()
    So3_loss_of_work_High_speed=  models.CharField(max_length=200)
    So3_loss_of_work_High_speed_rating = models.PositiveIntegerField()
    So3_loss_of_work_Crowding=  models.CharField(max_length=200)
    So3_loss_of_work_Crowding_rating = models.PositiveIntegerField()
    So3_loss_of_work_low_per_capita=  models.CharField(max_length=200)
    So3_loss_of_work_low_per_capita_rating = models.PositiveIntegerField()
    So3_loss_of_work_Food_security=  models.CharField(max_length=200)
    So3_loss_of_work_Food_security_rating = models.PositiveIntegerField()
    So3_loss_of_work_Community_resistance=  models.CharField(max_length=200)
    So3_loss_of_work_Community_resistance_rating = models.PositiveIntegerField()


# Hard to identify Project Affected Persons due to conflict/environmental/economic migration



    So4_Hard_to_identify_High_speed=  models.CharField(max_length=200)
    So4_Hard_to_identify_High_speed_rating = models.PositiveIntegerField()
    So4_Hard_to_identify_Crowding=  models.CharField(max_length=200)
    So4_Hard_to_identify_Crowding_rating = models.PositiveIntegerField()
    So4_Hard_to_identify_low_per_capita=  models.CharField(max_length=200)
    So4_Hard_to_identify_low_per_capita_rating = models.PositiveIntegerField()
    So4_Hard_to_identify_Food_security=  models.CharField(max_length=200)
    So4_Hard_to_identify_Food_security_rating = models.PositiveIntegerField()
    So4_Hard_to_identify_Community_resistance=  models.CharField(max_length=200)
    So4_Hard_to_identify_Community_resistance_rating = models.PositiveIntegerField()

# High-speed traffic and dangerous goods carriage threaten human safety/livelihood activities


    So5_High_speed_Crowding=  models.CharField(max_length=200)
    So5_High_speed_Crowding_rating = models.PositiveIntegerField()
    So5_High_speed_low_per_capita=  models.CharField(max_length=200)
    So5_High_speed_low_per_capita_rating = models.PositiveIntegerField()
    So5_High_speed_Food_security=  models.CharField(max_length=200)
    So5_High_speed_Food_security_rating = models.PositiveIntegerField()
    So5_High_speed_Community_resistance=  models.CharField(max_length=200)
    So5_High_speed_Community_resistance_rating = models.PositiveIntegerField()

# Crowding out local population due to increased cost of basic goods/services

    So6_Crowding_low_per_capita=  models.CharField(max_length=200)
    So6_Crowding_low_per_capita_rating = models.PositiveIntegerField()
    So6_Crowding_Food_security=  models.CharField(max_length=200)
    So6_Crowding_Food_security_rating = models.PositiveIntegerField()
    So6_Crowding_Community_resistance=  models.CharField(max_length=200)
    So6_Crowding_Community_resistance_rating = models.PositiveIntegerField()

# low per-capita income levels limits revenue mobilization from taxation  


    So7_low_per_capita_Food_security=  models.CharField(max_length=200)
    So7_low_per_capita_Food_security_rating = models.PositiveIntegerField()
    So7_low_per_capita_Community_resistance=  models.CharField(max_length=200)
    So7_low_per_capita_Community_resistance_rating = models.PositiveIntegerField()


# Food security threat by farmers switch to non-farming activity


    So8_Food_security_Community_resistance=  models.CharField(max_length=200)
    So8_Food_security_Community_resistance_rating = models.PositiveIntegerField()

    
    
       
    class Meta:
        verbose_name = _('Social Data')
        verbose_name_plural = _('Social Data')
        ordering = ('-pk',)

    def __str__(self):
        return f'{self.Correspondent_Email.email}'




    
class EnvironmentalFactorDataA(models.Model):
    
    Correspondent_Email = models.OneToOneField(SurveyUser, on_delete=models.CASCADE, blank=True, null=True)
    fullname = models.CharField(max_length=200, blank=True, null=True)
    
    
    # Disrupted social interaction by settlement split/displacement


# Extreme weather events (floods/hot-sun/humidity) shorten corridor lifespan

    En1_Extreme_weather_requirement_to_minimise=  models.CharField(max_length=200)
    En1_Extreme_weather_requirement_to_minimise_rating = models.PositiveIntegerField()
    En1_Extreme_weather_crossing_diverse=  models.CharField(max_length=200)
    En1_Extreme_weather_crossing_diverse_rating = models.PositiveIntegerField()
    En1_Extreme_weather_enhanced_access=  models.CharField(max_length=200)
    En1_Extreme_weather_enhanced_access_rating = models.PositiveIntegerField()
    En1_Extreme_weather_Disasters_due=  models.CharField(max_length=200)
    En1_Extreme_weather_Disasters_due_rating = models.PositiveIntegerField()
    En1_Extreme_weather_Ecosystem_resources=  models.CharField(max_length=200)
    En1_Extreme_weather_Ecosystem_resources_rating = models.PositiveIntegerField()
    En1_Extreme_weather_Human_induced=  models.CharField(max_length=200)
    En1_Extreme_weather_Human_induced_rating = models.PositiveIntegerField()
    En1_Extreme_weather_Climate_change=  models.CharField(max_length=200)
    En1_Extreme_weather_Climate_change_rating = models.PositiveIntegerField()
    En1_Extreme_weather_requirement_to_safeguard=  models.CharField(max_length=200)
    En1_Extreme_weather_requirement_to_safeguard_rating = models.PositiveIntegerField()

# requirement to minimise alteration of hydrological patterns/flora/fauna/migratory corridors


    En2_requirement_to_minimise_crossing_diverse=  models.CharField(max_length=200)
    En2_requirement_to_minimise_crossing_diverse_rating = models.PositiveIntegerField()
    En2_requirement_to_minimise_enhanced_access=  models.CharField(max_length=200)
    En2_requirement_to_minimise_enhanced_access_rating = models.PositiveIntegerField()
    En2_requirement_to_minimise_Disasters_due=  models.CharField(max_length=200)
    En2_requirement_to_minimise_Disasters_due_rating = models.PositiveIntegerField()
    En2_requirement_to_minimise_Ecosystem_resources=  models.CharField(max_length=200)
    En2_requirement_to_minimise_Ecosystem_resources_rating = models.PositiveIntegerField()
    En2_requirement_to_minimise_Human_induced=  models.CharField(max_length=200)
    En2_requirement_to_minimise_Human_induced_rating = models.PositiveIntegerField()
    En2_requirement_to_minimise_Climate_change=  models.CharField(max_length=200)
    En2_requirement_to_minimise_Climate_change_rating = models.PositiveIntegerField()
    En2_requirement_to_minimise_requirement_to_safeguard=  models.CharField(max_length=200)
    En2_requirement_to_minimise_requirement_to_safeguard_rating = models.PositiveIntegerField()

# crossing diverse climate zones impacts design complexity and maintainance cost


    En3_crossing_diverse_enhanced_access=  models.CharField(max_length=200)
    En3_crossing_diverse_enhanced_access_rating = models.PositiveIntegerField()
    En3_crossing_diverse_Disasters_due=  models.CharField(max_length=200)
    En3_crossing_diverse_Disasters_due_rating = models.PositiveIntegerField()
    En3_crossing_diverse_Ecosystem_resources=  models.CharField(max_length=200)
    En3_crossing_diverse_Ecosystem_resources_rating = models.PositiveIntegerField()
    En3_crossing_diverse_Human_induced=  models.CharField(max_length=200)
    En3_crossing_diverse_Human_induced_rating = models.PositiveIntegerField()
    En3_crossing_diverse_Climate_change=  models.CharField(max_length=200)
    En3_crossing_diverse_Climate_change_rating = models.PositiveIntegerField()
    En3_crossing_diverse_requirement_to_safeguard=  models.CharField(max_length=200)
    En3_crossing_diverse_requirement_to_safeguard_rating = models.PositiveIntegerField()

# enhanced access to aggravate poaching, illegal lumbering and mining


    En4_enhanced_access_Disasters_due=  models.CharField(max_length=200)
    En4_enhanced_access_Disasters_due_rating = models.PositiveIntegerField()
    En4_enhanced_access_Ecosystem_resources=  models.CharField(max_length=200)
    En4_enhanced_access_Ecosystem_resources_rating = models.PositiveIntegerField()
    En4_enhanced_access_Human_induced=  models.CharField(max_length=200)
    En4_enhanced_access_Human_induced_rating = models.PositiveIntegerField()
    En4_enhanced_access_Climate_change=  models.CharField(max_length=200)
    En4_enhanced_access_Climate_change_rating = models.PositiveIntegerField()
    En4_enhanced_access_requirement_to_safeguard=  models.CharField(max_length=200)
    En4_enhanced_access_requirement_to_safeguard_rating = models.PositiveIntegerField()

# Disasters due to weather related events


    En5_Disasters_due_Ecosystem_resources=  models.CharField(max_length=200)
    En5_Disasters_due_Ecosystem_resources_rating = models.PositiveIntegerField()
    En5_Disasters_due_Human_induced=  models.CharField(max_length=200)
    En5_Disasters_due_Human_induced_rating = models.PositiveIntegerField()
    En5_Disasters_due_Climate_change=  models.CharField(max_length=200)
    En5_Disasters_due_Climate_change_rating = models.PositiveIntegerField()
    En5_Disasters_due_requirement_to_safeguard=  models.CharField(max_length=200)
    En5_Disasters_due_requirement_to_safeguard_rating = models.PositiveIntegerField()


# Ecosystem resources degradadation by settlement densification/immigrants influx


    En6_Ecosystem_resources_Human_induced=  models.CharField(max_length=200)
    En6_Ecosystem_resources_Human_induced_rating = models.PositiveIntegerField()
    En6_Ecosystem_resources_Climate_change=  models.CharField(max_length=200)
    En6_Ecosystem_resources_Climate_change_rating = models.PositiveIntegerField()
    En6_Ecosystem_resources_requirement_to_safeguard=  models.CharField(max_length=200)
    En6_Ecosystem_resources_requirement_to_safeguard_rating = models.PositiveIntegerField()


# Human induced landslide, soil erosion and water-body sedimentation

    En7_Human_induced_Climate_change=  models.CharField(max_length=200)
    En7_Human_induced_Climate_change_rating = models.PositiveIntegerField()
    En7_Human_induced_requirement_to_safeguard=  models.CharField(max_length=200)
    En7_Human_induced_requirement_to_safeguard_rating = models.PositiveIntegerField()


# Climate change induced variation of average local weather patterns

    En8_Climate_change_requirement_to_safeguard=  models.CharField(max_length=200)
    En8_Climate_change_requirement_to_safeguard_rating = models.PositiveIntegerField()   
    
    
    class Meta:
        verbose_name = _('Environmental Data')
        verbose_name_plural = _('Environmental Data')
        ordering = ('-pk',)

    def __str__(self):
        return f'{self.Correspondent_Email.email}'