from langchain_community.llms import Ollama
from rich import print
import streamlit as st

llm=Ollama(model="llama3.2:1b")

def run_llm(prompt):
    response=llm.invoke(prompt)
    return response

def planner_agent(app_idea):
    prompt=f"""
    You are a senior software architect.

    Break down the following app idea into clear developement steps:
    {app_idea}

    Include:
    - Features
    - Tech stack
    - Step-by-step implementation plan
    """
    return run_llm(prompt)

def developer_agent(plan):
    prompt=f"""
    You are a python developer.
    Based on this plan:
    {plan}
     
    write clean, modular, production-ready Python code.
    """
    return run_llm(prompt)

def tester_agent(code):
    prompt=f"""
    You are a software tester.

    Analyze this code:
    {code}
     
    Identify:
    - Bugs
    - Edge cases
    - Improvements
    """
    return run_llm(prompt)

def reviewer_agent(code):
    prompt=f"""
    You are a senior code reviewer.

    Improve this code:
    {code}

    Focus on :
    - Readability
    - Performance
    - Best practices
    """
    return run_llm(prompt)

def build_app(app_idea):

    with st.status("Step 1:Planning....",expanded=True) as status:
        plan=planner_agent(app_idea)
        st.write(plan)
        status.update(label="Planning Complete.",state="complete",expanded=False)

    with st.status("Step 2:Developing....",expanded=True) as status:
        code=developer_agent(plan)
        st.code(code,language="python")
        status.update(label="Developement Complete.",state="complete",expanded=False)

    with st.status("Step 3:Testing....",expanded=True) as status:
        test_report = tester_agent(code)
        st.code(code,language="python")
        status.update(label="Testing Complete.",state="complete",expanded=False)

    with st.status("Step 4:Reviewing....",expanded=True) as status:
        final_code = reviewer_agent(code)
        st.code(code,language="python")
        status.update(label="Review Complete.",state="complete",expanded=True)

    return code


    # print("[bold cyan]Step 1:Planning....[/bold cyan]")
    # plan=planner_agent(app_idea)
    # print(plan)

    # print("\n[bold green]Step 2: Developing....[/bold green]")
    # code=developer_agent(plan)
    # print(code)

    # print("\n[bold yellow]Step 3: Testing...[/bold yellow]")
    # test_report = tester_agent(code)
    # print(test_report)

    # print("\n[bold magenta]Step 4: Reviewing...[/bold magenta]")
    # final_code = reviewer_agent(code)
    # print(final_code)

    # return final_code

st.set_page_config(page_title="AI App Builder")

st.title("AI Agent For End-to-End App Developement ")

st.write("Enter your app idea below")

idea=st.text_input(
    "What kind of app do you want to build?",
    placeholder="Enter app idea here" 
)

if st.button("Generate App",type="primary"):
    if idea.strip()=="":
        st.warning("Please enter an app idea!")

    else:
        st.subheader("Agent collaboration pipeline")
        final_output=build_app(idea)

        st.success("Final Application generated successfully")
        st.subheader("Final code output")
        st.code(final_output,language="python")



# if __name__ == "__main__":
#     idea = "Build a simple REST API for a todo app using FastAPI"
#     final_output = build_app(idea) 
