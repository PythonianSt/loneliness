import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -----------------------
# Language Content
# -----------------------
content = {
    "English": {
        "page_title": "Mental Health Screening",
        "title": "🧠 Student Mental Health Assessment",
        "subtitle": "A screening tool for depression, anxiety, and emotional wellbeing — by KU KPS Infirmary.",
        "phq_header": "😔 Depression Screening (PHQ-2)",
        "phq_q1": "Little interest or pleasure in doing things",
        "phq_q2": "Feeling down, depressed, or hopeless",
        "gad_header": "😟 Anxiety Screening (GAD-2)",
        "gad_q1": "Feeling nervous, anxious, or on edge",
        "gad_q2": "Not being able to stop or control worrying",
        "stress_header": "😤 Stress & Adjustment",
        "stress_q1": "How stressed do you feel about academic workload? (0=none, 10=extreme)",
        "stress_q2": "How difficult is it to adjust to life in a new country? (0=easy, 10=very hard)",
        "lonely_header": "🤝 Social Connection",
        "lonely_q1": "How lonely do you feel? (0=not at all, 10=very lonely)",
        "options": ["Not at all", "Several days", "More than half the days", "Nearly every day"],
        "button": "📊 Analyse & Get Recommendations",
        "results_header": "📈 Your Results",
        "ai_header": "🤖 Personalised Recommendations",
        "spinner": "Analysing your responses...",
        "error": "API connection error: ",
        "tips_header": "💡 General Wellbeing Tips",
        "tips": """
- Reach out to your university's international student support office
- Connect with student communities from your home country
- Practice regular sleep and eating routines
- Talk to a counsellor — most universities offer free sessions
- Stay physically active even with short daily walks
""",
        "score_labels": {
            "PHQ-2": "Depression score",
            "GAD-2": "Anxiety score",
            "Stress": "Academic stress",
            "Adjustment": "Adjustment difficulty",
            "Loneliness": "Loneliness"
        },
        "prompt": lambda phq, gad, stress, adjust, lonely: f"""
An international student completed a mental health screening with these results:
- PHQ-2 (depression): {phq}/6
- GAD-2 (anxiety): {gad}/6
- Academic stress: {stress}/10
- Adjustment difficulty: {adjust}/10
- Loneliness: {lonely}/10

Please:
1. Summarise their mental health status
2. Identify key risk areas
3. Provide practical, culturally sensitive recommendations
4. Suggest university resources and self-help strategies
Use empathetic, clear English suitable for a student audience.
"""
    },
    "ภาษาไทย": {
        "page_title": "ประเมินสุขภาพจิต",
        "title": "🧠 แบบประเมินสุขภาพจิตสำหรับนักศึกษาต่างชาติ",
        "subtitle": "เครื่องมือคัดกรองภาวะซึมเศร้า ความวิตกกังวล และสุขภาวะทางอารมณ์ — สำหรับนักศึกษาต่างชาติโดยเฉพาะ",
        "phq_header": "😔 คัดกรองภาวะซึมเศร้า (PHQ-2)",
        "phq_q1": "รู้สึกเบื่อ ไม่สนใจสิ่งต่าง ๆ",
        "phq_q2": "รู้สึกเศร้า ท้อแท้ หมดหวัง",
        "gad_header": "😟 คัดกรองความวิตกกังวล (GAD-2)",
        "gad_q1": "รู้สึกกังวล ประหม่า หรือตึงเครียด",
        "gad_q2": "ไม่สามารถหยุดหรือควบคุมความกังวลได้",
        "stress_header": "😤 ความเครียดและการปรับตัว",
        "stress_q1": "ความเครียดจากภาระการเรียน (0=ไม่มีเลย, 10=มากที่สุด)",
        "stress_q2": "ความยากในการปรับตัวในประเทศใหม่ (0=ง่าย, 10=ยากมาก)",
        "lonely_header": "🤝 ความสัมพันธ์ทางสังคม",
        "lonely_q1": "รู้สึกโดดเดี่ยวแค่ไหน (0=ไม่เลย, 10=โดดเดี่ยวมาก)",
        "options": ["ไม่มีเลย", "บางวัน", "บ่อยกว่าครึ่งของเวลา", "เกือบทุกวัน"],
        "button": "📊 วิเคราะห์และรับคำแนะนำ",
        "results_header": "📈 ผลการประเมิน",
        "ai_header": "🤖 คำแนะนำเฉพาะบุคคล",
        "spinner": "กำลังวิเคราะห์ข้อมูล...",
        "error": "เกิดข้อผิดพลาดในการเชื่อมต่อ API: ",
        "tips_header": "💡 แนวทางดูแลสุขภาพจิตเบื้องต้น",
        "tips": """
- ติดต่อสำนักงานดูแลนักศึกษาต่างชาติของมหาวิทยาลัย
- เข้าร่วมกลุ่มนักศึกษาจากประเทศเดียวกัน
- รักษาตารางนอนและรับประทานอาหารให้สม่ำเสมอ
- พูดคุยกับนักจิตวิทยาหรือที่ปรึกษา — มหาวิทยาลัยส่วนใหญ่มีบริการฟรี
- ออกกำลังกายเบา ๆ เช่น เดินทุกวัน
""",
        "score_labels": {
            "PHQ-2": "คะแนนซึมเศร้า",
            "GAD-2": "คะแนนความวิตกกังวล",
            "Stress": "ความเครียดจากการเรียน",
            "Adjustment": "ความยากในการปรับตัว",
            "Loneliness": "ความโดดเดี่ยว"
        },
        "prompt": lambda phq, gad, stress, adjust, lonely: f"""
นักศึกษาต่างชาติได้ทำแบบประเมินสุขภาพจิต ผลลัพธ์ดังนี้:
- PHQ-2 (ซึมเศร้า): {phq}/6
- GAD-2 (วิตกกังวล): {gad}/6
- ความเครียดจากการเรียน: {stress}/10
- ความยากในการปรับตัว: {adjust}/10
- ความโดดเดี่ยว: {lonely}/10

กรุณา:
1. สรุปสถานะสุขภาพจิต
2. ระบุจุดเสี่ยงสำคัญ
3. ให้คำแนะนำที่ปฏิบัติได้จริงและคำนึงถึงความแตกต่างทางวัฒนธรรม
4. แนะนำทรัพยากรของมหาวิทยาลัยและแนวทางช่วยเหลือตนเอง
ใช้ภาษาไทย น้ำเสียงอบอุ่น เหมาะสมกับนักศึกษา
"""
    }
}

