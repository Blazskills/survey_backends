import pprint
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from surveyapp.models import EconomicFactorDataA, EnvironmentalFactorDataA, GeographicFactorDataA, IntroSurveyDataA, LandUseFactorDataA, PoliticalFactorDataA, SocialFactorDataA, SurveyUser, TechnologicalFactorDataA
from django.db import transaction
from surveyapp.serializer import PoliticalFormSubmitSerializer, SurveyFormSubmitSerializer, SurveyUserListSerializer
# Create your views here.


class TestIndex(APIView):

    def get(self, request):
        data = {'status': 'It okay', 'code': 200}
        return Response(data)


class SurveyCorrespondentView(APIView):

    def post(self, request):
        # print(tenant)
        serializer = SurveyUserListSerializer(data=request.data)
        try:

            if serializer.is_valid():
                data = serializer.validated_data
                correspondent_created = SurveyUser(

                    full_name=data.get('full_name'),
                    email=data.get('email'),
                    country=data.get('country'),
                    occupation=data.get('occupation'),
                    education_level=data.get('education_level'),
                )
                correspondent_created.save()
                response = {
                    "message": "Correspondent register sucessfully",
                    "data": serializer.data
                }
                return Response(data=response, status=status.HTTP_200_OK)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response = {
                "status": 400,
                "message": str(e)
            }
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)


