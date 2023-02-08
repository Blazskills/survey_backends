from import_export import resources
from surveyapp.models import IntroSurveyDataA


class SurveyDataAResources(resources.ModelResource):
    class Meta:
        model = IntroSurveyDataA
        # fields = (
        #     "id", "First_name", "Last_name", "Gender", "Age", "email",
        #     "Question_1", "Question_2", "Question_3", "Question_4",
        #     "Question_5"
        # )
