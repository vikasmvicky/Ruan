import pandas as pd
import numpy as np
import os
import json


def clean_insights(insights):
    cleaned = {}
    for key, value in insights.items():
        try:
            cleaned[key] = value.item()
        except AttributeError:
            cleaned[key] = value
    return cleaned


def load_sales_data(file):
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
            df = pd.read_excel(file, engine='openpyxl')
        else:
            return None
        return df
    except Exception as e:
        print(f"File load error: {e}")
        return None


def get_industry_benchmark(business_type):
    benchmarks = {
        "Medical Shop":    {"normal": (18, 25), "red": 12, "green": 30},
        "Kirana Store":    {"normal": (10, 20), "red": 8,  "green": 25},
        "Textile Shop":    {"normal": (30, 45), "red": 20, "green": 50},
        "Shoe Showroom":   {"normal": (40, 50), "red": 30, "green": 55},
        "Fancy Store":     {"normal": (60, 70), "red": 45, "green": 75},
        "Vegetable Stall": {"normal": (15, 25), "red": 10, "green": 30},
        "Pan Shop":        {"normal": (25, 40), "red": 15, "green": 45},
        "Hardware Store":  {"normal": (20, 35), "red": 15, "green": 40},
        "Processed Meat":  {"normal": (15, 25), "red": 10, "green": 30},
        "Canned Foods":    {"normal": (20, 30), "red": 12, "green": 35},
        "Preserved Food":  {"normal": (18, 28), "red": 10, "green": 32},
    }
    return benchmarks.get(
        business_type,
        {"normal": (15, 30), "red": 10, "green": 35}
    )


def get_city_context(city):
    city_data = {
        "Bangalore":      {"cost": "Very High", "min_profit": 50000, "rent": 25000},
        "Bengaluru":      {"cost": "Very High", "min_profit": 50000, "rent": 25000},
        "bengaluru":      {"cost": "Very High", "min_profit": 50000, "rent": 25000},
        "Mumbai":         {"cost": "Very High", "min_profit": 60000, "rent": 30000},
        "Chennai":        {"cost": "Medium",    "min_profit": 30000, "rent": 15000},
        "Hyderabad":      {"cost": "Medium",    "min_profit": 28000, "rent": 14000},
        "Mysuru":         {"cost": "Low",       "min_profit": 15000, "rent": 8000},
        "Mysore":         {"cost": "Low",       "min_profit": 15000, "rent": 8000},
        "Pune":           {"cost": "High",      "min_profit": 40000, "rent": 20000},
        "Delhi":          {"cost": "High",      "min_profit": 45000, "rent": 22000},
        "Ghaziabad":      {"cost": "High",      "min_profit": 42000, "rent": 20000},
        "Jammu":          {"cost": "Low",       "min_profit": 12000, "rent": 6000},
        "Shillong":       {"cost": "Low",       "min_profit": 10000, "rent": 5000},
        "Kolkata":        {"cost": "Medium",    "min_profit": 25000, "rent": 12000},
        "Ahmedabad":      {"cost": "Medium",    "min_profit": 22000, "rent": 11000},
        "Jaipur":         {"cost": "Low",       "min_profit": 15000, "rent": 7000},
        "Lucknow":        {"cost": "Low",       "min_profit": 14000, "rent": 7000},
        "Nagpur":         {"cost": "Low",       "min_profit": 13000, "rent": 6000},
        "Indore":         {"cost": "Low",       "min_profit": 13000, "rent": 6000},
        "Coimbatore":     {"cost": "Low",       "min_profit": 14000, "rent": 7000},
        "Kochi":          {"cost": "Medium",    "min_profit": 20000, "rent": 10000},
    }
    for key in city_data:
        if key.lower() in city.lower():
            return city_data[key]
    return {"cost": "Low", "min_profit": 10000, "rent": 5000}


