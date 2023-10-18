""" A simple Streamlit UI to help farmers get
certified organic and other certifications."""

# Importing the required libraries
import os
from dotenv import load_dotenv
import openai
from PIL import Image
import streamlit as st

# Load environment variables
load_dotenv()

# Set OpenAI API key from Streamlit secrets
openai.api_key = os.getenv("OPENAI_KEY2")
openai.organization = os.getenv("OPENAI_ORG2")


if "goal_selection" not in st.session_state:
    st.session_state.goal_selection = "Home"
    # Initialize chat history
if "guru_state" not in st.session_state:
    st.session_state.guru_state = "off"


def certify_organic():
    """ Steps to get certified to sell organic """
    # Create a group of radio buttons to represent the steps
    # that the user has to take to get certified organic.  
    # Depending on which radio button is selected, we will display
    # a different set of instructions.
    st.title("Organic Certification Guide")

    st.markdown("""***Note that producers or handlers who sell $5000
        per year labeled or represented as "organic" must be certified.***
            If you do not meet that threshold, [you may not need to be certified](https://www.tn.gov/agriculture/farms/produce-nursery/ag-farms-organics/organic-certification.html).
            """)
    steps = [
        "Adopt organic practices and create an Organic System Plan (OSP)",
        "Contact a certifying agent for application",
        "On-site inspection",
        "Final review by certifying agent",
        "Issuance of organic certificate"
    ]

    selected_step = st.radio("Select a step to learn more:", steps)
    st.text("")
    if selected_step == steps[0]:
        st.markdown("#### Step 1: Adopt organic practices and create OSP (Organic System Plan)")
        st.markdown("""- The farm or business [adopts organic practices](https://www.ams.usda.gov/services/organic-certification/becoming-certified).""")
        st.markdown("""**:red[There is a transition period required.  The\
                land must be free of prohibited substances for 3 years before certification.]**
                """)
        st.markdown("""- [Create an OSP (Organic System Plan)](https://www.ams.usda.gov/services/organic-certification/organic-system-plan-osp)""")
    
    elif selected_step == steps[1]:
        st.subheader("Step 2: Contact certifying agent for application")
        st.markdown(""" - Select a [USDA-accredited certifying agent](https://www.ams.usda.gov/resources/organic-certifying-agents).\
                    This agent can walk you through the application process and any associated fees.""")
        st.markdown(""" - Submit an application and fees to the certifying agent.""")
        st.markdown("""- The certifying agent reviews the application\
                    and verifies that practices comply with USDA organic regulations.
        """)

    elif selected_step == steps[2]:
        st.subheader("Step 3: On-site inspection")
        st.markdown("""
        - An inspector conducts an [on-site inspection](https://www.ams.usda.gov/reports/what-expect-when-you%E2%80%99re-inspected) of the applicant’s operation.
        """)

    elif selected_step == steps[3]:
        st.subheader("Step 4: Final review by certifying agent")
        st.write("""
        - The certifying agent reviews the application and the inspector’s report.
        - Determines if the applicant complies with the USDA organic regulations.
        """)

    elif selected_step == steps[4]:
        st.subheader("Step 5: Issuance of organic certificate")
        st.write("""
        - Once approved, the certifying agent issues the organic certificate.
        You can now begin to market your products as [certified organic](https://www.ams.usda.gov/rules-regulations/organic/labeling)
        """)

def sell_produce_and_goods():
    """ Steps to sell produce and prepared foods """
    # Create a radio button to select between selling produce and prepared foods
    st.markdown("## Selling Produce and Prepared Foods")
    st.text("")
    sell_selection = st.radio("What would you like to sell?", ("Produce", "Prepared Foods"))
    st.text("")
    if sell_selection == "Produce":
        st.markdown("**Coming Soon**")
    elif sell_selection == "Prepared Foods":
        st.markdown("""**In July of 2022**, the\
        [Tennessee Food Freedom Act](https://www.tn.gov/agriculture/consumers/food-safety/tennessee-food-freedom-act.html)\
        greatly expanded the ability of home sellers to sell prepared foods.  This has\
        streamlined the process and is simple and straightforward."""
        )
def guru_chat():
    """ Chat bot to help farmers in Middle Tennessee """
    st.text("")
    # Set a the initial prompt
    new_prompt = [{"role": "system", "content" : """
            You are an organic farming and market farm expert, with not only
            expertise in farming practices but in the business and regulatory
            aspect as well.  The user is a farmer in Tennessee who needs to ask 
            various questions about establishing their market farm.  Answer in 
            a kind, helpful, and empathetic way to the user's questions.  Keep
            your answers brief and to the point."""}]
    
    # Etablsih chat history and default model
    if "messages" not in st.session_state:
        st.session_state.messages = new_prompt
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-4-0613"


    guru_pic = Image.open("./resources/farm_guru.png")

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        if message["role"] == "assistant":
            with st.chat_message(message["role"], avatar=guru_pic):
                st.markdown(message["content"])
        elif message["role"] == "user":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("How can I help you, fellow farmer?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Load the prophet image for the avatar
        # Display assistant response in chat message container
        with st.chat_message("assistant", avatar=guru_pic):
            message_placeholder = st.empty()
            full_response = ""

        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages= [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            stream=True,
            temperature=0.75,
            max_tokens=225,
            ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})



# Create a sidebar that will present the user's with the options
st.sidebar.title("Navigation")
# Create a radio button to select the page
goal_selection = st.sidebar.radio("Goals:", ["Home", "Organic Certification", "Sell Produce and Prepared Foods", "Taxes", "Permits"], index=0)
guru_status = st.sidebar.radio("**Chat with the Farm Guru?**", ("on", "off"), index=1)
st.session_state.guru_state = guru_status


def main():
    """ Initial Landing Page """
    st.markdown("##### Welcome to Farm Guru.\
                Select an option on the sidebar to get started.")
if goal_selection == "Home":
    main()
elif goal_selection == "Organic Certification":
    certify_organic()
elif goal_selection == "Sell Produce and Prepared Foods":
    sell_produce_and_goods()

if st.session_state.guru_state == "on":
    guru_chat()
        