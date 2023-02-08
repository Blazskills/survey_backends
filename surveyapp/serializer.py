from rest_framework import serializers

from surveyapp.models import IntroSurveyDataA, SurveyUser

from django.db import IntegrityError


class SurveyUserListSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(error_messages={
        'required': 'Full name is required.',
        'blank': 'Full name is required.'
    })
    country = serializers.CharField(error_messages={
        'required': 'country is required.',
        'blank': 'Country is required.'
    })
    class Meta:
        model = SurveyUser
        fields = ['id', 'full_name', 'email','country','occupation','education_level']



class SurveyFormSubmitSerializer(serializers.Serializer):
    
    useremail = serializers.CharField()
    username = serializers.CharField()
    pol_landuse = serializers.CharField()
    pol_landuse_rating = serializers.IntegerField()
    
    
    pol_Geographic = serializers.CharField()
    pol_Geographic_rating = serializers.IntegerField()
    pol_Economic = serializers.CharField()
    pol_Economic_rating = serializers.IntegerField()
    pol_Technological = serializers.CharField()
    pol_Technological_rating = serializers.IntegerField()
    pol_Social = serializers.CharField()
    pol_Social_rating = serializers.IntegerField()
    pol_Environmental = serializers.CharField()
    pol_Environmental_rating = serializers.IntegerField()

        
    landuse_geographic = serializers.CharField()
    landuse_geograhpic_rating = serializers.IntegerField()
    landuse_Economic = serializers.CharField()
    landuse_Economic_rating = serializers.IntegerField()
    landuse_Technological = serializers.CharField()
    landuse_Technological_rating = serializers.IntegerField()
    landuse_Social = serializers.CharField()
    landuse_Social_rating = serializers.IntegerField()
    landuse_Environmental = serializers.CharField()
    landuse_Environmental_rating = serializers.IntegerField()


    geographic_Economic = serializers.CharField()
    geographic_Economic_rating = serializers.IntegerField()
    geographic_Technological = serializers.CharField()
    geographic_Technological_rating = serializers.IntegerField()
    geographic_Social = serializers.CharField()
    geographic_Social_rating = serializers.IntegerField()
    geographic_Environmental = serializers.CharField()
    geographic_Environmental_rating = serializers.IntegerField()
    
    
    economic_Technological = serializers.CharField()
    economic_Technological_rating = serializers.IntegerField()
    economic_Social = serializers.CharField()
    economic_Social_rating = serializers.IntegerField()
    economic_Environmental = serializers.CharField()
    economic_Environmental_rating = serializers.IntegerField()
    
    
    technological_Social = serializers.CharField()
    technological_Social_rating = serializers.IntegerField()
    technological_Environmental = serializers.CharField()
    technological_Environmental_rating = serializers.IntegerField()
    
    
    social_Environmental = serializers.CharField()
    social_Environmental_rating = serializers.IntegerField()
    
    
