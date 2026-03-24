# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
At first the game didn't have the box to type in numbers.
Bugs:
1. Hitting 'enter' doesn't actually work for submitting the guess; you need to hit the submit guess button.
2. It always tells me to go higher, I entered increasingly larger numbers and even the highest number on the range (100). Then I entered '200' and the hint still told me to go higher. This indicates either the range is incorrect, or the hints are incorrect.


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Copilot ask and agent mode within VS Code.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Moving/refactoring logic into test_game_logic.py. Verified with the agent created test cases and also played the game on the app by relaunching the streamlit. 
Moved the st.button logic to be outside of the st.form so streamlit could run properly.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Attempted to move the st.button inside the col logic and inside st.form. I believe it didn't have access to the streamlit documentation because it kept making this error after 3 prompts. I then looked at the docs myself, saw the line that was erroring based on the streamlit app page, then copy pasted those lines and gave it to the agent mode chat. Then, it fixed the issue.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
The app should run and be able to take guesses.
I decided if it was fixed if the unit tests passed.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  Initially the pytests wouldn't run because it couldn't import from logic_utils. Copilot helped resolve this by adding the code snippet below that adds the parent directory to the path of the test folder:
import sys
import os

# Add parent directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic_utils import check_guess, parse_guess, update_score, get_range_for_difficulty

One example of a test is test_guess_too_low, where we input a number that's too lower. The game's initial logic had a bug that would tell us to guess lower if a number was too low. This test ensured our hints were correct for the too low case for users.


- Did AI help you design or understand any tests? How?
It helped design tests based on the bugs we fixed earlier.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
