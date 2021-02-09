from django.apps import AppConfig
import json
import csv


class ResolverConfig(AppConfig):
    name = 'resolver'

    INPUT_CSV_PATH = "resolver/resources/job_opportunities.csv"
    JOB_BOARD_DATA_PATH = "resolver/resources/jobBoards.json"

    resolved_opportunities = []
    job_board_data = None


    def ready(self):
        job_opportunities = self.read_job_opportunity_csv(self.INPUT_CSV_PATH)
        ResolverConfig.job_board_data = self.load_job_board_data(self.JOB_BOARD_DATA_PATH)

        for opportunity in job_opportunities:
            job_source = self.determine_job_source(opportunity, ResolverConfig.job_board_data)
            opportunity["Job Source"] = job_source
        
        ResolverConfig.resolved_opportunities = job_opportunities
        # self.part_e()
    
    # read and parse csv file and this method return a list of opportunities (dicts)
    def read_job_opportunity_csv(self, path):
        csv_file = open(path)
        opportunities = []

        job_opportunity_reader = csv.DictReader(csv_file)

        for opportunity_line in job_opportunity_reader:
            opportunities.append(opportunity_line)

        return opportunities
            

    # opportunity is a dict and this method returns a string
    # added classmethod to allow for unit testing without needing to mock
    @classmethod
    def determine_job_source(self, opportunity, job_board):
        board_list = job_board["job_boards"]
        for board in board_list:
            if board["root_domain"] in opportunity["Job URL"]:
                return board["name"]

        if opportunity["Company Name"] in opportunity["Job URL"]:
            return "Company Website"
        else:
            return "Unknown"

    def load_job_board_data(self, path):
        f = open(path)
        job_boards = json.load(f)
        f.close()
        return job_boards

    def part_e(self):
        fields = ["ID (primary key)", "Job Title", "Company Name", "Job URL", "Job Source"]
        filename = "complete_job_source_resolution_data.csv"
        
        with open(filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)

            for opp in ResolverConfig.resolved_opportunities:
                row = [opp["ID (primary key)"], opp["Job Title"], opp["Company Name"], opp["Job URL"], opp["Job Source"]]
                csvwriter.writerow(row)