#  Page 2
    
    p1_Insecurity_instability_Border_Check = serializers.CharField(max_length=200)
    p1_Insecurity_instability_Border_Check_rating = serializers.IntegerField()
    p1_Insecurity_instability_Policy_nonalignment = serializers.CharField(max_length=200)
    p1_Insecurity_instability_Policy_nonalignment_rating = serializers.IntegerField()
    p1_Insecurity_instability_weak_institutions = serializers.CharField(max_length=200)
    p1_Insecurity_instability_weak_institutions_rating = serializers.IntegerField()
    p1_Insecurity_instability_disimilar_regulation = serializers.CharField(max_length=200)
    p1_Insecurity_instability_disimilar_regulation_rating = serializers.IntegerField()
    p1_Insecurity_instability_inability_to_observe = serializers.CharField(max_length=200)
    p1_Insecurity_instability_inability_to_observe_rating = serializers.IntegerField()
    p1_Insecurity_instability_corruption_impact = serializers.CharField(max_length=200)
    p1_Insecurity_instability_corruption_impact_rating = serializers.IntegerField()
    p1_Insecurity_instability_realignment_design = serializers.CharField(max_length=200)
    p1_Insecurity_instability_realignment_design_rating = serializers.IntegerField()
    p1_Insecurity_instability_commitment_fluctuation = serializers.CharField(max_length=200)
    p1_Insecurity_instability_commitment_fluctuation_rating = serializers.IntegerField()

        
   
    p2_Border_Check_Policy_nonalignment = serializers.CharField(max_length=200)
    p2_Border_Check_Policy_nonalignment_rating = serializers.IntegerField()
    p2_Border_Check_weak_institutions = serializers.CharField(max_length=200)
    p2_Border_Check_weak_institutions_rating = serializers.IntegerField()
    p2_Border_Check_disimilar_regulation = serializers.CharField(max_length=200)
    p2_Border_Check_disimilar_regulation_rating = serializers.IntegerField()
    p2_Border_Check_inability_to_observe = serializers.CharField(max_length=200)
    p2_Border_Check_inability_to_observe_rating = serializers.IntegerField()
    p2_Border_Check_corruption_impact = serializers.CharField(max_length=200)
    p2_Border_Check_corruption_impact_rating = serializers.IntegerField()
    p2_Border_Check_realignment_design = serializers.CharField(max_length=200)
    p2_Border_Check_realignment_design_rating = serializers.IntegerField()
    p2_Border_Check_commitment_fluctuation = serializers.CharField(max_length=200)
    p2_Border_Check_commitment_fluctuation_rating = serializers.IntegerField()
    
    
    
    p3_Policy_nonalignment_weak_institutions = serializers.CharField(max_length=200)
    p3_Policy_nonalignment_weak_institutions_rating = serializers.IntegerField()
    p3_Policy_nonalignment_disimilar_regulation = serializers.CharField(max_length=200)
    p3_Policy_nonalignment_disimilar_regulation_rating = serializers.IntegerField()
    p3_Policy_nonalignment_inability_to_observe = serializers.CharField(max_length=200)
    p3_Policy_nonalignment_inability_to_observe_rating = serializers.IntegerField()
    p3_Policy_nonalignment_corruption_impact = serializers.CharField(max_length=200)
    p3_Policy_nonalignment_corruption_impact_rating = serializers.IntegerField()
    p3_Policy_nonalignment_realignment_design = serializers.CharField(max_length=200)
    p3_Policy_nonalignment_realignment_design_rating = serializers.IntegerField()
    p3_Policy_nonalignment_commitment_fluctuation = serializers.CharField(max_length=200)
    p3_Policy_nonalignment_commitment_fluctuation_rating = serializers.IntegerField()
    
    
    
    p4_weak_institutions_disimilar_regulation = serializers.CharField(max_length=200)
    p4_weak_institutions_disimilar_regulation_rating = serializers.IntegerField()
    p4_weak_institutions_inability_to_observe = serializers.CharField(max_length=200)
    p4_weak_institutions_inability_to_observe_rating = serializers.IntegerField()
    p4_weak_institutions_corruption_impact = serializers.CharField(max_length=200)
    p4_weak_institutions_corruption_impact_rating = serializers.IntegerField()
    p4_weak_institutions_realignment_design = serializers.CharField(max_length=200)
    p4_weak_institutions_realignment_design_rating = serializers.IntegerField()
    p4_weak_institutions_commitment_fluctuation = serializers.CharField(max_length=200)
    p4_weak_institutions_commitment_fluctuation_rating = serializers.IntegerField()
    
    
    p5_disimilar_regulation_inability_to_observe = serializers.CharField(max_length=200)
    p5_disimilar_regulation_inability_to_observe_rating = serializers.IntegerField()
    p5_disimilar_regulation_corruption_impact = serializers.CharField(max_length=200)
    p5_disimilar_regulation_corruption_impact_rating = serializers.IntegerField()
    p5_disimilar_regulation_realignment_design = serializers.CharField(max_length=200)
    p5_disimilar_regulation_realignment_design_rating = serializers.IntegerField()
    p5_disimilar_regulation_commitment_fluctuation = serializers.CharField(max_length=200)
    p5_disimilar_regulation_commitment_fluctuation_rating = serializers.IntegerField()
    
    
    p6_inability_to_observe_corruption_impact = serializers.CharField(max_length=200)
    p6_inability_to_observe_corruption_impact_rating = serializers.IntegerField()
    p6_inability_to_observe_realignment_design = serializers.CharField(max_length=200)
    p6_inability_to_observe_realignment_design_rating = serializers.IntegerField()
    p6_inability_to_observe_commitment_fluctuation = serializers.CharField(max_length=200)
    p6_inability_to_observe_commitment_fluctuation_rating = serializers.IntegerField()
    
    
    p7_corruption_impact_realignment_design = serializers.CharField(max_length=200)
    p7_corruption_impact_realignment_design_rating = serializers.IntegerField()
    p7_corruption_impact_commitment_fluctuation = serializers.CharField(max_length=200)
    p7_corruption_impact_commitment_fluctuation_rating = serializers.IntegerField()
    
    
    p8_realignment_design_commitment_fluctuation = serializers.CharField(max_length=200)
    p8_realignment_design_commitment_fluctuation_rating = serializers.IntegerField()
    
    # Page 3
    
    L1_Speculative_land_Likely_split = serializers.CharField(max_length=200)
    L1_Speculative_land_Likely_split_rating = serializers.IntegerField()
    L1_Speculative_land_Hard_to_determine = serializers.CharField(max_length=200)
    L1_Speculative_land_Hard_to_determine_rating = serializers.IntegerField()
    L1_Speculative_land_Perception_project = serializers.CharField(max_length=200)
    L1_Speculative_land_Perception_project_rating = serializers.IntegerField()
    L1_Speculative_land_Corridor_efficiency = serializers.CharField(max_length=200)
    L1_Speculative_land_Corridor_efficiency_rating = serializers.IntegerField()
    L1_Speculative_land_Perception_Land = serializers.CharField(max_length=200)
    L1_Speculative_land_Perception_Land_rating = serializers.IntegerField()
    L1_Speculative_land_limited_access = serializers.CharField(max_length=200)
    L1_Speculative_land_limited_access_rating = serializers.IntegerField()
    L1_Speculative_land_communal_informal = serializers.CharField(max_length=200)
    L1_Speculative_land_communal_informal_rating = serializers.IntegerField()
    L1_Speculative_land_weak_land = serializers.CharField(max_length=200)
    L1_Speculative_land_weak_land_rating = serializers.IntegerField()
    
    
    L2_Likely_split_Hard_to_determine = serializers.CharField(max_length=200)
    L2_Likely_split_Hard_to_determine_rating = serializers.IntegerField()
    L2_Likely_split_Perception_project = serializers.CharField(max_length=200)
    L2_Likely_split_Perception_project_rating = serializers.IntegerField()
    L2_Likely_split_Corridor_efficiency = serializers.CharField(max_length=200)
    L2_Likely_split_Corridor_efficiency_rating = serializers.IntegerField()
    L2_Likely_split_Perception_Land = serializers.CharField(max_length=200)
    L2_Likely_split_Perception_Land_rating = serializers.IntegerField()
    L2_Likely_split_limited_access = serializers.CharField(max_length=200)
    L2_Likely_split_limited_access_rating = serializers.IntegerField()
    L2_Likely_split_communal_informal = serializers.CharField(max_length=200)
    L2_Likely_split_communal_informal_rating = serializers.IntegerField()
    L2_Likely_split_weak_land = serializers.CharField(max_length=200)
    L2_Likely_split_weak_land_rating = serializers.IntegerField()
    

    L3_Hard_to_determine_Perception_project = serializers.CharField(max_length=200)
    L3_Hard_to_determine_Perception_project_rating = serializers.IntegerField()
    L3_Hard_to_determine_Corridor_efficiency = serializers.CharField(max_length=200)
    L3_Hard_to_determine_Corridor_efficiency_rating = serializers.IntegerField()
    L3_Hard_to_determine_Perception_Land = serializers.CharField(max_length=200)
    L3_Hard_to_determine_Perception_Land_rating = serializers.IntegerField()
    L3_Hard_to_determine_limited_access = serializers.CharField(max_length=200)
    L3_Hard_to_determine_limited_access_rating = serializers.IntegerField()
    L3_Hard_to_determine_communal_informal = serializers.CharField(max_length=200)
    L3_Hard_to_determine_communal_informal_rating = serializers.IntegerField()
    L3_Hard_to_determine_weak_land = serializers.CharField(max_length=200)
    L3_Hard_to_determine_weak_land_rating = serializers.IntegerField()
    
    
    
    L4_Perception_project_Corridor_efficiency = serializers.CharField(max_length=200)
    L4_Perception_project_Corridor_efficiency_rating = serializers.IntegerField()
    L4_Perception_project_Perception_Land = serializers.CharField(max_length=200)
    L4_Perception_project_Perception_Land_rating = serializers.IntegerField()
    L4_Perception_project_limited_access = serializers.CharField(max_length=200)
    L4_Perception_project_limited_access_rating = serializers.IntegerField()
    L4_Perception_project_communal_informal = serializers.CharField(max_length=200)
    L4_Perception_project_communal_informal_rating = serializers.IntegerField()
    L4_Perception_project_weak_land = serializers.CharField(max_length=200)
    L4_Perception_project_weak_land_rating = serializers.IntegerField()
    
    
    L5_Corridor_efficiency_Perception_Land = serializers.CharField(max_length=200)
    L5_Corridor_efficiency_Perception_Land_rating = serializers.IntegerField()
    L5_Corridor_efficiency_limited_access = serializers.CharField(max_length=200)
    L5_Corridor_efficiency_limited_access_rating = serializers.IntegerField()
    L5_Corridor_efficiency_communal_informal = serializers.CharField(max_length=200)
    L5_Corridor_efficiency_communal_informal_rating = serializers.IntegerField()
    L5_Corridor_efficiency_weak_land = serializers.CharField(max_length=200)
    L5_Corridor_efficiency_weak_land_rating = serializers.IntegerField()
    
    
    L6_Perception_Land_limited_access = serializers.CharField(max_length=200)
    L6_Perception_Land_limited_access_rating = serializers.IntegerField()
    L6_Perception_Land_communal_informal = serializers.CharField(max_length=200)
    L6_Perception_Land_communal_informal_rating = serializers.IntegerField()
    L6_Perception_Land_weak_land = serializers.CharField(max_length=200)
    L6_Perception_Land_weak_land_rating = serializers.IntegerField()
  
    
    L7_limited_access_communal_informal = serializers.CharField(max_length=200)
    L7_limited_access_communal_informal_rating = serializers.IntegerField()
    L7_limited_access_weak_land = serializers.CharField(max_length=200)
    L7_limited_access_weak_land_rating = serializers.IntegerField()
    
    
    L8_communal_informal_weak_land = serializers.CharField(max_length=200)
    L8_communal_informal_weak_land_rating = serializers.IntegerField()
    
    
    
    # page 4
    
    G1_Lateritic_soft_Flood_prone_water =  serializers.CharField(max_length=200)
    G1_Lateritic_soft_Flood_prone_water_rating = serializers.IntegerField()
    G1_Lateritic_soft_Diverse_terrain =  serializers.CharField(max_length=200)
    G1_Lateritic_soft_Diverse_terrain_rating = serializers.IntegerField()
    G1_Lateritic_soft_Crossing_seismic =  serializers.CharField(max_length=200)
    G1_Lateritic_soft_Crossing_seismic_rating = serializers.IntegerField()
    G1_Lateritic_soft_Landslide_flooding =  serializers.CharField(max_length=200)
    G1_Lateritic_soft_Landslide_flooding_rating = serializers.IntegerField()
    G1_Lateritic_soft_Traversing_mining =  serializers.CharField(max_length=200)
    G1_Lateritic_soft_Traversing_mining_rating = serializers.IntegerField()
    G1_Lateritic_soft_Sparse_detached =  serializers.CharField(max_length=200)
    G1_Lateritic_soft_Sparse_detached_rating = serializers.IntegerField()
    G1_Lateritic_soft_undocumented_geological =  serializers.CharField(max_length=200)
    G1_Lateritic_soft_undocumented_geological_rating = serializers.IntegerField()
    G1_Lateritic_soft_Geopolitical_consideration =  serializers.CharField(max_length=200)
    G1_Lateritic_soft_Geopolitical_consideration_rating = serializers.IntegerField()


   #Flood-prone/water logged areas necessitating costly foundation design 


    G2_Flood_prone_water_Diverse_terrain =  serializers.CharField(max_length=200)
    G2_Flood_prone_water_Diverse_terrain_rating = serializers.IntegerField()
    G2_Flood_prone_water_Crossing_seismic =  serializers.CharField(max_length=200)
    G2_Flood_prone_water_Crossing_seismic_rating = serializers.IntegerField()
    G2_Flood_prone_water_Landslide_flooding =  serializers.CharField(max_length=200)
    G2_Flood_prone_water_Landslide_flooding_rating = serializers.IntegerField()
    G2_Flood_prone_water_Traversing_mining =  serializers.CharField(max_length=200)
    G2_Flood_prone_water_Traversing_mining_rating = serializers.IntegerField()
    G2_Flood_prone_water_Sparse_detached =  serializers.CharField(max_length=200)
    G2_Flood_prone_water_Sparse_detached_rating = serializers.IntegerField()
    G2_Flood_prone_water_undocumented_geological =  serializers.CharField(max_length=200)
    G2_Flood_prone_water_undocumented_geological_rating = serializers.IntegerField()
    G2_Flood_prone_water_Geopolitical_consideration =  serializers.CharField(max_length=200)
    G2_Flood_prone_water_Geopolitical_consideration_rating = serializers.IntegerField()



   #Diverse terrain (flat/ rolling/mountain/escarpments) increase design and technology complexity 


    G3_Diverse_terrain_Crossing_seismic =  serializers.CharField(max_length=200)
    G3_Diverse_terrain_Crossing_seismic_rating = serializers.IntegerField()
    G3_Diverse_terrain_Landslide_flooding =  serializers.CharField(max_length=200)
    G3_Diverse_terrain_Landslide_flooding_rating = serializers.IntegerField()
    G3_Diverse_terrain_Traversing_mining =  serializers.CharField(max_length=200)
    G3_Diverse_terrain_Traversing_mining_rating = serializers.IntegerField()
    G3_Diverse_terrain_Sparse_detached =  serializers.CharField(max_length=200)
    G3_Diverse_terrain_Sparse_detached_rating = serializers.IntegerField()
    G3_Diverse_terrain_undocumented_geological =  serializers.CharField(max_length=200)
    G3_Diverse_terrain_undocumented_geological_rating = serializers.IntegerField()
    G3_Diverse_terrain_Geopolitical_consideration =  serializers.CharField(max_length=200)
    G3_Diverse_terrain_Geopolitical_consideration_rating = serializers.IntegerField()



   #Crossing seismic active Great Rift Valley 


    G4_Crossing_seismic_Landslide_flooding =  serializers.CharField(max_length=200)
    G4_Crossing_seismic_Landslide_flooding_rating = serializers.IntegerField()
    G4_Crossing_seismic_Traversing_mining =  serializers.CharField(max_length=200)
    G4_Crossing_seismic_Traversing_mining_rating = serializers.IntegerField()
    G4_Crossing_seismic_Sparse_detached =  serializers.CharField(max_length=200)
    G4_Crossing_seismic_Sparse_detached_rating = serializers.IntegerField()
    G4_Crossing_seismic_undocumented_geological =  serializers.CharField(max_length=200)
    G4_Crossing_seismic_undocumented_geological_rating = serializers.IntegerField()
    G4_Crossing_seismic_Geopolitical_consideration =  serializers.CharField(max_length=200)
    G4_Crossing_seismic_Geopolitical_consideration_rating = serializers.IntegerField()

   #Landslide,flooding, erosion events could potentially delay project schedule and disrupt operations


    G5_Landslide_flooding_Traversing_mining =  serializers.CharField(max_length=200)
    G5_Landslide_flooding_Traversing_mining_rating = serializers.IntegerField()
    G5_Landslide_flooding_Sparse_detached =  serializers.CharField(max_length=200)
    G5_Landslide_flooding_Sparse_detached_rating = serializers.IntegerField()
    G5_Landslide_flooding_undocumented_geological =  serializers.CharField(max_length=200)
    G5_Landslide_flooding_undocumented_geological_rating = serializers.IntegerField()
    G5_Landslide_flooding_Geopolitical_consideration =  serializers.CharField(max_length=200)
    G5_Landslide_flooding_Geopolitical_consideration_rating = serializers.IntegerField()

   #Traversing mining areas with active blasting/ explosions


    G6_Traversing_mining_Sparse_detached =  serializers.CharField(max_length=200)
    G6_Traversing_mining_Sparse_detached_rating = serializers.IntegerField()
    G6_Traversing_mining_undocumented_geological =  serializers.CharField(max_length=200)
    G6_Traversing_mining_undocumented_geological_rating = serializers.IntegerField()
    G6_Traversing_mining_Geopolitical_consideration =  serializers.CharField(max_length=200)
    G6_Traversing_mining_Geopolitical_consideration_rating = serializers.IntegerField()



   #Sparse/detached settlement pattern unfeasible to link with GELB

    G7_Sparse_detached_undocumented_geological =  serializers.CharField(max_length=200)
    G7_Sparse_detached_undocumented_geological_rating = serializers.IntegerField()
    G7_Sparse_detached_Geopolitical_consideration =  serializers.CharField(max_length=200)
    G7_Sparse_detached_Geopolitical_consideration_rating = serializers.IntegerField()


    ##undocumented geological/subsurface condition

    G8_undocumented_geological_Geopolitical_consideration =  serializers.CharField(max_length=200)
    G8_undocumented_geological_Geopolitical_consideration_rating = serializers.IntegerField()
    
    
    
    # Page 5
    
    #  Dependance on scarce govt finance with few alternatives

    Ec1_Dependance_Fiscally_strong =  serializers.CharField(max_length=200)
    Ec1_Dependance_Fiscally_strong_rating = serializers.IntegerField()
    Ec1_Dependance_Forex_loss =  serializers.CharField(max_length=200)
    Ec1_Dependance_Forex_loss_rating = serializers.IntegerField()
    Ec1_Dependance_inability_to_agree =  serializers.CharField(max_length=200)
    Ec1_Dependance_inability_to_agree_rating = serializers.IntegerField()
    Ec1_Dependance_user_fees =  serializers.CharField(max_length=200)
    Ec1_Dependance_user_fees_rating = serializers.IntegerField()
    Ec1_Dependance_budgetary_focus =  serializers.CharField(max_length=200)
    Ec1_Dependance_budgetary_focus_rating = serializers.IntegerField()
    Ec1_Dependance_fluctuation_of_exchange =  serializers.CharField(max_length=200)
    Ec1_Dependance_fluctuation_of_exchange_rating = serializers.IntegerField()
    Ec1_Dependance_Economic_vulnerability =  serializers.CharField(max_length=200)
    Ec1_Dependance_Economic_vulnerability_rating = serializers.IntegerField()

    #  Fiscally strong states emasculating economically weak


    Ec2_Fiscally_strong_Forex_loss =  serializers.CharField(max_length=200)
    Ec2_Fiscally_strong_Forex_loss_rating = serializers.IntegerField()
    Ec2_Fiscally_strong_inability_to_agree =  serializers.CharField(max_length=200)
    Ec2_Fiscally_strong_inability_to_agree_rating = serializers.IntegerField()
    Ec2_Fiscally_strong_user_fees =  serializers.CharField(max_length=200)
    Ec2_Fiscally_strong_user_fees_rating = serializers.IntegerField()
    Ec2_Fiscally_strong_budgetary_focus =  serializers.CharField(max_length=200)
    Ec2_Fiscally_strong_budgetary_focus_rating = serializers.IntegerField()
    Ec2_Fiscally_strong_fluctuation_of_exchange =  serializers.CharField(max_length=200)
    Ec2_Fiscally_strong_fluctuation_of_exchange_rating = serializers.IntegerField()
    Ec2_Fiscally_strong_Economic_vulnerability =  serializers.CharField(max_length=200)
    Ec2_Fiscally_strong_Economic_vulnerability_rating = serializers.IntegerField()

    #  Forex loss through import of project inputs/labour


    Ec3_Forex_loss_inability_to_agree =  serializers.CharField(max_length=200)
    Ec3_Forex_loss_inability_to_agree_rating = serializers.IntegerField()
    Ec3_Forex_loss_user_fees =  serializers.CharField(max_length=200)
    Ec3_Forex_loss_user_fees_rating = serializers.IntegerField()
    Ec3_Forex_loss_budgetary_focus =  serializers.CharField(max_length=200)
    Ec3_Forex_loss_budgetary_focus_rating = serializers.IntegerField()
    Ec3_Forex_loss_fluctuation_of_exchange =  serializers.CharField(max_length=200)
    Ec3_Forex_loss_fluctuation_of_exchange_rating = serializers.IntegerField()
    Ec3_Forex_loss_Economic_vulnerability =  serializers.CharField(max_length=200)
    Ec3_Forex_loss_Economic_vulnerability_rating = serializers.IntegerField()

    #  inability to agree on benefit/cost sharing related to common facility


    Ec4_inability_to_agree_user_fees =  serializers.CharField(max_length=200)
    Ec4_inability_to_agree_user_fees_rating = serializers.IntegerField()
    Ec4_inability_to_agree_budgetary_focus =  serializers.CharField(max_length=200)
    Ec4_inability_to_agree_budgetary_focus_rating = serializers.IntegerField()
    Ec4_inability_to_agree_fluctuation_of_exchange =  serializers.CharField(max_length=200)
    Ec4_inability_to_agree_fluctuation_of_exchange_rating = serializers.IntegerField()
    Ec4_inability_to_agree_Economic_vulnerability =  serializers.CharField(max_length=200)
    Ec4_inability_to_agree_Economic_vulnerability_rating = serializers.IntegerField()

    #  user-fees to limit access if community/users if unable/unwilling to pay



    Ec5_user_fees_budgetary_focus =  serializers.CharField(max_length=200)
    Ec5_user_fees_budgetary_focus_rating = serializers.IntegerField()
    Ec5_user_fees_fluctuation_of_exchange =  serializers.CharField(max_length=200)
    Ec5_user_fees_fluctuation_of_exchange_rating = serializers.IntegerField()
    Ec5_user_fees_Economic_vulnerability =  serializers.CharField(max_length=200)
    Ec5_user_fees_Economic_vulnerability_rating = serializers.IntegerField()


    #  budgetary focus inclined to expansion and new roads than maintainance, 


    Ec6_budgetary_focus_fluctuation_of_exchange =  serializers.CharField(max_length=200)
    Ec6_budgetary_focus_fluctuation_of_exchange_rating = serializers.IntegerField()
    Ec6_budgetary_focus_Economic_vulnerability =  serializers.CharField(max_length=200)
    Ec6_budgetary_focus_Economic_vulnerability_rating = serializers.IntegerField()


    #  fluctuation of exchange rate and construction material prices


    Ec7_fluctuation_of_exchange_Economic_vulnerability =  serializers.CharField(max_length=200)
    Ec7_fluctuation_of_exchange_Economic_vulnerability_rating = serializers.IntegerField()

    
    
    # Page 6
    
    
    # Variation among states in highway classification by purpose & capacity
    
    Tc1_Variation_among_Telecommuting_technology =  serializers.CharField(max_length=200)
    Tc1_Variation_among_Telecommuting_technology_rating = serializers.IntegerField()
    Tc1_Variation_among_Evolving_technology =  serializers.CharField(max_length=200)
    Tc1_Variation_among_Evolving_technology_rating = serializers.IntegerField()
    Tc1_Variation_among_necesstiy_of_tunnels =  serializers.CharField(max_length=200)
    Tc1_Variation_among_necesstiy_of_tunnels_rating = serializers.IntegerField()
    Tc1_Variation_among_use_of_monopolistic =  serializers.CharField(max_length=200)
    Tc1_Variation_among_use_of_monopolistic_rating = serializers.IntegerField()
    Tc1_Variation_among_Favoring_politically_popular =  serializers.CharField(max_length=200)
    Tc1_Variation_among_Favoring_politically_popular_rating = serializers.IntegerField()
    Tc1_Variation_among_Delays_downtime =  serializers.CharField(max_length=200)
    Tc1_Variation_among_Delays_downtime_rating = serializers.IntegerField()
    Tc1_Variation_among_Equipment_parts =  serializers.CharField(max_length=200)
    Tc1_Variation_among_Equipment_parts_rating = serializers.IntegerField()
    Tc1_Variation_among_construction_preceding =  serializers.CharField(max_length=200)
    Tc1_Variation_among_construction_preceding_rating = serializers.IntegerField()


