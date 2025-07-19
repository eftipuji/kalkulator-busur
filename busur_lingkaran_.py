# --- Main Aplikasi Streamlit ---
def main():
    # Konfigurasi halaman umum
    st.set_page_config(
        page_title="Aplikasi Geometri Lingkaran Interaktif 🌌",
        page_icon="🧭",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.sidebar.title("Navigasi Aplikasi")
    menu_selection = st.sidebar.radio(
        "Pilih Menu:",
        ["Kalkulator Busur & Juring", "Penjelasan Rumus", "Lembar Kerja"] # Menu baru ditambahkan di sini
    )

    if menu_selection == "Kalkulator Busur & Juring":
        kalkulator_menu()
    elif menu_selection == "Penjelasan Rumus":
        penjelasan_rumus_menu()
    elif menu_selection == "Lembar Kerja": # Kondisi baru untuk menu "Lembar Kerja"
        lembar_kerja_menu() # Panggil fungsi baru untuk menampilkan konten lembar kerja

    current_time = time.strftime("%A, %d %B %Y", time.localtime())
    st.sidebar.markdown("---")
    st.sidebar.caption(f"Versi Aplikasi v2.3. Dibuat dengan ❤️ di Pekalongan, {current_time}.")

# --- Halaman Menu 3: Lembar Kerja ---
def lembar_kerja_menu():
    st.title("📚 Lembar Kerja & Sumber Daya Tambahan 📚")
    st.markdown("""
    Di sini Anda dapat menemukan lembar kerja dan sumber daya tambahan untuk membantu Anda
    lebih memahami konsep panjang busur dan luas juring lingkaran.
    """)

    st.write("---")

    st.header("🔗 Tautan ke Lembar Kerja")
    st.markdown("""
    Klik tautan di bawah ini untuk mengakses folder Google Drive yang berisi lembar kerja:
    """)
    # Menambahkan tautan dengan Markdown
    st.markdown("[Akses Lembar Kerja di Google Drive](https://drive.google.com/drive/folders/1o8V2F_DG2JiIRJSgac105okyHnXJKTIb)")
    
    st.info("Pastikan Anda memiliki akses internet untuk membuka tautan ini.")
    st.write("---")
    st.markdown("""
    Kami berharap lembar kerja ini dapat menjadi alat bantu yang bermanfaat dalam proses belajar Anda!
    """)
