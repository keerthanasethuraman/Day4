# Student Grading System 🚀

A sleek, lightweight web application built using **Python** and **Streamlit** to manage student marks and assign academic grades dynamically. This project demonstrates persistent session state management, native HTML table layouts in Streamlit, custom Exception handling, and robust regular expression (`re`) text validations.

## 🌟 Features

*   **Persistent In-Memory Storage:** Uses Streamlit's `st.session_state` to store and maintain student details dynamically across app reruns without a heavy database dependency.
*   **Strict Input Validation:** 
    *   Rejects empty student names.
    *   Uses Regex to block names containing numerical characters or special symbols.
    *   Enforces strict integer validation for marks.
    *   Triggers real-time alerts if marks fall outside the legitimate **0 to 100** range.
*   **Dynamic Grade Assignment:** Instantly evaluates student performance based on a standard grading scale:
    *   `90 - 100` : **A**
    *   `80 - 89`  : **B**
    *   `70 - 79`  : **C**
    *   `60 - 69`  : **D**
    *   `< 60`     : **E**
*   **Custom UI Enhancements:** Styled with custom CSS backgrounds, clean column grids, and a beautifully structured **HTML5 preview data table** that conditionally highlights failing (**Grade E**) letters in bold red.

---

## 🛠️ Prerequisites & Installation

Make sure you have Python installed on your local machine.

1. Install Streamlit via your command line interface:
   ```bash
   pip install streamlit
   ```

2. Save the application script file as `student_grade_system.py`.

---

## 🚀 How to Run the Application

Navigate to the project directory containing your script and execute the following command:

```bash
streamlit run student_grade_system.py
```

Streamlit will automatically set up a local development web server and launch the application interface inside your default web browser at `http://localhost:8501`.

---

## 📂 Code Structure & Logic Highlights

### 🔒 Custom Error Handling & Data Validations
The program utilizes custom runtime exceptions (`Invalidname`) along with standard `ValueError` and `TypeError` catches to ensure dirty data never compromises your runtime dictionary:

```python
def Invaliddata(name, mark):
    if (not name.strip()):
        raise Invalidname("Name should not be empty")
    if (re.search(r'[^a-zA-Z\s]+', name.strip())):
        raise Invalidname("Name should not contain numeric values or special characters")
    if mark > 100 or mark < 0:
        raise ValueError("Mark should be between 0 and 100")
```

### 🎨 Conditional HTML Grid Rendering
When displaying records, the script avoids external layout dependencies by cleanly injecting strings into a structured HTML container using `st.markdown()`. It applies alternating text styling targeting low boundaries specifically:

```python
if Grade == 'E':
    grade_color = "color: #FF0000; font-weight: bold;"
else:
    grade_color = "color: #333333;"
```

---

## 📝 Future Improvements
*   Add a feature to export records to a downloadable `.csv` file.
*   Incorporate class metric summaries (e.g., Class Average, Highest Mark, Pass Rate).
*   Add a single-click reset button to completely flush out the active `st.session_state` storage cache.
