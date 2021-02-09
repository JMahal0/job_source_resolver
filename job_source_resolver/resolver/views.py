from django.shortcuts import render
from resolver.models import JobDataModel
from resolver.apps import ResolverConfig

# Create your views here.
def index(request):
    save_models_to_db()

    job_source_data = ResolverConfig.job_board_data
    job_board_list = job_source_data["job_boards"]
    
    context = {"job_board_list": job_board_list}
    return render(request, 'resolver/index.html', context)

def job_source(request):
    save_models_to_db()

    query_string = request.GET.urlencode()
    job_source = query_string[10:]

    job_details_list = []
    jobs_with_correct_source = JobDataModel.objects.filter(job_source=job_source)
    if jobs_with_correct_source.exists():
        job_details_list = jobs_with_correct_source

    context = {"job_details_list" : job_details_list, "source" : job_source}
    return render(request, "resolver/jobsource.html", context)

# makes the model from the all the resolved opportunities and saves it in the db, if db is empty
def save_models_to_db():
    if JobDataModel.objects.exists():
        return

    jobdataModels = []
    for opp in ResolverConfig.resolved_opportunities:
        jobdataModels.append(JobDataModel(opp["ID (primary key)"], opp["Job Title"], opp["Company Name"], opp["Job URL"], opp["Job Source"]))
    
    JobDataModel.objects.bulk_create(jobdataModels)
