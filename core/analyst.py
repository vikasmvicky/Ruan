import pandas as pd
import numpy as np


def clean_insights(insights):
    """Convert numpy types to Python native types"""
    cleaned = {}

    for key, value in insights.items():
        try:
            cleaned[key] = value.item()
        except AttributeError:
            cleaned[key] = value

    return cleaned


def load_sales_data(file):
    """Load uploaded sales CSV or Excel file"""

    try:
        name = file.name.lower()

        if name.endswith('.csv'):

            try:
                df = pd.read_csv(file, encoding='utf-8')

            except UnicodeDecodeError:

                file.seek(0)

                try:
                    df = pd.read_csv(file, encoding='latin1')

                except Exception:
                    file.seek(0)
                    df = pd.read_csv(file, encoding='cp1252')

        elif name.endswith(('.xlsx', '.xls')):

            df = pd.read_excel(
                file,
                engine='openpyxl'
            )

        else:
            return None

        return df

    except Exception as e:
        print(f"File load error: {e}")
        return None


def load_retail_database():
    """Load Indian retail dataset"""

    try:
        df = pd.read_excel(
            "data/INDIA_RETAIL_DATA.xlsx",
            engine='openpyxl'
        )

        return df

    except Exception as e:
        print(f"Error loading retail database: {e}")
        return None


def analyse_sales(df):
    """Core analysis using Indian retail dataset"""

    insights = {}

    try:

        # Total orders
        insights['total_orders'] = len(df)

        # Revenue
        if 'Sales' in df.columns:

            insights['total_revenue'] = round(
                df['Sales'].sum(),
                2
            )

            insights['avg_order_value'] = round(
                df['Sales'].mean(),
                2
            )

        # Profit
        if 'Profit' in df.columns:

            insights['total_profit'] = round(
                df['Profit'].sum(),
                2
            )

            insights['avg_profit'] = round(
                df['Profit'].mean(),
                2
            )

            insights['profit_margin'] = round(
                (
                    df['Profit'].sum()
                    / df['Sales'].sum()
                ) * 100,
                2
            ) if df['Sales'].sum() > 0 else 0

            insights['profitable_orders'] = int(
                (df['Profit'] > 0).sum()
            )

            insights['loss_orders'] = int(
                (df['Profit'] < 0).sum()
            )

        # Product analysis
        if (
            'Product Type' in df.columns
            and 'Profit' in df.columns
        ):

            product_profit = df.groupby(
                'Product Type'
            )['Profit'].sum()

            insights['best_product'] = (
                product_profit.idxmax()
            )

            insights['best_product_profit'] = round(
                product_profit.max(),
                2
            )

            insights['worst_product'] = (
                product_profit.idxmin()
            )

            insights['worst_product_profit'] = round(
                product_profit.min(),
                2
            )

        # Subcategory analysis
        if (
            'Product Sub-Category' in df.columns
            and 'Profit' in df.columns
        ):

            sub_profit = df.groupby(
                'Product Sub-Category'
            )['Profit'].sum().sort_values(
                ascending=False
            )

            insights['best_subcategory'] = (
                sub_profit.index[0]
            )

            insights['worst_subcategory'] = (
                sub_profit.index[-1]
            )

        # City analysis
        if (
            'City' in df.columns
            and 'Profit' in df.columns
        ):

            city_profit = df.groupby(
                'City'
            )['Profit'].sum()

            insights['best_city'] = (
                city_profit.idxmax()
            )

            insights['worst_city'] = (
                city_profit.idxmin()
            )

        # Discount analysis
        if (
            'Discount offered' in df.columns
            and 'Profit' in df.columns
        ):

            high_discount = df[
                df['Discount offered'] > 0.2
            ]['Profit'].mean()

            low_discount = df[
                df['Discount offered'] <= 0.2
            ]['Profit'].mean()

            insights['discount_hurts'] = (
                high_discount < low_discount
            )

            insights['high_discount_profit'] = round(
                high_discount,
                2
            )

            insights['low_discount_profit'] = round(
                low_discount,
                2
            )

        # Date analysis
        if 'Order Date' in df.columns:

            df['Order Date'] = pd.to_datetime(
                df['Order Date'],
                dayfirst=True,
                errors='coerce'
            )

            df['Month'] = (
                df['Order Date'].dt.month
            )

            df['DayOfWeek'] = (
                df['Order Date'].dt.day_name()
            )

            monthly = df.groupby(
                'Month'
            )['Profit'].sum()

            if not monthly.empty:

                insights['best_month'] = int(
                    monthly.idxmax()
                )

                insights['worst_month'] = int(
                    monthly.idxmin()
                )

            daily = df.groupby(
                'DayOfWeek'
            )['Profit'].sum()

            if not daily.empty:

                insights['best_day'] = (
                    daily.idxmax()
                )

                insights['worst_day'] = (
                    daily.idxmin()
                )

        # Freight analysis
        if (
            'Freight Mode' in df.columns
            and 'Freight Expenses' in df.columns
        ):

            freight = df.groupby(
                'Freight Mode'
            )['Freight Expenses'].mean()

            insights['cheapest_freight'] = (
                freight.idxmin()
            )

            insights['cheapest_freight_cost'] = round(
                freight.min(),
                2
            )

        # Order priority analysis
        if (
            'Order Priority' in df.columns
            and 'Profit' in df.columns
        ):

            priority_profit = df.groupby(
                'Order Priority'
            )['Profit'].mean()

            insights['best_priority'] = (
                priority_profit.idxmax()
            )

        # Segment analysis
        if (
            'Segment' in df.columns
            and 'Profit' in df.columns
        ):

            segment_profit = df.groupby(
                'Segment'
            )['Profit'].sum()

            insights['best_segment'] = (
                segment_profit.idxmax()
            )

            insights['best_segment_profit'] = round(
                segment_profit.max(),
                2
            )

    except Exception as e:
        print(f"Analysis error: {e}")

    # Clean numpy types
    insights = clean_insights(insights)

    return insights


