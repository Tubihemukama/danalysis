import streamlit as st


st.set_page_config(
    page_title="data-analysis-app",
    page_icon= "🖐️"
)
st.title("Magnify Analysis")
st.sidebar.success("Select page Above")
st.markdown("""
<style>
    body {
        background-color: #002060;
        color: #333333;  # Change text color to dark gray
    }
    </style>       




<div style="
    background-color: #002060;
    border: 1px solid #002060;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 2px 2px 6px rgba(0,0,0,0.05);
    font-family: 'Segoe UI', sans-serif;
    color: #FFFFFF;
    ">
    <h4 style="color: #FFFFFF; font-weight: bold;"> This App will do the following</h4>
    <ul>
        <li>📂 Upload Data</li>
        <li>🧹 Wrangle Data</li>
        <li>📊 Visualize Insights</li>
        <li>📈 Analyze Trends</li>
    </ul>
</div>
""", unsafe_allow_html=True)



# Add a title or description
st.write("We'd love to hear your feedback! Please let us know what to improve in the app.")

# Create a text area for user input
feedback = st.text_area("What would you like to see improve in this app?", "")

# Add a button to submit feedback
if st.button("Submit Feedback"):
    if feedback:
        # Save the feedback to a text file
        with open("user_feedback.txt", "a") as f:
            f.write(feedback + "\n")
        
        # Acknowledge the user
        st.write("Thank you for your feedback! We'll take it into consideration.")
    else:
        st.write("Please enter some feedback before submitting.")




