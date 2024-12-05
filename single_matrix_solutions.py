import streamlit as st
import numpy as np
import sys

# --------------------- Streamlit webpage designing --------------- #

st.header(":orange[Nano Matrix]")
st.divider()

EXAMPLE_MATRIX_STR = """1,0,2
    3,1,2
    6,2,1"""

st.write(f"""#### Single matrix
You can continue with single matrix, with *n*-dimensions.
\n**Note:** Your matrix pattern:\n
Elements separate by comma`,` and
rows separate by clicking `enter`.

Example:\n 
    {EXAMPLE_MATRIX_STR}
""")

EXAMPLE_MATRIX = np.array([
    [1, 0, 2],
    [3, 1, 2],
    [6, 2, 1]
])

# matrix input label
matrix_input_label = st.text_area(
    "Input matrix",
    help="Use example matrix (if you have any problem in input section)",
    key="matrix_input_label",
    placeholder="Enter your matrix here"
)


# -------------------- Declaring useful functions --------------- #

def dynamic_msg(element, msg) -> None:
    """ changes the message of element dynamically """
    element.write(msg)

def clear_input_field() -> None:
    """ clear the input field of `matrix_input text field` """
    st.session_state.matrix_input_label = None

def put_example_matrix_in_input_label() -> None:
    """ put the EXAMPLE matrix in input label """
    st.session_state.matrix_input_label = "1,0,2\n3,1,2\n6,2,1"

@st.dialog("Invalid matrix!")
def empty_matrix_dialog():
    st.write("Input matrix field not be empty.\nUse example matrix or enter manually.")




# ----------------- Adding buttons ------------------------------- #

# done button
done_btn = st.button(
    "Done",
    key='done_btn_key',
    type='primary'
)

# clear button
clear_btn = st.button(
    "Clear",
    on_click=clear_input_field
)

# use example as input button
use_example_btn = st.button(
    "Use Example",
    on_click=put_example_matrix_in_input_label
)

if st.session_state.done_btn_key == True:
    if matrix_input_label is None :
        empty_matrix_dialog()
    else:
        try:

            # extracting matrix from user input data
            temp_list = []
            for row in matrix_input_label.split('\n'):
                temp_list.append([int(element) for element in row.split(',')])
            input_matrix = np.array(temp_list)

            st.divider()

            # ---------------- Displaying outputs ----------------- #
            analysis_report = {
                "rank": np.linalg.matrix_rank(input_matrix),
                "max_value": input_matrix.max(),
                "min_value": input_matrix.min(),
                "average": input_matrix.mean(),
                "order": input_matrix.shape,
                "determinant": np.linalg.det(input_matrix),
                "inverse": np.linalg.inv(input_matrix),
                "norm": np.linalg.norm(input_matrix),
                "trace": np.linalg.trace(input_matrix),
                # results in the form of matrix
                "squarred_matrix": input_matrix @ input_matrix,
                "transpose": input_matrix.transpose(),
                "element_squarred_matrix": input_matrix ** 2
            }

            st.write(f"## :green[Basic Information] \
            \nMatrix rank           : **:blue[{analysis_report.get('rank')}]** \
            \nOrder of matrix     : **:blue[{analysis_report.get('order')}]** \
            \nAverage value       : **:blue[{analysis_report.get('average')}]** \
            \nMin value           : **:blue[{analysis_report.get('min_value')}]** \
            \nMax value           : **:blue[{analysis_report.get('max_value')}]**")

            st.write(f"## :green[Transpose of matrix: ]")
            st.write(analysis_report.get('transpose'))

            st.write(f"## :green[Square of matrix: ]")
            st.write(analysis_report.get('squarred_matrix'))

        	st.write("## :green[Element wise Square]")
            st.write(analysis_report.get('element_squarred_matrix'))

        except Exception as e:
            print(e)

