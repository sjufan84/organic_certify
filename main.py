""" A simple Streamlit UI to help farmers get
certified organic and other certifications."""

# Importing the required libraries
import streamlit as st

if "goal_selection" not in st.session_state:
    st.session_state.goal_selection = "Home"

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

    st.header("Steps to Become Certified Organic")

    steps = [
        "Adopt organic practices and create an Organic System Plan (OSP)",
        "Contact a certifying agent for application",
        "On-site inspection",
        "Final review by certifying agent",
        "Issuance of organic certificate"
    ]

    selected_step = st.radio("Select a step to learn more:", steps)

    if selected_step == steps[0]:
        st.markdown("#### Step 1: Adopt organic practices and create OSP (Organic System Plan)")
        st.markdown("""- The farm or business [adopts organic practices](https://www.ams.usda.gov/services/organic-certification/becoming-certified).""")
        st.warning("""**Note:  There is a transition period required.  The\
                land must be free of prohibited substances for 3 years before certification.**
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




# Create a sidebar that will present the user's with the options
st.sidebar.title("Navigation")
# Create a radio button to select the page
goal_selection = st.sidebar.radio("Goals:", ("Home", "Organic Certification", "Sell produce\
                            and prepared foods", "Taxes", "Permits"), index=0)
# Set the session state to the selected page
st.session_state.goal_selection = goal_selection


def main():
    """ Initial Landing Page """
    st.markdown("##### Welcome to Farm Guru.\
                Select an option on the sidebar to get started.")
    

if __name__ == "__main__":
    if st.session_state.goal_selection == "Home":
        main()
    elif st.session_state.goal_selection == "Organic Certification":
        certify_organic()
    