# Telecommuting technology making redundant human movement


    Tc2_Telecommuting_technology_Evolving_technology =  serializers.CharField(max_length=200)
    Tc2_Telecommuting_technology_Evolving_technology_rating = serializers.IntegerField()
    Tc2_Telecommuting_technology_necesstiy_of_tunnels =  serializers.CharField(max_length=200)
    Tc2_Telecommuting_technology_necesstiy_of_tunnels_rating = serializers.IntegerField()
    Tc2_Telecommuting_technology_use_of_monopolistic =  serializers.CharField(max_length=200)
    Tc2_Telecommuting_technology_use_of_monopolistic_rating = serializers.IntegerField()
    Tc2_Telecommuting_technology_Favoring_politically_popular =  serializers.CharField(max_length=200)
    Tc2_Telecommuting_technology_Favoring_politically_popular_rating = serializers.IntegerField()
    Tc2_Telecommuting_technology_Delays_downtime =  serializers.CharField(max_length=200)
    Tc2_Telecommuting_technology_Delays_downtime_rating = serializers.IntegerField()
    Tc2_Telecommuting_technology_Equipment_parts =  serializers.CharField(max_length=200)
    Tc2_Telecommuting_technology_Equipment_parts_rating = serializers.IntegerField()
    Tc2_Telecommuting_technology_construction_preceding =  serializers.CharField(max_length=200)
    Tc2_Telecommuting_technology_construction_preceding_rating = serializers.IntegerField()


