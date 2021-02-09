from django.shortcuts import render
from resolver.models import JobDataModel
from resolver.apps import ResolverConfig

# Create your views here.
def index(request):
    save_models_to_db()

    job_source_data = ResolverConfig.job_board_data
    # print(job_source_data)
    job_board_list = job_source_data["job_boards"]
    
    context = {"job_board_list": job_board_list}
    return render(request, 'resolver/index.html', context)

def job_source(request):
    save_models_to_db()
    return render(request, "resolver/jobsource.html")

# makes the model from the all the resolved opportunities and saves it in the db, if db is empty
def save_models_to_db():
    if JobDataModel.objects.exists():
        return

    jobdataModels = []
    for opp in ResolverConfig.resolved_opportunities:
        jobdataModels.append(JobDataModel(opp["ID (primary key)"], opp["Job Title"], opp["Company Name"], opp["Job URL"], opp["Job Source"]))
    
    JobDataModel.objects.bulk_create(jobdataModels)
