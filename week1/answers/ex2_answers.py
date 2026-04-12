"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = ["check_pub_availability", "check_pub_availability", "calculate_catering_cost", "get_edinburgh_weather", "generate_event_flyer"]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = True

TASK_A_NOTES = ""   # optional — anything unexpected

# ── Task B ─────────────────────────────────────────────────────────────────

# Has generate_event_flyer been implemented (not just the stub)?
TASK_B_IMPLEMENTED = None   # True or False

# The image URL returned (or the error message if still a stub).
TASK_B_IMAGE_URL_OR_ERROR = "https://pictures-storage.storage.eu-north1.nebius.cloud/text2img-4a759a56-1789-4b02-86d9-f8b3669a0c11_00001_.webp"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = """A sleek, modern event flyer for 'Edinburgh AI Meetup, tech professionals, modern venue'. 
                        Venue: The Haymarket Vaults, Edinburgh, Scotland. Capacity: 160 guests. Visual style: 
                        dark navy and gold color palette, atmospheric Scottish pub interior, warm amber lighting, 
                        exposed stone walls, polished wood. Typography: bold sans-serif headline 'AI MEETUP EDINBURGH' 
                        centered at top, clean white subtext with venue name and guest count below. Mood: professional, 
                        innovative, intimate. No people, no faces. Photorealistic. 16:9 landscape format.\""""

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
Okay, let's see. The user wanted to check The Bow Bar for 160 vegan guests. The tool response says the capacity is 80, which is less than the required 160. So it doesn't meet the capacity constraint. The vegan requirement is met, but since the capacity isn't, the overall status is "full" and meets_all_constraints is false.

Now, the user's instruction was to check another venue if The Bow Bar doesn't work. The next step is to try another pub. The known venues is The Albanach
"""

SCENARIO_1_FALLBACK_VENUE = "The Albanach"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False   # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
Okay, let's see. The user is looking for a venue in Edinburgh that can accommodate 300 people with vegan options. 
They provided a list of known venues: The Albanach, The Haymarket Vaults, The Guilford Arms, and The Bow Bar.
 I checked each one using the check_pub_availability function.\n\nThe Albanach has a capacity of 180, 
 which is too small. The Haymarket Vaults can only hold 160, also too small. The Guilford Arms has 200 capacity but 
 doesn't offer vegan options. The Bow Bar has 80 capacity and vegan options but is already full. None of the venues
  meet both the capacity and availability requirements. The user might need to look for other options outside the 
  provided list or adjust their requirements.\n</think>\n\nNone of the known Edinburgh venues can accommodate 300 
  guests with vegan options. The closest options have:\n- The Albanach (180 capacity, vegan available)
  \n- The Haymarket Vaults (160 capacity, vegan available)\n- The Guilford Arms (200 capacity, no vegan)
  \n- The Bow Bar (80 capacity, vegan but full)\n\nWould you like to:\n1. Adjust guest count or dietary requirements?
  \n2. Search for alternative venues outside this list?\n3. Get help with a smaller-scale event?
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False   # True or False

SCENARIO_3_RESPONSE = """Okay, the user is asking about the last train from Edinburgh Waverley to London tonight.
 Let me check the tools provided.\n\nLooking at the functions available: check_pub_availability, get_edinburgh_weather,
  calculate_catering_cost, generate_event_flyer. None of these are related to train schedules. 
  The functions are for checking pub availability, weather, catering costs, and generating flyers. 
  \n\nSince there's no tool for train times, I can't use any of the provided functions. 
  I need to inform the user that I don't have access to that information. 
  I should apologize and suggest they check a train service website or app for the most accurate details.\n</think>
  \n\nI don't have access to real-time train schedules or transportation data. For the most accurate information about 
  the last train from Edinburgh Waverley to London, I recommend checking:
  \n1. The ScotRail website/app
  \n2. National Rail Enquiries (www.nationalrail.co.uk)
  \n3. Train service apps like Citymapper or Google Maps
\n\nWould you like me to help with anything related to Edinburgh venues, weather, or event planning instead?"""

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
The real assistant wouldn't be limited in the tools it may accesss.
The agent listed the right websites where this information could be found,
but it simply didn't have an acccesss to them. The agent thought proccess
shows it's potential to tackle this kind of requests.
"""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
graph TD;
    __start__([__start__]):::first
    agent(agent)
    tools(tools)
    __end__([__end__]):::last
    __start__ --> agent;
    agent -.-> __end__;
    agent -.-> tools;
    tools --> agent;
    classDef default fill:#f2f0ff,line-height:1.2
    classDef first fill-opacity:0
    classDef last fill:#bfb6fc
"""

# Compare the LangGraph graph to exercise3_rasa/data/rules.yml. Min 30 words.
TASK_D_COMPARISON = """
FILL ME IN
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
FILL ME IN
"""