# Evolving technology rendering obsolete construction/ maintainance/operation equipment


    Tc3_Evolving_technology_necesstiy_of_tunnels =  serializers.CharField(max_length=200)
    Tc3_Evolving_technology_necesstiy_of_tunnels_rating = serializers.IntegerField()
    Tc3_Evolving_technology_use_of_monopolistic =  serializers.CharField(max_length=200)
    Tc3_Evolving_technology_use_of_monopolistic_rating = serializers.IntegerField()
    Tc3_Evolving_technology_Favoring_politically_popular =  serializers.CharField(max_length=200)
    Tc3_Evolving_technology_Favoring_politically_popular_rating = serializers.IntegerField()
    Tc3_Evolving_technology_Delays_downtime =  serializers.CharField(max_length=200)
    Tc3_Evolving_technology_Delays_downtime_rating = serializers.IntegerField()
    Tc3_Evolving_technology_Equipment_parts =  serializers.CharField(max_length=200)
    Tc3_Evolving_technology_Equipment_parts_rating = serializers.IntegerField()
    Tc3_Evolving_technology_construction_preceding =  serializers.CharField(max_length=200)
    Tc3_Evolving_technology_construction_preceding_rating = serializers.IntegerField()


# necesstiy of tunnels, overpasses, barriers in areas with flora/fauna/water-bodies/settlements 


    Tc4_necesstiy_of_tunnels_use_of_monopolistic =  serializers.CharField(max_length=200)
    Tc4_necesstiy_of_tunnels_use_of_monopolistic_rating = serializers.IntegerField()
    Tc4_necesstiy_of_tunnels_Favoring_politically_popular =  serializers.CharField(max_length=200)
    Tc4_necesstiy_of_tunnels_Favoring_politically_popular_rating = serializers.IntegerField()
    Tc4_necesstiy_of_tunnels_Delays_downtime =  serializers.CharField(max_length=200)
    Tc4_necesstiy_of_tunnels_Delays_downtime_rating = serializers.IntegerField()
    Tc4_necesstiy_of_tunnels_Equipment_parts =  serializers.CharField(max_length=200)
    Tc4_necesstiy_of_tunnels_Equipment_parts_rating = serializers.IntegerField()
    Tc4_necesstiy_of_tunnels_construction_preceding =  serializers.CharField(max_length=200)
    Tc4_necesstiy_of_tunnels_construction_preceding_rating = serializers.IntegerField()


