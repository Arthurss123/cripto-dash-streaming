import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(page_title="📊 Dashboard de Moedas", layout="wide")
st.title("💰 Dashboard de Transações de Moedas")

def get_data():
    conn = psycopg2.connect(
        dbname="kafka_streaming",
        user="postgres",
        password="19081969",
        host="localhost",
        port="5432"
    )
    query = "SELECT * FROM transacoes_moedas"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

df = get_data()
df['data_transacao'] = pd.to_datetime(df['data_transacao'])

st.sidebar.header("🔎 Filtros")
moedas = df['moeda'].unique()
moeda_escolhida = st.sidebar.selectbox("Escolha a moeda", moedas)

periodo = st.sidebar.selectbox(
    "Período",
    ("Últimas 24h", "Últimos 7 dias", "Últimos 30 dias", "Tudo")
)

df_filtrado = df[df['moeda'] == moeda_escolhida]

agora = datetime.now()
if periodo == "Últimas 24h":
    df_filtrado = df_filtrado[df_filtrado['data_transacao'] >= agora - timedelta(days=1)]
elif periodo == "Últimos 7 dias":
    df_filtrado = df_filtrado[df_filtrado['data_transacao'] >= agora - timedelta(days=7)]
elif periodo == "Últimos 30 dias":
    df_filtrado = df_filtrado[df_filtrado['data_transacao'] >= agora - timedelta(days=30)]


if not df_filtrado.empty:
    media = df_filtrado['valor_venda'].mean()
    minimo = df_filtrado['valor_venda'].min()
    maximo = df_filtrado['valor_venda'].max()
    ultimo = df_filtrado.sort_values(by='data_transacao', ascending=False)['valor_venda'].iloc[0]
    primeiro = df_filtrado.sort_values(by='data_transacao')['valor_venda'].iloc[0]
    variacao = ((ultimo - primeiro) / primeiro) * 100 if primeiro != 0 else 0

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("📈 Preço Médio", f"R$ {media:.2f}")
    col2.metric("🔼 Máximo", f"R$ {maximo:.2f}")
    col3.metric("🔽 Mínimo", f"R$ {minimo:.2f}")
    col4.metric("📊 Variação %", f"{variacao:.2f} %")

    fig = px.line(
        df_filtrado.sort_values(by="data_transacao"),
        x="data_transacao",
        y="valor_venda",
        title=f"📉 Variação de preço da moeda {moeda_escolhida}",
        markers=True
    )
    st.plotly_chart(fig, use_container_width=True)

    csv = df_filtrado.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Baixar dados CSV", data=csv, file_name="transacoes_filtradas.csv", mime="text/csv", key=f"download_{moeda_escolhida}")

    with st.expander("🧾 Ver dados brutos"):
        st.dataframe(df_filtrado)

else:
    st.warning("⚠️ Nenhum dado encontrado para os filtros selecionados.")
