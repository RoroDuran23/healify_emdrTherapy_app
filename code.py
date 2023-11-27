import streamlit as st
import time

# Initialize session state variables
if 'started_round2' not in st.session_state:
    st.session_state.started_round2 = False
if 'started_animation' not in st.session_state:
    st.session_state.started_animation = False
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False
if 'animation_triggered' not in st.session_state:
    st.session_state.animation_triggered = False

# Set page configuration
st.set_page_config(page_title="Healify 🌿")

# Add a title to the home page
st.title("Healify 🌿")

# Define the first round of questions
questions_round1 = [
    "Did you experience a traumatic event?",
    "Do you regularly relive or re-experience the event?",
    "Do you avoid certain people, situations, or places?",
    "Do you blame yourself for what happened?",
    "Do you have a hard time remembering certain features of the event?",
    "Do you feel irritable, hyper-aware, or jumpy?",
    "Have you withdrawn from friends, family, or other loved ones?",
    "Is it difficult for you to function in daily life?",
    "Have your symptoms lasted for a month or longer"
]

# Define the second round of questions
questions_round2 = [
    "What traumatic experiences or memories are causing distress?",
    "How do these traumatic memories affect your thoughts, emotions, and behaviors?",
    "What specific symptoms of PTSD do you want to target in therapy?",
    "On a scale from 0 to 5, how distressing are these memories for you right now?",
    "Have you experienced any adverse reactions or triggers during previous therapy or discussions about trauma?"
]

# Custom component to display the moving ball animation with sliding effect
def moving_ball(speed=2):
    st.subheader("Ball Animation")
    animation_container = st.empty()
    positionX = 0
    animation_duration = 3  # Duration of the animation in seconds

    # Wait for 7 seconds before starting the animation
    time.sleep(7)

    # Start counting the animation time from now
    start_time = time.time()

    while time.time() - start_time < animation_duration and not st.session_state.form_submitted:
        # Update the position of the ball
        positionX += speed

        # Display the animated ball
        animation_container.markdown(
            f'<div style="width: 800px; height: 300px; background: #333; position: relative; border-radius: 10px;">'
            f'<div style="position: absolute; width: 40px; height: 40px; background-color: green; border-radius: 50%; left: {positionX}px; top: 130px;"></div>'
            f'</div>',
            unsafe_allow_html=True,
        )

        # Add a delay to control the animation speed
        time.sleep(0.03)

        # Reverse direction when reaching the end
        if positionX >= 760:
            speed = -abs(speed)
        if positionX <= 0:
            speed = abs(speed)



# Display two buttons on the home page with larger sizes
st.markdown(
    '<style>div.css-19pkdgt{font-size:24px;}</style>',
    unsafe_allow_html=True
)

# Define the option using st.sidebar
option = st.sidebar.radio("Choose an option:", ["User Guide", "Start Questionnaire"], key="options")

# Page 1: User Guide
if option == "User Guide":
    st.title("Healify App User Guide")
    st.markdown("""
    Welcome to Healify, an app designed to assist you in understanding and addressing traumatic experiences and their impact on your well-being. This user guide will walk you through the key features and functionalities of the Healify app.

    ## Getting Started

    1. **Home Page**: When you open Healify, you'll be greeted with the Home Page. Here, you can choose between two main options:
       - **User Guide**: Click on "User Guide" to access this guide.
       - **Start Questionnaire**: Select "Start Questionnaire" to begin the assessment process.

    2. **First Round of Questions**: If you choose to "Start Questionnaire," you'll be presented with a series of questions in the First Round. These questions are designed to gauge your initial responses to traumatic events.

       - Answer each question honestly, choosing "Yes" or "No" for each one.

       - If you answer "No" to critical questions, you'll receive guidance not to continue the questionnaire.

       - If you answer "Yes" to all critical questions, you'll proceed to the Second Round.

    3. **Second Round of Questions**: The Second Round of questions delves deeper into your experiences and symptoms. You'll have the opportunity to provide more detailed information about your situation.

       - Answer the questions as accurately as possible, choosing the appropriate options, and using text boxes for additional comments as needed.

       - Once you complete this round, you'll initiate an animation.

    4. **Follow the Red Ball**: During the animation, focus on the red ball and describe any changes in your thoughts, emotions, or physical sensations.

       - The animation is designed to help you better understand your emotional responses.

    ## Tips for Using Healify

    - Be honest: Open and truthful responses will lead to more accurate results and better assistance.

    - Seek professional help: If you find that your symptoms are severe and affecting your daily life, it's advisable to seek professional guidance.

    - Self-care: Remember that while Healify can be a helpful tool, it's essential to practice self-care and engage in activities that promote your well-being.

    - Privacy: Your responses are private and confidential. The app does not store or share your answers with anyone.

    ## Conclusion

    Healify is intended to provide insight and guidance into your emotional well-being and responses to trauma. Please use it as a tool to gain a better understanding of your feelings and experiences.

    Remember, while Healify can be a valuable resource, it should not replace professional help if you are struggling with the effects of trauma. Reach out to a mental health professional for further support and assistance.

    Thank you for using Healify!
    """)

