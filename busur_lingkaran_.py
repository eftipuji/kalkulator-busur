import streamlit as st
import math
import time
import random
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# --- Fungsi Inti Perhitungan ---
def hitung_busur_juring(radius, sudut_derajat):
    """
    Menghitung panjang busur dan luas juring lingkaran.
    Mengembalikan tuple (panjang_busur, luas_juring) atau (None, None) jika input tidak valid.
    """
    if radius <= 0:
        return None, None # Jari-jari harus positif

    sudut_radian = math.radians(sudut_derajat)
    panjang_busur = radius * sudut_radian
    luas_juring = 0.5 * (radius**2) * sudut_radian
    return panjang_busur, luas_juring

# --- Fungsi untuk Membuat Visualisasi Lingkaran ---
def plot_lingkaran_juring(radius, sudut_derajat):
    fig = go.Figure()

    # Gambar Lingkaran Penuh
    theta_full = np.linspace(0, 2 * np.pi, 100)
    x_full = radius * np.cos(theta_full)
    y_full = radius * np.sin(theta_full)
    fig.add_trace(go.Scatter(x=x_full, y=y_full, mode='lines', name='Lingkaran',
                             line=dict(color='lightgray', width=2)))

    # Gambar Juring
    if sudut_derajat != 0 and radius > 0:
        sudut_radian = math.radians(sudut_derajat)
        
        # Batasi sudut agar tidak terlalu berputar dalam visualisasi jika melebihi 360
        visual_sudut_radian = sudut_radian % (2 * math.pi)
        if visual_sudut_radian < 0:
            visual_sudut_radian += 2 * math.pi

        # Titik-titik untuk juring
        theta_juring = np.linspace(0, visual_sudut_radian, 50)
        x_juring_busur = radius * np.cos(theta_juring)
        y_juring_busur = radius * np.sin(theta_juring)

        x_juring = np.concatenate([[0], x_juring_busur, [0]])
        y_juring = np.concatenate([[0], y_juring_busur, [0]])

        fig.add_trace(go.Scatter(x=x_juring, y=y_juring, mode='lines', fill='toself', name='Juring',
                                 fillcolor='rgba(100, 149, 237, 0.5)',
                                 line=dict(color='cornflowerblue', width=2)))
        
        # Garis radius
        fig.add_trace(go.Scatter(x=[0, radius * math.cos(0)], y=[0, radius * math.sin(0)],
                                 mode='lines', name='Radius 1', line=dict(color='darkblue', width=2)))
        if visual_sudut_radian > 0:
             fig.add_trace(go.Scatter(x=[0, radius * math.cos(visual_sudut_radian)], y=[0, radius * math.sin(visual_sudut_radian)],
                                 mode='lines', name='Radius 2', line=dict(color='darkblue', width=2)))
        
        # --- Menambahkan Label pada Visualisasi ---
        # Titik Pusat O
        fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers+text',
                                 marker=dict(size=8, color='black'),
                                 text=['O'], textposition='bottom right', textfont=dict(size=14, color='black')))
        
        # Titik A (pada sudut 0)
        fig.add_trace(go.Scatter(x=[radius * math.cos(0)], y=[radius * math.sin(0)],
                                 mode='markers+text',
                                 marker=dict(size=8, color='red'),
                                 text=['A'], textposition='top right', textfont=dict(size=14, color='red')))
        
        # Titik B (pada sudut visual_sudut_radian)
        fig.add_trace(go.Scatter(x=[radius * math.cos(visual_sudut_radian)], y=[radius * math.sin(visual_sudut_radian)],
                                 mode='markers+text',
                                 marker=dict(size=8, color='red'),
                                 text=['B'], textposition='top left', textfont=dict(size=14, color='red')))
                                 
        # Posisi Teks Sudut Alfa (di tengah juring)
        mid_angle = visual_sudut_radian / 2
        label_radius_offset = radius * 0.4
        fig.add_trace(go.Scatter(x=[label_radius_offset * math.cos(mid_angle)],
                                 y=[label_radius_offset * math.sin(mid_angle)],
                                 mode='text',
                                 text=[r'$\alpha$'],
                                 textposition='middle center', textfont=dict(size=20, color='darkgreen')))


    # Pengaturan layout
    max_val = radius * 1.2
    fig.update_xaxes(range=[-max_val, max_val], showgrid=False, zeroline=False, showticklabels=False)
    fig.update_yaxes(range=[-max_val, max_val], showgrid=False, zeroline=False, showticklabels=False, scaleanchor="x", scaleratio=1)
    fig.update_layout(title='Visualisasi Lingkaran dan Juring', showlegend=False,
                      plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')

    return fig


# --- Halaman Menu 1: Kalkulator Busur & Juring ---
def kalkulator_menu():
    st.title("📏 Kalkulator Panjang Busur & Luas Juring Lingkaran 📐")
    st.markdown("""
    Selamat datang di kalkulator interaktif! Masukkan nilai **
