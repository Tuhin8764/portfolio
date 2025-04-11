import streamlit as st
import time


def main():
    st.set_page_config(page_title='🚀 My Portfolio', layout='wide')

    # Sidebar for profile photo and social media links
    with st.sidebar:
        st.image("Tuhin Santra.JPG", width=200)
        st.title("Your Name ✨")
        st.write("💡 Business Analytics & Data Science Enthusiast")
        st.markdown("[🔗 LinkedIn](https://linkedin.com/in/yourprofile)")
        st.markdown("[🐙 GitHub](https://github.com/yourprofile)")
        st.markdown("[🐦 Twitter](https://twitter.com/yourprofile)")

    # Animated welcome message
    st.write("## 👋 Welcome to My Portfolio!")
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress_bar.progress(i + 1)
    st.success("🚀 Portfolio Loaded Successfully!")

    # Main sections
    st.header("📌 Summary")
    st.write("""📝 Write a short summary about yourself, your expertise, and what you are passionate about.""")

    st.header("🎓 Education")
    st.write("**MBA - Business Analytics & Data Science** 🎯")
    st.write("🏫 University Name | 📅 Year")
    st.write("**B.Com** 🎯")
    st.write("🏫 University Name | 📅 Year")

    st.header("💼 Experience")
    st.write("**Intern | Company Name** 🏢")
    st.write("📌 Role description and key contributions")

    st.header("🛠 Skills")
    skills = ["🐍 Python", "🗄 SQL", "📊 Power BI", "📈 Tableau", "📑 Excel", "🤖 Machine Learning", "🎨 Data Visualization"]
    st.write(", ".join(skills))

    st.header("🚀 Projects")
    st.image("Tuhin Santra.JPG", width=700)
    st.write("**🌍 Global Happiness Analysis**")
    st.write("🔍 Analyzed global happiness scores using Power BI and Excel.")
    st.write("[🔗 View Project](https://github.com/yourprofile/project-link)")

    st.header("🏆 Certifications & Achievements")
    st.write("✅ **ML Certification - IIT Kanpur**")
    st.write("✅ **Advanced Excel Certification**")

    st.header("🎭 Hobbies & Interests")
    hobbies = ["📖 Reading", "🎮 Gaming", "✍️ Blogging", "✈️ Traveling"]
    st.write(", ".join(hobbies))


if __name__ == "__main__":
    main()