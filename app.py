import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

# Application setup
st.set_page_config(page_title="testapp10", layout="wide")

# Helper functions
def simulate_cod(prompt, model, steps_limit=5):
    """
    Simulate the Chain-of-Draft (CoD) technique by processing the prompt
    and generating minimalistic reasoning steps.
    """
    steps = []
    remaining = prompt
    for _ in range(steps_limit):
        # Simulate a minimal reasoning step
        draft_step = f"Step {_+1}: Processed '{remaining[:10]}...'"
        steps.append(draft_step)
        remaining = remaining[10:]
        if not remaining:
            break
    # Final answer simulation
    final_answer = f"Final Answer: {len(prompt)}"
    return steps, final_answer

def simulate_cot(prompt, model):
    """
    Simulate the Chain-of-Thought (CoT) technique by generating verbose reasoning steps.
    """
    steps = [f"Step 1: Analyzing the problem..."]
    for i in range(2, 6):
        steps.append(f"Step {i}: Continuing analysis... (verbose)")
    final_answer = f"Final Answer: {len(prompt)}"
    return steps, final_answer

# Sidebar configuration
st.sidebar.header("Configuration")
model_selection = st.sidebar.selectbox("Select LLM Model", ["GPT-4o", "Claude 3.5 Sonnet"])
prompt_input = st.sidebar.text_area("Input Prompt", "Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?")
steps_limit = st.sidebar.slider("CoD Steps Limit", 1, 10, 5, help="Limit the number of steps in CoD")

# Main panel
st.title("Chain of Draft vs. Chain of Thought")
st.markdown("### Explore concise reasoning with Chain of Draft (CoD) compared to verbose Chain of Thought (CoT)")

# Display input prompt
st.subheader("Input Prompt")
st.write(f"Model: {model_selection}")
st.write(prompt_input)

# Simulate CoD
st.subheader("Chain-of-Draft Simulation")
cod_steps, cod_final_answer = simulate_cod(prompt_input, model_selection, steps_limit)
st.write("**Steps:**")
for step in cod_steps:
    st.write(step)
st.write(f"**{cod_final_answer}**")

# Simulate CoT
st.subheader("Chain-of-Thought Simulation")
cot_steps, cot_final_answer = simulate_cot(prompt_input, model_selection)
st.write("**Steps:**")
for step in cot_steps:
    st.write(step)
st.write(f"**{cot_final_answer}**")

# Comparison Visualization
st.subheader("Token Usage Comparison")
labels = ['CoD', 'CoT']
tokens_usage = [len(cod_steps), len(cot_steps)]
fig, ax = plt.subplots()
ax.bar(labels, tokens_usage, color=['blue', 'orange'])
ax.set_ylabel('Number of Steps')
ax.set_title('Comparison of Token Usage')
st.pyplot(fig)

# Download results
st.subheader("Download Results")
if st.button("Download CoD Steps as CSV"):
    cod_df = pd.DataFrame({'Steps': cod_steps + [cod_final_answer]})
    cod_df.to_csv('cod_steps.csv', index=False)
    st.success("CoD steps downloaded as cod_steps.csv")

# Simulation capabilities
st.subheader("Simulation Capabilities")
st.markdown("Use the sliders and inputs on the sidebar to simulate different scenarios and observe the impact on CoD and CoT performance.")

# Conclusion
st.subheader("Conclusion")
st.markdown("Chain of Draft (CoD) provides a more concise and efficient alternative to Chain of Thought (CoT), maintaining accuracy with reduced verbosity.")