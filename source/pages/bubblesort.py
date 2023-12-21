import streamlit as st
import time

class Bubblesort():
    def __init__(self):
        pass

    def show(self):

        st.write(
            """<p style='font-size: 20px;'>
            Dieser Bubblesort ist von ChatGPT generiert. Wenn man sich etwas einarbeitet sollten noch deutlich bessere Dinge möglich sein.""",
            unsafe_allow_html=True
        )

        def bubble_sort(arr):
            n = len(arr)

            for i in range(n):
                for j in range(0, n - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        visualize_bubble_sort(arr)

        def visualize_bubble_sort(arr):
            st.bar_chart(arr, height=400)
            time.sleep(0.2)

        
        st.title("Bubble Sort Visualization")

        # Create a list of integers
        original_list = st.text_input("Enter a list of integers separated by spaces:")
        try:
            input_list = [int(x) for x in original_list.split()]
        except ValueError:
            st.warning("Please enter a valid list of integers.")
            return

        # Display the original list
        st.subheader("Original List:")
        st.bar_chart(input_list, height=400)

        # Sort the list using bubble sort
        st.subheader("Sorting in Progress:")
        bubble_sort(input_list)

        # Display the sorted list
        st.subheader("Sorted List:")
        st.bar_chart(input_list, height=400)