import plotly.graph_objects as go
import pandas as pd

COLORS = {
    "green":      "#4AD295",
    "dark_green": "#1D9E75",
    "amber":      "#EF9F27",
    "red":        "#EF4444",
    "bg":         "rgba(0,0,0,0)",
    "grid":       "rgba(74,210,149,0.08)",
    "text":       "rgba(255,255,255,0.7)",
    "title":      "#FFFFFF",
}

LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Inter, Arial", color=COLORS["text"], size=12),
    margin=dict(l=20, r=20, t=40, b=20),
    showlegend=False,
)


def revenue_profit_chart(insights):
    try:
        revenue = insights.get('total_revenue', 0)
        profit = insights.get('total_profit', 0)
        loss = abs(min(profit, 0))
        actual_profit = max(profit, 0)

        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=["Revenue", "Profit", "Loss"],
            y=[revenue, actual_profit, loss],
            marker_color=[COLORS["green"], COLORS["dark_green"], COLORS["red"]],
            marker_line_color="rgba(0,0,0,0)",
            text=[f"Rs {revenue:,.0f}", f"Rs {actual_profit:,.0f}", f"Rs {loss:,.0f}"],
            textposition="outside",
            textfont=dict(color=COLORS["text"], size=11),
            hovertemplate="%{x}: Rs %{y:,.0f}<extra></extra>",
            width=0.5
        ))

        fig.update_layout(
            **LAYOUT,
            title=dict(text="Revenue vs Profit vs Loss",
                      font=dict(color=COLORS["title"], size=14), x=0),
            yaxis=dict(gridcolor=COLORS["grid"], showgrid=True,
                      zeroline=False, tickformat=",.0f",
                      tickfont=dict(size=10)),
            xaxis=dict(showgrid=False),
            height=300
        )
        return fig
    except Exception as e:
        print(f"Revenue chart error: {e}")
        return None


def daily_trend_chart(df):
    try:
        if 'Order Date' not in df.columns or 'Profit' not in df.columns:
            return None

        df_copy = df.copy()
        df_copy['Order Date'] = pd.to_datetime(
            df_copy['Order Date'], dayfirst=True, errors='coerce')
        df_copy = df_copy.dropna(subset=['Order Date'])
        daily = df_copy.groupby('Order Date')['Profit'].sum().reset_index()
        daily = daily.sort_values('Order Date')
        daily['Rolling'] = daily['Profit'].rolling(window=7, min_periods=1).mean()

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=daily['Order Date'], y=daily['Profit'],
            mode='lines', name='Daily Profit',
            line=dict(color=COLORS["green"], width=1.5),
            fill='tozeroy', fillcolor='rgba(74,210,149,0.08)',
            hovertemplate="%{x|%d %b}: Rs %{y:,.0f}<extra></extra>"
        ))
        fig.add_trace(go.Scatter(
            x=daily['Order Date'], y=daily['Rolling'],
            mode='lines', name='7-day Average',
            line=dict(color=COLORS["amber"], width=2, dash='dot'),
            hovertemplate="7-day avg: Rs %{y:,.0f}<extra></extra>"
        ))

        fig.update_layout(
            **LAYOUT,
            title=dict(text="Daily Profit Trend",
                      font=dict(color=COLORS["title"], size=14), x=0),
            yaxis=dict(gridcolor=COLORS["grid"], showgrid=True,
                      zeroline=True, zerolinecolor=COLORS["red"],
                      tickformat=",.0f", tickfont=dict(size=10)),
            xaxis=dict(showgrid=False, tickfont=dict(size=10)),
            showlegend=True,
            legend=dict(font=dict(color=COLORS["text"], size=11),
                       bgcolor="rgba(0,0,0,0)"),
            height=300
        )
        return fig
    except Exception as e:
        print(f"Daily trend error: {e}")
        return None


