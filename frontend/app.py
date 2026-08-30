import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="АКВА-СТРАЖ", page_icon="", layout="wide")

st.title(" АКВА-СТРАЖ")
st.subheader("Система мониторинга качества воды")

st.sidebar.header("⚙️ Настройки")
station_id = st.sidebar.text_input("ID станции", "STATION_001")

MOCK_DATA = {
    "station_id": "STATION_001",
    "status": "online",
    "risk_index": 0.15,
    "last_reading": {
        "dissolved_oxygen": 7.8,
        "ph": 7.4,
        "temperature": 11.5,
        "conductivity": 4.8,
        "turbidity": 8.2
    }
}

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Станция", station_id)

with col2:
    status = MOCK_DATA
    st.metric("Индекс риска", f"{status['risk_index']:.3f}")

with col3:
    st.metric("Статус", "🟢 Online")

st.markdown("---")
st.subheader("📊 Текущие показатели")

col1, col2, col3, col4, col5 = st.columns(5)

reading = status['last_reading']

with col1:
    st.metric("💧 Кислород", f"{reading['dissolved_oxygen']:.2f} мг/л")
with col2:
    st.metric("⚗️ pH", f"{reading['ph']:.2f}")
with col3:
    st.metric("🌡️ Температура", f"{reading['temperature']:.2f}°C")
with col4:
    st.metric("⚡ Электропроводность", f"{reading['conductivity']:.2f} мСм/см")
with col5:
    st.metric("️ Мутность", f"{reading['turbidity']:.2f} NTU")

st.markdown("---")
st.subheader("📈 График индекса риска")

df = pd.DataFrame({
    'Время': pd.date_range(start='2024-01-01', periods=24, freq='h'),
    'Риск': [0.1 + 0.05 * i for i in range(24)]
})

fig = px.line(df, x='Время', y='Риск', title='Динамика индекса риска')
st.plotly_chart(fig, use_container_width=True)

st.sidebar.info("""
**Нормативы:**
- Кислород: 8.0 мг/л
- pH: 7.5
- Температура: 12°C
- Электропроводность: 5.0 мСм/см
- Мутность: 10 NTU
""")
