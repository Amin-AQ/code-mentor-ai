import openai
import random
from datasets import load_dataset

openai.api_key = "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"

def select_random_problem(difficulty,language):
    """Select a random problem from the dataset's training split filtered by difficulty."""
    # Load the LeetCode dataset
    dataset = load_dataset("greengerong/leetcode")
    difficulty = difficulty.replace('Novice','Easy').replace('Intermediate','Medium').replace('Expert','Hard')
    # Filter out problems with a valid 'difficulty' field and match the chosen difficulty
    problems = [p for p in dataset['train'] if p['difficulty'] and p['difficulty'].lower() == difficulty.lower()]
    language = language.replace('cpp','c++')
    if not problems:
        raise ValueError(f"No problems found for difficulty level '{difficulty}'.")
    problem = random.choice(problems)
    solution = problem.get(language.lower())
    return problem, solution


def generate_hint(problem, conversation_history, language):
    """Generate a hint for the user based on the current conversation history."""
    language = language.replace('cpp','c++')
    prompt = (
        f"Problem: {problem['title']} (Difficulty: {problem['difficulty']})\n"
        f"{problem['content']}\n\n"
        f"Conversation History:\n{conversation_history}\n\n"
    )

    system_prompt = (
        f"You are a helpful coding mentor. Your task is to guide the user step by step in solving coding problems. "
        f"Provide hints based on the solution approach that uses {language}. "
        f"Only provide the **next immediate step** the user should take without revealing further parts of the solution. "
        "The user does not have access to the complete solution. Guide them as if you are a mentor providing one step at a time to help them progress."
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ]
    )

    hint = response.choices[0].message['content']
    return hint