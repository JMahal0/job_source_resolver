from django.shortcuts import render
from resolver.models import JobDataModel
from resolver.apps import ResolverConfig

# Create your views here.
def index(request):
    pass


# makes the model from the all the resolved opportunities and saves it in the db
def load_models():
    if ResolverConfig.resolved_opportunities["loaded"] == True:
        return

    for opp in ResolverConfig.resolved_opportunities["opportunities"]:
        model = JobDataModel(opp["ID (primary key)"], opp["Job Title"], opp["Company Name"], opp["Job URL"], opp["Job Source"])
        model.save()