def generate_ruan_message(
    insights,
    business,
    city,
    lang="English"
):
    """Convert insights into simple business language"""

    if not insights:

        return (
            "Upload your sales data and "
            "I will analyse it for you!"
        )

    profit = insights.get('total_profit', 0)

    margin = insights.get(
        'profit_margin',
        0
    )

    loss_orders = insights.get(
        'loss_orders',
        0
    )

    discount_hurts = insights.get(
        'discount_hurts',
        False
    )

    msg = f"""
📊 Here is what I found for your {business} in {city}:

💰 Total Revenue: ₹{insights.get('total_revenue', 0):,.2f}

📈 Total Profit: ₹{profit:,.2f}

📉 Profit Margin: {margin}%

🛒 Total Orders: {insights.get('total_orders', 0)}

⚠️ Loss-making Orders: {loss_orders}

⭐ Best Product: {insights.get('best_product', 'N/A')}
Profit: ₹{insights.get('best_product_profit', 0):,.2f}

📦 Best Sub-Category:
{insights.get('best_subcategory', 'N/A')}

🏙️ Best City:
{insights.get('best_city', 'N/A')}

📅 Best Day:
{insights.get('best_day', 'N/A')}

📅 Worst Day:
{insights.get('worst_day', 'N/A')}

🚚 Cheapest Freight:
{insights.get('cheapest_freight', 'N/A')}

Avg Cost:
₹{insights.get('cheapest_freight_cost', 0):,.2f}
"""

    if discount_hurts:

        msg += f"""

⚠️ Discount Warning:

High discount orders average
₹{insights.get('high_discount_profit', 0):,.2f}

Low discount orders average
₹{insights.get('low_discount_profit', 0):,.2f}

Your heavy discounts are hurting profits!
"""

    return msg