def analyse_sales(df):
    insights = {}
    try:
        insights['total_orders'] = len(df)

        if 'Sales' in df.columns:
            insights['total_revenue'] = round(df['Sales'].sum(), 2)
            insights['avg_order_value'] = round(df['Sales'].mean(), 2)

        if 'Profit' in df.columns:
            insights['total_profit'] = round(df['Profit'].sum(), 2)
            insights['avg_profit'] = round(df['Profit'].mean(), 2)
            insights['profit_margin'] = round(
                (df['Profit'].sum() / df['Sales'].sum()) * 100, 2
            ) if 'Sales' in df.columns and df['Sales'].sum() > 0 else 0
            insights['profitable_orders'] = int((df['Profit'] > 0).sum())
            insights['loss_orders'] = int((df['Profit'] < 0).sum())

        profit_col = 'Product Sub-Category' \
            if 'Product Sub-Category' in df.columns \
            else 'Product Type'

        if profit_col in df.columns and 'Profit' in df.columns:
            product_profit = df.groupby(profit_col)['Profit'].sum()
            insights['best_product'] = product_profit.idxmax()
            insights['best_product_profit'] = round(product_profit.max(), 2)
            insights['worst_product'] = product_profit.idxmin()
            insights['worst_product_profit'] = round(product_profit.min(), 2)

        if 'Segment' in df.columns and 'Profit' in df.columns:
            segment_profit = df.groupby('Segment')['Profit'].sum()
            insights['best_segment'] = segment_profit.idxmax()
            insights['best_segment_profit'] = round(segment_profit.max(), 2)

        if 'City' in df.columns and 'Profit' in df.columns:
            city_profit = df.groupby('City')['Profit'].sum()
            insights['best_city'] = city_profit.idxmax()
            insights['worst_city'] = city_profit.idxmin()

        if 'Discount offered' in df.columns and 'Profit' in df.columns:
            high_discount = df[df['Discount offered'] > 0.2]['Profit'].mean()
            low_discount = df[df['Discount offered'] <= 0.2]['Profit'].mean()
            insights['discount_hurts'] = bool(high_discount < low_discount) \
                if not (np.isnan(high_discount) or np.isnan(low_discount)) \
                else False
            insights['high_discount_profit'] = round(high_discount, 2) \
                if not np.isnan(high_discount) else 0
            insights['low_discount_profit'] = round(low_discount, 2) \
                if not np.isnan(low_discount) else 0

        if 'Order Date' in df.columns:
            df['Order Date'] = pd.to_datetime(
                df['Order Date'], dayfirst=True, errors='coerce')
            df['Month'] = df['Order Date'].dt.month
            df['DayOfWeek'] = df['Order Date'].dt.day_name()

            if 'Profit' in df.columns:
                monthly = df.groupby('Month')['Profit'].sum()
                if not monthly.empty:
                    insights['best_month'] = int(monthly.idxmax())
                    insights['worst_month'] = int(monthly.idxmin())

                daily = df.groupby('DayOfWeek')['Profit'].sum()
                if not daily.empty:
                    insights['best_day'] = daily.idxmax()
                    insights['worst_day'] = daily.idxmin()

        if 'Freight Mode' in df.columns and 'Freight Expenses' in df.columns:
            freight = df.groupby('Freight Mode')['Freight Expenses'].mean()
            insights['cheapest_freight'] = freight.idxmin()
            insights['cheapest_freight_cost'] = round(freight.min(), 2)

        if 'Order Priority' in df.columns and 'Profit' in df.columns:
            priority_profit = df.groupby('Order Priority')['Profit'].mean()
            insights['best_priority'] = priority_profit.idxmax()

    except Exception as e:
        print(f"Analysis error: {e}")

    insights = clean_insights(insights)
    return insights


