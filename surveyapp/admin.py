from django.contrib import admin

from surveyapp.models import EconomicFactorDataA, EnvironmentalFactorDataA, GeographicFactorDataA, IntroSurveyDataA, LandUseFactorDataA, PoliticalFactorDataA, SocialFactorDataA, SurveyUser, TechnologicalFactorDataA
from import_export.admin import ImportExportActionModelAdmin, ImportExportModelAdmin

# from surveyapp.resources import SurveyDataAResources
# Register your models here.

class SurveyDataAAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = [
        "id", "fullname"
      
    ]
    search_fields = ['Correspondent_Email']
    autocomplete_fields = ["Correspondent_Email"]
    # list_filter = ['Gender', "Age"]
    
admin.site.register(IntroSurveyDataA, SurveyDataAAdmin)



class PoliticalFactorDataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = [
        "id", "fullname"
      
    ]
    search_fields = ['Correspondent_Email']
    autocomplete_fields = ["Correspondent_Email"]
    # list_filter = ['Gender', "Age"]
    
admin.site.register(PoliticalFactorDataA, PoliticalFactorDataAdmin)


class LandUseFactorDataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = [
        "id", "fullname"
      
    ]
    search_fields = ['Correspondent_Email']
    autocomplete_fields = ["Correspondent_Email"]
    # list_filter = ['Gender', "Age"]
    
admin.site.register(LandUseFactorDataA, LandUseFactorDataAdmin)


class GeographicFactorDataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = [
        "id", "fullname"
      
    ]
    search_fields = ['Correspondent_Email']
    autocomplete_fields = ["Correspondent_Email"]
    # list_filter = ['Gender', "Age"]
    
admin.site.register(GeographicFactorDataA, GeographicFactorDataAdmin)


class EconomicFactorDataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = [
        "id", "fullname"
      
    ]
    search_fields = ['Correspondent_Email']
    autocomplete_fields = ["Correspondent_Email"]
    # list_filter = ['Gender', "Age"]
    
admin.site.register(EconomicFactorDataA, EconomicFactorDataAdmin)



class TechnologycalFactorDataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = [
        "id", "fullname"
      
    ]
    search_fields = ['Correspondent_Email']
    autocomplete_fields = ["Correspondent_Email"]
    # list_filter = ['Gender', "Age"]
    
admin.site.register(TechnologicalFactorDataA, TechnologycalFactorDataAdmin)


class SocialFactorDataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = [
        "id", "fullname"
      
    ]
    search_fields = ['Correspondent_Email']
    autocomplete_fields = ["Correspondent_Email"]
    # list_filter = ['Gender', "Age"]
    
admin.site.register(SocialFactorDataA, SocialFactorDataAdmin)

class EnvironmentalFactorDataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = [
        "id", "fullname"
      
    ]
    search_fields = ['Correspondent_Email']
    autocomplete_fields = ["Correspondent_Email"]
    # list_filter = ['Gender', "Age"]
    
admin.site.register(EnvironmentalFactorDataA, EnvironmentalFactorDataAdmin)

# @admin.register(IntroSurveyDataA)
# class SurveyDataAAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     ...
# admin.site.register(IntroSurveyDataA, SurveyDataAAdmin)

    # list_display = ["id","First_name","Last_name","Gender","Age","email",
    #                 "Question_1","Question_2","Question_3","Question_4",
    #                 "Question_5",
    #                 ]
    # search_fields = ['Frist_name', 'Age', 'email']
    # # autocomplete_fields = ['Age', 'email']
    # list_filter = ['Gender', "Age"]
    # list_per_page = 500
    
    # resource_class = SurveyDataAResources
# @admin.register(IntroSurveyDataA)
# class SurveyDataAAdmin(ImportExportActionModelAdmin):
#     list_display = ["id","First_name","Last_name","Gender","Age","email",
#                     "Question_1","Question_2","Question_3","Question_4",
#                     "Question_5",
#                     ]
#     search_fields = ['Frist_name', 'Age', 'email']
#     # autocomplete_fields = ['Age', 'email']
#     list_filter = ['Gender', "Age"]
#     list_per_page = 500
    
#     resource_class = SurveyDataAResources


@admin.register(SurveyUser)
class SurveyUserAdmin(admin.ModelAdmin):
    # valid_lookups = ('country')
    list_display = (
        "id", "full_name", "email", "country", "occupation", "education_level", "created", "updated", )
    list_per_page = 500
    list_filter = ("created",)
    search_fields = ('full_name', 'email', 'country', 'notify', 'created_by')
