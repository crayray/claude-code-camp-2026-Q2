# Preweek Technical Documentation

## Technical Goal
The technical goal of preweek explore is to determine how well do Agent Architectures fit our business use-case. 

[Ref 1] Examples of Agent architectures that scale with effort: 
    - An Agent file with referenced files
    - Agent skills driven by main agent
    - Filesystem subagent driven by a coding hardnes or coding agent SDK
    - AI workflow automation platform
    - Use a generic AI Agent SDK that leverages plug and plays generic AI packages
    - Use low level first-party LLM SDKs to write out own agentic loop
    - Use REST APIs directly, write our own agentic loop
         - The agentic loop is model-driven orcestration with middlewarte programmatic guidance
         - The agentic loop is code driven orchestration

## Technical Uncertainty
- I'm uncertain how to teach the agent how to more intelligently navigate the game and world. 
      - How do we build a graph or map of the world that the agent can access and remember where it's location is? 
-  We're working with different architectures and there's technical uncerataintly about the pros and cons of each architecture. 
- I'm uncertain if a coding hardnesses loop is effective enough to drive a non-coding workload. 
- I'm uncertain if AI model's thinking mode and other intelligent parameters is sufficient enough to hold memory and drive decisions for our task. 
- I'm uncertain that a coding harness can interact with a MUD without an interface or SDK or manage the telnet session

## Technical Hypothesis
 - Based on [Ref 1] i think we'll have issues with the coding harness driving the MUD without an interface bc we don't have a a defined API, we are driving commands over a protocol we need to live monitor.

 - I think we'll need an interface because managing a long-lived telnet session may prove difficult. 

- I think the only agent architecture able to drive the our use case will be where we implement a specialized agentic loop, as I think memory will not be capable enough to remember and navigate the MUD world. 

 - I think we need to roll our own agent without an SDK bc generic primitives for observabitily , for memory and our use-case will require specialized implementations. ANd we want to connect broadly with all frontier models and many SDKs will lack one of them. 


## Technical Observations 
 - I used Cursor as opposed to Claude Code - Comparing how it navigated prompts and tooling, I felt that the Cursor harness performed better than Claude Code - fewer requests for approval, fewer shell commands, and it made better architecural decisions on how to interact with the MUD. 
 - An agent.md file could not connect to the MUD, it could produce scripts but it was unreliable in creating a connection to the MUD and needed knowledge of the deterministic TUI of the MUD. 
  - Skills and subagents performed pretty well - they were able to play the MUD but not efficiently or at a high level - I got the sense the agent was stubmbling blindly through the world. 
   - The Skills and agents become hyper focused on a single goal and working towards it, instead of asking for more information or taking a step back to prioritize next steps. 
 - Using MD files where the agent updates it was not effective as the same player would be in a specific location and when a new task is presented, state is not accurately captured. It stored brittle navigation paths as well, navigating without a mental map. We may need a graph database to provide our own agent with the map. 


## Technical Conclusions
- Skills and Subagents are capable of driving MUD
- We do need specialized memory for map navigation and world data
- We opened a new technical use case of if we should have our agent handle multiple sessions of multiple players playing at the same time since co-op is a common factor in MUDS which we forgot to consider in our design. 
- We could not explore n8n completely due to technical restraints 
- Implementing our own loops remains technically unceratin and needs to be explored in more detail in week 1. 
- Wihtout a customized agentic loop the agents could not perform exploration goals efficiently - we need modes and personas about how indibidual palyers play. It did not have any meta or journey player strategies. 

## Key Takeaway
When we have a specialized use-case like playing a MUD we likely cannot leverage generic SDKs for Agents bc we need specialized tooling and agentic loops. 

We may also need to build some tooling - like a knowledge graph for our custom agent to use to navigate the world. 
