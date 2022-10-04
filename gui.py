import streamlit as st
import misandcinV2 as mc
header = st.container()
input = st.container()
result=st.container()

@st.cache  # 👈 This function will be cached
def Searchingbfs(x,y,z):
    r1,r2=mc.BFS(int(mis),int(cin),int(boat))
    return r1,r2
@st.cache  # 👈 This function will be cached
def Searching(x,y,z):
    return mc.bfsids(x,y,z)

with header:
    st.title("missionaries and cannibals Generlized Problem")


with input:
    st.header("Please enter the number of missionaries, cannibals and the boat capacity")
    mis_col,cin_col,boat_col=st.columns(3)
    mis=mis_col.text_input("Enter Number of missionaries:")
    cin=cin_col.text_input("Enter Number of cannibals:")
    boat=boat_col.text_input("Enter The boat capacity:")
    



with result:
    st.header("Searching result:")
    r1,r2,r4,r3="","","",""
    try:
        r3,r4=Searchingbfs(int(mis),int(cin),int(boat))
        r1,r2=Searching(int(mis),int(cin),int(boat))
    except ValueError:
        mis,cin,boat=0,0,0

    bfs_col , ids_col =st.columns(2)
    bfs_col.text(r4)
    ids_col.text(r2)


