import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Product Feedback Classifier", page_icon="🤖")
st.title("Making Work Life Better: AI-Powered Feedback Analysis")
st.write("This app transforms 'messy' HR feedback into clear product insights.")

#Mock Dataset: Real-world HCM feedback
# Mock Dataset with categories
mock_data = [
    {"text": "The payroll system is so slow and clunky", "category": "Performance"},
    {"text": "I love the new onboarding process", "category": "Onboarding"},
    {"text": "The benefits portal is confusing", "category": "UX/UI"},
    {"text": "The mobile app needs improvement", "category": "Mobile"},
    {"text": "The reporting features are limited", "category": "Features"},
    {"text": "I can't find the 'Request Time off' button on the mobile app", "category": "Mobile"}
]

#  UI for data Input
st.subheader("Step 1: Ingest Feedback Data")
if st.button("Load Sample HR Feedback"):
    df = pd.DataFrame(mock_data)
    st.session_state['data'] = df
    st.success("Sample data loaded successfully!")

#Simulated AI classification
if 'data' in st.session_state:
    st.subheader("Step 2: AI-Powered Classification")

    if st.button("Run AI Analysis"):
        st.write("## AI Analysis Complete!")
        st.write("Your feedback has been categorized into actionable insights.")
        st.table(st.session_state['data'])

        # Calculate insights from data
        if 'category' in st.session_state['data'].columns:
            category_counts = st.session_state['data']['category'].value_counts()
            top_category = category_counts.idxmax()
            top_count = category_counts.max()
            total = len(st.session_state['data'])
            percentage = int((top_count / total) * 100)
            
            st.info(f"Product Insight Summary: {percentage}% of feedback focuses on {top_category} improvements.")
        else:
            st.warning("No category data available for analysis.")

# Analytics Integration
st.subheader("Step 3: Roadmap Impact")
st.write("Priority Level: High (Based on 150+ users impacted)")

# Data Visualization
if 'data' in st.session_state:
    st.write("---")
    st.subheader("Product Area Insights")
    
    try:
        if 'category' in st.session_state['data'].columns:
            category_counts = st.session_state['data']['category'].value_counts()
            st.bar_chart(category_counts)
            
            top_issue = category_counts.idxmax()
            st.info(f"💡 **Strategic Insights**: The **{top_issue}** module is receiving the most feedback. Recommend prioritizing this in the Summer 2026 roadmap.")
        else:
            st.warning("No category data available for visualization.")
    except Exception as e:
        st.error(f"Error generating visualization: {str(e)}")