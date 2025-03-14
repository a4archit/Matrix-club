import streamlit as st
import numpy as np

# --------------------- Streamlit webpage designing --------------- #

st.sidebar.title("About the developer")
st.sidebar.divider()
st.sidebar.write("I am try to create this web application through the use of \
**Streamlit** and **NumPy**. You can check my social media accounts: ")
st.sidebar.write("[Kaggle](https://www.kaggle.com/architty108)")
st.sidebar.write("[Github](https://www.github.com/a4archit)")
st.sidebar.write("[LinkedIn](https://www.linkedin.com/in/archit-tyagi-191323296)")

st.header("Nano Matrix", divider=True)

EXAMPLE_MATRIX_STR = """
    1,0,2
    3,1,2
    6,2,1"""

st.write(f"""#### Single matrix
You can continue with single matrix, with *n*-dimensions.
Elements separate by comma`,` and
rows separate by clicking `enter`.
""")

EXAMPLE_MATRIX = np.array([
    [1, 0, 2],
    [3, 1, 2],
    [6, 2, 1]
])

reserved_space_for_use_example_btn = st.empty()

# matrix input label
matrix_input_label = st.text_area(
    "Input matrix",
    help="Use example matrix (if you have any problem in input section)",
    key="matrix_input_label",
    placeholder="Enter your matrix here",
    label_visibility="visible"
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

def round_matrix(matrix: np.ndarray, decimals = 1) -> np.ndarray:
    """ returns the matrix after rounding off """
    return np.round(matrix, decimals=decimals)


# ----------------- Adding buttons ------------------------------- #

# done button
done_btn = st.button(
    "Done",
    key='done_btn_key',
    type='primary',
    use_container_width=True
)


# clear button
clear_btn = st.button(
    "Clear",
    on_click=clear_input_field,
    use_container_width=True
)

# use example as input button
reserved_space_for_use_example_btn.button(
    f"Use this Example\n\n{EXAMPLE_MATRIX_STR}",
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
                # basic information
                "rank"          : np.linalg.matrix_rank(input_matrix),
                "max_value"     : input_matrix.max(),
                "min_value"     : input_matrix.min(),
                "average"       : input_matrix.mean(),
                "order"         : input_matrix.shape,
                "determinant"   : np.linalg.det(input_matrix),
                "norm"          : np.linalg.norm(input_matrix),
                "trace"         : np.linalg.trace(input_matrix),
                # results in the form of matrix
                "squared_matrix"        : input_matrix @ input_matrix,
                "transpose"             : input_matrix.transpose(),
                "inverse"       : np.linalg.inv(input_matrix),
                "element_squared_matrix": input_matrix ** 2
            }

            # creating tabs for displaying the output
            basic_information_tab, matrix_outputs_tab = st.tabs(['Information','Matrix Outputs'])

            with basic_information_tab:
                st.write(
                    f"## :green[Basic Information] \
                    \nMax value           : **:blue[{analysis_report.get('max_value')}]** \
                    \nMin value           : **:blue[{analysis_report.get('min_value')}]** \
                    \nMatrix rank         : **:blue[{analysis_report.get('rank')}]** \
                    \nAverage value       : **:blue[{analysis_report.get('average')}]** \
                    \nOrder of matrix     : **:blue[{analysis_report.get('order')}]** \
                    \nMagnitude of matrix : **:blue[{round(analysis_report.get('norm'),2)}]** \
                ")

            with matrix_outputs_tab:
                col1, col2 = st.columns(2)

                with col1:
                    # transpose
                    st.write(f"## Transpose of matrix: ")
                    st.write(analysis_report.get('transpose'))

                    # matrix square
                    st.write(f"## Square of matrix: ")
                    st.write(analysis_report.get('squared_matrix'))

                with col2:
                    # matrix element-wise square
                    st.write(f"## Element wise Square: ")
                    st.write(analysis_report.get('element_squared_matrix'))

                    # matrix inverse
                    st.write(f"## Inverse of matrix: ")
                    st.write(round_matrix(analysis_report.get('inverse')))



        except Exception as e:
            print(f"Error: {e}")