def get_industry_benchmark(business_type):
    """Industry benchmark margins"""

    benchmarks = {

        "Medical Shop": {
            "normal": (18, 25),
            "red": 12,
            "green": 30
        },

        "Kirana Store": {
            "normal": (10, 20),
            "red": 8,
            "green": 25
        },

        "Textile Shop": {
            "normal": (30, 45),
            "red": 20,
            "green": 50
        },

        "Shoe Showroom": {
            "normal": (40, 50),
            "red": 30,
            "green": 55
        },

        "Fancy Store": {
            "normal": (60, 70),
            "red": 45,
            "green": 75
        },

        "Vegetable Stall": {
            "normal": (15, 25),
            "red": 10,
            "green": 30
        },

        "Pan Shop": {
            "normal": (25, 40),
            "red": 15,
            "green": 45
        },

        "Hardware Store": {
            "normal": (20, 35),
            "red": 15,
            "green": 40
        }
    }

    return benchmarks.get(
        business_type,
        {
            "normal": (15, 30),
            "red": 10,
            "green": 35
        }
    )


def get_city_context(city):
    """City based business context"""

    city_data = {

        "Bangalore": {
            "cost": "Very High",
            "min_profit": 50000,
            "rent": 25000
        },

        "Mumbai": {
            "cost": "Very High",
            "min_profit": 60000,
            "rent": 30000
        },

        "Chennai": {
            "cost": "Medium",
            "min_profit": 30000,
            "rent": 15000
        },

        "Hyderabad": {
            "cost": "Medium",
            "min_profit": 28000,
            "rent": 14000
        },

        "Mysuru": {
            "cost": "Low",
            "min_profit": 15000,
            "rent": 8000
        }
    }

    for key in city_data:

        if key.lower() in city.lower():
            return city_data[key]

    return {
        "cost": "Low",
        "min_profit": 10000,
        "rent": 5000
    }


def check_profit_health(
    total_profit,
    business_type,
    city,
    avg_margin
):
    """Business health evaluation"""

    benchmark = get_industry_benchmark(
        business_type
    )

    city_ctx = get_city_context(city)

    min_viable = city_ctx['min_profit']

    if total_profit < 0:

        status = "loss"

        color = "#FCEBEB"

        emoji = "🔴"

        advice = (
            f"You are at a loss! "
            f"In {city}, minimum viable "
            f"profit is ₹{min_viable:,}."
        )

    elif total_profit < min_viable:

        status = "warning"

        color = "#FAEEDA"

        emoji = "🟡"

        advice = (
            f"Profit of ₹{total_profit:,.0f} "
            f"is below comfortable level "
            f"for {city}."
        )

    elif avg_margin < benchmark['red']:

        status = "warning"

        color = "#FAEEDA"

        emoji = "🟡"

        advice = (
            f"Your {avg_margin}% margin "
            f"is below normal for "
            f"{business_type}."
        )

    else:

        status = "healthy"

        color = "#E1F5EE"

        emoji = "🟢"

        advice = (
            f"Your business looks healthy "
            f"for {city}!"
        )

    return {
        "status": status,
        "color": color,
        "emoji": emoji,
        "advice": advice
    }


def get_quick_wins(insights):
    """Generate actionable recommendations"""

    wins = []

    if insights.get('discount_hurts'):

        wins.append(
            "🎯 Reduce heavy discounts — "
            "they are reducing profits"
        )

    if insights.get('loss_orders', 0) > 0:

        wins.append(
            f"⚠️ You have "
            f"{insights['loss_orders']} "
            f"loss-making orders"
        )

    if insights.get('worst_product'):

        wins.append(
            f"📦 Reduce stock of "
            f"{insights['worst_product']}"
        )

    if insights.get('cheapest_freight'):

        wins.append(
            f"🚚 Use "
            f"{insights['cheapest_freight']} "
            f"more often"
        )

    if insights.get('best_day'):

        wins.append(
            f"📅 Stock up before "
            f"{insights['best_day']}"
        )

    return wins[:3]