# use of monopolistic foreign contractor limiting technology transfer to local firms/citizens 



    Tc5_use_of_monopolistic_Favoring_politically_popular =  serializers.CharField(max_length=200)
    Tc5_use_of_monopolistic_Favoring_politically_popular_rating = serializers.IntegerField()
    Tc5_use_of_monopolistic_Delays_downtime =  serializers.CharField(max_length=200)
    Tc5_use_of_monopolistic_Delays_downtime_rating = serializers.IntegerField()
    Tc5_use_of_monopolistic_Equipment_parts =  serializers.CharField(max_length=200)
    Tc5_use_of_monopolistic_Equipment_parts_rating = serializers.IntegerField()
    Tc5_use_of_monopolistic_construction_preceding =  serializers.CharField(max_length=200)
    Tc5_use_of_monopolistic_construction_preceding_rating = serializers.IntegerField()


# Favoring politically-popular but inefficient labor intensive technology


    Tc6_Favoring_politically_popular_Delays_downtime =  serializers.CharField(max_length=200)
    Tc6_Favoring_politically_popular_Delays_downtime_rating = serializers.IntegerField()
    Tc6_Favoring_politically_popular_Equipment_parts =  serializers.CharField(max_length=200)
    Tc6_Favoring_politically_popular_Equipment_parts_rating = serializers.IntegerField()
    Tc6_Favoring_politically_popular_construction_preceding =  serializers.CharField(max_length=200)
    Tc6_Favoring_politically_popular_construction_preceding_rating = serializers.IntegerField()


