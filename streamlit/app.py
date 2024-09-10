import streamlit as st

from challange_descrpition import show_overview, show_completed_tasks, show_next_steps
from task1 import show_task_1_description
from tesk2 import show_task_2_description
from task3 import show_task_3_description
from task4 import show_task_4_description
from task5 import show_task_5_description


# Initial page config
st.set_page_config(
    page_title='KAIM Week 2',
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    selected_task = app_sidebar()
    app_body(selected_task)
    
    st.markdown('---')
    st.header('Contact Information')
    st.markdown('**Name:** Getachew Getu Enyew')
    st.markdown("**GitHub:** [Getachew's GitHub](https://github.com/Getachew0557)")
    st.markdown("**LinkedIn:** [Getachew's LinkedIn](https://www.linkedin.com/in/getachew-getu-9534041a4/)")
    

# Sidebar
def app_sidebar():
    st.sidebar.header('KAIM Week 2 Challenges')
    
    tasks = ['Challenge Description', 'User Overview Analysis', 'User Engagement Analysis', 'Experience Analysis', 'Satisfaction Analysis', 'Dashboard Development']
    selected_task = st.sidebar.selectbox('Select a task', tasks, key='task_selector')
    
    st.sidebar.markdown('---')
    st.sidebar.header('Contact Information')
    st.sidebar.markdown('**Name:** Getachew Getu Enyew')
    st.sidebar.markdown('Msc in Computer Engineering ')
    st.sidebar.markdown('**GitHub:** [Getachew Getu GitHub](https://github.com/Getachew0557)')
    st.sidebar.markdown('**LinkedIn:** [Getachew LinkedIn](https://www.linkedin.com/in/getachew-getu-9534041a4)')
    
    return selected_task

# Main body
def app_body(selected_task):
    st.title('KAIM Week 2 Challenges')
    
    if selected_task == 'Challenge Description':
        
        st.title("Enhancing Telecom Business Insights through Comprehensive Data Analysis and Machine Learning Techniques for Optimal Investment Decisions")
        show_overview()
        show_completed_tasks()
        show_next_steps()
    
    elif selected_task == 'User Overview Analysis':
        st.title('Task 1 - User Overview Analysis Report')
        
        show_task_1_description()


    
    elif selected_task == 'User Engagement Analysis':

        st.title('Task 2 - User Engagement Analysis Report')

        show_task_2_description()

    
    elif selected_task == 'Experience Analysis':

        st.title('Task 3 - Experience Analytics Report')

        show_task_3_description()

    
    elif selected_task == 'Satisfaction Analysis':

        st.title('Task 4 - Satisfaction Analysis Report')

        show_task_4_description()


    elif selected_task == 'Dashboard Development':
        st.title('Task 5 - Dashboard Development')
        
        show_task_5_description()
        

# Run main()
if __name__ == '__main__':
    main()