def detect_data_type(df):
    result = {
        "type": "unknown",
        "confidence": 0,
        "missing_cols": [],
        "found_cols": [],
        "suggestion": ""
    }

    if df is None or df.empty:
        result["type"] = "empty"
        result["suggestion"] = "Your file appears to be empty."
        return result

    cols = [str(c).lower().strip() for c in df.columns]

    sales_keywords = ['sales', 'revenue', 'amount', 'total', 'income']
    profit_keywords = ['profit', 'loss', 'margin', 'earnings', 'net']
    product_keywords = ['product', 'item', 'medicine', 'goods', 'name', 'category']
    date_keywords = ['date', 'day', 'month', 'year', 'time']
    qty_keywords = ['qty', 'quantity', 'units', 'count', 'sold']

    score = 0
    found = []
    missing = []

    has_sales = any(any(k in c for k in sales_keywords) for c in cols)
    has_profit = any(any(k in c for k in profit_keywords) for c in cols)
    has_product = any(any(k in c for k in product_keywords) for c in cols)
    has_date = any(any(k in c for k in date_keywords) for c in cols)
    has_qty = any(any(k in c for k in qty_keywords) for c in cols)

    if has_sales:
        score += 30
        found.append("Sales column")
    else:
        missing.append("Sales/Revenue column")

    if has_profit:
        score += 30
        found.append("Profit column")
    else:
        missing.append("Profit/Loss column")

    if has_product:
        score += 20
        found.append("Product column")
    else:
        missing.append("Product/Item column")

    if has_date:
        score += 10
        found.append("Date column")

    if has_qty:
        score += 10
        found.append("Quantity column")

    result["found_cols"] = found
    result["missing_cols"] = missing
    result["confidence"] = score

    if score >= 60:
        result["type"] = "sales_data"
        result["suggestion"] = "Good data! Ready to analyse."
    elif score >= 30:
        result["type"] = "partial_data"
        result["suggestion"] = "I found some useful columns. I will do my best!"
    else:
        result["type"] = "unrelated_data"
        result["suggestion"] = "This doesn't look like sales data. Let me try anyway!"

    return result


def handle_no_data_fallback(business, city):
    benchmarks = get_industry_benchmark(business)
    city_ctx = get_city_context(city)

    return {
        "type": "fallback",
        "business": business,
        "city": city,
        "message": (
            f"No data uploaded yet — showing industry "
            f"averages for {business} in {city}"
        ),
        "avg_margin_low": benchmarks['normal'][0],
        "avg_margin_high": benchmarks['normal'][1],
        "min_viable_profit": city_ctx['min_profit'],
        "typical_rent": city_ctx['rent'],
        "tips": [
            f"A healthy {business} in {city} should have "
            f"{benchmarks['normal'][0]}-{benchmarks['normal'][1]}% profit margin",
            f"Minimum viable monthly profit in {city} is Rs {city_ctx['min_profit']:,}",
            f"Typical monthly rent in {city} is Rs {city_ctx['rent']:,}",
            "Track daily sales for 7 days — Ruan will then give real insights",
            "Start with manual entry — just fill in today's sales"
        ]
    }


def smart_analyse(df, business, city):
    detection = detect_data_type(df)

    if detection["type"] == "empty":
        return {
            "status": "empty",
            "message": detection["suggestion"],
            "fallback": handle_no_data_fallback(business, city)
        }

    if detection["type"] == "unrelated_data":
        try:
            num_cols = df.select_dtypes(include=['number']).columns.tolist()
            if len(num_cols) >= 2:
                df_temp = df.copy()
                df_temp['Sales'] = df[num_cols[-2]]
                df_temp['Profit'] = df[num_cols[-1]]
                insights = analyse_sales(df_temp)
                insights['warning'] = "Data format was unusual — best guess analysis"
                return {"status": "guessed", "insights": insights, "detection": detection}
        except Exception:
            pass

        return {
            "status": "no_data",
            "message": detection["suggestion"],
            "fallback": handle_no_data_fallback(business, city)
        }

    insights = analyse_sales(df)
    insights['detection'] = detection
    return {"status": "success", "insights": insights, "detection": detection}


