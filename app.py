import streamlit as st
import pandas as pd
import numpy as np

# Mobil uyumlu geniş ekran ve sayfa ayarları
st.set_page_config(page_title="Emlak Yıldızı - Karar Destek Sistemi", layout="wide", initial_sidebar_state="collapsed")

# Sabit Şifre Koruması
PASSWORD = "130604"

def check_password():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    
    if not st.session_state.authenticated:
        st.title("🌟 Emlak Yıldızı Giriş Masası")
        st.write("Sistem Kocaeli bölge analitiği ve müşteri portföyünü içerir.")
        user_input = st.text_input("Giriş Şifresi:", type="password")
        if st.button("Sisteme Giriş Yap"):
            if user_input == PASSWORD:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Hatalı Şifre! Lütfen tekrar deneyiniz.")
        return False
    return True

if check_password():
    # --- CANLI HABER BANDI ---
    st.markdown(
        """
        <div style="background-color:#1e293b; padding:8px; border-radius:5px; margin-bottom:15px; text-align:center;">
            <span style="color:#f59e0b; font-weight:bold;">🔥 CANLI BÖLGE AKIŞI:</span> 
            <marquee style="color:white; font-family:sans-serif;" scrollamount="5">
                Kocaeli genelinde amortisman süreleri optimize edildi... Kartepe ve Başiskele bölgesinde arsa taleplerinde %14 artış gözleniyor... İzmit merkezde kiralık konut stoku daralıyor...
            </marquee>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # --- ANA BAŞLIK ---
    st.title("✨ Emlak Yıldızı Pro - Mobil Saha Yönetimi")
    st.caption("Kocaeli Gayrimenkul Yatırım ve Karar Destek Sihirbazı")
    
    # Sekmeli Tasarım (Sahada hızlı geçiş için harika)
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Yatırım Sihirbazı (ROI)", "🔍 Bölge Röntgeni", "💼 Müşteri Masası & CRM", "🏠 İlan Havuzu"])
    
    # ==========================================
    # TAB 1: YATIRIM SİHİRBAZI & ROI (SAHADA MÜŞTERİ KAPATAN MODÜL)
    # ==========================================
    with tab1:
        st.header("💰 Canlı Yatırım & ROI Analizörü")
        st.write("Müşterinizin yanındayken bütçe ve beklenti simülasyonunu anında yapın.")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            client_name = st.text_input("Müşteri Adı Soyadı:", "Ahmet Yılmaz")
            budget = st.number_input("Yatırım Bütçesi (TL):", min_value=1000000, value=4500000, step=100000)
            target_type = st.selectbox("Hedef Portföy Tipi:", ["Konut", "Ticari (Dükkan/Ofis)", "Arsa/Arazi"])
            expected_years = st.slider("Yatırım Tutma Süresi (Yıl):", 1, 10, 5)
            
            # Arka plandaki zeki bölge eşleştirme simülasyonu
            success_score = 92 if budget >= 4000000 else 78
            recommended_region = "Başiskele / İzmit Merkez" if target_type == "Konut" else "Kartepe / Dilovası"
            
        with col2:
            st.subheader(f"🎯 {client_name} İçin Özel Analiz Raporu")
            
            m1, m2 = st.columns(2)
            m1.metric("Önerilen En Uygun Bölge", recommended_region)
            m2.metric("Yatırım Başarı Skoru", f"%{success_score}")
            
            st.info("💡 **Yapay Zeka Yatırım Notu:** Girdiğiniz bütçe, seçilen bölgedeki amortisman süreleri ve yıllık değerlenme trendleri dikkate alındığında Kocaeli ortalamasının üzerinde bir prim potansiyeli sunuyor.")
            
            # Basit Gelecek Değer Projeksiyon Tablosu
            st.write("📈 **Yıllara Göre Tahmini Varlık Değer Çizelgesi (Enflasyon Arındırılmış):**")
            years_data = [f"Yıl {i}" for i in range(1, expected_years + 1)]
            projected_values = [str(int(budget * (1.15 ** i))) + " TL" for i in range(1, expected_years + 1)]
            
            roi_df = pd.DataFrame({
                "Zaman": years_data,
                "Tahmini Portföy Değeri": projected_values
            })
            st.table(roi_df)
            
            # Anlık WhatsApp Metni Oluşturma
            whatsapp_msg = f"Merhaba {client_name}, bugün sizinle görüştüğümüz {budget:,} TL bütçeli {target_type} yatırımı için en uygun bölge %{success_score} başarı skoruyla {recommended_region} olarak analiz edilmiştir. Detayları ofisimizde kahve eşliğinde netleştirmek üzere bekliyorum."
            st.download_button("📲 Dijital Teklif Özeti İndir", whatsapp_msg, file_name="emlak_yildizi_teklif.txt")
            
    # ==========================================
    # TAB 2: BÖLGE RÖNTGENİ
    # ==========================================
    with tab2:
        st.header("📍 Kocaeli İlçe Veri Bankası")
        ilce = st.selectbox("Detayını İncelemek İstediğiniz İlçe:", ["İzmit", "Başiskele", "Kartepe", "Gebze", "Gölcük", "Derince"])
        
        # Statik veri tabanı simülasyonu (Numpy tipi hatalarından arındırılmış saf string yapısı)
        ilce_veri = {
            "İzmit": {"m2": "28.500 TL", "amortisman": "16 Yıl", "avantaj": "Merkezi lokasyon, yüksek kiralık talebi.", "ulasim": "Merkezde / Havalimanı 30 dk"},
            "Başiskele": {"m2": "34.000 TL", "amortisman": "18 Yıl", "avantaj": "Yeni lüks konut projeleri, elit profil.", "ulasim": "Merkeze 10 dk / İstanbul 60 dk"},
            "Kartepe": {"m2": "31.000 TL", "amortisman": "19 Yıl", "avantaj": "Turizm teşviki, sürekli değerlenen arsa stoğu.", "ulasim": "Merkeze 15 dk / Kayak Merkezi 20 dk"}
        }
        
        secilen = ilce_veri.get(ilce, {"m2": "Veri Yok", "amortisman": "Veri Yok", "avantaj": "Genel Kocaeli gelişimi içinde.", "ulasim": "Ulaşım akslarına yakın"})
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Ortalama m² Fiyatı", secilen["m2"])
        c2.metric("Ortalama Amortisman Süresi", secilen["amortisman"])
        c3.metric("Ulaşım Sürat Faktörü", secilen["ulasim"])
        
        st.warning(f"⚠️ **Bölge Karakteristiği:** {secilen['avantaj']}")

    # ==========================================
    # TAB 3: MÜŞTERİ CRM & WHATSAPP ENTEGRASYONU
    # ==========================================
    with tab3:
        st.header("👥 Müşteri CRM Masası")
        # Basit statik müşteri veri tablosu
        crm_data = pd.DataFrame({
            "Müşteri": ["Mehmet Öz", "Ayşe Can", "Bülent Yılmaz"],
            "Telefon": ["+905551112233", "+905423334455", "+905329998877"],
            "İlgi Alanı": ["İzmit Ticari", "Başiskele Villa", "Kartepe Arsa"],
            "Durum": ["Teklif Verildi", "Sıcak Takip", "Randevu Ayarlandı"]
        })
        st.dataframe(crm_data, use_container_width=True)
        st.info("ℹ️ Mobil cihazınızdan müşterinin yanındaki 'Telefon' numarasını kopyalayarak hızlıca WhatsApp entegrasyonu sağlayabilirsiniz.")

    # ==========================================
    # TAB 4: İLAN HAVUZU
    # ==========================================
    with tab4:
        st.header("🏠 Sahibinden / Portföy Yönetim Havuzu")
        st.write("Kendi kriterlerinize göre anlık portföy durumunu filtreleyin.")
        
        f_durum = st.radio("İlan Durumu Filtresi:", ["Aktif Portföy", "Pasif / Satılmış"], horizontal=True)
        
        # Örnek ilan tablosu
        ilan_data = pd.DataFrame({
            "İlan Başlığı": ["İzmit Merkez Satılık 3+1", "Başiskele Sahile Yakın Dubleks", "Kartepe İmar sınırında Arsa"],
            "Fiyat": ["3.850.000 TL", "6.200.000 TL", "2.900.000 TL"],
            "Bina Yaşı": ["5", "0 (Yeni)", "Yok"],
            "Durum": ["Aktif Portföy", "Aktif Portföy", "Pasif / Satılmış"]
        })
        
        filtrelenmiş_ilanlar = ilan_data[ilan_data["Durum"] == f_durum]
        st.dataframe(filtrelenmiş_ilanlar, use_container_width=True)