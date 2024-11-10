import pandas as pd
import streamlit as st


# Page Config
st.set_page_config(page_title='全國大專院校 ESG暨Big Data數據應用大賽',  layout='wide')


# Title
st.title("_全國大專院校 ESG暨Big Data數據應用大賽_")


# Partition
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["活動宗旨", "活動對象", "競賽類別", "評分標準", "參賽獎勵", '競賽資訊'])


# Content
with tab1:
    container1 = st.container()
    input_a1, input_a2, input_a3 = container1.columns((1, 3, 1))
    sentence_1 = "本活動旨在鼓勵大學部學生參與專題競賽，激發創意思維並提出創新解決方案。創新是推動人類文明進步的核心動力，透過專題競賽，學生將運用各種研究與分析工具，並在團隊合作中展現綜合實力。過程中，學生將學習訂定主題、蒐集資料、進行實驗與測試，從而有效培養知識整合與問題解決的能力，並激發企劃、執行與行銷潛能。"
    sentence_2 = "本次ESG暨Big Data數據應用大賽，旨在引導學生以商業創新角度探索並實踐專題成果，結合核心素養與課程所學，在創新產品設計、商業模式構思及活動改善中展現學習成效，提升學生在實務與專業領域的競爭力。"
    input_a2.header("活動宗旨：")
    input_a2.write(sentence_1)
    input_a2.write(sentence_2)
with tab2:
    container2 = st.container()
    input_b1, input_b2, input_b3 = container2.columns((1, 3, 1))
    sentence_1 = "全國大專院校在學學生，含大學部(含五專之四、五年級)、碩士班及在職專班，非本國籍者必須同時持有居留證，每一參賽隊伍人數2至5人，至多得指定3位指導老師。"
    input_b2.header("活動對象：")
    input_b2.write(sentence_1)
with tab3:
    container3 = st.container()
    input_c1, input_c2, input_c3 = container3.columns((1, 3, 1))
    sentence_1 = "參賽者以台灣公務機關、民營機關、營利或非營利組織為標的，依據不同的背景考量基準，以組織發展、組織結構、資源(人、財、物、資訊)決策評估、分析、運用為基礎，進一步提出永續發展組織具備之基礎。參賽學生如何將永續發展目標融合組織行為、經濟學、財務管理、行銷學與企業管理實務產銷人發展財接軌的實戰演練，建立正確的組織永續發展觀念並與全台學生交流；指導老師亦藉此了解學生的學習應用成效，以提昇未來的教學績效。"
    sentence_2 = "報名時間：2025年01月01日至2025年01月10日"
    sentence_3 = "計畫繳交：2025年01月20日至2025年01月25日"
    sentence_4 = "得獎公告：2025年02月10日"
    input_c2.header("競賽類別：")
    input_c2.subheader("A.ESG綠色管理組：")
    input_c2.write(sentence_1)
    input_c2.write(sentence_2)
    input_c2.write(sentence_3)
    input_c2.write(sentence_4)
    sentence_1 = "參賽者以台灣上市櫃股票為標的，依不同的考量因素，以總體經濟、產業、計量模型、基本面、技術面等分析為基礎，進一步選擇台股以建構相對應之投資組合。參賽學生將經濟學、財務管理與投資學理論實現於台股的投資組合配置，競賽評分重點在於投資組合配置的邏輯依據，參賽學生將獲得與真實證券市場接軌的實戰演練，建立正確的投資理財觀念並與全台學生交流；指導老師亦藉此了解學生的學習應用成效，以提昇未來的教學績效。"
    sentence_2 = "報名時間：2024年12月20日至2024年12月30日"
    sentence_3 = "計畫繳交：2025年01月05日至2025年01月10日"
    sentence_4 = "得獎公告：2025年01月22日"
    input_c2.subheader("B.ESG投資計畫應用組：")
    input_c2.write(sentence_1)
    input_c2.write(sentence_2)
    input_c2.write(sentence_3)
    input_c2.write(sentence_4)
    sentence_1 = "有關以金融科技運用為主題之創新商業模式、創新創業、行動商務等相關主題之企劃案，例如：資安、支付、大數據、智能理財、人工智慧、AML/KYC、雲端服務、區塊鏈、生物辨識、法遵科技、保險科技、借貸及物聯網。因金融科技發展受限於法規機制之下，如何將金融科技創新服務且又符合法規，期許透過金融科技，營造一個更具金融包容性的友善科技應用環境。"
    sentence_2 = "報名時間：2024年12月20日至2024年12月30日"
    sentence_3 = "計畫繳交：2025年01月05日至2025年01月10日"
    sentence_4 = "得獎公告：2025年01月22日"
    input_c2.subheader("C.金融科技應用組：")
    input_c2.write(sentence_1)
    input_c2.write(sentence_2)
    input_c2.write(sentence_3)
    input_c2.write(sentence_4)
    sentence_1 = "有關以大數據創意專題為主題之創新創業、服務業管理、行動商務等相關主題之專題企劃案，期許透過大數據，營造一個更具包容性的友善科技應用環境。"
    sentence_2 = "報名時間：2024年12月20日至2024年12月30日"
    sentence_3 = "計畫繳交：2025年01月05日至2025年01月10日"
    sentence_4 = "得獎公告：2025年01月22日"
    input_c2.subheader("D.大數據創意專題企劃組：")
    input_c2.write(sentence_1)
    input_c2.write(sentence_2)
    input_c2.write(sentence_3)
    input_c2.write(sentence_4)