class SurveyFromsView(APIView):

    def post(self, request):
        pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(request.data)
        # print('\n')
        # print('\n')
        # form_data = request.data.get('formData')
        # form_data = request.data.get('polFormData')
        # pp.pprint(form_data)
        # pp.pprint(form_data)

        # # pp.pprint(form_data)
        # # pp.pprint(form_data)
        # # print('\n')
        # # print('\n')

        # print(form_data.get('useremail'))
        # # print(form_data.get('username'))
        # print(form_data.get('p1_Insecurity_instability_Border_Check'))
        # print(form_data.get('L1_Speculative_land_Likely_split'))
        # print(form_data.get('username'))
        # print(form_data.get('pol_landuse'))
        # print(form_data.get('pol_landuse_rating'))
        # print('\n')
        # print('\n')

        # serializer = SurveyFormSubmitSerializer(data=request.data.get('formData'))

        form_data = request.data.get('formData')
        pol_form_data = request.data.get('polFormData')
        landuse_form_data = request.data.get('landuseFormData')
        geographic_form_data = request.data.get('geographicFormData')
        economic_form_data = request.data.get('economicFormData')
        technology_form_data = request.data.get('technologicalFormData')
        social_form_data = request.data.get('socialFormData')
        environmental_form_data = request.data.get('environmentalFormData')
        # pp.pprint(social_form_data)

        serializer = SurveyFormSubmitSerializer(
            data={**form_data, **pol_form_data, **landuse_form_data, **geographic_form_data, **economic_form_data, **technology_form_data, **social_form_data, **environmental_form_data})

        try:

            if serializer.is_valid():
                data = serializer.validated_data
                survey_userExist = SurveyUser.objects.get(
                    email=data.get('useremail'))
                survey_user = SurveyUser.objects.get(
                    email=data.get('useremail'))
                # print(survey_user)
                if IntroSurveyDataA.objects.filter(Correspondent_Email__email=survey_userExist).exists():
                    response = {
                        "message": (f"You have filled this survery before. Thank you {data.get('username')} for the support.")
                    }
                    return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

            with transaction.atomic():
                surveydata_created = IntroSurveyDataA(
                    Correspondent_Email=survey_user,
                    fullname=data.get('username'),
                    pol_landuse=data.get('pol_landuse'),
                    pol_landuse_rating=data.get('pol_landuse_rating'),
                    pol_Geographic=data.get('pol_Geographic'),
                    pol_Geographic_rating=data.get('pol_Geographic_rating'),
                    pol_Economic=data.get('pol_Economic'),
                    pol_Economic_rating=data.get('pol_Economic_rating'),
                    pol_Technological=data.get('pol_Technological'),
                    pol_Technological_rating=data.get(
                        'pol_Technological_rating'),
                    pol_Social=data.get('pol_Social'),
                    pol_Social_rating=data.get('pol_Social_rating'),
                    pol_Environmental=data.get('pol_Environmental'),
                    pol_Environmental_rating=data.get(
                        'pol_Environmental_rating'),
                    landuse_geographic=data.get('landuse_geographic'),
                    landuse_geograhpic_rating=data.get(
                        'landuse_geograhpic_rating'),
                    landuse_Economic=data.get('landuse_Economic'),
                    landuse_Economic_rating=data.get(
                        'landuse_Economic_rating'),
                    landuse_Technological=data.get('landuse_Technological'),
                    landuse_Technological_rating=data.get(
                        'landuse_Technological_rating'),
                    landuse_Social=data.get('landuse_Social'),
                    landuse_Social_rating=data.get('landuse_Social_rating'),
                    landuse_Environmental=data.get('landuse_Environmental'),
                    landuse_Environmental_rating=data.get(
                        'landuse_Environmental_rating'),
                    geographic_Economic=data.get('geographic_Economic'),
                    geographic_Economic_rating=data.get(
                        'geographic_Economic_rating'),
                    geographic_Technological=data.get(
                        'geographic_Technological'),
                    geographic_Technological_rating=data.get(
                        'geographic_Technological_rating'),
                    geographic_Social=data.get('geographic_Social'),
                    geographic_Social_rating=data.get(
                        'geographic_Social_rating'),
                    geographic_Environmental=data.get(
                        'geographic_Environmental'),
                    geographic_Environmental_rating=data.get(
                        'geographic_Environmental_rating'),
                    economic_Technological=data.get('economic_Technological'),
                    economic_Technological_rating=data.get(
                        'economic_Technological_rating'),
                    economic_Social=data.get('economic_Social'),
                    economic_Social_rating=data.get('economic_Social_rating'),
                    economic_Environmental=data.get('economic_Environmental'),
                    economic_Environmental_rating=data.get(
                        'economic_Environmental_rating'),
                    technological_Social=data.get('technological_Social'),
                    technological_Social_rating=data.get(
                        'technological_Social_rating'),
                    technological_Environmental=data.get(
                        'technological_Environmental'),
                    technological_Environmental_rating=data.get(
                        'technological_Environmental_rating'),
                    social_Environmental=data.get('social_Environmental'),
                    social_Environmental_rating=data.get(
                        'social_Environmental_rating'),

                )
                surveydata_created.save()

                politicaldata_created = PoliticalFactorDataA(
                    Correspondent_Email=survey_user,
                    fullname=data.get('username'),
                    p1_Insecurity_instability_Border_Check=data.get(
                        'p1_Insecurity_instability_Border_Check'),
                    p1_Insecurity_instability_Border_Check_rating=data.get(
                        'p1_Insecurity_instability_Border_Check_rating'),
                    p1_Insecurity_instability_Policy_nonalignment=data.get(
                        'p1_Insecurity_instability_Policy_nonalignment'),
                    p1_Insecurity_instability_Policy_nonalignment_rating=data.get(
                        'p1_Insecurity_instability_Policy_nonalignment_rating'),
                    p1_Insecurity_instability_weak_institutions=data.get(
                        'p1_Insecurity_instability_weak_institutions'),
                    p1_Insecurity_instability_weak_institutions_rating=data.get(
                        'p1_Insecurity_instability_weak_institutions_rating'),
                    p1_Insecurity_instability_disimilar_regulation=data.get(
                        'p1_Insecurity_instability_disimilar_regulation'),
                    p1_Insecurity_instability_disimilar_regulation_rating=data.get(
                        'p1_Insecurity_instability_disimilar_regulation_rating'),
                    p1_Insecurity_instability_inability_to_observe=data.get(
                        'p1_Insecurity_instability_inability_to_observe'),
                    p1_Insecurity_instability_inability_to_observe_rating=data.get(
                        'p1_Insecurity_instability_inability_to_observe_rating'),
                    p1_Insecurity_instability_corruption_impact=data.get(
                        'p1_Insecurity_instability_corruption_impact'),
                    p1_Insecurity_instability_corruption_impact_rating=data.get(
                        'p1_Insecurity_instability_corruption_impact_rating'),
                    p1_Insecurity_instability_realignment_design=data.get(
                        'p1_Insecurity_instability_realignment_design'),
                    p1_Insecurity_instability_realignment_design_rating=data.get(
                        'p1_Insecurity_instability_realignment_design_rating'),
                    p1_Insecurity_instability_commitment_fluctuation=data.get(
                        'p1_Insecurity_instability_commitment_fluctuation'),
                    p1_Insecurity_instability_commitment_fluctuation_rating=data.get(
                        'p1_Insecurity_instability_commitment_fluctuation_rating'),



                    p2_Border_Check_Policy_nonalignment=data.get(
                        'p2_Border_Check_Policy_nonalignment'),
                    p2_Border_Check_Policy_nonalignment_rating=data.get(
                        'p2_Border_Check_Policy_nonalignment_rating'),
                    p2_Border_Check_weak_institutions=data.get(
                        'p2_Border_Check_weak_institutions'),
                    p2_Border_Check_weak_institutions_rating=data.get(
                        'p2_Border_Check_weak_institutions_rating'),
                    p2_Border_Check_disimilar_regulation=data.get(
                        'p2_Border_Check_disimilar_regulation'),
                    p2_Border_Check_disimilar_regulation_rating=data.get(
                        'p2_Border_Check_disimilar_regulation_rating'),
                    p2_Border_Check_inability_to_observe=data.get(
                        'p2_Border_Check_inability_to_observe'),
                    p2_Border_Check_inability_to_observe_rating=data.get(
                        'p2_Border_Check_inability_to_observe_rating'),
                    p2_Border_Check_corruption_impact=data.get(
                        'p2_Border_Check_corruption_impact'),
                    p2_Border_Check_corruption_impact_rating=data.get(
                        'p2_Border_Check_corruption_impact_rating'),
                    p2_Border_Check_realignment_design=data.get(
                        'p2_Border_Check_realignment_design'),
                    p2_Border_Check_realignment_design_rating=data.get(
                        'p2_Border_Check_realignment_design_rating'),
                    p2_Border_Check_commitment_fluctuation=data.get(
                        'p2_Border_Check_commitment_fluctuation'),
                    p2_Border_Check_commitment_fluctuation_rating=data.get(
                        'p2_Border_Check_commitment_fluctuation_rating'),



                    p3_Policy_nonalignment_weak_institutions=data.get(
                        'p3_Policy_nonalignment_weak_institutions'),
                    p3_Policy_nonalignment_weak_institutions_rating=data.get(
                        'p3_Policy_nonalignment_weak_institutions_rating'),
                    p3_Policy_nonalignment_disimilar_regulation=data.get(
                        'p3_Policy_nonalignment_disimilar_regulation'),
                    p3_Policy_nonalignment_disimilar_regulation_rating=data.get(
                        'p3_Policy_nonalignment_disimilar_regulation_rating'),
                    p3_Policy_nonalignment_inability_to_observe=data.get(
                        'p3_Policy_nonalignment_inability_to_observe'),
                    p3_Policy_nonalignment_inability_to_observe_rating=data.get(
                        'p3_Policy_nonalignment_inability_to_observe_rating'),
                    p3_Policy_nonalignment_corruption_impact=data.get(
                        'p3_Policy_nonalignment_corruption_impact'),
                    p3_Policy_nonalignment_corruption_impact_rating=data.get(
                        'p3_Policy_nonalignment_corruption_impact_rating'),
                    p3_Policy_nonalignment_realignment_design=data.get(
                        'p3_Policy_nonalignment_realignment_design'),
                    p3_Policy_nonalignment_realignment_design_rating=data.get(
                        'p3_Policy_nonalignment_realignment_design_rating'),
                    p3_Policy_nonalignment_commitment_fluctuation=data.get(
                        'p3_Policy_nonalignment_commitment_fluctuation'),
                    p3_Policy_nonalignment_commitment_fluctuation_rating=data.get(
                        'p3_Policy_nonalignment_commitment_fluctuation_rating'),



                    p4_weak_institutions_disimilar_regulation=data.get(
                        'p4_weak_institutions_disimilar_regulation'),
                    p4_weak_institutions_disimilar_regulation_rating=data.get(
                        'p4_weak_institutions_disimilar_regulation_rating'),
                    p4_weak_institutions_inability_to_observe=data.get(
                        'p4_weak_institutions_inability_to_observe'),
                    p4_weak_institutions_inability_to_observe_rating=data.get(
                        'p4_weak_institutions_inability_to_observe_rating'),
                    p4_weak_institutions_corruption_impact=data.get(
                        'p4_weak_institutions_corruption_impact'),
                    p4_weak_institutions_corruption_impact_rating=data.get(
                        'p4_weak_institutions_corruption_impact_rating'),
                    p4_weak_institutions_realignment_design=data.get(
                        'p4_weak_institutions_realignment_design'),
                    p4_weak_institutions_realignment_design_rating=data.get(
                        'p4_weak_institutions_realignment_design_rating'),
                    p4_weak_institutions_commitment_fluctuation=data.get(
                        'p4_weak_institutions_commitment_fluctuation'),
                    p4_weak_institutions_commitment_fluctuation_rating=data.get(
                        'p4_weak_institutions_commitment_fluctuation_rating'),


                    p5_disimilar_regulation_inability_to_observe=data.get(
                        'p5_disimilar_regulation_inability_to_observe'),
                    p5_disimilar_regulation_inability_to_observe_rating=data.get(
                        'p5_disimilar_regulation_inability_to_observe_rating'),
                    p5_disimilar_regulation_corruption_impact=data.get(
                        'p5_disimilar_regulation_corruption_impact'),
                    p5_disimilar_regulation_corruption_impact_rating=data.get(
                        'p5_disimilar_regulation_corruption_impact_rating'),
                    p5_disimilar_regulation_realignment_design=data.get(
                        'p5_disimilar_regulation_realignment_design'),
                    p5_disimilar_regulation_realignment_design_rating=data.get(
                        'p5_disimilar_regulation_realignment_design_rating'),
                    p5_disimilar_regulation_commitment_fluctuation=data.get(
                        'p5_disimilar_regulation_commitment_fluctuation'),
                    p5_disimilar_regulation_commitment_fluctuation_rating=data.get(
                        'p5_disimilar_regulation_commitment_fluctuation_rating'),


                    p6_inability_to_observe_corruption_impact=data.get(
                        'p6_inability_to_observe_corruption_impact'),
                    p6_inability_to_observe_corruption_impact_rating=data.get(
                        'p6_inability_to_observe_corruption_impact_rating'),
                    p6_inability_to_observe_realignment_design=data.get(
                        'p6_inability_to_observe_realignment_design'),
                    p6_inability_to_observe_realignment_design_rating=data.get(
                        'p6_inability_to_observe_realignment_design_rating'),
                    p6_inability_to_observe_commitment_fluctuation=data.get(
                        'p6_inability_to_observe_commitment_fluctuation'),
                    p6_inability_to_observe_commitment_fluctuation_rating=data.get(
                        'p6_inability_to_observe_commitment_fluctuation_rating'),


                    p7_corruption_impact_realignment_design=data.get(
                        'p7_corruption_impact_realignment_design'),
                    p7_corruption_impact_realignment_design_rating=data.get(
                        'p7_corruption_impact_realignment_design_rating'),
                    p7_corruption_impact_commitment_fluctuation=data.get(
                        'p7_corruption_impact_commitment_fluctuation'),
                    p7_corruption_impact_commitment_fluctuation_rating=data.get(
                        'p7_corruption_impact_commitment_fluctuation_rating'),


                    p8_realignment_design_commitment_fluctuation=data.get(
                        'p8_realignment_design_commitment_fluctuation'),
                    p8_realignment_design_commitment_fluctuation_rating=data.get(
                        'p8_realignment_design_commitment_fluctuation_rating'),


                )
                politicaldata_created.save()

                landusedata_create = LandUseFactorDataA(

                    Correspondent_Email=survey_user,
                    fullname=data.get('username'),
                    L1_Speculative_land_Likely_split=data.get(
                        'L1_Speculative_land_Likely_split'),
                    L1_Speculative_land_Likely_split_rating=data.get(
                        'L1_Speculative_land_Likely_split_rating'),
                    L1_Speculative_land_Hard_to_determine=data.get(
                        'L1_Speculative_land_Hard_to_determine'),
                    L1_Speculative_land_Hard_to_determine_rating=data.get(
                        'L1_Speculative_land_Hard_to_determine_rating'),
                    L1_Speculative_land_Perception_project=data.get(
                        'L1_Speculative_land_Perception_project'),
                    L1_Speculative_land_Perception_project_rating=data.get(
                        'L1_Speculative_land_Perception_project_rating'),
                    L1_Speculative_land_Corridor_efficiency=data.get(
                        'L1_Speculative_land_Corridor_efficiency'),
                    L1_Speculative_land_Corridor_efficiency_rating=data.get(
                        'L1_Speculative_land_Corridor_efficiency_rating'),
                    L1_Speculative_land_Perception_Land=data.get(
                        'L1_Speculative_land_Perception_Land'),
                    L1_Speculative_land_Perception_Land_rating=data.get(
                        'L1_Speculative_land_Perception_Land_rating'),
                    L1_Speculative_land_limited_access=data.get(
                        'L1_Speculative_land_limited_access'),
                    L1_Speculative_land_limited_access_rating=data.get(
                        'L1_Speculative_land_limited_access_rating'),
                    L1_Speculative_land_communal_informal=data.get(
                        'L1_Speculative_land_communal_informal'),
                    L1_Speculative_land_communal_informal_rating=data.get(
                        'L1_Speculative_land_communal_informal_rating'),
                    L1_Speculative_land_weak_land=data.get(
                        'L1_Speculative_land_weak_land'),
                    L1_Speculative_land_weak_land_rating=data.get(
                        'L1_Speculative_land_weak_land_rating'),


                    L2_Likely_split_Hard_to_determine=data.get(
                        'L2_Likely_split_Hard_to_determine'),
                    L2_Likely_split_Hard_to_determine_rating=data.get(
                        'L2_Likely_split_Hard_to_determine_rating'),
                    L2_Likely_split_Perception_project=data.get(
                        'L2_Likely_split_Perception_project'),
                    L2_Likely_split_Perception_project_rating=data.get(
                        'L2_Likely_split_Perception_project_rating'),
                    L2_Likely_split_Corridor_efficiency=data.get(
                        'L2_Likely_split_Corridor_efficiency'),
                    L2_Likely_split_Corridor_efficiency_rating=data.get(
                        'L2_Likely_split_Corridor_efficiency_rating'),
                    L2_Likely_split_Perception_Land=data.get(
                        'L2_Likely_split_Perception_Land'),
                    L2_Likely_split_Perception_Land_rating=data.get(
                        'L2_Likely_split_Perception_Land_rating'),
                    L2_Likely_split_limited_access=data.get(
                        'L2_Likely_split_limited_access'),
                    L2_Likely_split_limited_access_rating=data.get(
                        'L2_Likely_split_limited_access_rating'),
                    L2_Likely_split_communal_informal=data.get(
                        'L2_Likely_split_communal_informal'),
                    L2_Likely_split_communal_informal_rating=data.get(
                        'L2_Likely_split_communal_informal_rating'),
                    L2_Likely_split_weak_land=data.get(
                        'L2_Likely_split_weak_land'),
                    L2_Likely_split_weak_land_rating=data.get(
                        'L2_Likely_split_weak_land_rating'),


                    L3_Hard_to_determine_Perception_project=data.get(
                        'L3_Hard_to_determine_Perception_project'),
                    L3_Hard_to_determine_Perception_project_rating=data.get(
                        'L3_Hard_to_determine_Perception_project_rating'),
                    L3_Hard_to_determine_Corridor_efficiency=data.get(
                        'L3_Hard_to_determine_Corridor_efficiency'),
                    L3_Hard_to_determine_Corridor_efficiency_rating=data.get(
                        'L3_Hard_to_determine_Corridor_efficiency_rating'),
                    L3_Hard_to_determine_Perception_Land=data.get(
                        'L3_Hard_to_determine_Perception_Land'),
                    L3_Hard_to_determine_Perception_Land_rating=data.get(
                        'L3_Hard_to_determine_Perception_Land_rating'),
                    L3_Hard_to_determine_limited_access=data.get(
                        'L3_Hard_to_determine_limited_access'),
                    L3_Hard_to_determine_limited_access_rating=data.get(
                        'L3_Hard_to_determine_limited_access_rating'),
                    L3_Hard_to_determine_communal_informal=data.get(
                        'L3_Hard_to_determine_communal_informal'),
                    L3_Hard_to_determine_communal_informal_rating=data.get(
                        'L3_Hard_to_determine_communal_informal_rating'),
                    L3_Hard_to_determine_weak_land=data.get(
                        'L3_Hard_to_determine_weak_land'),
                    L3_Hard_to_determine_weak_land_rating=data.get(
                        'L3_Hard_to_determine_weak_land_rating'),



                    L4_Perception_project_Corridor_efficiency=data.get(
                        'L4_Perception_project_Corridor_efficiency'),
                    L4_Perception_project_Corridor_efficiency_rating=data.get(
                        'L4_Perception_project_Corridor_efficiency_rating'),
                    L4_Perception_project_Perception_Land=data.get(
                        'L4_Perception_project_Perception_Land'),
                    L4_Perception_project_Perception_Land_rating=data.get(
                        'L4_Perception_project_Perception_Land_rating'),
                    L4_Perception_project_limited_access=data.get(
                        'L4_Perception_project_limited_access'),
                    L4_Perception_project_limited_access_rating=data.get(
                        'L4_Perception_project_limited_access_rating'),
                    L4_Perception_project_communal_informal=data.get(
                        'L4_Perception_project_communal_informal'),
                    L4_Perception_project_communal_informal_rating=data.get(
                        'L4_Perception_project_communal_informal_rating'),
                    L4_Perception_project_weak_land=data.get(
                        'L4_Perception_project_weak_land'),
                    L4_Perception_project_weak_land_rating=data.get(
                        'L4_Perception_project_weak_land_rating'),


                    L5_Corridor_efficiency_Perception_Land=data.get(
                        'L5_Corridor_efficiency_Perception_Land'),
                    L5_Corridor_efficiency_Perception_Land_rating=data.get(
                        'L5_Corridor_efficiency_Perception_Land_rating'),
                    L5_Corridor_efficiency_limited_access=data.get(
                        'L5_Corridor_efficiency_limited_access'),
                    L5_Corridor_efficiency_limited_access_rating=data.get(
                        'L5_Corridor_efficiency_limited_access_rating'),
                    L5_Corridor_efficiency_communal_informal=data.get(
                        'L5_Corridor_efficiency_communal_informal'),
                    L5_Corridor_efficiency_communal_informal_rating=data.get(
                        'L5_Corridor_efficiency_communal_informal_rating'),
                    L5_Corridor_efficiency_weak_land=data.get(
                        'L5_Corridor_efficiency_weak_land'),
                    L5_Corridor_efficiency_weak_land_rating=data.get(
                        'L5_Corridor_efficiency_weak_land_rating'),


                    L6_Perception_Land_limited_access=data.get(
                        'L6_Perception_Land_limited_access'),
                    L6_Perception_Land_limited_access_rating=data.get(
                        'L6_Perception_Land_limited_access_rating'),
                    L6_Perception_Land_communal_informal=data.get(
                        'L6_Perception_Land_communal_informal'),
                    L6_Perception_Land_communal_informal_rating=data.get(
                        'L6_Perception_Land_communal_informal_rating'),
                    L6_Perception_Land_weak_land=data.get(
                        'L6_Perception_Land_weak_land'),
                    L6_Perception_Land_weak_land_rating=data.get(
                        'L6_Perception_Land_weak_land_rating'),


                    L7_limited_access_communal_informal=data.get(
                        'L7_limited_access_communal_informal'),
                    L7_limited_access_communal_informal_rating=data.get(
                        'L7_limited_access_communal_informal_rating'),
                    L7_limited_access_weak_land=data.get(
                        'L7_limited_access_weak_land'),
                    L7_limited_access_weak_land_rating=data.get(
                        'L7_limited_access_weak_land_rating'),


                    L8_communal_informal_weak_land=data.get(
                        'L8_communal_informal_weak_land'),
                    L8_communal_informal_weak_land_rating=data.get(
                        'L8_communal_informal_weak_land_rating'),
                )
                landusedata_create.save()

                geographicdata_create = GeographicFactorDataA(

                    Correspondent_Email=survey_user,
                    fullname=data.get('username'),
                    G1_Lateritic_soft_Flood_prone_water=data.get(
                        'G1_Lateritic_soft_Flood_prone_water'),
                    G1_Lateritic_soft_Flood_prone_water_rating=data.get(
                        'G1_Lateritic_soft_Flood_prone_water_rating'),
                    G1_Lateritic_soft_Diverse_terrain=data.get(
                        'G1_Lateritic_soft_Diverse_terrain'),
                    G1_Lateritic_soft_Diverse_terrain_rating=data.get(
                        'G1_Lateritic_soft_Diverse_terrain_rating'),
                    G1_Lateritic_soft_Crossing_seismic=data.get(
                        'G1_Lateritic_soft_Crossing_seismic'),
                    G1_Lateritic_soft_Crossing_seismic_rating=data.get(
                        'G1_Lateritic_soft_Crossing_seismic_rating'),
                    G1_Lateritic_soft_Landslide_flooding=data.get(
                        'G1_Lateritic_soft_Landslide_flooding'),
                    G1_Lateritic_soft_Landslide_flooding_rating=data.get(
                        'G1_Lateritic_soft_Landslide_flooding_rating'),
                    G1_Lateritic_soft_Traversing_mining=data.get(
                        'G1_Lateritic_soft_Traversing_mining'),
                    G1_Lateritic_soft_Traversing_mining_rating=data.get(
                        'G1_Lateritic_soft_Traversing_mining_rating'),
                    G1_Lateritic_soft_Sparse_detached=data.get(
                        'G1_Lateritic_soft_Sparse_detached'),
                    G1_Lateritic_soft_Sparse_detached_rating=data.get(
                        'G1_Lateritic_soft_Sparse_detached_rating'),
                    G1_Lateritic_soft_undocumented_geological=data.get(
                        'G1_Lateritic_soft_undocumented_geological'),
                    G1_Lateritic_soft_undocumented_geological_rating=data.get(
                        'G1_Lateritic_soft_undocumented_geological_rating'),
                    G1_Lateritic_soft_Geopolitical_consideration=data.get(
                        'G1_Lateritic_soft_Geopolitical_consideration'),
                    G1_Lateritic_soft_Geopolitical_consideration_rating=data.get(
                        'G1_Lateritic_soft_Geopolitical_consideration_rating'),


                    # Flood-prone/water logged areas necessitating costly foundation design


                    G2_Flood_prone_water_Diverse_terrain=data.get(
                        'G2_Flood_prone_water_Diverse_terrain'),
                    G2_Flood_prone_water_Diverse_terrain_rating=data.get(
                        'G2_Flood_prone_water_Diverse_terrain_rating'),
                    G2_Flood_prone_water_Crossing_seismic=data.get(
                        'G2_Flood_prone_water_Crossing_seismic'),
                    G2_Flood_prone_water_Crossing_seismic_rating=data.get(
                        'G2_Flood_prone_water_Crossing_seismic_rating'),
                    G2_Flood_prone_water_Landslide_flooding=data.get(
                        'G2_Flood_prone_water_Landslide_flooding'),
                    G2_Flood_prone_water_Landslide_flooding_rating=data.get(
                        'G2_Flood_prone_water_Landslide_flooding_rating'),
                    G2_Flood_prone_water_Traversing_mining=data.get(
                        'G2_Flood_prone_water_Traversing_mining'),
                    G2_Flood_prone_water_Traversing_mining_rating=data.get(
                        'G2_Flood_prone_water_Traversing_mining_rating'),
                    G2_Flood_prone_water_Sparse_detached=data.get(
                        'G2_Flood_prone_water_Sparse_detached'),
                    G2_Flood_prone_water_Sparse_detached_rating=data.get(
                        'G2_Flood_prone_water_Sparse_detached_rating'),
                    G2_Flood_prone_water_undocumented_geological=data.get(
                        'G2_Flood_prone_water_undocumented_geological'),
                    G2_Flood_prone_water_undocumented_geological_rating=data.get(
                        'G2_Flood_prone_water_undocumented_geological_rating'),
                    G2_Flood_prone_water_Geopolitical_consideration=data.get(
                        'G2_Flood_prone_water_Geopolitical_consideration'),
                    G2_Flood_prone_water_Geopolitical_consideration_rating=data.get(
                        'G2_Flood_prone_water_Geopolitical_consideration_rating'),



                    # Diverse terrain (flat/ rolling/mountain/escarpments) increase design and technology complexity


                    G3_Diverse_terrain_Crossing_seismic=data.get(
                        'G3_Diverse_terrain_Crossing_seismic'),
                    G3_Diverse_terrain_Crossing_seismic_rating=data.get(
                        'G3_Diverse_terrain_Crossing_seismic_rating'),
                    G3_Diverse_terrain_Landslide_flooding=data.get(
                        'G3_Diverse_terrain_Landslide_flooding'),
                    G3_Diverse_terrain_Landslide_flooding_rating=data.get(
                        'G3_Diverse_terrain_Landslide_flooding_rating'),
                    G3_Diverse_terrain_Traversing_mining=data.get(
                        'G3_Diverse_terrain_Traversing_mining'),
                    G3_Diverse_terrain_Traversing_mining_rating=data.get(
                        'G3_Diverse_terrain_Traversing_mining_rating'),
                    G3_Diverse_terrain_Sparse_detached=data.get(
                        'G3_Diverse_terrain_Sparse_detached'),
                    G3_Diverse_terrain_Sparse_detached_rating=data.get(
                        'G3_Diverse_terrain_Sparse_detached_rating'),
                    G3_Diverse_terrain_undocumented_geological=data.get(
                        'G3_Diverse_terrain_undocumented_geological'),
                    G3_Diverse_terrain_undocumented_geological_rating=data.get(
                        'G3_Diverse_terrain_undocumented_geological_rating'),
                    G3_Diverse_terrain_Geopolitical_consideration=data.get(
                        'G3_Diverse_terrain_Geopolitical_consideration'),
                    G3_Diverse_terrain_Geopolitical_consideration_rating=data.get(
                        'G3_Diverse_terrain_Geopolitical_consideration_rating'),



                    # Crossing seismic active Great Rift Valley


                    G4_Crossing_seismic_Landslide_flooding=data.get(
                        'G4_Crossing_seismic_Landslide_flooding'),
                    G4_Crossing_seismic_Landslide_flooding_rating=data.get(
                        'G4_Crossing_seismic_Landslide_flooding_rating'),
                    G4_Crossing_seismic_Traversing_mining=data.get(
                        'G4_Crossing_seismic_Traversing_mining'),
                    G4_Crossing_seismic_Traversing_mining_rating=data.get(
                        'G4_Crossing_seismic_Traversing_mining_rating'),
                    G4_Crossing_seismic_Sparse_detached=data.get(
                        'G4_Crossing_seismic_Sparse_detached'),
                    G4_Crossing_seismic_Sparse_detached_rating=data.get(
                        'G4_Crossing_seismic_Sparse_detached_rating'),
                    G4_Crossing_seismic_undocumented_geological=data.get(
                        'G4_Crossing_seismic_undocumented_geological'),
                    G4_Crossing_seismic_undocumented_geological_rating=data.get(
                        'G4_Crossing_seismic_undocumented_geological_rating'),
                    G4_Crossing_seismic_Geopolitical_consideration=data.get(
                        'G4_Crossing_seismic_Geopolitical_consideration'),
                    G4_Crossing_seismic_Geopolitical_consideration_rating=data.get(
                        'G4_Crossing_seismic_Geopolitical_consideration_rating'),

                    # Landslide,flooding, erosion events could potentially delay project schedule and disrupt operations


                    G5_Landslide_flooding_Traversing_mining=data.get(
                        'G5_Landslide_flooding_Traversing_mining'),
                    G5_Landslide_flooding_Traversing_mining_rating=data.get(
                        'G5_Landslide_flooding_Traversing_mining_rating'),
                    G5_Landslide_flooding_Sparse_detached=data.get(
                        'G5_Landslide_flooding_Sparse_detached'),
                    G5_Landslide_flooding_Sparse_detached_rating=data.get(
                        'G5_Landslide_flooding_Sparse_detached_rating'),
                    G5_Landslide_flooding_undocumented_geological=data.get(
                        'G5_Landslide_flooding_undocumented_geological'),
                    G5_Landslide_flooding_undocumented_geological_rating=data.get(
                        'G5_Landslide_flooding_undocumented_geological_rating'),
                    G5_Landslide_flooding_Geopolitical_consideration=data.get(
                        'G5_Landslide_flooding_Geopolitical_consideration'),
                    G5_Landslide_flooding_Geopolitical_consideration_rating=data.get(
                        'G5_Landslide_flooding_Geopolitical_consideration_rating'),

                    # Traversing mining areas with active blasting/ explosions


                    G6_Traversing_mining_Sparse_detached=data.get(
                        'G6_Traversing_mining_Sparse_detached'),
                    G6_Traversing_mining_Sparse_detached_rating=data.get(
                        'G6_Traversing_mining_Sparse_detached_rating'),
                    G6_Traversing_mining_undocumented_geological=data.get(
                        'G6_Traversing_mining_undocumented_geological'),
                    G6_Traversing_mining_undocumented_geological_rating=data.get(
                        'G6_Traversing_mining_undocumented_geological_rating'),
                    G6_Traversing_mining_Geopolitical_consideration=data.get(
                        'G6_Traversing_mining_Geopolitical_consideration'),
                    G6_Traversing_mining_Geopolitical_consideration_rating=data.get(
                        'G6_Traversing_mining_Geopolitical_consideration_rating'),



                    # Sparse/detached settlement pattern unfeasible to link with GELB

                    G7_Sparse_detached_undocumented_geological=data.get(
                        'G7_Sparse_detached_undocumented_geological'),
                    G7_Sparse_detached_undocumented_geological_rating=data.get(
                        'G7_Sparse_detached_undocumented_geological_rating'),
                    G7_Sparse_detached_Geopolitical_consideration=data.get(
                        'G7_Sparse_detached_Geopolitical_consideration'),
                    G7_Sparse_detached_Geopolitical_consideration_rating=data.get(
                        'G7_Sparse_detached_Geopolitical_consideration_rating'),


                    # undocumented geological/subsurface condition

                    G8_undocumented_geological_Geopolitical_consideration=data.get(
                        'G8_undocumented_geological_Geopolitical_consideration'),
                    G8_undocumented_geological_Geopolitical_consideration_rating=data.get(
                        'G8_undocumented_geological_Geopolitical_consideration_rating')
                )
                geographicdata_create.save()

                economicdata_create = EconomicFactorDataA(

                    Correspondent_Email=survey_user,
                    fullname=data.get('username'),
                    Ec1_Dependance_Fiscally_strong=data.get(
                        'Ec1_Dependance_Fiscally_strong'),
                    Ec1_Dependance_Fiscally_strong_rating=data.get(
                        'Ec1_Dependance_Fiscally_strong_rating'),
                    Ec1_Dependance_Forex_loss=data.get(
                        'Ec1_Dependance_Forex_loss'),
                    Ec1_Dependance_Forex_loss_rating=data.get(
                        'Ec1_Dependance_Forex_loss_rating'),
                    Ec1_Dependance_inability_to_agree=data.get(
                        'Ec1_Dependance_inability_to_agree'),
                    Ec1_Dependance_inability_to_agree_rating=data.get(
                        'Ec1_Dependance_inability_to_agree_rating'),
                    Ec1_Dependance_user_fees=data.get(
                        'Ec1_Dependance_user_fees'),
                    Ec1_Dependance_user_fees_rating=data.get(
                        'Ec1_Dependance_user_fees_rating'),
                    Ec1_Dependance_budgetary_focus=data.get(
                        'Ec1_Dependance_budgetary_focus'),
                    Ec1_Dependance_budgetary_focus_rating=data.get(
                        'Ec1_Dependance_budgetary_focus_rating'),
                    Ec1_Dependance_fluctuation_of_exchange=data.get(
                        'Ec1_Dependance_fluctuation_of_exchange'),
                    Ec1_Dependance_fluctuation_of_exchange_rating=data.get(
                        'Ec1_Dependance_fluctuation_of_exchange_rating'),
                    Ec1_Dependance_Economic_vulnerability=data.get(
                        'Ec1_Dependance_Economic_vulnerability'),
                    Ec1_Dependance_Economic_vulnerability_rating=data.get(
                        'Ec1_Dependance_Economic_vulnerability_rating'),
                    Ec2_Fiscally_strong_Forex_loss=data.get(
                        'Ec2_Fiscally_strong_Forex_loss'),
                    Ec2_Fiscally_strong_Forex_loss_rating=data.get(
                        'Ec2_Fiscally_strong_Forex_loss_rating'),
                    Ec2_Fiscally_strong_inability_to_agree=data.get(
                        'Ec2_Fiscally_strong_inability_to_agree'),
                    Ec2_Fiscally_strong_inability_to_agree_rating=data.get(
                        'Ec2_Fiscally_strong_inability_to_agree_rating'),
                    Ec2_Fiscally_strong_user_fees=data.get(
                        'Ec2_Fiscally_strong_user_fees'),
                    Ec2_Fiscally_strong_user_fees_rating=data.get(
                        'Ec2_Fiscally_strong_user_fees_rating'),
                    Ec2_Fiscally_strong_budgetary_focus=data.get(
                        'Ec2_Fiscally_strong_budgetary_focus'),
                    Ec2_Fiscally_strong_budgetary_focus_rating=data.get(
                        'Ec2_Fiscally_strong_budgetary_focus_rating'),
                    Ec2_Fiscally_strong_fluctuation_of_exchange=data.get(
                        'Ec2_Fiscally_strong_fluctuation_of_exchange'),
                    Ec2_Fiscally_strong_fluctuation_of_exchange_rating=data.get(
                        'Ec2_Fiscally_strong_fluctuation_of_exchange_rating'),
                    Ec2_Fiscally_strong_Economic_vulnerability=data.get(
                        'Ec2_Fiscally_strong_Economic_vulnerability'),
                    Ec2_Fiscally_strong_Economic_vulnerability_rating=data.get(
                        'Ec2_Fiscally_strong_Economic_vulnerability_rating'),
                    Ec3_Forex_loss_inability_to_agree=data.get(
                        'Ec3_Forex_loss_inability_to_agree'),
                    Ec3_Forex_loss_inability_to_agree_rating=data.get(
                        'Ec3_Forex_loss_inability_to_agree_rating'),
                    Ec3_Forex_loss_user_fees=data.get(
                        'Ec3_Forex_loss_user_fees'),
                    Ec3_Forex_loss_user_fees_rating=data.get(
                        'Ec3_Forex_loss_user_fees_rating'),
                    Ec3_Forex_loss_budgetary_focus=data.get(
                        'Ec3_Forex_loss_budgetary_focus'),
                    Ec3_Forex_loss_budgetary_focus_rating=data.get(
                        'Ec3_Forex_loss_budgetary_focus_rating'),
                    Ec3_Forex_loss_fluctuation_of_exchange=data.get(
                        'Ec3_Forex_loss_fluctuation_of_exchange'),
                    Ec3_Forex_loss_fluctuation_of_exchange_rating=data.get(
                        'Ec3_Forex_loss_fluctuation_of_exchange_rating'),
                    Ec3_Forex_loss_Economic_vulnerability=data.get(
                        'Ec3_Forex_loss_Economic_vulnerability'),
                    Ec3_Forex_loss_Economic_vulnerability_rating=data.get(
                        'Ec3_Forex_loss_Economic_vulnerability_rating'),
                    Ec4_inability_to_agree_user_fees=data.get(
                        'Ec4_inability_to_agree_user_fees'),
                    Ec4_inability_to_agree_user_fees_rating=data.get(
                        'Ec4_inability_to_agree_user_fees_rating'),
                    Ec4_inability_to_agree_budgetary_focus=data.get(
                        'Ec4_inability_to_agree_budgetary_focus'),
                    Ec4_inability_to_agree_budgetary_focus_rating=data.get(
                        'Ec4_inability_to_agree_budgetary_focus_rating'),
                    Ec4_inability_to_agree_fluctuation_of_exchange=data.get(
                        'Ec4_inability_to_agree_fluctuation_of_exchange'),
                    Ec4_inability_to_agree_fluctuation_of_exchange_rating=data.get(
                        'Ec4_inability_to_agree_fluctuation_of_exchange_rating'),
                    Ec4_inability_to_agree_Economic_vulnerability=data.get(
                        'Ec4_inability_to_agree_Economic_vulnerability'),
                    Ec4_inability_to_agree_Economic_vulnerability_rating=data.get(
                        'Ec4_inability_to_agree_Economic_vulnerability_rating'),
                    Ec5_user_fees_budgetary_focus=data.get(
                        'Ec5_user_fees_budgetary_focus'),
                    Ec5_user_fees_budgetary_focus_rating=data.get(
                        'Ec5_user_fees_budgetary_focus_rating'),
                    Ec5_user_fees_fluctuation_of_exchange=data.get(
                        'Ec5_user_fees_fluctuation_of_exchange'),
                    Ec5_user_fees_fluctuation_of_exchange_rating=data.get(
                        'Ec5_user_fees_fluctuation_of_exchange_rating'),
                    Ec5_user_fees_Economic_vulnerability=data.get(
                        'Ec5_user_fees_Economic_vulnerability'),
                    Ec5_user_fees_Economic_vulnerability_rating=data.get(
                        'Ec5_user_fees_Economic_vulnerability_rating'),
                    Ec6_budgetary_focus_fluctuation_of_exchange=data.get(
                        'Ec6_budgetary_focus_fluctuation_of_exchange'),
                    Ec6_budgetary_focus_fluctuation_of_exchange_rating=data.get(
                        'Ec6_budgetary_focus_fluctuation_of_exchange_rating'),
                    Ec6_budgetary_focus_Economic_vulnerability=data.get(
                        'Ec6_budgetary_focus_Economic_vulnerability'),
                    Ec6_budgetary_focus_Economic_vulnerability_rating=data.get(
                        'Ec6_budgetary_focus_Economic_vulnerability_rating'),
                    Ec7_fluctuation_of_exchange_Economic_vulnerability=data.get(
                        'Ec7_fluctuation_of_exchange_Economic_vulnerability'),
                    Ec7_fluctuation_of_exchange_Economic_vulnerability_rating=data.get(
                        'Ec7_fluctuation_of_exchange_Economic_vulnerability_rating'),

                )
                economicdata_create.save()

                technologydata_create = TechnologicalFactorDataA(

                    Correspondent_Email=survey_user,
                    fullname=data.get('username'),


                    # Variation among states in highway classification by purpose & capacity

                    Tc1_Variation_among_Telecommuting_technology=data.get(
                        'Tc1_Variation_among_Telecommuting_technology'),
                    Tc1_Variation_among_Telecommuting_technology_rating=data.get(
                        'Tc1_Variation_among_Telecommuting_technology_rating'),
                    Tc1_Variation_among_Evolving_technology=data.get(
                        'Tc1_Variation_among_Evolving_technology'),
                    Tc1_Variation_among_Evolving_technology_rating=data.get(
                        'Tc1_Variation_among_Evolving_technology_rating'),
                    Tc1_Variation_among_necesstiy_of_tunnels=data.get(
                        'Tc1_Variation_among_necesstiy_of_tunnels'),
                    Tc1_Variation_among_necesstiy_of_tunnels_rating=data.get(
                        'Tc1_Variation_among_necesstiy_of_tunnels_rating'),
                    Tc1_Variation_among_use_of_monopolistic=data.get(
                        'Tc1_Variation_among_use_of_monopolistic'),
                    Tc1_Variation_among_use_of_monopolistic_rating=data.get(
                        'Tc1_Variation_among_use_of_monopolistic_rating'),
                    Tc1_Variation_among_Favoring_politically_popular=data.get(
                        'Tc1_Variation_among_Favoring_politically_popular'),
                    Tc1_Variation_among_Favoring_politically_popular_rating=data.get(
                        'Tc1_Variation_among_Favoring_politically_popular_rating'),
                    Tc1_Variation_among_Delays_downtime=data.get(
                        'Tc1_Variation_among_Delays_downtime'),
                    Tc1_Variation_among_Delays_downtime_rating=data.get(
                        'Tc1_Variation_among_Delays_downtime_rating'),
                    Tc1_Variation_among_Equipment_parts=data.get(
                        'Tc1_Variation_among_Equipment_parts'),
                    Tc1_Variation_among_Equipment_parts_rating=data.get(
                        'Tc1_Variation_among_Equipment_parts_rating'),
                    Tc1_Variation_among_construction_preceding=data.get(
                        'Tc1_Variation_among_construction_preceding'),
                    Tc1_Variation_among_construction_preceding_rating=data.get(
                        'Tc1_Variation_among_construction_preceding_rating'),


                    # Telecommuting technology making redundant human movement


                    Tc2_Telecommuting_technology_Evolving_technology=data.get(
                        'Tc2_Telecommuting_technology_Evolving_technology'),
                    Tc2_Telecommuting_technology_Evolving_technology_rating=data.get(
                        'Tc2_Telecommuting_technology_Evolving_technology_rating'),
                    Tc2_Telecommuting_technology_necesstiy_of_tunnels=data.get(
                        'Tc2_Telecommuting_technology_necesstiy_of_tunnels'),
                    Tc2_Telecommuting_technology_necesstiy_of_tunnels_rating=data.get(
                        'Tc2_Telecommuting_technology_necesstiy_of_tunnels_rating'),
                    Tc2_Telecommuting_technology_use_of_monopolistic=data.get(
                        'Tc2_Telecommuting_technology_use_of_monopolistic'),
                    Tc2_Telecommuting_technology_use_of_monopolistic_rating=data.get(
                        'Tc2_Telecommuting_technology_use_of_monopolistic_rating'),
                    Tc2_Telecommuting_technology_Favoring_politically_popular=data.get(
                        'Tc2_Telecommuting_technology_Favoring_politically_popular'),
                    Tc2_Telecommuting_technology_Favoring_politically_popular_rating=data.get(
                        'Tc2_Telecommuting_technology_Favoring_politically_popular_rating'),
                    Tc2_Telecommuting_technology_Delays_downtime=data.get(
                        'Tc2_Telecommuting_technology_Delays_downtime'),
                    Tc2_Telecommuting_technology_Delays_downtime_rating=data.get(
                        'Tc2_Telecommuting_technology_Delays_downtime_rating'),
                    Tc2_Telecommuting_technology_Equipment_parts=data.get(
                        'Tc2_Telecommuting_technology_Equipment_parts'),
                    Tc2_Telecommuting_technology_Equipment_parts_rating=data.get(
                        'Tc2_Telecommuting_technology_Equipment_parts_rating'),
                    Tc2_Telecommuting_technology_construction_preceding=data.get(
                        'Tc2_Telecommuting_technology_construction_preceding'),
                    Tc2_Telecommuting_technology_construction_preceding_rating=data.get(
                        'Tc2_Telecommuting_technology_construction_preceding_rating'),


                    # Evolving technology rendering obsolete construction/ maintainance/operation equipment


                    Tc3_Evolving_technology_necesstiy_of_tunnels=data.get(
                        'Tc3_Evolving_technology_necesstiy_of_tunnels'),
                    Tc3_Evolving_technology_necesstiy_of_tunnels_rating=data.get(
                        'Tc3_Evolving_technology_necesstiy_of_tunnels_rating'),
                    Tc3_Evolving_technology_use_of_monopolistic=data.get(
                        'Tc3_Evolving_technology_use_of_monopolistic'),
                    Tc3_Evolving_technology_use_of_monopolistic_rating=data.get(
                        'Tc3_Evolving_technology_use_of_monopolistic_rating'),
                    Tc3_Evolving_technology_Favoring_politically_popular=data.get(
                        'Tc3_Evolving_technology_Favoring_politically_popular'),
                    Tc3_Evolving_technology_Favoring_politically_popular_rating=data.get(
                        'Tc3_Evolving_technology_Favoring_politically_popular_rating'),
                    Tc3_Evolving_technology_Delays_downtime=data.get(
                        'Tc3_Evolving_technology_Delays_downtime'),
                    Tc3_Evolving_technology_Delays_downtime_rating=data.get(
                        'Tc3_Evolving_technology_Delays_downtime_rating'),
                    Tc3_Evolving_technology_Equipment_parts=data.get(
                        'Tc3_Evolving_technology_Equipment_parts'),
                    Tc3_Evolving_technology_Equipment_parts_rating=data.get(
                        'Tc3_Evolving_technology_Equipment_parts_rating'),
                    Tc3_Evolving_technology_construction_preceding=data.get(
                        'Tc3_Evolving_technology_construction_preceding'),
                    Tc3_Evolving_technology_construction_preceding_rating=data.get(
                        'Tc3_Evolving_technology_construction_preceding_rating'),


                    # necesstiy of tunnels, overpasses, barriers in areas with flora/fauna/water-bodies/settlements


                    Tc4_necesstiy_of_tunnels_use_of_monopolistic=data.get(
                        'Tc4_necesstiy_of_tunnels_use_of_monopolistic'),
                    Tc4_necesstiy_of_tunnels_use_of_monopolistic_rating=data.get(
                        'Tc4_necesstiy_of_tunnels_use_of_monopolistic_rating'),
                    Tc4_necesstiy_of_tunnels_Favoring_politically_popular=data.get(
                        'Tc4_necesstiy_of_tunnels_Favoring_politically_popular'),
                    Tc4_necesstiy_of_tunnels_Favoring_politically_popular_rating=data.get(
                        'Tc4_necesstiy_of_tunnels_Favoring_politically_popular_rating'),
                    Tc4_necesstiy_of_tunnels_Delays_downtime=data.get(
                        'Tc4_necesstiy_of_tunnels_Delays_downtime'),
                    Tc4_necesstiy_of_tunnels_Delays_downtime_rating=data.get(
                        'Tc4_necesstiy_of_tunnels_Delays_downtime_rating'),
                    Tc4_necesstiy_of_tunnels_Equipment_parts=data.get(
                        'Tc4_necesstiy_of_tunnels_Equipment_parts'),
                    Tc4_necesstiy_of_tunnels_Equipment_parts_rating=data.get(
                        'Tc4_necesstiy_of_tunnels_Equipment_parts_rating'),
                    Tc4_necesstiy_of_tunnels_construction_preceding=data.get(
                        'Tc4_necesstiy_of_tunnels_construction_preceding'),
                    Tc4_necesstiy_of_tunnels_construction_preceding_rating=data.get(
                        'Tc4_necesstiy_of_tunnels_construction_preceding_rating'),


                    # use of monopolistic foreign contractor limiting technology transfer to local firms/citizens



                    Tc5_use_of_monopolistic_Favoring_politically_popular=data.get(
                        'Tc5_use_of_monopolistic_Favoring_politically_popular'),
                    Tc5_use_of_monopolistic_Favoring_politically_popular_rating=data.get(
                        'Tc5_use_of_monopolistic_Favoring_politically_popular_rating'),
                    Tc5_use_of_monopolistic_Delays_downtime=data.get(
                        'Tc5_use_of_monopolistic_Delays_downtime'),
                    Tc5_use_of_monopolistic_Delays_downtime_rating=data.get(
                        'Tc5_use_of_monopolistic_Delays_downtime_rating'),
                    Tc5_use_of_monopolistic_Equipment_parts=data.get(
                        'Tc5_use_of_monopolistic_Equipment_parts'),
                    Tc5_use_of_monopolistic_Equipment_parts_rating=data.get(
                        'Tc5_use_of_monopolistic_Equipment_parts_rating'),
                    Tc5_use_of_monopolistic_construction_preceding=data.get(
                        'Tc5_use_of_monopolistic_construction_preceding'),
                    Tc5_use_of_monopolistic_construction_preceding_rating=data.get(
                        'Tc5_use_of_monopolistic_construction_preceding_rating'),


                    # Favoring politically-popular but inefficient labor intensive technology


                    Tc6_Favoring_politically_popular_Delays_downtime=data.get(
                        'Tc6_Favoring_politically_popular_Delays_downtime'),
                    Tc6_Favoring_politically_popular_Delays_downtime_rating=data.get(
                        'Tc6_Favoring_politically_popular_Delays_downtime_rating'),
                    Tc6_Favoring_politically_popular_Equipment_parts=data.get(
                        'Tc6_Favoring_politically_popular_Equipment_parts'),
                    Tc6_Favoring_politically_popular_Equipment_parts_rating=data.get(
                        'Tc6_Favoring_politically_popular_Equipment_parts_rating'),
                    Tc6_Favoring_politically_popular_construction_preceding=data.get(
                        'Tc6_Favoring_politically_popular_construction_preceding'),
                    Tc6_Favoring_politically_popular_construction_preceding_rating=data.get(
                        'Tc6_Favoring_politically_popular_construction_preceding_rating'),


                    # Delays/downtime due to low-utilization of efficient border clearance technology


                    Tc7_Delays_downtime_Equipment_parts=data.get(
                        'Tc7_Delays_downtime_Equipment_parts'),
                    Tc7_Delays_downtime_Equipment_parts_rating=data.get(
                        'Tc7_Delays_downtime_Equipment_parts_rating'),
                    Tc7_Delays_downtime_construction_preceding=data.get(
                        'Tc7_Delays_downtime_construction_preceding'),
                    Tc7_Delays_downtime_construction_preceding_rating=data.get(
                        'Tc7_Delays_downtime_construction_preceding_rating'),


                    # Equipment/parts supply disruption by pandemics and local unavailability of equipment dealers

                    Tc8_Equipment_parts_construction_preceding=data.get(
                        'Tc8_Equipment_parts_construction_preceding'),
                    Tc8_Equipment_parts_construction_preceding_rating=data.get(
                        'Tc8_Equipment_parts_construction_preceding_rating'),


                )
                technologydata_create.save()
                
                socialdata_create = SocialFactorDataA(

                    Correspondent_Email=survey_user,
                    fullname=data.get('username'),

                    # Disrupted social interaction by settlement split/displacement


                    So1_Disrupted_social_Benefits_unlikely=data.get(
                        'So1_Disrupted_social_Benefits_unlikely'),
                    So1_Disrupted_social_Benefits_unlikely_rating=data.get(
                        'So1_Disrupted_social_Benefits_unlikely_rating'),
                    So1_Disrupted_social_loss_of_work=data.get(
                        'So1_Disrupted_social_loss_of_work'),
                    So1_Disrupted_social_loss_of_work_rating=data.get(
                        'So1_Disrupted_social_loss_of_work_rating'),
                    So1_Disrupted_social_Hard_to_identify=data.get(
                        'So1_Disrupted_social_Hard_to_identify'),
                    So1_Disrupted_social_Hard_to_identify_rating=data.get(
                        'So1_Disrupted_social_Hard_to_identify_rating'),
                    So1_Disrupted_social_High_speed=data.get(
                        'So1_Disrupted_social_High_speed'),
                    So1_Disrupted_social_High_speed_rating=data.get(
                        'So1_Disrupted_social_High_speed_rating'),
                    So1_Disrupted_social_Crowding=data.get(
                        'So1_Disrupted_social_Crowding'),
                    So1_Disrupted_social_Crowding_rating=data.get(
                        'So1_Disrupted_social_Crowding_rating'),
                    So1_Disrupted_social_low_per_capita=data.get(
                        'So1_Disrupted_social_low_per_capita'),
                    So1_Disrupted_social_low_per_capita_rating=data.get(
                        'So1_Disrupted_social_low_per_capita_rating'),
                    So1_Disrupted_social_Food_security=data.get(
                        'So1_Disrupted_social_Food_security'),
                    So1_Disrupted_social_Food_security_rating=data.get(
                        'So1_Disrupted_social_Food_security_rating'),
                    So1_Disrupted_social_Community_resistance=data.get(
                        'So1_Disrupted_social_Community_resistance'),
                    So1_Disrupted_social_Community_resistance_rating=data.get(
                        'So1_Disrupted_social_Community_resistance_rating'),


                    # Benefits unlikely to trickle to local communities


                    So2_Benefits_unlikely_loss_of_work=data.get(
                        'So2_Benefits_unlikely_loss_of_work'),
                    So2_Benefits_unlikely_loss_of_work_rating=data.get(
                        'So2_Benefits_unlikely_loss_of_work_rating'),
                    So2_Benefits_unlikely_Hard_to_identify=data.get(
                        'So2_Benefits_unlikely_Hard_to_identify'),
                    So2_Benefits_unlikely_Hard_to_identify_rating=data.get(
                        'So2_Benefits_unlikely_Hard_to_identify_rating'),
                    So2_Benefits_unlikely_High_speed=data.get(
                        'So2_Benefits_unlikely_High_speed'),
                    So2_Benefits_unlikely_High_speed_rating=data.get(
                        'So2_Benefits_unlikely_High_speed_rating'),
                    So2_Benefits_unlikely_Crowding=data.get(
                        'So2_Benefits_unlikely_Crowding'),
                    So2_Benefits_unlikely_Crowding_rating=data.get(
                        'So2_Benefits_unlikely_Crowding_rating'),
                    So2_Benefits_unlikely_low_per_capita=data.get(
                        'So2_Benefits_unlikely_low_per_capita'),
                    So2_Benefits_unlikely_low_per_capita_rating=data.get(
                        'So2_Benefits_unlikely_low_per_capita_rating'),
                    So2_Benefits_unlikely_Food_security=data.get(
                        'So2_Benefits_unlikely_Food_security'),
                    So2_Benefits_unlikely_Food_security_rating=data.get(
                        'So2_Benefits_unlikely_Food_security_rating'),
                    So2_Benefits_unlikely_Community_resistance=data.get(
                        'So2_Benefits_unlikely_Community_resistance'),
                    So2_Benefits_unlikely_Community_resistance_rating=data.get(
                        'So2_Benefits_unlikely_Community_resistance_rating'),


                    # loss of work/opportunity to immigrants due to inadequate skill and language barrier



                    So3_loss_of_work_Hard_to_identify=data.get(
                        'So3_loss_of_work_Hard_to_identify'),
                    So3_loss_of_work_Hard_to_identify_rating=data.get(
                        'So3_loss_of_work_Hard_to_identify_rating'),
                    So3_loss_of_work_High_speed=data.get(
                        'So3_loss_of_work_High_speed'),
                    So3_loss_of_work_High_speed_rating=data.get(
                        'So3_loss_of_work_High_speed_rating'),
                    So3_loss_of_work_Crowding=data.get(
                        'So3_loss_of_work_Crowding'),
                    So3_loss_of_work_Crowding_rating=data.get(
                        'So3_loss_of_work_Crowding_rating'),
                    So3_loss_of_work_low_per_capita=data.get(
                        'So3_loss_of_work_low_per_capita'),
                    So3_loss_of_work_low_per_capita_rating=data.get(
                        'So3_loss_of_work_low_per_capita_rating'),
                    So3_loss_of_work_Food_security=data.get(
                        'So3_loss_of_work_Food_security'),
                    So3_loss_of_work_Food_security_rating=data.get(
                        'So3_loss_of_work_Food_security_rating'),
                    So3_loss_of_work_Community_resistance=data.get(
                        'So3_loss_of_work_Community_resistance'),
                    So3_loss_of_work_Community_resistance_rating=data.get(
                        'So3_loss_of_work_Community_resistance_rating'),


                    # Hard to identify Project Affected Persons due to conflict/environmental/economic migration



                    So4_Hard_to_identify_High_speed=data.get(
                        'So4_Hard_to_identify_High_speed'),
                    So4_Hard_to_identify_High_speed_rating=data.get(
                        'So4_Hard_to_identify_High_speed_rating'),
                    So4_Hard_to_identify_Crowding=data.get(
                        'So4_Hard_to_identify_Crowding'),
                    So4_Hard_to_identify_Crowding_rating=data.get(
                        'So4_Hard_to_identify_Crowding_rating'),
                    So4_Hard_to_identify_low_per_capita=data.get(
                        'So4_Hard_to_identify_low_per_capita'),
                    So4_Hard_to_identify_low_per_capita_rating=data.get(
                        'So4_Hard_to_identify_low_per_capita_rating'),
                    So4_Hard_to_identify_Food_security=data.get(
                        'So4_Hard_to_identify_Food_security'),
                    So4_Hard_to_identify_Food_security_rating=data.get(
                        'So4_Hard_to_identify_Food_security_rating'),
                    So4_Hard_to_identify_Community_resistance=data.get(
                        'So4_Hard_to_identify_Community_resistance'),
                    So4_Hard_to_identify_Community_resistance_rating=data.get(
                        'So4_Hard_to_identify_Community_resistance_rating'),

                    # High-speed traffic and dangerous goods carriage threaten human safety/livelihood activities


                    So5_High_speed_Crowding=data.get(
                        'So5_High_speed_Crowding'),
                    So5_High_speed_Crowding_rating=data.get(
                        'So5_High_speed_Crowding_rating'),
                    So5_High_speed_low_per_capita=data.get(
                        'So5_High_speed_low_per_capita'),
                    So5_High_speed_low_per_capita_rating=data.get(
                        'So5_High_speed_low_per_capita_rating'),
                    So5_High_speed_Food_security=data.get(
                        'So5_High_speed_Food_security'),
                    So5_High_speed_Food_security_rating=data.get(
                        'So5_High_speed_Food_security_rating'),
                    So5_High_speed_Community_resistance=data.get(
                        'So5_High_speed_Community_resistance'),
                    So5_High_speed_Community_resistance_rating=data.get(
                        'So5_High_speed_Community_resistance_rating'),

                    # Crowding out local population due to increased cost of basic goods/services

                    So6_Crowding_low_per_capita=data.get(
                        'So6_Crowding_low_per_capita'),
                    So6_Crowding_low_per_capita_rating=data.get(
                        'So6_Crowding_low_per_capita_rating'),
                    So6_Crowding_Food_security=data.get(
                        'So6_Crowding_Food_security'),
                    So6_Crowding_Food_security_rating=data.get(
                        'So6_Crowding_Food_security_rating'),
                    So6_Crowding_Community_resistance=data.get(
                        'So6_Crowding_Community_resistance'),
                    So6_Crowding_Community_resistance_rating=data.get(
                        'So6_Crowding_Community_resistance_rating'),

                    # low per-capita income levels limits revenue mobilization from taxation


                    So7_low_per_capita_Food_security=data.get(
                        'So7_low_per_capita_Food_security'),
                    So7_low_per_capita_Food_security_rating=data.get(
                        'So7_low_per_capita_Food_security_rating'),
                    So7_low_per_capita_Community_resistance=data.get(
                        'So7_low_per_capita_Community_resistance'),
                    So7_low_per_capita_Community_resistance_rating=data.get(
                        'So7_low_per_capita_Community_resistance_rating'),


                    # Food security threat by farmers switch to non-farming activity


                    So8_Food_security_Community_resistance=data.get(
                        'So8_Food_security_Community_resistance'),
                    So8_Food_security_Community_resistance_rating=data.get(
                        'So8_Food_security_Community_resistance_rating')

                )
                socialdata_create.save()
                
                environmentaldata_create = EnvironmentalFactorDataA(

                    Correspondent_Email=survey_user,
                    fullname=data.get('username'),
                    
                       # Extreme weather events (floods/hot-sun/humidity) shorten corridor lifespan
                    En1_Extreme_weather_requirement_to_minimise=data.get('En1_Extreme_weather_requirement_to_minimise'),
                    En1_Extreme_weather_requirement_to_minimise_rating =data.get('En1_Extreme_weather_requirement_to_minimise_rating'),
                    En1_Extreme_weather_crossing_diverse=data.get('En1_Extreme_weather_crossing_diverse'),
                    En1_Extreme_weather_crossing_diverse_rating =data.get('En1_Extreme_weather_crossing_diverse_rating'),
                    En1_Extreme_weather_enhanced_access=data.get('En1_Extreme_weather_enhanced_access'),
                    En1_Extreme_weather_enhanced_access_rating =data.get('En1_Extreme_weather_enhanced_access_rating'),
                    En1_Extreme_weather_Disasters_due=data.get('En1_Extreme_weather_Disasters_due'),
                    En1_Extreme_weather_Disasters_due_rating =data.get('En1_Extreme_weather_Disasters_due_rating'),
                    En1_Extreme_weather_Ecosystem_resources=data.get('En1_Extreme_weather_Ecosystem_resources'),
                    En1_Extreme_weather_Ecosystem_resources_rating =data.get('En1_Extreme_weather_Ecosystem_resources_rating'),
                    En1_Extreme_weather_Human_induced=data.get('En1_Extreme_weather_Human_induced'),
                    En1_Extreme_weather_Human_induced_rating =data.get('En1_Extreme_weather_Human_induced_rating'),
                    En1_Extreme_weather_Climate_change=data.get('En1_Extreme_weather_Climate_change'),
                    En1_Extreme_weather_Climate_change_rating =data.get('En1_Extreme_weather_Climate_change_rating'),
                    En1_Extreme_weather_requirement_to_safeguard=data.get('En1_Extreme_weather_requirement_to_safeguard'),
                    En1_Extreme_weather_requirement_to_safeguard_rating =data.get('En1_Extreme_weather_requirement_to_safeguard_rating'),

            # requirement to minimise alteration of hydrological patterns/flora/fauna/migratory corridors


                    En2_requirement_to_minimise_crossing_diverse=data.get('En2_requirement_to_minimise_crossing_diverse'),
                    En2_requirement_to_minimise_crossing_diverse_rating =data.get('En2_requirement_to_minimise_crossing_diverse_rating'),
                    En2_requirement_to_minimise_enhanced_access=data.get('En2_requirement_to_minimise_enhanced_access'),
                    En2_requirement_to_minimise_enhanced_access_rating =data.get('En2_requirement_to_minimise_enhanced_access_rating'),
                    En2_requirement_to_minimise_Disasters_due=data.get('En2_requirement_to_minimise_Disasters_due'),
                    En2_requirement_to_minimise_Disasters_due_rating =data.get('En2_requirement_to_minimise_Disasters_due_rating'),
                    En2_requirement_to_minimise_Ecosystem_resources=data.get('En2_requirement_to_minimise_Ecosystem_resources'),
                    En2_requirement_to_minimise_Ecosystem_resources_rating =data.get('En2_requirement_to_minimise_Ecosystem_resources_rating'),
                    En2_requirement_to_minimise_Human_induced=data.get('En2_requirement_to_minimise_Human_induced'),
                    En2_requirement_to_minimise_Human_induced_rating =data.get('En2_requirement_to_minimise_Human_induced_rating'),
                    En2_requirement_to_minimise_Climate_change=data.get('En2_requirement_to_minimise_Climate_change'),
                    En2_requirement_to_minimise_Climate_change_rating =data.get('En2_requirement_to_minimise_Climate_change_rating'),
                    En2_requirement_to_minimise_requirement_to_safeguard=data.get('En2_requirement_to_minimise_requirement_to_safeguard'),
                    En2_requirement_to_minimise_requirement_to_safeguard_rating =data.get('En2_requirement_to_minimise_requirement_to_safeguard_rating'),

            # crossing diverse climate zones impacts design complexity and maintainance cost


                    En3_crossing_diverse_enhanced_access=data.get('En3_crossing_diverse_enhanced_access'),
                    En3_crossing_diverse_enhanced_access_rating =data.get('En3_crossing_diverse_enhanced_access_rating'),
                    En3_crossing_diverse_Disasters_due=data.get('En3_crossing_diverse_Disasters_due'),
                    En3_crossing_diverse_Disasters_due_rating =data.get('En3_crossing_diverse_Disasters_due_rating'),
                    En3_crossing_diverse_Ecosystem_resources=data.get('En3_crossing_diverse_Ecosystem_resources'),
                    En3_crossing_diverse_Ecosystem_resources_rating =data.get('En3_crossing_diverse_Ecosystem_resources_rating'),
                    En3_crossing_diverse_Human_induced=data.get('En3_crossing_diverse_Human_induced'),
                    En3_crossing_diverse_Human_induced_rating =data.get('En3_crossing_diverse_Human_induced_rating'),
                    En3_crossing_diverse_Climate_change=data.get('En3_crossing_diverse_Climate_change'),
                    En3_crossing_diverse_Climate_change_rating =data.get('En3_crossing_diverse_Climate_change_rating'),
                    En3_crossing_diverse_requirement_to_safeguard=data.get('En3_crossing_diverse_requirement_to_safeguard'),
                    En3_crossing_diverse_requirement_to_safeguard_rating =data.get('En3_crossing_diverse_requirement_to_safeguard_rating'),

            # enhanced access to aggravate poaching, illegal lumbering and mining


                    En4_enhanced_access_Disasters_due=data.get('En4_enhanced_access_Disasters_due'),
                    En4_enhanced_access_Disasters_due_rating =data.get('En4_enhanced_access_Disasters_due_rating'),
                    En4_enhanced_access_Ecosystem_resources=data.get('En4_enhanced_access_Ecosystem_resources'),
                    En4_enhanced_access_Ecosystem_resources_rating =data.get('En4_enhanced_access_Ecosystem_resources_rating'),
                    En4_enhanced_access_Human_induced=data.get('En4_enhanced_access_Human_induced'),
                    En4_enhanced_access_Human_induced_rating =data.get('En4_enhanced_access_Human_induced_rating'),
                    En4_enhanced_access_Climate_change=data.get('En4_enhanced_access_Climate_change'),
                    En4_enhanced_access_Climate_change_rating =data.get('En4_enhanced_access_Climate_change_rating'),
                    En4_enhanced_access_requirement_to_safeguard=data.get('En4_enhanced_access_requirement_to_safeguard'),
                    En4_enhanced_access_requirement_to_safeguard_rating =data.get('En4_enhanced_access_requirement_to_safeguard_rating'),

            # Disasters due to weather related events

            
                    En5_Disasters_due_Ecosystem_resources=data.get('En5_Disasters_due_Ecosystem_resources'),
                    En5_Disasters_due_Ecosystem_resources_rating =data.get('En5_Disasters_due_Ecosystem_resources_rating'),
                    En5_Disasters_due_Human_induced=data.get('En5_Disasters_due_Human_induced'),
                    En5_Disasters_due_Human_induced_rating =data.get('En5_Disasters_due_Human_induced_rating'),
                    En5_Disasters_due_Climate_change=data.get('En5_Disasters_due_Climate_change'),
                    En5_Disasters_due_Climate_change_rating =data.get('En5_Disasters_due_Climate_change_rating'),
                    En5_Disasters_due_requirement_to_safeguard=data.get('En5_Disasters_due_requirement_to_safeguard'),
                    En5_Disasters_due_requirement_to_safeguard_rating =data.get('En5_Disasters_due_requirement_to_safeguard_rating'),


            # Ecosystem resources degradadation by settlement densification/immigrants influx


                    En6_Ecosystem_resources_Human_induced=data.get('En6_Ecosystem_resources_Human_induced'),
                    En6_Ecosystem_resources_Human_induced_rating =data.get('En6_Ecosystem_resources_Human_induced_rating'),
                    En6_Ecosystem_resources_Climate_change=data.get('En6_Ecosystem_resources_Climate_change'),
                    En6_Ecosystem_resources_Climate_change_rating =data.get('En6_Ecosystem_resources_Climate_change_rating'),
                    En6_Ecosystem_resources_requirement_to_safeguard=data.get('En6_Ecosystem_resources_requirement_to_safeguard'),
                    En6_Ecosystem_resources_requirement_to_safeguard_rating =data.get('En6_Ecosystem_resources_requirement_to_safeguard_rating'),


            # Human induced landslide, soil erosion and water-body sedimentation

                    En7_Human_induced_Climate_change=data.get('En7_Human_induced_Climate_change'),
                    En7_Human_induced_Climate_change_rating =data.get('En7_Human_induced_Climate_change_rating'),
                    En7_Human_induced_requirement_to_safeguard=data.get('En7_Human_induced_requirement_to_safeguard'),
                    En7_Human_induced_requirement_to_safeguard_rating =data.get('En7_Human_induced_requirement_to_safeguard_rating'),


            # Climate change induced variation of average local weather patterns

                    En8_Climate_change_requirement_to_safeguard=data.get('En8_Climate_change_requirement_to_safeguard'),
                    En8_Climate_change_requirement_to_safeguard_rating =data.get('En8_Climate_change_requirement_to_safeguard_rating')
                )
                environmentaldata_create.save()
                response = {
                    "message": "Correspondent register sucessfully",
                    "data": serializer.data
                }
                return Response(data=response, status=status.HTTP_200_OK)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response = {
                "status": 400,
                "message": str(e)
            }
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
