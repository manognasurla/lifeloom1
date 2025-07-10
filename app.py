import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Lifeloom – Personal Mental Wellness Risk Checker", layout="wide")
st.title("🌿 LifeLoom – Personal Mental Wellness Risk Checker")

st.markdown("""
LifeLoom helps you reflect on your **passive and active wellness data** to detect early signs of **stress, anxiety, or depression**.

Fill in the fields below to get a **personalized risk score**, receive **tailored CBT suggestions**, and start taking control of your mental well-being.
""")

# --- User Input Form ---
st.subheader("🧍‍♀️ Your Personal Wellness Data")
with st.form("wellness_form"):
    col1, col2 = st.columns(2)
    with col1:
        sleep_hours = st.slider("Sleep (hours per night)", 0.0, 12.0, 6.0)
        screen_time = st.slider("Screen Time (hours/day)", 0.0, 15.0, 5.0)
        steps = st.number_input("Step Count (per day)", min_value=0, value=4000)
        typing_speed = st.slider("Typing Speed (WPM)", 0, 100, 40)
    with col2:
        mood = st.slider("Mood (1 = Low, 10 = Great)", 1, 10, 5)
        journaling_days = st.slider("Journaling Days per Week", 0, 7, 2)
        voice_notes = st.slider("Voice Journals (per week)", 0, 7, 1)
        social_contacts = st.slider("Social Interactions per Day", 0, 20, 3)

    submitted = st.form_submit_button("🔍 Analyze My Risk")

# --- Risk Engine ---
if submitted:
    st.subheader("📈 Your Mental Wellness Risk Analysis")

    # Risk scoring (simple rule-based)
    risk_score = 0
    if sleep_hours < 6: risk_score += 1
    if screen_time > 6: risk_score += 1
    if steps < 3000: risk_score += 1
    if mood <= 4: risk_score += 2
    if journaling_days < 2: risk_score += 1
    if voice_notes < 1: risk_score += 1
    if typing_speed < 30: risk_score += 1
    if social_contacts < 2: risk_score += 1

    # Risk Level
    if risk_score <= 2:
        risk_level = "🟢 Low"
        issue = "You're doing well! Maintain your current habits."
    elif 3 <= risk_score <= 5:
        risk_level = "🟡 Moderate"
        issue = "Signs of possible stress or low mood. Consider self-care."
    else:
        risk_level = "🔴 High"
        issue = "High mental stress risk. Consider reaching out or professional help."

    # Show result
    st.metric("Your Risk Score", f"{risk_score} / 8")
    st.markdown(f"**Risk Level:** {risk_level}")
    st.markdown(f"**Interpretation:** {issue}")

    # --- CBT Suggestion ---
    st.subheader("💡 Tailored CBT Suggestion")
    if mood <= 4:
        st.info("Try writing 3 good things that happened today. It boosts mood.")
    elif sleep_hours < 6:
        st.info("Avoid screens 1 hour before bed. Try a wind-down routine.")
    elif screen_time > 6:
        st.info("Consider scheduling no-screen blocks during the day.")
    elif journaling_days < 2:
        st.info("Journaling even once a week helps track feelings and gain insight.")
    else:
        st.info("Great job! Keep up your wellness habits.")

    # --- Optional Visual Feedback ---
    st.subheader("📊 Your Wellness Inputs")
    fig, ax = plt.subplots()
    metrics = [sleep_hours, screen_time, steps/1000, mood, social_contacts]
    labels = ["Sleep (hrs)", "Screen (hrs)", "Steps (k)", "Mood", "Social"]
    ax.bar(labels, metrics, color='skyblue')
    ax.set_ylabel("Value")
    st.pyplot(fig)

# Footer
st.markdown("---")
st.caption("Developed with ❤️ | LifeLoom 2025 – AI for Mental Wellness")