def product_performance_chart(df):
    try:
        profit_col = 'Product Sub-Category' \
            if 'Product Sub-Category' in df.columns \
            else 'Product Type'

        if profit_col not in df.columns or 'Profit' not in df.columns:
            return None

        product_profit = df.groupby(profit_col)['Profit'].sum().sort_values()
        colors = [COLORS["red"] if p < 0 else COLORS["green"]
                 for p in product_profit.values]

        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=product_profit.values,
            y=product_profit.index,
            orientation='h',
            marker_color=colors,
            marker_line_color="rgba(0,0,0,0)",
            text=[f"Rs {p:,.0f}" for p in product_profit.values],
            textposition='outside',
            textfont=dict(color=COLORS["text"], size=10),
            hovertemplate="%{y}: Rs %{x:,.0f}<extra></extra>"
        ))

        fig.update_layout(
            **LAYOUT,
            title=dict(text="Product Performance",
                      font=dict(color=COLORS["title"], size=14), x=0),
            xaxis=dict(gridcolor=COLORS["grid"], showgrid=True,
                      zeroline=True, zerolinecolor=COLORS["red"],
                      zerolinewidth=1.5, tickformat=",.0f",
                      tickfont=dict(size=10)),
            yaxis=dict(showgrid=False, tickfont=dict(size=11)),
            height=max(250, len(product_profit) * 45)
        )
        return fig
    except Exception as e:
        print(f"Product chart error: {e}")
        return None


def profit_margin_gauge(margin, business_type="Medical Shop"):
    try:
        benchmarks = {
            "Medical Shop":    (18, 25),
            "Kirana Store":    (10, 20),
            "Textile Shop":    (30, 45),
            "Shoe Showroom":   (40, 50),
            "Fancy Store":     (60, 70),
            "Vegetable Stall": (15, 25),
            "Pan Shop":        (25, 40),
            "Hardware Store":  (20, 35),
        }
        low, high = benchmarks.get(business_type, (15, 30))

        if margin < low:
            color = COLORS["red"]
            status = "Below Target"
        elif margin > high:
            color = COLORS["dark_green"]
            status = "Excellent"
        else:
            color = COLORS["green"]
            status = "On Target"

        fig = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=margin,
            number=dict(suffix="%", font=dict(color=COLORS["title"], size=28)),
            delta=dict(
                reference=(low + high) / 2,
                increasing=dict(color=COLORS["green"]),
                decreasing=dict(color=COLORS["red"]),
                font=dict(size=14)
            ),
            title=dict(
                text=f"Profit Margin<br>"
                     f"<span style='font-size:12px;color:{COLORS['text']}'>"
                     f"Target: {low}-{high}% ({status})</span>",
                font=dict(color=COLORS["title"], size=14)
            ),
            gauge=dict(
                axis=dict(range=[0, max(60, margin + 10)],
                         tickcolor=COLORS["text"],
                         ticksuffix="%"),
                bar=dict(color=color, thickness=0.7),
                bgcolor="rgba(74,210,149,0.05)",
                bordercolor="rgba(74,210,149,0.2)",
                steps=[
                    dict(range=[0, low], color="rgba(239,68,68,0.1)"),
                    dict(range=[low, high], color="rgba(74,210,149,0.1)"),
                    dict(range=[high, max(60, margin+10)],
                         color="rgba(29,158,117,0.15)"),
                ],
                threshold=dict(
                    line=dict(color=COLORS["amber"], width=2),
                    thickness=0.75,
                    value=(low + high) / 2
                )
            )
        ))
        fig.update_layout(**LAYOUT, height=250)
        return fig
    except Exception as e:
        print(f"Gauge error: {e}")
        return None


def day_performance_chart(df):
    try:
        if 'Order Date' not in df.columns or 'Profit' not in df.columns:
            return None

        df_copy = df.copy()
        df_copy['Order Date'] = pd.to_datetime(
            df_copy['Order Date'], dayfirst=True, errors='coerce')
        df_copy['Day'] = df_copy['Order Date'].dt.day_name()

        day_order = ['Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday', 'Sunday']
        daily = df_copy.groupby('Day')['Profit'].sum().reindex(
            day_order).fillna(0)

        max_day = daily.idxmax()
        colors = [COLORS["dark_green"] if d == max_day
                 else COLORS["green"] for d in daily.index]

        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=daily.index, y=daily.values,
            marker_color=colors,
            marker_line_color="rgba(0,0,0,0)",
            text=[f"Rs {v:,.0f}" for v in daily.values],
            textposition='outside',
            textfont=dict(color=COLORS["text"], size=9),
            hovertemplate="%{x}: Rs %{y:,.0f}<extra></extra>"
        ))

        fig.update_layout(
            **LAYOUT,
            title=dict(text="Sales by Day of Week",
                      font=dict(color=COLORS["title"], size=14), x=0),
            yaxis=dict(gridcolor=COLORS["grid"], showgrid=True,
                      zeroline=False, tickformat=",.0f",
                      tickfont=dict(size=10)),
            xaxis=dict(showgrid=False, tickfont=dict(size=11)),
            height=280
        )
        return fig
    except Exception as e:
        print(f"Day chart error: {e}")
        return None