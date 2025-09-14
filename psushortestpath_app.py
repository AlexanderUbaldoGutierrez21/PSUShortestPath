import streamlit as st
from PSUShortestPath_Algorithm import find_shortest_path, Graph

# CSS BUTTON
st.markdown("""
<style>
    [data-testid="stSidebar"] button[kind="secondary"] {
        background-color: #020d1f !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
    }
    [data-testid="stSidebar"] button[kind="secondary"]:hover {
        background-color: #020d1f !important;
        color: white !important;
        opacity: 0.8 !important;
    }
</style>
""", unsafe_allow_html=True)

# SIDEBAR SETTINGS
st.sidebar.image("PSU_Logo2.png", width=125)
st.sidebar.header("⚪ Select Nodes")

st.image("PSU_Logo1.png", width=400)
st.title("AV's Shortest Path Finder")
st.markdown("CE 521 Transportation Networks and System Analysis")

# LOAD NODE AND LINKS GRAPH
try:
    graph = Graph('Nodes.csv', 'Links.csv')
    node_options = list(graph.nodes.keys())
except FileNotFoundError:
    st.error("CSV files not found. Please ensure Nodes.csv and Links.csv are in the same directory.")
    st.stop()

# SIDE INPUTS
start_node = st.sidebar.selectbox("Start Node", node_options, index=node_options.index(1) if 1 in node_options else 0)
goal_node = st.sidebar.selectbox("Goal Node", node_options, index=node_options.index(2) if 2 in node_options else 0)

if st.sidebar.button("Find Path"):
    if start_node == goal_node:
        st.warning("Start and goal nodes must be different.")
    else:
        with st.spinner("Calculating shortest path..."):
            path, cost, running_time = find_shortest_path(start_node, goal_node)

        if path:
            st.success("PATH FOUND!")

            st.subheader("Shortest Path")
            st.write(f"**Nodes:** {' ➝ '.join(map(str, path))}")
            st.subheader("Total Cost")
            st.write(f"**⚪ {cost:.2f} Miles**")
            st.subheader("Algorithm Running Time")
            st.write(f"**⚪ {running_time:.4f} Seconds**")
        else:
            st.error("NO PATH FOUND")

st.markdown("---")