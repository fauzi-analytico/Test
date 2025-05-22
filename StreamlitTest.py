import streamlit as st
import pandas as pd
import numpy as np

# Streamlit app to generate and display a large DataFrame with its average
def main():
    st.title("Streamlit Test")
    st.write("Click 'Start' to generate and display the full 300,000×3 DataFrame with its average shown above.")

    if st.button("Start"):
        # Generate DataFrame
        df = pd.DataFrame(
            np.random.randint(1, 1000, size=(300_000, 3)),
            columns=["A", "B", "C"]
        )
        avg_value = df.values.mean()

        # Display average in larger font
        st.markdown(f"### Average of all values: {round(avg_value, 2)}")

        # Render entire DataFrame
        st.dataframe(df)

if __name__ == "__main__":
    main()
