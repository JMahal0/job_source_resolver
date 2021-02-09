from django.test import TestCase
from resolver.apps import ResolverConfig

class ResolverConfigTestCase(TestCase):

    def test_determine_job_source_job_board(self):
        company_name = "Glassdoor"
        job_board_data = {"job_boards" : [{"name" : company_name, "root_domain" : "glassdoor.com"}, {"name" : "Google", "root_domain" : "google.com"}]}
        opportunities = {"Job URL" : "glassdoor.com/foobar", "Company Name" : "Foobar"}
    
        self.assertEqual(company_name, ResolverConfig.determine_job_source(opportunities, job_board_data))
    
    def test_determine_job_source_company_website(self):
        job_board_data = {"job_boards" : [{"name" : "Glassdoor", "root_domain" : "glassdoor.com"}, {"name" : "Google", "root_domain" : "google.com"}]}
        opportunities = {"Job URL" : "Foobar.com/jobs", "Company Name" : "Foobar"}
    
        self.assertEqual("Company Website", ResolverConfig.determine_job_source(opportunities, job_board_data))

    def test_determine_job_source_unknown(self):
        job_board_data = {"job_boards" : [{"name" : "Glassdoor", "root_domain" : "glassdoor.com"}, {"name" : "Google", "root_domain" : "google.com"}]}
        opportunities = {"Job URL" : "www.wackyjobs.co.uk/foobar", "Company Name" : "Foobar"}
    
        self.assertEqual("Unknown", ResolverConfig.determine_job_source(opportunities, job_board_data))

