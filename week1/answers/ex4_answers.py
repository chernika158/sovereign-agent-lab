"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = [
    "search_venues",
    "get_venue_details"
  ]

QUERY_1_VENUE_NAME    = "The Haymarket Vaults"
QUERY_1_VENUE_ADDRESS = "1 Dalry Road, Edinburgh"
QUERY_2_FINAL_ANSWER  = """No venues found for 300 people with vegan options.
                     Agent suggested relaxing capacity or removing vegan requirement."""

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True

EX4_EXPERIMENT_RESULT = """
Before the change, search_venues returned two matches for Query 1: The Albanach (capacity 180)
and The Haymarket Vaults (capacity 160). After changing The Albanach's status to 'full' in,
it was automatically excluded and only The Haymarket Vaults was returned.
Oone data change in the server propagated instantly to the agent's behaviour.
Query 2 was unaffected in both runs.
"""


# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 283    # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 202   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP means the agent discovers tools at runtime rather than importing them at code level.
When I changed The Albanach's status in mcp_venue_server.py, the agent's behaviour changed
instantly without touching the client code. Beyond separation of concerns, it means a second
agent can connect to the same server and see the same data,
so venue availability never goes out of sync between the two agents.
"""

# ── Week 5 architecture ────────────────────────────────────────────────────
# Describe your full sovereign agent at Week 5 scale.
# At least 5 bullet points. Each bullet must be a complete sentence
# naming a component and explaining why that component does that job.

WEEK_5_ARCHITECTURE = """
for the upcomig week
- FILL ME IN
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
LangGraph suits the research task and Rasa CALM suits the confirmation call, and swapping
them would feel wrong for specific reasons observed in this homeworl. In Exercise 2 and 4,
the LangGraph agent improvised when asked about trains it had no tool for, it suggested
National Rail and ScotRail unprompted. That flexibility is useful for open-ended research
but dangerous for a booking call where every step must be auditable. Rasa CALM, by contrast,
always collected guest_count, vegan_count, and deposit in order before running the Python
validation i.e. no improvisation, no skipped steps. If you swapped them, a LangGraph confirmation
agent might accept a booking without checking all three constraints, while a Rasa research
agent could never answer a question outside its defined flows, making it useless for
the kind of exploratory venue search Exercise 4 demonstrated.
"""
