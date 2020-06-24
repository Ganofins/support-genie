import json
import random

#to read agents data from data.json file, just to ease the usage
with open("data.json", "r") as fp:
    agent_details = json.loads(fp.read())


class AgentSelector():
    '''Class to select agent from based on their roles, availability and the selection mode defined in data.json file'''
    selected_agents = []

    def __init__(self, issues:list):
        self.issues = issues

    def select_agent(self):
        filtered_agents = []
        for each_issue in self.issues:
            for each_agent in agent_details["agents"]:
                    if any(item in each_issue["roles"] for item in each_agent["roles"]) and each_agent["is_available"] == True:
                        filtered_agents.append(each_agent)

            if agent_details["selection_mode"] == "all_available":
                self.selected_agents.append({"issue_id" : each_issue["id"], "present_to_agent": filtered_agents})

            elif agent_details["selection_mode"] == "least_busy":
                time = 0
                for each_agent in filtered_agents:
                    if each_agent["available_since"] > time:
                        time = int(each_agent["available_since"])
                        selected_agent = each_agent
                self.selected_agents.append({"issue_id" : each_issue["id"], "present_to_agent": selected_agent})

            elif agent_details["selection_mode"] == "random":
                self.selected_agents.append({"issue_id" : each_issue["id"], "present_to_agent": random.choice(filtered_agents)})

        return self.selected_agents


if __name__ == "__main__":
    select_agent = AgentSelector([{"id":"1", "roles":["sales","support"]}, {"id":"2", "roles":"support"}])
    print(select_agent.select_agent())