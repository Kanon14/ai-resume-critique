from apify_client import ApifyClient
import os
from dotenv import load_dotenv
load_dotenv()

apify_client = ApifyClient(os.getenv("APIFY_API_TOKEN"))


# Fetch Linkedin jobs based on search query and location
def fetch_linkedin_jobs(search_query, location="malaysia", rows=30):
    run_input = {
            "title": search_query,
            "location": location,
            "rows": rows,
            "proxy": {
                "useApifyProxy": True,
                "apifyProxyGroups": ["RESIDENTIAL"],
            }
        }
    run = apify_client.actor("BHzefUZlZRKWxkTck").call(run_input=run_input)
    jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs


# Fetch Jobstreet jobs based on search query and location
# def fetch_jobstreet_jobs(search_query, place="kuala lumpur", country="malaysia", rows=30):
#     run_input = {
#         "keyword": search_query,
#         "place": place,
#         "sort_by": "Relevance",
#         "work_type": "Any",
#         "remote_option": "Any",
#         "maxitems": rows,
#         "country": country
#     }
#     run = apify_client.actor("iIjDnfHjkzORmnIN6").call(run_input=run_input)
#     jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
#     return jobs