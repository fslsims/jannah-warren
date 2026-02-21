import streamlit as st
import google.generativeai as genai

# جلب المفتاح بأمان
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # استخدام الموديل بالاسم الصحيح والمباشر
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except Exception as e:
    st.error(f"حدث خطأ في الإعدادات: {e}")
    st.stop()

st.title("🏛️ جنة وارن بافيت (النسخة الذكية)")
stock = st.text_input("أدخل اسم سهم الريت للتحليل الحقيقي:", placeholder="مثال: الراجحي ريت")

if st.button("بدء تحليل الوكلاء الخمسة"):
    if stock:
        with st.spinner(f"جاري استشارة مجلس الإدارة حول {stock}..."):
            # طلب التحليل من Gemini لكل وكيل ببرومبت مخصص
            prompt = f"""أنت مجلس إدارة مكون من 5 خبراء (محلل عقاري، محقق عالمي، مدقق مالي، راصد أخبار، ورئيس تنفيذي). 
            قم بتحليل سهم '{stock}' في السوق السعودي. 
            أعطِ تقريراً مختصراً لكل وكيل، وفي النهاية قرار 'وارن بافيت' النهائي. 
            اجعل الإجابة احترافية وباللغة العربية."""
            
            response = model.generate_content(prompt)
            st.markdown(response.text)
    else:
        st.warning("يرجى إدخال اسم السهم.")
