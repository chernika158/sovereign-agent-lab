"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach" 
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
The model selected correct answers in all three case. However, the format 
influenced the answer.The plain format led to chosing The Haymarket which
apperas closer to the end of the prompt, while XML and sandwich formats 
led to chosing The Albanach option which is in the very begining of the list 
of the venues.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
The Holyrood Arms would theoretically be the most dangerous distractor, as it
satisfies two of the three constraints (capacity 160, vegan yes) and fails only
on status=full making it nearly identical to the correct answer. However, in
practice neither distractor caused the 70B model to fail. All three conditions
remained correct, suggesting the model reliably evaluated all constraints even
with near-miss options present.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
the 8B model returned The Haymarket Vaults for all three conditions. This is 
different from the 70B's preference for The Albanach under XML/sandwich formats. 
This suggests the 8B model may exhibit stronger recency bias (Haymarket appears 
later in the list), while the 70B's XML and sandwich responses showed primacy bias 
(Albanach appears first). That both models answered correctly despite different 
biases illustrates that on clean, short datasets, format effects shift which 
correct answer is chosen rather than causing outright failures.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matters most when the signal-to-noise ratio is low, 
that is, when distractors are plausible, the context is long, or the model is smaller 
and less capable of sustained attention. In those conditions, structural cues like XML 
tags and query repetition (in sandwich) guide the model's attention toward the task. 
On strong models with clean, short data, format still influences which correct answer 
is selected but doesn't determine whether the model succeeds. 
The risk in real agent systems is that retrieved context is rarely clean or short,
 making these formatting choices genuinely important .

"""
