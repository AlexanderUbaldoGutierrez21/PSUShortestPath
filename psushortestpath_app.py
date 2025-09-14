import streamlit as st
from PSUShortestPath_Algorithm import find_shortest_path, Graph

# Apple-style CSS for clean, minimalistic look
st.markdown("""
<style>
    .main {
        background-color: #f5f5f7;
        color: #1d1d1f;
    }
    .stButton>button {
        background-color: #000C19;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        font-size: 15px;
    }
    .stButton>button:hover {
        color: white;
    }
    .stSelectbox, .stNumberInput {
        border-radius: 8px;
    }
    h1, h2, h3 {
        color: #1d1d1f;
    }
    .result-box {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar configuration
st.sidebar.image("PSU_Logo2.png", width=125)
st.sidebar.header("⚪ Select Nodes")
st.image("PSU_Logo1.png", width=400)
st.title("AV's Shortest Path Finder")
st.markdown("CE 521 Transportation Networks and System Analysis")

# Load graph to get available nodes
try:
    graph = Graph('Nodes.csv', 'Links.csv')
    node_options = list(graph.nodes.keys())
except FileNotFoundError:
    st.error("CSV files not found. Please ensure Nodes.csv and Links.csv are in the same directory.")
    st.stop()

# Sidebar inputs
start_node = st.sidebar.selectbox("Start Node", node_options, index=node_options.index(1) if 1 in node_options else 0)
goal_node = st.sidebar.selectbox("Goal Node", node_options, index=node_options.index(2) if 2 in node_options else 0)

if st.sidebar.button("Find"):
    if start_node == goal_node:
        st.warning("Start and goal nodes must be different.")
    else:
        with st.spinner("Calculating shortest path..."):
            path, cost, running_time = find_shortest_path(start_node, goal_node)

        if path:
            st.success("PATH FOUND!")

            st.subheader("Shortest Path")
            st.write(f"**Nodes:** {'  ⟶  '.join(map(str, path))}")
            st.subheader("Total Cost")
            st.write(f"**{cost:.2f} Miles**")
            st.subheader("Algorithm Running Time")
            st.write(f"**{running_time:.4f} Seconds**")
            
            # Result box below results
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            # Optional: Display map or visualization
            st.subheader("Path Visualization")
        else:
            st.error("NO PATH FOUND")

st.markdown("---")
