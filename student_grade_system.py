import re
import streamlit as st
Invalidname=type('Invalidname', (Exception,), {})

"""Exception to be raised when the name is invalid 
(empty or contains numeric values or special characters)."""

def Invaliddata(name,mark):
    if (not name.strip()):
        raise Invalidname("Name should not be empty")
    if (re.search(r'[^a-zA-Z\s]+', name.strip())) :
        raise Invalidname("Name should not contain numeric values or special characters")
    if mark>100 or mark<0:
        raise ValueError("Mark should be between 0 and 100")
    if mark and not isinstance(mark,int):
        raise TypeError("Mark should be an integer")
    
def get_grade(mark):
    """
    90-100:A
    80-89:B
    70-79:C
    60-69:D
    < 60: E
    """                        
    if mark>=90 and mark<=100:
        grade='A'
    elif mark>=80 and mark<=89:
        grade='B'
    elif mark>=70 and mark<=79:
        grade='C'
    elif mark>=60 and mark<=69:
        grade='D'
    else:
        grade='E'
    return grade

   
#data structure to store student records
if 'dict_student_data' not in st.session_state:
    st.session_state['dict_student_data']={'Name':[],'Mark':[],'Grade':[]}
st.markdown("""
<style>
    .stApp {
        background-color: #f4f7fb;
    }

</style>
<header><h1 style="text-align: center; color: #4CAF50;">Student Grading System</h1></header>

""", unsafe_allow_html=True)
st.divider()
col1, col2 = st.columns(2)
#container for input fields
with col1:
    student_name = st.text_input("Enter Student Name:")
with col2:
    #value=0,step=1 ensures that the input is an integer and cannot be a float or string
    student_mark=st.number_input("Enter Student Mark:",value=0,step=1)   
#container for buttons"""
col3,col4=st.columns(2)
with col3:
    add=st.button("Add Student Record")
with col4:
    view= st.button("View All Records")
 
  
st.divider()

if add:
    try:
        if student_name:    
            invalid_data=Invaliddata(student_name,student_mark)        
            st.session_state['dict_student_data']['Name'].append(student_name.strip())
            st.session_state['dict_student_data']['Mark'].append(student_mark)
            
            grade = get_grade(int(student_mark))
            st.session_state['dict_student_data']['Grade'].append(grade)
            st.success(f"Record Added: {student_name} - {student_mark} - Grade: {grade}")
        else:
            st.error("Please enter a valid student name.")
    except Exception as e:
        st.error(f"Error occurred while adding record: {e}")        
    

if view:      
    
    try:
        if st.session_state['dict_student_data']['Name']==[]:
            raise Invalidname("No records found")
        else:
            table_html = """<table style="width:100%; border-collapse: collapse; margin-top: 10px; font-family: sans-serif;">
            <thead>
                <tr style="background-color: #4CAF50; color: white; text-align: left;">
                    <th style="padding: 12px; border: 1px solid #ddd;">Student Name</th>
                    <th style="padding: 12px; border: 1px solid #ddd;">Mark</th>
                    <th style="padding: 12px; border: 1px solid #ddd;">Grade</th>
                </tr>
            </thead>
            <tbody>
        """
            for i in range(len(st.session_state['dict_student_data']['Name'])):
                Name= st.session_state['dict_student_data']['Name'][i]
                Mark= st.session_state['dict_student_data']['Mark'][i]
                Grade= st.session_state['dict_student_data']['Grade'][i]
                if Grade == 'E':
                    grade_color = "color: #FF0000; font-weight: bold;"
                else:
                    grade_color = "color: #333333;"
                table_html += f"""<tr>
                        <td style="padding: 12px; border: 1px solid #ddd;">{Name}</td>
                        <td style="padding: 12px; border: 1px solid #ddd;">{Mark}</td>
                        <td style="padding: 12px; border: 1px solid #ddd; {grade_color}">{Grade}</td>
                    </tr>
                """
            table_html += """</tbody> </table>"""
            st.markdown(table_html, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error Occured while viewing records: {e}")
    
        