# Delays/downtime due to low-utilization of efficient border clearance technology


    Tc7_Delays_downtime_Equipment_parts =  serializers.CharField(max_length=200)
    Tc7_Delays_downtime_Equipment_parts_rating = serializers.IntegerField()
    Tc7_Delays_downtime_construction_preceding =  serializers.CharField(max_length=200)
    Tc7_Delays_downtime_construction_preceding_rating = serializers.IntegerField()


# Equipment/parts supply disruption by pandemics and local unavailability of equipment dealers

    Tc8_Equipment_parts_construction_preceding =  serializers.CharField(max_length=200)
    Tc8_Equipment_parts_construction_preceding_rating = serializers.IntegerField()
    
    
    
    # page 7
    
    # Disrupted social interaction by settlement split/displacement


    So1_Disrupted_social_Benefits_unlikely=  serializers.CharField(max_length=200)
    So1_Disrupted_social_Benefits_unlikely_rating = serializers.IntegerField()
    So1_Disrupted_social_loss_of_work=  serializers.CharField(max_length=200)
    So1_Disrupted_social_loss_of_work_rating = serializers.IntegerField()
    So1_Disrupted_social_Hard_to_identify=  serializers.CharField(max_length=200)
    So1_Disrupted_social_Hard_to_identify_rating = serializers.IntegerField()
    So1_Disrupted_social_High_speed=  serializers.CharField(max_length=200)
    So1_Disrupted_social_High_speed_rating = serializers.IntegerField()
    So1_Disrupted_social_Crowding=  serializers.CharField(max_length=200)
    So1_Disrupted_social_Crowding_rating = serializers.IntegerField()
    So1_Disrupted_social_low_per_capita=  serializers.CharField(max_length=200)
    So1_Disrupted_social_low_per_capita_rating = serializers.IntegerField()
    So1_Disrupted_social_Food_security=  serializers.CharField(max_length=200)
    So1_Disrupted_social_Food_security_rating = serializers.IntegerField()
    So1_Disrupted_social_Community_resistance=  serializers.CharField(max_length=200)
    So1_Disrupted_social_Community_resistance_rating = serializers.IntegerField()


# Benefits unlikely to trickle to local communities


    So2_Benefits_unlikely_loss_of_work=  serializers.CharField(max_length=200)
    So2_Benefits_unlikely_loss_of_work_rating = serializers.IntegerField()
    So2_Benefits_unlikely_Hard_to_identify=  serializers.CharField(max_length=200)
    So2_Benefits_unlikely_Hard_to_identify_rating = serializers.IntegerField()
    So2_Benefits_unlikely_High_speed=  serializers.CharField(max_length=200)
    So2_Benefits_unlikely_High_speed_rating = serializers.IntegerField()
    So2_Benefits_unlikely_Crowding=  serializers.CharField(max_length=200)
    So2_Benefits_unlikely_Crowding_rating = serializers.IntegerField()
    So2_Benefits_unlikely_low_per_capita=  serializers.CharField(max_length=200)
    So2_Benefits_unlikely_low_per_capita_rating = serializers.IntegerField()
    So2_Benefits_unlikely_Food_security=  serializers.CharField(max_length=200)
    So2_Benefits_unlikely_Food_security_rating = serializers.IntegerField()
    So2_Benefits_unlikely_Community_resistance=  serializers.CharField(max_length=200)
    So2_Benefits_unlikely_Community_resistance_rating = serializers.IntegerField()


# loss of work/opportunity to immigrants due to inadequate skill and language barrier



    So3_loss_of_work_Hard_to_identify=  serializers.CharField(max_length=200)
    So3_loss_of_work_Hard_to_identify_rating = serializers.IntegerField()
    So3_loss_of_work_High_speed=  serializers.CharField(max_length=200)
    So3_loss_of_work_High_speed_rating = serializers.IntegerField()
    So3_loss_of_work_Crowding=  serializers.CharField(max_length=200)
    So3_loss_of_work_Crowding_rating = serializers.IntegerField()
    So3_loss_of_work_low_per_capita=  serializers.CharField(max_length=200)
    So3_loss_of_work_low_per_capita_rating = serializers.IntegerField()
    So3_loss_of_work_Food_security=  serializers.CharField(max_length=200)
    So3_loss_of_work_Food_security_rating = serializers.IntegerField()
    So3_loss_of_work_Community_resistance=  serializers.CharField(max_length=200)
    So3_loss_of_work_Community_resistance_rating = serializers.IntegerField()


# Hard to identify Project Affected Persons due to conflict/environmental/economic migration



    So4_Hard_to_identify_High_speed=  serializers.CharField(max_length=200)
    So4_Hard_to_identify_High_speed_rating = serializers.IntegerField()
    So4_Hard_to_identify_Crowding=  serializers.CharField(max_length=200)
    So4_Hard_to_identify_Crowding_rating = serializers.IntegerField()
    So4_Hard_to_identify_low_per_capita=  serializers.CharField(max_length=200)
    So4_Hard_to_identify_low_per_capita_rating = serializers.IntegerField()
    So4_Hard_to_identify_Food_security=  serializers.CharField(max_length=200)
    So4_Hard_to_identify_Food_security_rating = serializers.IntegerField()
    So4_Hard_to_identify_Community_resistance=  serializers.CharField(max_length=200)
    So4_Hard_to_identify_Community_resistance_rating = serializers.IntegerField()

# High-speed traffic and dangerous goods carriage threaten human safety/livelihood activities


    So5_High_speed_Crowding=  serializers.CharField(max_length=200)
    So5_High_speed_Crowding_rating = serializers.IntegerField()
    So5_High_speed_low_per_capita=  serializers.CharField(max_length=200)
    So5_High_speed_low_per_capita_rating = serializers.IntegerField()
    So5_High_speed_Food_security=  serializers.CharField(max_length=200)
    So5_High_speed_Food_security_rating = serializers.IntegerField()
    So5_High_speed_Community_resistance=  serializers.CharField(max_length=200)
    So5_High_speed_Community_resistance_rating = serializers.IntegerField()

# Crowding out local population due to increased cost of basic goods/services

    So6_Crowding_low_per_capita=  serializers.CharField(max_length=200)
    So6_Crowding_low_per_capita_rating = serializers.IntegerField()
    So6_Crowding_Food_security=  serializers.CharField(max_length=200)
    So6_Crowding_Food_security_rating = serializers.IntegerField()
    So6_Crowding_Community_resistance=  serializers.CharField(max_length=200)
    So6_Crowding_Community_resistance_rating = serializers.IntegerField()

