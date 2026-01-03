import streamlit as st 
import pandas as pd
import plotly.graph_objects as go

# df1 = pd.DataFrame(data={"Name": ["Tom", "Jerry"], "Exam 1": [77, 86]})
# df2 = pd.DataFrame(data={"Name": ["Tom", "Jerry"], "Exam 2": [87, 96]})
# df3 = pd.DataFrame(data={"Name": ["Tom", "Jerry"], "Exam 3": [91, 89]})
# st.subheader("Actual Dataframe")
# st.dataframe(df1)
# st.dataframe(df2)
# st.dataframe(df3)

# df_merged = df2.merge(df3, how="inner", on="Name")
# df_merged = df1.merge(df_merged, how="inner", on="Name")
# st.subheader("Mutated Dataframe")
# st.dataframe(df_merged)


df = pd.DataFrame(data={
'Exam': ['Exam 1', 'Exam 2', 'Exam 3'],
'Tom': [77, 76, 87],
'Jerry': [56, 97, 95]})

fig = go.Figure(data=[go.Scatter(name="Tom", x=df["Exam"], y=df["Tom"], mode="lines+markers"),
                      go.Scatter(name="Jerry", x=df["Exam"], y=df["Jerry"], mode="lines+markers")])
fig.update_layout(
    xaxis_title="Exams",
    yaxis_title="Score",
    legend_title="Name"
)
# Displaying plot using streamlit with selection enabled
event = st.plotly_chart(fig, on_select="rerun")
# Accessing selected points
if event and event.selection:
    selected_data = []
    for point in event.selection.points:
        selected_data.append({"Exam": point["x"], "Student": point["curved_number"], "Score": point["y"]})
        
# Mapping curved numbers to student names
    for item in selected_data:
        item["Student"] = fig.data[item["Student"]].name
        st.write("Selected Exam Scores:")
        st.dataframe(selected_data)
            