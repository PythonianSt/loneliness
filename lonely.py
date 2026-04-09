import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Mental Health Screening", layout="centered")

# --------------------------------
# LANGUAGE CONTENT
# --------------------------------
content = {

"English": {

"title":"🧠 Student Mental Health Assessment: KU KPS Infirmary",
"options":["Not at all","Several days","More than half the days","Nearly every day"],

"phq_header":"😔 Depression Screening (PHQ-9)",
"phq_questions":[
"Little interest or pleasure in doing things",
"Feeling down, depressed, or hopeless",
"Trouble falling or staying asleep, or sleeping too much",
"Feeling tired or having little energy",
"Poor appetite or overeating",
"Feeling bad about yourself",
"Trouble concentrating",
"Moving or speaking slowly or being restless",
"Thoughts that you would be better off dead or hurting yourself"
],

"gad_header":"😟 Anxiety Screening (GAD-7)",
"gad_questions":[
"Feeling nervous, anxious, or on edge",
"Not being able to stop worrying",
"Worrying too much about different things",
"Trouble relaxing",
"Being restless",
"Becoming easily annoyed or irritable",
"Feeling afraid something awful might happen"
],

"button":"📊 Analyse & Get Recommendations",
"ai_header":"🤖 Personalised Recommendations",
"spinner":"Analysing responses..."
},

"ภาษาไทย":{

"title":"🧠 แบบประเมินสุขภาพจิตนักศึกษา สถานศึกษา มหาวิทยาลัยเกษตรศาสตร์ วิทยาเขตกำแพงแสน",
"options":["ไม่มีเลย","บางวัน","บ่อยกว่าครึ่งเวลา","เกือบทุกวัน"],

"phq_header":"😔 คัดกรองซึมเศร้า (PHQ-9)",
"phq_questions":[
"เบื่อ ไม่สนใจสิ่งต่าง ๆ",
"รู้สึกเศร้า ท้อแท้",
"นอนหลับยากหรือมากเกินไป",
"อ่อนเพลีย ไม่มีแรง",
"เบื่ออาหารหรือกินมากเกิน",
"รู้สึกว่าตนเองล้มเหลว",
"สมาธิลดลง",
"เชื่องช้าหรือกระสับกระส่าย",
"มีความคิดอยากตายหรือทำร้ายตนเอง"
],

"gad_header":"😟 คัดกรองความวิตกกังวล (GAD-7)",
"gad_questions":[
"รู้สึกกังวล ตึงเครียด",
"หยุดความกังวลไม่ได้",
"กังวลหลายเรื่อง",
"ผ่อนคลายยาก",
"กระสับกระส่าย",
"หงุดหงิดง่าย",
"กลัวสิ่งไม่ดีจะเกิดขึ้น"
],

"button":"📊 วิเคราะห์และรับคำแนะนำ",
"ai_header":"🤖 คำแนะนำเฉพาะบุคคล",
"spinner":"กำลังวิเคราะห์..."
}
}

# --------------------------------
# LANGUAGE SELECT
# --------------------------------
lang = st.sidebar.radio("Language / ภาษา",["English","ภาษาไทย"])
c = content[lang]

score_map={c["options"][i]:i for i in range(4)}

st.title(c["title"])

# --------------------------------
# PHQ-9
# --------------------------------
st.header(c["phq_header"])

phq_scores=[]
for i,q in enumerate(c["phq_questions"]):
    ans=st.radio(q,c["options"],key=f"phq{i}")
    phq_scores.append(score_map[ans])

phq_total=sum(phq_scores)
suicide_flag=phq_scores[8] >=1   # Question 9

# --------------------------------
# GAD-7
# --------------------------------
st.header(c["gad_header"])

gad_scores=[]
for i,q in enumerate(c["gad_questions"]):
    ans=st.radio(q,c["options"],key=f"gad{i}")
    gad_scores.append(score_map[ans])

gad_total=sum(gad_scores)

# --------------------------------
# SEVERITY FUNCTIONS
# --------------------------------
def phq_level(s):
    if s<=4:return "Minimal"
    elif s<=9:return "Mild"
    elif s<=14:return "Moderate"
    elif s<=19:return "Moderately Severe"
    else:return "Severe"

def gad_level(s):
    if s<=4:return "Minimal"
    elif s<=9:return "Mild"
    elif s<=14:return "Moderate"
    else:return "Severe"

# --------------------------------
# ANALYSE BUTTON
# --------------------------------
if st.button(c["button"]):

    st.subheader("📈 Results")

    st.write(f"PHQ-9 Score: {phq_total}/27 ({phq_level(phq_total)})")
    st.write(f"GAD-7 Score: {gad_total}/21 ({gad_level(gad_total)})")

    if suicide_flag:
        st.error("⚠️ Positive response to self-harm question. Clinical follow-up recommended.")

    prompt=f"""
Student mental health screening:

PHQ-9 score: {phq_total}/27 ({phq_level(phq_total)})
GAD-7 score: {gad_total}/21 ({gad_level(gad_total)})
Self-harm item positive: {suicide_flag}

Please:
1. Summarise mental health status
2. Assess risk level
3. Give supportive and culturally sensitive advice
4. Suggest when to seek professional help
Use empathetic tone.
"""

    with st.spinner(c["spinner"]):
        response=client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role":"user","content":prompt}]
        )

    st.subheader(c["ai_header"])
    st.write(response.choices[0].message.content)

# --------------------------------
# DISCLAIMER
# --------------------------------
st.markdown("---")
st.caption("Screening tool only and your data will not be stored.")