# low per-capita income levels limits revenue mobilization from taxation  


    So7_low_per_capita_Food_security=  serializers.CharField(max_length=200)
    So7_low_per_capita_Food_security_rating = serializers.IntegerField()
    So7_low_per_capita_Community_resistance=  serializers.CharField(max_length=200)
    So7_low_per_capita_Community_resistance_rating = serializers.IntegerField()


# Food security threat by farmers switch to non-farming activity


    So8_Food_security_Community_resistance=  serializers.CharField(max_length=200)
    So8_Food_security_Community_resistance_rating = serializers.IntegerField()
    
    
    # page 8
    
    
    # Extreme weather events (floods/hot-sun/humidity) shorten corridor lifespan

    En1_Extreme_weather_requirement_to_minimise=  serializers.CharField(max_length=200)
    En1_Extreme_weather_requirement_to_minimise_rating = serializers.IntegerField()
    En1_Extreme_weather_crossing_diverse=  serializers.CharField(max_length=200)
    En1_Extreme_weather_crossing_diverse_rating = serializers.IntegerField()
    En1_Extreme_weather_enhanced_access=  serializers.CharField(max_length=200)
    En1_Extreme_weather_enhanced_access_rating = serializers.IntegerField()
    En1_Extreme_weather_Disasters_due=  serializers.CharField(max_length=200)
    En1_Extreme_weather_Disasters_due_rating = serializers.IntegerField()
    En1_Extreme_weather_Ecosystem_resources=  serializers.CharField(max_length=200)
    En1_Extreme_weather_Ecosystem_resources_rating = serializers.IntegerField()
    En1_Extreme_weather_Human_induced=  serializers.CharField(max_length=200)
    En1_Extreme_weather_Human_induced_rating = serializers.IntegerField()
    En1_Extreme_weather_Climate_change=  serializers.CharField(max_length=200)
    En1_Extreme_weather_Climate_change_rating = serializers.IntegerField()
    En1_Extreme_weather_requirement_to_safeguard=  serializers.CharField(max_length=200)
    En1_Extreme_weather_requirement_to_safeguard_rating = serializers.IntegerField()

# requirement to minimise alteration of hydrological patterns/flora/fauna/migratory corridors


    En2_requirement_to_minimise_crossing_diverse=  serializers.CharField(max_length=200)
    En2_requirement_to_minimise_crossing_diverse_rating = serializers.IntegerField()
    En2_requirement_to_minimise_enhanced_access=  serializers.CharField(max_length=200)
    En2_requirement_to_minimise_enhanced_access_rating = serializers.IntegerField()
    En2_requirement_to_minimise_Disasters_due=  serializers.CharField(max_length=200)
    En2_requirement_to_minimise_Disasters_due_rating = serializers.IntegerField()
    En2_requirement_to_minimise_Ecosystem_resources=  serializers.CharField(max_length=200)
    En2_requirement_to_minimise_Ecosystem_resources_rating = serializers.IntegerField()
    En2_requirement_to_minimise_Human_induced=  serializers.CharField(max_length=200)
    En2_requirement_to_minimise_Human_induced_rating = serializers.IntegerField()
    En2_requirement_to_minimise_Climate_change=  serializers.CharField(max_length=200)
    En2_requirement_to_minimise_Climate_change_rating = serializers.IntegerField()
    En2_requirement_to_minimise_requirement_to_safeguard=  serializers.CharField(max_length=200)
    En2_requirement_to_minimise_requirement_to_safeguard_rating = serializers.IntegerField()

# crossing diverse climate zones impacts design complexity and maintainance cost


    En3_crossing_diverse_enhanced_access=  serializers.CharField(max_length=200)
    En3_crossing_diverse_enhanced_access_rating = serializers.IntegerField()
    En3_crossing_diverse_Disasters_due=  serializers.CharField(max_length=200)
    En3_crossing_diverse_Disasters_due_rating = serializers.IntegerField()
    En3_crossing_diverse_Ecosystem_resources=  serializers.CharField(max_length=200)
    En3_crossing_diverse_Ecosystem_resources_rating = serializers.IntegerField()
    En3_crossing_diverse_Human_induced=  serializers.CharField(max_length=200)
    En3_crossing_diverse_Human_induced_rating = serializers.IntegerField()
    En3_crossing_diverse_Climate_change=  serializers.CharField(max_length=200)
    En3_crossing_diverse_Climate_change_rating = serializers.IntegerField()
    En3_crossing_diverse_requirement_to_safeguard=  serializers.CharField(max_length=200)
    En3_crossing_diverse_requirement_to_safeguard_rating = serializers.IntegerField()

# enhanced access to aggravate poaching, illegal lumbering and mining


    En4_enhanced_access_Disasters_due=  serializers.CharField(max_length=200)
    En4_enhanced_access_Disasters_due_rating = serializers.IntegerField()
    En4_enhanced_access_Ecosystem_resources=  serializers.CharField(max_length=200)
    En4_enhanced_access_Ecosystem_resources_rating = serializers.IntegerField()
    En4_enhanced_access_Human_induced=  serializers.CharField(max_length=200)
    En4_enhanced_access_Human_induced_rating = serializers.IntegerField()
    En4_enhanced_access_Climate_change=  serializers.CharField(max_length=200)
    En4_enhanced_access_Climate_change_rating = serializers.IntegerField()
    En4_enhanced_access_requirement_to_safeguard=  serializers.CharField(max_length=200)
    En4_enhanced_access_requirement_to_safeguard_rating = serializers.IntegerField()

# Disasters due to weather related events


    En5_Disasters_due_Ecosystem_resources=  serializers.CharField(max_length=200)
    En5_Disasters_due_Ecosystem_resources_rating = serializers.IntegerField()
    En5_Disasters_due_Human_induced=  serializers.CharField(max_length=200)
    En5_Disasters_due_Human_induced_rating = serializers.IntegerField()
    En5_Disasters_due_Climate_change=  serializers.CharField(max_length=200)
    En5_Disasters_due_Climate_change_rating = serializers.IntegerField()
    En5_Disasters_due_requirement_to_safeguard=  serializers.CharField(max_length=200)
    En5_Disasters_due_requirement_to_safeguard_rating = serializers.IntegerField()


# Ecosystem resources degradadation by settlement densification/immigrants influx


    En6_Ecosystem_resources_Human_induced=  serializers.CharField(max_length=200)
    En6_Ecosystem_resources_Human_induced_rating = serializers.IntegerField()
    En6_Ecosystem_resources_Climate_change=  serializers.CharField(max_length=200)
    En6_Ecosystem_resources_Climate_change_rating = serializers.IntegerField()
    En6_Ecosystem_resources_requirement_to_safeguard=  serializers.CharField(max_length=200)
    En6_Ecosystem_resources_requirement_to_safeguard_rating = serializers.IntegerField()


