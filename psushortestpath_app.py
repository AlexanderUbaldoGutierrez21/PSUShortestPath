import streamlit as st
from PSUShortestPath_Algorithm import find_shortest_path, Graph

# Apple-style CSS for clean, minimalistic look
st.markdown("""
<style>
    .main {
        background-color: #f5f5f7;
        color: #1d1d1f;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    .stButton>button {
        background-color: #007aff;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #0056cc;
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

st.title("🚗 Autonomous Vehicle Shortest Path Finder")
st.markdown("Using A* Algorithm for efficient pathfinding")

# Load graph to get available nodes
try:
    graph = Graph('Nodes.csv', 'Links.csv')
    node_options = list(graph.nodes.keys())
except FileNotFoundError:
    st.error("CSV files not found. Please ensure Nodes.csv and Links.csv are in the same directory.")
    st.stop()

col1, col2 = st.columns(2)

with col1:
    start_node = st.selectbox("Start Node", node_options, index=node_options.index(1) if 1 in node_options else 0)

with col2:
    goal_node = st.selectbox("Goal Node", node_options, index=node_options.index(2) if 2 in node_options else 0)

if st.button("Find Shortest Path"):
    if start_node == goal_node:
        st.warning("Start and goal nodes must be different.")
    else:
        with st.spinner("Calculating shortest path..."):
            path, cost, running_time = find_shortest_path(start_node, goal_node)

        if path:
            st.success("Path found!")

            with st.container():
                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                st.subheader("📍 Shortest Path")
                st.write(f"**Nodes:** {' → '.join(map(str, path))}")
                st.subheader("💰 Total Cost")
                st.write(f"**{cost:.2f} miles**")
                st.subheader("⏱️ Algorithm Running Time")
                st.write(f"**{running_time:.4f} seconds**")
                st.markdown('</div>', unsafe_allow_html=True)

            # Optional: Display map or visualization
            st.subheader("🗺️ Path Visualization")
            st.info("Map visualization can be added here using folium or similar library.")
        else:
            st.error("No path found between the selected nodes.")

st.markdown("---")
st.markdown("*Academic project for autonomous vehicle pathfinding using A* algorithm.*")
