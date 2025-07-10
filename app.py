import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Lifeloom – AI Mental Wellness Companion", layout="wide")
st.title("🌿 LifeLoom – AI Mental Wellness Companion")
st.markdown("""
Lifeloom is your 24/7 mental wellness companion that uses passive and active signals to **detect early signs of stress, anxiety, or depression**.

It provides:
- A **personalized risk score**
- **Tailored support** based on your needs
- An **empathetic AI chat assistant**
- **Anonymous insights** for schools or counselors
""")

# --- Form Input ---
st.header("🧍 Personal Wellness Check-In")
with st.form("lifeloom_form"):
    col1, col2 = st.columns(2)
    with col1:
        sleep = st.slider("🛌 Sleep Hours (per night)", 0.0, 12.0, 6.0)
        screen = st.slider("📱 Screen Time (hours/day)", 0.0, 15.0, 6.0)
        steps = st.number_input("👣 Step Count (per day)", min_value=0, value=4000)
        typing = st.slider("⌨️ Typing Speed (WPM)", 0, 100, 40)
    with col2:
        mood = st.slider("🙂 Mood Today (1-10)", 1, 10, 6)
        journaling = st.slider("📓 Journaling Days/week", 0, 7, 2)
        voice_logs = st.slider("🎤 Voice Logs/week", 0, 7, 1)
        social = st.slider("🧑‍🤝‍🧑 Social Interactions/day", 0, 20, 3)

    submit = st.form_submit_button("🔍 Analyze My Risk")

# --- Risk Engine ---
if submit:
    st.header("📊 Your Lifeloom Risk Report")

    # Rule-based Risk Score
    risk_score = 0
    if sleep < 6: risk_score += 1
    if screen > 6: risk_score += 1
    if steps < 3000: risk_score += 1
    if mood <= 4: risk_score += 2
    if journaling < 2: risk_score += 1
    if voice_logs < 1: risk_score += 1
    if typing < 30: risk_score += 1
    if social < 2: risk_score += 1

    # Risk Level + Tiered Support
    if risk_score <= 2:
        risk_label = "🟢 Low Risk"
        support = "✅ Try daily gratitude, journaling, and breathing routines."
    elif 3 <= risk_score <= 5:
        risk_label = "🟡 Moderate Risk"
        support = "🧘 Start 5-min CBT, breathing games, mindfulness apps."
    else:
        risk_label = "🔴 High Risk"
        support = "📞 Please reach out to a friend, counselor, or professional help."

    st.metric("Your Risk Score", f"{risk_score} / 8")
    st.markdown(f"**Mental Wellness Risk Level:** {risk_label}")
    st.success(f"🧠 Suggested Support: {support}")

    # --- Personalized CBT Tip ---
    st.subheader("💡 Your Personalized Self-Care Tip")
    if mood <= 4:
        st.info("Write 3 things you’re grateful for. It improves mood by 25%.")
    elif screen > 8:
        st.info("Take a screen detox break for 1 hour. Try nature or walking.")
    elif sleep < 5:
        st.info("Aim for 7-8 hours of sleep. Avoid screens before bed.")
    elif social < 2:
        st.info("Call or meet a friend today. Connection helps.")
    else:
        st.info("You're doing well. Stay consistent with self-care!")

    # --- Graph: Passive Metrics ---
    st.subheader("📈 Your Passive Wellness Snapshot")
    fig, ax = plt.subplots(figsize=(6, 3))
    labels = ["Sleep", "Screen", "Steps (k)", "Typing", "Mood"]
    values = [sleep, screen, steps / 1000, typing, mood]
    ax.bar(labels, values, color='teal')
    st.pyplot(fig)

    # --- AI Chat Placeholder ---
    st.subheader("🤖 24/7 AI Chat Companion")
    st.markdown("Coming soon: Your AI listener that provides real-time support, active listening, and empathy.")

    # --- School/Counselor Dashboard Placeholder ---
    st.subheader("🏫 Counselor Dashboard (Demo)")
    st.markdown("Anonymous trend data from students can help schools act early.")
    st.image("https://i.imgur.com/NsS5JbJ.png", caption="Sample Dashboard (Anonymized)", use_column_width=True)

# Footer
st.markdown("---")
st.caption("Developed with ❤️ by Team Binary Brains | ANITS | LifeLoom 2025")