# Human induced landslide, soil erosion and water-body sedimentation

    En7_Human_induced_Climate_change=  serializers.CharField(max_length=200)
    En7_Human_induced_Climate_change_rating = serializers.IntegerField()
    En7_Human_induced_requirement_to_safeguard=  serializers.CharField(max_length=200)
    En7_Human_induced_requirement_to_safeguard_rating = serializers.IntegerField()


# Climate change induced variation of average local weather patterns

    En8_Climate_change_requirement_to_safeguard=  serializers.CharField(max_length=200)
    En8_Climate_change_requirement_to_safeguard_rating = serializers.IntegerField()
    
    # Political Factor
class PoliticalFormSubmitSerializer(serializers.Serializer):
       
    p1_Insecurity_instability_Border_Check = serializers.CharField(max_length=200)
    p1_Insecurity_instability_Border_Check_rating = serializers.IntegerField()
    p1_Insecurity_instability_Policy_nonalignment = serializers.CharField(max_length=200)
    p1_Insecurity_instability_Policy_nonalignment_rating = serializers.IntegerField()
    p1_Insecurity_instability_weak_institutions = serializers.CharField(max_length=200)
    p1_Insecurity_instability_weak_institutions_rating = serializers.IntegerField()
    p1_Insecurity_instability_disimilar_regulation = serializers.CharField(max_length=200)
    p1_Insecurity_instability_disimilar_regulation_rating = serializers.IntegerField()
    p1_Insecurity_instability_inability_to_observe = serializers.CharField(max_length=200)
    p1_Insecurity_instability_inability_to_observe_rating = serializers.IntegerField()
    p1_Insecurity_instability_corruption_impact = serializers.CharField(max_length=200)
    p1_Insecurity_instability_corruption_impact_rating = serializers.IntegerField()
    p1_Insecurity_instability_realignment_design = serializers.CharField(max_length=200)
    p1_Insecurity_instability_realignment_design_rating = serializers.IntegerField()
    p1_Insecurity_instability_commitment_fluctuation = serializers.CharField(max_length=200)
    p1_Insecurity_instability_commitment_fluctuation_rating = serializers.IntegerField()

        
   
    p2_Border_Check_Policy_nonalignment = serializers.CharField(max_length=200)
    p2_Border_Check_Policy_nonalignment_rating = serializers.IntegerField()
    p2_Border_Check_weak_institutions = serializers.CharField(max_length=200)
    p2_Border_Check_weak_institutions_rating = serializers.IntegerField()
    p2_Border_Check_disimilar_regulation = serializers.CharField(max_length=200)
    p2_Border_Check_disimilar_regulation_rating = serializers.IntegerField()
    p2_Border_Check_inability_to_observe = serializers.CharField(max_length=200)
    p2_Border_Check_inability_to_observe_rating = serializers.IntegerField()
    p2_Border_Check_corruption_impact = serializers.CharField(max_length=200)
    p2_Border_Check_corruption_impact_rating = serializers.IntegerField()
    p2_Border_Check_realignment_design = serializers.CharField(max_length=200)
    p2_Border_Check_realignment_design_rating = serializers.IntegerField()
    p2_Border_Check_commitment_fluctuation = serializers.CharField(max_length=200)
    p2_Border_Check_commitment_fluctuation_rating = serializers.IntegerField()
    
    
    
    p3_Policy_nonalignment_weak_institutions = serializers.CharField(max_length=200)
    p3_Policy_nonalignment_weak_institutions_rating = serializers.IntegerField()
    p3_Policy_nonalignment_disimilar_regulation = serializers.CharField(max_length=200)
    p3_Policy_nonalignment_disimilar_regulation_rating = serializers.IntegerField()
    p3_Policy_nonalignment_inability_to_observe = serializers.CharField(max_length=200)
    p3_Policy_nonalignment_inability_to_observe_rating = serializers.IntegerField()
    p3_Policy_nonalignment_corruption_impact = serializers.CharField(max_length=200)
    p3_Policy_nonalignment_corruption_impact_rating = serializers.IntegerField()
    p3_Policy_nonalignment_realignment_design = serializers.CharField(max_length=200)
    p3_Policy_nonalignment_realignment_design_rating = serializers.IntegerField()
    p3_Policy_nonalignment_commitment_fluctuation = serializers.CharField(max_length=200)
    p3_Policy_nonalignment_commitment_fluctuation_rating = serializers.IntegerField()
    
    
    
    p4_weak_institutions_disimilar_regulation = serializers.CharField(max_length=200)
    p4_weak_institutions_disimilar_regulation_rating = serializers.IntegerField()
    p4_weak_institutions_inability_to_observe = serializers.CharField(max_length=200)
    p4_weak_institutions_inability_to_observe_rating = serializers.IntegerField()
    p4_weak_institutions_corruption_impact = serializers.CharField(max_length=200)
    p4_weak_institutions_corruption_impact_rating = serializers.IntegerField()
    p4_weak_institutions_realignment_design = serializers.CharField(max_length=200)
    p4_weak_institutions_realignment_design_rating = serializers.IntegerField()
    p4_weak_institutions_commitment_fluctuation = serializers.CharField(max_length=200)
    p4_weak_institutions_commitment_fluctuation_rating = serializers.IntegerField()
    
    
    p5_disimilar_regulation_inability_to_observe = serializers.CharField(max_length=200)
    p5_disimilar_regulation_inability_to_observe_rating = serializers.IntegerField()
    p5_disimilar_regulation_corruption_impact = serializers.CharField(max_length=200)
    p5_disimilar_regulation_corruption_impact_rating = serializers.IntegerField()
    p5_disimilar_regulation_realignment_design = serializers.CharField(max_length=200)
    p5_disimilar_regulation_realignment_design_rating = serializers.IntegerField()
    p5_disimilar_regulation_commitment_fluctuation = serializers.CharField(max_length=200)
    p5_disimilar_regulation_commitment_fluctuation_rating = serializers.IntegerField()
    
    
    p6_inability_to_observe_corruption_impact = serializers.CharField(max_length=200)
    p6_inability_to_observe_corruption_impact_rating = serializers.IntegerField()
    p6_inability_to_observe_realignment_design = serializers.CharField(max_length=200)
    p6_inability_to_observe_realignment_design_rating = serializers.IntegerField()
    p6_inability_to_observe_commitment_fluctuation = serializers.CharField(max_length=200)
    p6_inability_to_observe_commitment_fluctuation_rating = serializers.IntegerField()
    
    
    p7_corruption_impact_realignment_design = serializers.CharField(max_length=200)
    p7_corruption_impact_realignment_design_rating = serializers.IntegerField()
    p7_corruption_impact_commitment_fluctuation = serializers.CharField(max_length=200)
    p7_corruption_impact_commitment_fluctuation_rating = serializers.IntegerField()
    
    
    p8_realignment_design_commitment_fluctuation = serializers.CharField(max_length=200)
    p8_realignment_design_commitment_fluctuation_rating = serializers.IntegerField()