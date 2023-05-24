import openai

prompt_template = """
You are an agent controlling a browser. You are given:

	(1) an objective that you are trying to achieve
Based on your given objective, issue whatever command you believe will get you closest to achieving your goal.
You always start on Google; you should submit a search query to Google that will take you to the best page for
achieving your objective. And then interact with that page to achieve your objective.


Here are some examples:

EXAMPLE 1:

OBJECTIVE:

login to Amazon.in with chockynaresh18@gmail.com and password is 8977821555. Add ikigai_english_book from Bestsellers, add to the cart and proceed to buy
==================================================
YOUR ANSWER:
------------------

search for amazon.in

click amazon.in

click sign in

Enter email-address "chockynaresh18@gmail.com"

Click Continue

Enter password "8977821555"

Click Sign in

search for ikigai book in english

click the best seller book

click add to Cart

click proceed to buy

close the tab



------------------



==================================================

EXAMPLE 2:


OBJECTIVE: finding a house in houston using refin.com
YOUR ANSWER:

==================================================

search redfin Houston houses

click on the first link

click on price

enter 600 thousand

click on done

open the four bed link
------------------

==================================================

given an objective that you are trying to achieve.
u give sequence of steps to achieve the task
Based on my given objective, you issue whatever command you believe will get me closest to achieving my goal.
you always start on Google; you should submit a search query to Google that will take me to the best page for achieving my objective.

Given objective, write sequence of steps to achieve the task.


------------------

OBJECTIVE: $objective
YOUR COMMAND:
"""


openai.api_key = "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"
# objective = input("What is your objective?")
file_path = "file.txt"
def get_idea_from_open_ai(objective):
        prompt = prompt_template
        prompt = prompt.replace("$objective", objective)
        response = openai.Completion.create(model="text-davinci-002",prompt=prompt, temperature=0.7, best_of=10, n=1, max_tokens=64, stop =None)
        with open(file_path, "w") as file:
             file.write(response.choices[0].text)


# get_idea_from_open_ai(objective)