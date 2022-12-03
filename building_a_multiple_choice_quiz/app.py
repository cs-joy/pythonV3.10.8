from Question import Questions

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magneta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Questions(question_prompts[0], "a"),
    Questions(question_prompts[1], "c"),
    Questions(question_prompts[2], "b")
]