with tab4:
    container4 = st.container()
    input_d1, input_d2, input_d3 = container4.columns((1, 3, 1))
    sentence_1 = "請於報名時間內填寫 Google 表單：https://forms.gle/p2eXJpcWAKaFw5Lm9"
    sentence_2 = "請於計畫繳交時間內寄信至：chuma0702@gmail.com"
    sentence_3 = "信件主旨請寫：組別_作品名稱"
    sentence_4 = "(舉例：ESG綠色管理組_環境保護專題)"
    sentence_5 = "上傳不超過20頁的簡報檔，超過不予評分。"
    sentence_6 = "(請轉成PDF後上傳)。"
    sentence_7 = "評分類別：書面審查"
    df = pd.DataFrame(
        {
            '評分項目': ['創意概念', '可行性分析', '簡報內容(PPT)'],
            '比例': ['20%', '20%', '60%']
        }
    )
    input_d2.header("評分標準：")
    input_d2.subheader("報名資料：")
    input_d2.write(sentence_1)
    input_d2.subheader("計畫繳交：")
    input_d2.write(sentence_2)
    input_d2.write(sentence_3)
    input_d2.write(sentence_4)
    input_d2.subheader("繳交內容：")
    input_d2.write(sentence_5)
    input_d2.write(sentence_6)
    input_d2.subheader("分數標準：")
    input_d2.dataframe(df, hide_index=True)
    input_d2.write(sentence_7)
with tab5:
    container5 = st.container()
    input_e1, input_e2, input_e3 = container5.columns((1, 3, 1))
    sentence_1 = "依據各競賽類別提供下列獎項"
    sentence_2 = "第一名：獎金500元，並頒發參賽學生及指導老師獎狀每人乙紙。"
    sentence_3 = "第二名：獎金300元，並頒發參賽學生及指導老師獎狀每人乙紙。"
    sentence_4 = "第三名：獎金200元，並頒發參賽學生及指導老師獎狀每人乙紙。"
    sentence_5 = "為感謝參加同學之辛勞，每人頒發感謝函乙紙。"
    input_e2.header("參賽獎勵：")
    input_e2.write(sentence_1)
    input_e2.write(sentence_2)
    input_e2.write(sentence_3)
    input_e2.write(sentence_4)
    input_e2.write(sentence_5)
with tab6:
    container6 = st.container()
    input_f1, input_f2, input_f3 = container6.columns((1, 3, 1))
    sentence_1 = "報名網址：https://forms.gle/p2eXJpcWAKaFw5Lm9"
    sentence_2 = "一、參賽作品均不退件，參賽者請自行保留參賽作品之原始檔備查。"
    sentence_3 = "二、競賽參加之議題不可參加過其他專題競賽，否則取消比賽資格，且通報學術倫理。"
    sentence_4 = "三、凡報名參賽者，即視為同意本報名簡章的各項內容及規定，若有未盡事宜或不可抗拒因素而有所異動，主辦單位保有變更內容權力，請參賽者若有疑問請寄信主辦單位。"
    sentence_5 = "信箱：chuma0702@gmail.com (學校服務組)"
    sentence_6 = "新北市板橋區板新社區發展協會。"
    input_f2.header("競賽資訊：")
    input_f2.subheader("報名資訊：")
    input_f2.write(sentence_1)
    input_f2.subheader("競賽規則：")
    input_f2.write(sentence_2)
    input_f2.write(sentence_3)
    input_f2.write(sentence_4)
    input_f2.subheader("聯絡方式：")
    input_f2.write(sentence_5)
    input_f2.subheader("主辦單位：")
    input_f2.write(sentence_6)
    input_f2.image('./協會logo.jpg')