# -----------------------
# Sidebar Language Toggle
# -----------------------
with st.sidebar:
    st.markdown("## 🌐 Language / ภาษา")
    lang = st.radio("Select language:", ["English", "ภาษาไทย"])
    st.markdown("---")
    st.markdown("### ℹ️ About / เกี่ยวกับ")
    if lang == "English":
        st.markdown("This tool screens for common mental health challenges faced by students. It is **not a clinical diagnosis** nor it will save any data.")
    else:
        st.markdown("เครื่องมือนี้ใช้คัดกรองปัญหาสุขภาพจิตที่พบบ่อยในนักศึกษา **ไม่ใช่การวินิจฉัยทางคลินิก** และไม่มีการเก็บข้อมูลใดๆ")

c = content[lang]
score_map = {c["options"][i]: i for i in range(4)}

st.set_page_config(page_title=c["page_title"], layout="centered")
st.title(c["title"])
st.markdown(c["subtitle"])

# -----------------------
# PHQ-2
# -----------------------
st.header(c["phq_header"])
phq_q1 = st.radio(c["phq_q1"], c["options"], key="phq1")
phq_q2 = st.radio(c["phq_q2"], c["options"], key="phq2")
phq_score = score_map[phq_q1] + score_map[phq_q2]

# -----------------------
# GAD-2
# -----------------------
st.header(c["gad_header"])
gad_q1 = st.radio(c["gad_q1"], c["options"], key="gad1")
gad_q2 = st.radio(c["gad_q2"], c["options"], key="gad2")
gad_score = score_map[gad_q1] + score_map[gad_q2]

# -----------------------
# Stress & Adjustment
# -----------------------
st.header(c["stress_header"])
stress  = st.slider(c["stress_q1"], 0, 10, 5)
adjust  = st.slider(c["stress_q2"], 0, 10, 5)

# -----------------------
# Social Connection
# -----------------------
st.header(c["lonely_header"])
lonely = st.slider(c["lonely_q1"], 0, 10, 5)

# -----------------------
# Analyse
# -----------------------
if st.button(c["button"]):
    labels = c["score_labels"]

    st.subheader(c["results_header"])
    st.write(f"{labels['PHQ-2']}: {phq_score}/6")
    st.write(f"{labels['GAD-2']}: {gad_score}/6")
    st.write(f"{labels['Stress']}: {stress}/10")
    st.write(f"{labels['Adjustment']}: {adjust}/10")
    st.write(f"{labels['Loneliness']}: {lonely}/10")

    prompt = c["prompt"](phq_score, gad_score, stress, adjust, lonely)

    try:
        with st.spinner(c["spinner"]):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
        st.subheader(c["ai_header"])
        st.write(response.choices[0].message.content)

    except Exception as e:
        st.error(f"{c['error']}{e}")

# -----------------------
# Tips (always visible)
# -----------------------
st.markdown("---")
st.markdown(f"### {c['tips_header']}")
st.markdown(c["tips"])