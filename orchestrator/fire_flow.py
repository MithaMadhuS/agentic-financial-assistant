from agents.fire_agent import FireAgent
from agents.advisor_agent import AdvisorAgent

def run_fire(query):
    fire_agent = FireAgent()
    advisor = AdvisorAgent()
    result = fire_agent.run(query)
    return advisor.run(result)
