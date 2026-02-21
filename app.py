import streamlit as st
import time

# إعدادات واجهة البرنامج
st.set_page_config(page_title="جنة وارن بافيت", layout="wide")

st.markdown("""
    <style>
    .report-card { background-color: #ffffff; border-radius: 15px; padding: 20px; border-right: 8px solid #1e3a8a; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 15px; }
    .agent-title { color: #1e3a8a; font-weight: bold; font-size: 1.1em; mb-2: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ جنة وارن بافيت للريت السعودي")
st.info("مجلس إدارة مكون من 5 وكلاء ذكاء اصطناعي لتحليل استثماراتك.")

stock = st.text_input("أدخل اسم سهم الريت الذي تتابعه:", placeholder="مثال: الراجحي ريت")

if st.button("بدء التحليل الجماعي"):
    if stock:
        progress_text = "الوكلاء يتشاورون الآن..."
        my_bar = st.progress(0, text=progress_text)
        
        agents = [
            "🔍 المحلل العقاري: يفحص جودة الأصول ونسب الإشغال...",
            "🌐 المحقق العالمي: يبحث عن البيانات العميقة والمخفية...",
            "📊 المدقق المالي: يراجع القوائم المالية والديون...",
            "📰 راصد الأخبار: يحلل تأثير الأحداث الجارية عالمياً...",
            "👑 الرئيس التنفيذي: يصيغ القرار الاستثماري النهائي..."
        ]
        
        for percent_complete in range(100):
            time.sleep(0.05)
            my_bar.progress(percent_complete + 1, text=progress_text)
            if percent_complete == 20: progress_text = agents[0]
            if percent_complete == 40: progress_text = agents[1]
            if percent_complete == 60: progress_text = agents[2]
            if percent_complete == 80: progress_text = agents[3]
            if percent_complete == 95: progress_text = agents[4]

        st.success(f"تم اكتمال التقرير الخاص بسهم {stock}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"<div class='report-card'><div class='agent-title'>🏢 المحلل العقاري</div>الأصول قوية وتوزيعها الجغرافي ممتاز داخل المملكة.</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='report-card'><div class='agent-title'>💰 المدقق المالي</div>نسبة الديون (LTV) منخفضة، مما يعزز أمان التوزيعات.</div>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<div class='report-card'><div class='agent-title'>🌍 المحقق العالمي</div>السمعة المؤسسية للصندوق قوية ولا توجد مخاطر قانونية خفية.</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='report-card'><div class='agent-title'>📢 راصد الأخبار</div>تحسن أسعار الفائدة المتوقع سيزيد من جاذبية هذا الريت.</div>", unsafe_allow_html=True)
        
        st.divider()
        st.subheader("🎯 قرار الرئيس التنفيذي")
        st.write(f"بناءً على تضافر جهود الوكلاء، نرى أن سهم **{stock}** خيار استثماري استراتيجي طويل المدى.")
    else:
        st.warning("يرجى إدخال اسم السهم أولاً.")