def generate_ruan_message(insights, business, city, lang="English"):
    if not insights:
        return "Upload your sales data and I will analyse it!"

    profit = insights.get('total_profit', 0)
    margin = insights.get('profit_margin', 0)
    loss_orders = insights.get('loss_orders', 0)

    msg = (
        f"Here is what I found for your {business} in {city}:\n\n"
        f"Total Revenue: Rs {insights.get('total_revenue', 0):,.2f}\n"
        f"Total Profit: Rs {profit:,.2f}\n"
        f"Profit Margin: {margin}%\n"
        f"Total Orders: {insights.get('total_orders', 0):,}\n"
        f"Loss-making Orders: {loss_orders}\n\n"
        f"Best Product: {insights.get('best_product', 'N/A')}\n"
        f"Best Day: {insights.get('best_day', 'N/A')}\n"
        f"Worst Day: {insights.get('worst_day', 'N/A')}"
    )

    if insights.get('discount_hurts'):
        msg += "\n\nWarning: High discounts are cutting your profits!"

    return msg


def check_profit_health(total_profit, business_type, city, avg_margin):
    benchmark = get_industry_benchmark(business_type)
    city_ctx = get_city_context(city)
    min_viable = city_ctx['min_profit']

    if total_profit < 0:
        status = "loss"
        color = "rgba(121,31,31,0.3)"
        border = "#791F1F"
        emoji = "🔴"
        advice = (
            f"You are at a loss! In {city}, minimum viable "
            f"monthly profit is Rs {min_viable:,}. "
            f"Let's find what is costing you money."
        )
    elif total_profit < min_viable:
        status = "warning"
        color = "rgba(186,117,23,0.2)"
        border = "#BA7517"
        emoji = "🟡"
        advice = (
            f"Profit of Rs {total_profit:,.0f} is below "
            f"comfortable level for {city} (Rs {min_viable:,}/month). "
            f"You need to improve margins."
        )
    elif avg_margin < benchmark['red']:
        status = "warning"
        color = "rgba(186,117,23,0.2)"
        border = "#BA7517"
        emoji = "🟡"
        advice = (
            f"Your {avg_margin}% margin is below normal "
            f"for {business_type} "
            f"({benchmark['normal'][0]}-{benchmark['normal'][1]}%). "
            f"Focus on high margin products."
        )
    else:
        status = "healthy"
        color = "rgba(74,210,149,0.1)"
        border = "#4AD295"
        emoji = "🟢"
        advice = (
            f"Your business looks healthy for {city}! "
            f"Margin of {avg_margin}% is within normal "
            f"range for a {business_type}."
        )

    return {
        "status": status,
        "color": color,
        "border": border,
        "emoji": emoji,
        "advice": advice
    }


def get_quick_wins(insights):
    wins = []

    if insights.get('discount_hurts'):
        wins.append("Reduce heavy discounts — they are cutting your profits significantly")

    if insights.get('loss_orders', 0) > 0:
        wins.append(
            f"You have {insights['loss_orders']} loss-making orders — "
            f"review pricing on these immediately"
        )

    if insights.get('worst_product'):
        wins.append(
            f"Consider reducing stock of '{insights['worst_product']}' "
            f"— lowest profit product"
        )

    if insights.get('best_day'):
        wins.append(
            f"Stock up before {insights['best_day']} — your best performing day"
        )

    if insights.get('cheapest_freight'):
        wins.append(
            f"Use '{insights['cheapest_freight']}' freight more often — cheapest option"
        )

    return wins[:3]


def save_vendor_data(vendor_name, city, business, insights):
    try:
        safe_name = vendor_name.replace(" ", "_").lower().strip()
        folder = f"data/vendors/{safe_name}"
        os.makedirs(folder, exist_ok=True)

        save_insights = {
            k: v for k, v in insights.items()
            if not isinstance(v, dict)
        }

        with open(f"{folder}/latest.json", "w") as f:
            json.dump({
                "vendor": vendor_name,
                "city": city,
                "business": business,
                "insights": save_insights
            }, f, indent=2)
    except Exception as e:
        print(f"Save vendor error: {e}")


def load_vendor_history(vendor_name):
    try:
        safe_name = vendor_name.replace(" ", "_").lower().strip()
        path = f"data/vendors/{safe_name}/latest.json"
        if os.path.exists(path):
            with open(path) as f:
                return json.load(f)
    except Exception as e:
        print(f"Load vendor error: {e}")
    return None