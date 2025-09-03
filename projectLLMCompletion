CSCI 1010 -- Lab Exercise for October 18, 2024

Hello!

In this lab, the goal is to explore modern “LLMs” and explore a little deeper how they work, and what some of their failure modes are.

We talked in the first lecture about GPT4, and how it is trained to predict the next word, but in reality today’s models (GPT4, Claude, Google Bard/Gemini) put a lot of infrastructure around that, including hidden instructions to both make the model do more of what you ask, be more effective at chatting with you, and aligning its responses acceptable norms.

Today, we are going to explore earlier models that are closer to seeing “what was the next word”.  You can choose one of the following model styles:

Style 1: Long text completion::

https://textsynth.com/completion.html 
https://huggingface.co/distilbert/distilgpt2 (type in the box by: “Inference API”)
[If you feel confident in downloading software to your own computer, you could try ollama or gpt4all and download
[You can suggest something here!]

Style 2: Short text completion

This model predicts exactly the next word, and gives the probability that (it believes) each work would be next.

https://huggingface.co/spaces/Bhagu69/next-word-predictor

Your goal is to explore ways that they can give both correct and incorrect answers in surprising ways. The goal is to give you familiarity with these tools and some understanding of the ways that they can make mistakes.

The endpoint of the lab is a blog post that you will write to share what you have learned.  This should be posted to your GWU blog.  When you are done, you are to submit your blog post here:

SUBMISSION LINK: https://forms.gle/ZWnTYV98yEJm6V6b6 (note, this is a new link)

Details:


Option 1: Long form text completion:

Choose a model from the list:		
https://textsynth.com/completion.html
https://huggingface.co/distilbert/distilgpt2 (type in the box by: “Inference API”)
[If you feel confident in downloading software to your own computer, you could try ollama or gpt4all and download a simple model (that doesn’t have chat or instruct in its name)
[You can suggest something here! As long as it is a text completion model]

Start the text completion model with a sample prompts, including (but not exactly) those below:
Short, factual statements (e.g., "The capital of France is...")
Creative writing prompts (e.g., "Once upon a time...")
Open-ended philosophical questions (e.g., "What is the meaning of life?")
Ethical dilemmas or opinion-based questions (e.g., "Should self-driving cars be used on public roads?")
Write your blog post so it is clear what you put as the prompt and what the model answered, then give your own analysis of how well the modelNext Word Fun - a Hugging Face Space by Bhagu69 did, when it succeeded, when it failed, and your best explanation about why.

Option 2: Short text completion

Consider this model: https://huggingface.co/spaces/Bhagu69/next-word-predictor

Start the text completion model with a sample prompts, including (but not exactly) those below:
Short, factual statements (e.g., "The capital of France is...")
Obvious sequences, “one two three four five” 
One thing that you will see reflects Dr. Hwa’s comment that some words (“a”, “the”) are very common, see if you can find prompts that have more interesting words as top answers.
Write a blog post with some examples where the next word prediction is correct, some where it is wrong, some where it is “silly” or not grammatical.  Can you find a case where the model has two top predictions that are (a) interesting, (b) different, and (c) have pretty similar probabilities?
