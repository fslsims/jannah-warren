import streamlit as st
import google.generativeai as genai

# إعداد الصفحة
st.set_page_config(page_title="جنة وارن بافيت", layout="wide")

# محاولة جلب المفتاح وتفعيل الموديل بأكثر من طريقة لضمان العمل
try:
    if "GEMINI_API_KEY" not in st.secrets:
        st.error("❌ خطأ: لم يتم العثور على المفتاح في Secrets. يرجى إضافته باسم GEMINI_API_KEY")
        st.stop()
    
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    
    # اختيار الموديل (تم تجربة هذه التسمية لتعمل مع كافة الإصدارات)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
except Exception as e:
    st.error(f"⚠️ فشل في الاتصال بذكاء جوجل: {e}")
    st.stop()

st.title("🏛️ جنة وارن بافيت (النسخة الذكية)")
st.write("مجلس إدارة مكون من 5 خبراء يحللون لك أسهم الريت السعودية.")

stock = st.text_input("أدخل اسم سهم الريت للتحليل (مثال: الراجحي ريت):", placeholder="اكتب هنا...")

if st.button("بدء تحليل الوكلاء الخمسة"):
    if stock:
        with st.spinner(f"جاري استشارة مجلس الإدارة حول {stock}..."):
            try:
                # طلب التحليل ببرومبت احترافي
                prompt = f"""أنت مجلس إدارة مكون من 5 خبراء (محلل عقاري، محقق عالمي، مدقق مالي، راصد أخبار، ورئيس تنفيذي). 
                قم بتحليل سهم '{stock}' في السوق السعودي. 
                أعطِ تقريراً مختصراً لكل وكيل، وفي النهاية قرار 'وارن بافيت' النهائي. 
                اجعل الإجابة احترافية، دقيقة، وباللغة العربية."""
                
                # استخدام generate_content وهي الوظيفة الأساسية
                response = model.generate_content(prompt)
                
                if response.text:
                    st.success("تم اكتمال التحليل بنجاح!")
                    st.markdown(response.text)
                else:
                    st.warning("الموديل لم يعطِ ردًا، حاول مرة أخرى.")
                    
            except Exception as e:
                st.error(f"حدث خطأ أثناء التحليل: {e}")
                st.info("نصيحة: تأكد أنك كتبت اسم السهم بشكل صحيح أو جرب سهمًا آخر.")
    else:
        st.warning("يرجى إدخال اسم السهم أولاً.")
