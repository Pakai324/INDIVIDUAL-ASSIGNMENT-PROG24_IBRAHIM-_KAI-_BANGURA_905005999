# Digital Exam & Results Management System

A simple Python program that lets a school create exams, record results, correct mistakes, publish results, and let each candidate check their own result with a candidate code. Built with Object-Oriented Programming (OOP) 
**Domain:** Education  
**Problem:** Exam results kept on paper or in loose spreadsheets are slow to total, easy to get wrong, and often show students' names to everyone. This tool calculates percentages, grades and pass rates automatically, locks results once they are published, and lets each candidate see only their own result, on any computer with Python.

## Features

- Create an exam (course code, title and total marks) and receive an exam ID
- Add each candidate's score using a candidate code, such as `S-101`, never a name
- Correct a score before the exam is published
- Automatic percentage, letter grade (A to F) and Pass or Fail for every result
- Exam statistics: average, highest score, pass rate and number of each grade
- Publish an exam: this locks the results so they cannot be changed
- Candidates check their own results by code, and only from published exams
- Remove an exam and its results
- Checks every input (scores out of range, duplicate results, invalid codes) and shows clear error messages instead of crashing

## How to Run

1. Install Python 3.8 or later.
2. Download or clone this repository:
 
3. Run the program:
   ```
   python exam_results_system.py
   ```

The program starts empty and opens a menu. You add your own exams:

```
1. Create exam  2. Add result  3. Correct score  4. Publish exam
5. Show exams  6. Show exam results  7. Check my results
8. Remove exam  9. Exit
```

To create an exam, type the course code, title and total marks on one line, separated by commas (the title cannot contain a comma):

```
MATH101,Algebra Midterm,100
```

Sample data is available but does not run by default: call `demo(registry)` in the last lines of the file to load it.

## Project Structure

| File | Purpose |
|------|---------|
| `exam_results_system.py` | Classes, demo and menu |
| `README.md` | Documentation |
| `LICENSE` | MIT open-source licence |

## OOP Concepts Used

### Task 1: Classes and Objects
- **`Exam`**: attributes `exam_id`, `course_code`, `title`, `total_marks`, `pass_mark`, `status`, `published_on`, `results`; methods `add_result()`, `correct_score()`, `publish()`, `update_record()`, `has_result()`, `result_for()`, `average_score()`, `highest_score()`, `pass_rate()`, `describe_result()`, `display_info()`, `display_results()`
- **`ExamRegistry`**: attributes `school_name`, `exams`; methods `add_exam()`, `find()`, `display_all()`, `remove_exam()`, `check_candidate()`, `status_summary()`
- The registry holds and manages `Exam` objects, which demonstrates interaction between objects. For example, `check_candidate()` asks each exam for its status and for that candidate's score.

### Task 2: Data Structure
- A **dictionary** (`{exam_id: Exam}`) stores all exams, so any exam can be found instantly by its ID.
- `add_exam()` and `display_all()` add and display records.
- **Bonus (tuples):** each result is a **tuple** `(candidate_code, score)`, and an exam's `results` is a tuple of these. Tuples cannot be changed, so adding or correcting a result builds a new tuple. The grade scale is also a tuple of `(minimum percentage, grade)` tuples. The dictionary is the only data structure holding the exam objects.

### Task 3: Methods
| Type | Method | Purpose |
|------|--------|---------|
| Instance | `add_result()`, `correct_score()`, `publish()`, `update_record()`, `average_score()`, `pass_rate()`, `display_results()` and others | Work on one exam's data and enforce the rules (no changes after publishing, no duplicate results) |
| Class (`@classmethod`) | `Exam.from_string("MATH101, Algebra Midterm, 100")` | Alternative way to create an exam from one line of text |
| Class (`@classmethod`) | `Exam.grade_scale_text()` | Builds the grade scale text from the shared grade scale |
| Static (`@staticmethod`) | `Exam.percentage()` | Converts a score to a percentage |
| Static (`@staticmethod`) | `Exam.grade()` | Converts a percentage to a letter grade |
| Static (`@staticmethod`) | `Exam.is_pass()` | Checks a percentage against the pass mark |
| Static (`@staticmethod`) | `Exam.normalize_candidate()` | Checks and standardises a candidate code |

## Digital Public Goods (DPG) Alignment

| DPG Principle | How this project meets it |
|---------------|---------------------------|
| **Open-source** | The full source code is public on GitHub under the MIT licence, so anyone can use, study, modify and share it. |
| **Inclusive and accessible design** | Plain-language prompts, a numbered menu, and clear error messages that say how to fix a mistake. The grade scale is shown when the program starts. It runs on any low-spec computer, needs no internet connection and has no cost. |
| **Privacy-respecting** | No student names or personal data are stored. Results belong to a short candidate code chosen by the school, and the program rejects entries that look like names (spaces or other characters). A candidate can see only their own result, and only after the exam is published. Data is kept in memory only and is not sent anywhere. An exam can be removed at any time. |
| **Modular and reusable** | `Exam` and `ExamRegistry` are separate, self-contained classes. They can be imported into other projects, for example a timetable tool or an attendance tracker, without changing the code. The start block means importing the file does not run the menu. |

## Sample Output

```
Grade scale: A = 80%+  B = 70%+  C = 60%+  D = 50%+  F = 0%+

Choose: 1
Course code,title,total marks (e.g. MATH101,Algebra Midterm,100): math101,Algebra Midterm,100
Exam created: EXM001 (MATH101 - Algebra Midterm).

Choose: 2
Exam ID: exm001
Use a candidate code (like S-101), never a student name.
Candidate code: s-101
Score: 78
Result added.

Choose: 2
Exam ID: EXM001
Candidate code: S-102
Score: 45.5
Result added.

Choose: 4
Exam ID: EXM001
EXM001 is now published.

Choose: 6
Exam ID: EXM001
ID: EXM001 | MATH101 | Algebra Midterm | Total: 100.0 | Pass mark: 50.0% | Status: Published | Results: 2
    S-101 | 78.0/100.0 | 78.0% | Grade B | Pass
    S-102 | 45.5/100.0 | 45.5% | Grade F | Fail
    Average: 61.8 | Highest: 78.0 | Pass rate: 50.0%
    Grades -> A: 0  B: 1  C: 0  D: 0  F: 1

Choose: 7
Your candidate code: s-102

=== Published results for S-102 ===
MATH101 | Algebra Midterm | 45.5/100.0 | 45.5% | Grade F | Fail
```

## Limitations and Future Improvements

- Results are lost when the program closes (kept in memory for privacy). A future version could add optional local storage.
- Anyone who has the program can add or publish results, and anyone who knows a candidate code can look it up. A future version could add staff logins and candidate PINs.
- The grade scale and pass mark are general values. Each school could set its own.
- Add a graphical interface and local-language support (e.g. Krio).

## Author

Ibrahim Kai Bangura

## Licence

Released under the [MIT Licence](LICENSE).
