# Agent Selector

**Agent Selector** is a simple Python script to select agents from a list of agents stored in [data.json](https://github.com/Ganofins/support-genie/blob/master/data.json) file.

I created here data.json file, just for easiness in entering list of agents and mode of agent selection. I have created a class AgentSelector, which takes list of issues with their roles and ID, in order to assign a issue to specific agents based on their agent selection mode which can be

- available
- least busy
- random

can be defined in data.json file.

<hr>

##### to run
```
git clone https://github.com/Ganofins/support-genie.git

cd agent_selector

python3 main.py
```