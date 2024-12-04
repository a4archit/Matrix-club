import streamlit as st
import numpy as np

# --------------------- Streamlit webpage designing --------------- #

st.header(":orange[Matrix mall]")
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

# matrix input label
matrix_input_label = st.text_area(
    "Input matrix",
    help="Use example matrix (if you have any problem in input section)",
    key="matrix_input_label",
    placeholder="Enter your matrix here"
)

reserved_space_for_done_button = st.empty()
reserved_space_for_clear_button = st.empty()
reserved_space_for_use_button = st.empty()


# displaying given matrix
st.write("Given Matrix is")
# reserving space
reserved_space_for_given_matrix = st.empty()




# ------------------------ Declaring useful variables ----------------- #
global input_matrix

EXAMPLE_MATRIX = np.array([
    [1, 0, 2],
    [3, 1, 2],
    [6, 2, 1]
])




# -------------------- Declaring useful functions --------------- #

def dynamic_msg(element, msg) -> None:
    """ changes the message of element dynamically """
    element.write(msg)

def clear_input_field() -> None:
    """ clear the input field of `matrix_input text field` """
    st.session_state.matrix_input_label = None

def put_example_matrix_in_input_label() -> None:
    """ put the EXAMPLE matrix in input label """
    st.session_state.matrix_input_label = EXAMPLE_MATRIX_STR

def done_button_code() -> None:
    """ This code runs when user click on `Done` button """
    # getting user input data from the input label
    user_input_data = matrix_input_label

    # extracting matrix from user input data
    temp_list = []
    for row in user_input_data.split('\n'):
        temp_list.append([int(element) for element in row.split(',')])
    input_matrix = np.array(temp_list)

    # getting matrix analysis report
    matrix_report: dict = matrix_analysis(input_matrix)

    # ---------------- Displaying section -------------- #
    # user provided matrix
    dynamic_msg(reserved_space_for_given_matrix,input_matrix)
    global given_matrix
    given_matrix = input_matrix

    print('done function is successfully executed')








# ------------------- Taking matrix as input from user --------- #



# done button
reserved_space_for_done_button.button(
    "Done",
    type='primary',
    on_click=done_button_code
)

# clear button
reserved_space_for_clear_button.button(
    "Clear",
    on_click=clear_input_field
)
# use example as input button
reserved_space_for_use_button.button(
    "Use Example",
    on_click=put_example_matrix_in_input_label
)





# ************************* This code will shift in another file in future **********************
def matrix_analysis(matrix: np.ndarray) -> dict:
    """
    Matrix analysis :
    ================
    Returns a python dictionary containing information about matrix(given as parameter).
    Information collected by performing a lot of operations on the given matrix

    Parameters:
    matrix: a numpy matrix

    Returns:
    dictionary: {'title': value}
    """

    analysis_report = {
        "rank": np.linalg.matrix_rank(matrix),
        "max_value": matrix.max(),
        "min_value": matrix.min(),
        "average": matrix.mean(),
        "order": matrix.shape
    }

    return analysis_report