# Container for the First Round of Questions
round1_container = st.container()

# Page 2: First Round of Questions
with round1_container:
    if option == "Start Questionnaire" and not st.session_state.started_round2:
        st.markdown("## First Round of Questions")
        st.write("Please answer the following questions:")
        answers_round1 = []
        for i, question in enumerate(questions_round1):
            answer = st.radio(f"{i + 1}. {question}", ["Yes", "No"])
            answers_round1.append(answer)

        # Check if all critical questions are answered with "Yes" to proceed
        if all(answer == "Yes" for answer in answers_round1[:2]) and answers_round1[-1] == "Yes":
            if st.button("Submit - Round 1", key="submit_round1"):
                st.session_state.started_round2 = True
        else:
            st.write("You answered 'No' to a critical question. No need to continue. You may now close this window")

# Page 3: Second Round of Questions
if st.session_state.started_round2 and not st.session_state.started_animation:
    st.markdown("## Second Round of Questions")
    st.write("Please answer the following questions:")
    answers_round2 = []
    for i, question in enumerate(questions_round2):
        if i == 0:
            question1_choices = [
                "Physical Abuse",
                "Death of a loved one",
                "Car Crash",
                "Serious Health Illness",
                "Other"
            ]
            answer = st.selectbox(f"{i + 1}. {question}", question1_choices)
        elif i == 2:
            question3_choices = [
                "Intrusive Thoughts and Memories",
                "Emotional Dysregulation",
                "Avoidance and Numbing",
                "Hyperarousal and Hypervigilance",
                "Negative Beliefs and Self-Blame"
            ]
            answer = st.multiselect(f"{i + 1}. {question}", question3_choices)
        elif i == 3:
            answer = st.slider(f"{i + 1}. {question}", 0, 5, step=1)
        elif i == 4:
            answer = st.radio(f"{i + 1}. {question}", ["Yes", "No"])
        else:
            answer = st.text_area(f"{i + 1}. {question}")
        answers_round2.append(answer)

    if st.button("Submit - Round 2", key="submit_round2"):
        st.session_state.started_animation = True

# Page 4: Ball Animation
# The animation should only be triggered once after the second round of questions
if st.session_state.started_animation and not st.session_state.animation_triggered:
    st.markdown("## Follow the Green Ball")
    st.write("While focusing on the traumatic memory, follow the green ball. Describe any changes in your thoughts, emotions, or physical sensations as we do this.")
    moving_ball(5)
    st.session_state.animation_triggered = True  # Set this to True after the animation is done

# Page 5: Form for user response after animation
if st.session_state.started_round2 and st.session_state.started_animation and not st.session_state.form_submitted:
    st.markdown("## Reflection")
    with st.form(key='user_response_form'):
        user_response = st.text_input("What positive thoughts or beliefs would you like to adopt to replace the negative associations tied to this memory?")
        submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            st.session_state.form_submitted = True
            st.success("Thank you for your response!")
