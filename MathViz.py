import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import plotly.graph_objects as go

# Custom CSS for fixing sidebar
# Custom CSS for fixing sidebar background color to white
sidebar_style = """
    <style>
        [data-testid="stSidebarContent"] {
            position: fixed;
            top: 0;
            left: 0;
            width: 300px;
            height: 100vh;
            background-color: #FFFFFF !important;  /* White background */
            overflow-y: auto;
        }
        [data-testid="stSidebar"] {
            width: 300px !important;
        }
        /* Change sidebar text color to black for better visibility */
        [data-testid="stSidebarContent"] * {
            color: black !important;
        }
    </style>
"""
st.markdown(sidebar_style, unsafe_allow_html=True)


# Sidebar Content (Fixed)
with st.sidebar:
    st.header("📌 Navigation")
    equation_type = st.radio(
        "Choose the equation type:",
        ["Cartesian (y = f(x))", "Parametric (x = f(t), y = g(t))", "Polar (r = f(θ))", "3D Surface (z = f(x, y))"]
    )

    # Developer Section
    st.markdown("---")
    st.subheader("👨‍💻 About the Developer")
    st.markdown("""
    **Manas Pratim Das**  
    🎓 *Electronics and Communication Engineering (MTech/MS)*  

    🤖 **Focus Areas:**  
           ✅ Artificial Intelligence & Machine Learning  
           ✅ Deep Learning & Secure Computing  
           ✅ Neuromorphic Computing  

    📌 **Connect with Me:**  
    🔗 [LinkedIn](https://www.linkedin.com/in/manas-pratim-das-b95200197/)     
    🐙 [GitHub](https://github.com/manas-pr)     
    📧 [Email](mailto:manas.pr94@gmail.com)     
    """)

# App title
st.title("🔢📈 Dynamic Math Graph Visualizer")

# Cartesian Graph (y = f(x))
if equation_type == "Cartesian (y = f(x))":
    equation = st.text_input("Enter the equation (use 'x' as the variable):", "x**2")
    x_min, x_max = st.slider("Select x range:", -10.0, 10.0, (-5.0, 5.0))
    x_vals = np.linspace(x_min, x_max, 400)

    try:
        y_vals = [eval(equation, {"x": x, "np": np}) for x in x_vals]
        data = pd.DataFrame({"x": x_vals, "y": y_vals})
        chart = alt.Chart(data).mark_line(color='blue').encode(x='x:Q', y='y:Q')
        st.altair_chart(chart, use_container_width=True)
    except Exception as e:
        st.error(f"Error in equation: {e}")

# Parametric Graph (x = f(t), y = g(t))
elif equation_type == "Parametric (x = f(t), y = g(t))":
    eq_x = st.text_input("Enter the x equation (use 't' as the variable):", "np.sin(t)")
    eq_y = st.text_input("Enter the y equation (use 't' as the variable):", "np.cos(t)")
    t_min, t_max = st.slider("Select t range:", -10.0, 10.0, (-5.0, 5.0))
    t_vals = np.linspace(t_min, t_max, 400)

    try:
        x_vals = [eval(eq_x, {"t": t, "np": np}) for t in t_vals]
        y_vals = [eval(eq_y, {"t": t, "np": np}) for t in t_vals]
        data = pd.DataFrame({"x": x_vals, "y": y_vals})
        chart = alt.Chart(data).mark_line(color='red').encode(x='x:Q', y='y:Q')
        st.altair_chart(chart, use_container_width=True)
    except Exception as e:
        st.error(f"Error in equations: {e}")

# Polar Graph (r = f(θ))
elif equation_type == "Polar (r = f(θ))":
    equation = st.text_input("Enter the polar equation (use 'theta' as the variable):", "1 + np.sin(4*theta)")
    theta_vals = np.linspace(0, 2 * np.pi, 400)

    try:
        r_vals = [eval(equation, {"theta": theta, "np": np}) for theta in theta_vals]
        x_vals = r_vals * np.cos(theta_vals)
        y_vals = r_vals * np.sin(theta_vals)
        data = pd.DataFrame({"x": x_vals, "y": y_vals})
        chart = alt.Chart(data).mark_line(color='green').encode(x='x:Q', y='y:Q')
        st.altair_chart(chart, use_container_width=True)
    except Exception as e:
        st.error(f"Error in equation: {e}")

# 3D Surface Plot (z = f(x, y))
elif equation_type == "3D Surface (z = f(x, y))":
    equation = st.text_input("Enter the 3D surface equation (use 'x' and 'y' as variables):", "np.sin(np.sqrt(x**2 + y**2))")
    x_range = np.linspace(-5, 5, 50)
    y_range = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x_range, y_range)

    try:
        Z = eval(equation, {"x": X, "y": Y, "np": np})
        fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Error in equation: {e}")

st.write("🎨 Enter mathematical expressions to visualize graphs dynamically!")
