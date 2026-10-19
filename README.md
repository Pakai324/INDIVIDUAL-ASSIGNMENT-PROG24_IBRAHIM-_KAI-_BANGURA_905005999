# Citizen Complaint System

A simple Python program that lets citizens report public service problems (water, electricity, roads, health, education, waste) and lets a district office track each complaint from submission to resolution. Built with Object-Oriented Programming (OOP) 

**Domain:** Government  
**Problem:** Citizens often do not know whether their complaint was received or what happened to it, and offices struggle to see which complaints have waited too long. This tool gives every complaint a reference ID, a clear status history, and an overdue alert, on any computer with Python.

## Features

- Submit a complaint (category, area and description) and receive an automatically generated reference ID
- Track any complaint by its reference ID and see its full status history
- Update a complaint's status: In review, Resolved or Rejected (with an optional note)
- Closed complaints (Resolved or Rejected) are locked, so their history cannot be changed
- Suggest a starting priority by category (High, Medium or Low)
- Show overdue complaints: open longer than 7 days (High), 14 days (Medium) or 30 days (Low)
- Show a category summary
- Remove a complaint (for example one sent by mistake)
- Checks every input and shows clear error messages instead of crashing

## How to Run

1. Install Python 3.8 or later.
2. Download or clone this repository:
   
   ```
3. Run the program:
   ```
   python citizen_complaint_system.py
   ```

The program starts empty and opens a menu. You add your own complaints:

```
1. Submit complaint  2. Update status  3. Show all  4. Track one
5. Overdue complaints  6. Category summary  7. Remove complaint  8. Exit
```

To submit a complaint, type the category, area and description on one line, separated by commas:

```
Water,Kissy,No water from the community tap for three days
```

Sample data is available but does not run by default: call `demo(registry)` in the last lines of the file to load it.

## Project Structure

| File | Purpose |
|------|---------|
| `citizen_complaint_system.py` | Classes, demo and menu |
| `README.md` | Documentation |
| `LICENSE` | MIT open-source licence |

## OOP Concepts Used

### Task 1: Classes and Objects
- **`Complaint`**: attributes `complaint_id`, `category`, `area`, `description`, `priority`, `status_log`; methods `update_status()`, `update_record()`, `current_status()`, `is_closed()`, `days_open()`, `is_overdue()`, `display_info()`
- **`ComplaintRegistry`**: attributes `office_name`, `complaints`; methods `add_complaint()`, `find()`, `display_all()`, `remove_complaint()`, `display_overdue()`, `category_summary()`
- The registry holds and manages `Complaint` objects, which demonstrates interaction between objects. For example, `display_overdue()` asks each complaint whether it `is_overdue()`, and `category_summary()` reads each complaint's category.

### Task 2: Data Structure
- A **dictionary** (`{complaint_id: Complaint}`) stores all complaints, so any record can be found instantly by its reference ID.
- `add_complaint()` and `display_all()` add and display records.
- **Bonus (tuples):** each status change is a **tuple** `(date, status, note)`, and a complaint's `status_log` is a tuple of these. Tuples cannot be changed, so each update builds a new tuple and the history of a complaint cannot be rewritten by accident. The lists of allowed categories, statuses and priorities are also tuples. The dictionary is the only data structure holding the complaint objects.

### Task 3: Methods
| Type | Method | Purpose |
|------|--------|---------|
| Instance | `update_status()`, `update_record()`, `current_status()`, `is_closed()`, `days_open()`, `is_overdue()`, `display_info()` | Work on one complaint's data |
| Class (`@classmethod`) | `Complaint.from_string("Water,Kissy,No water...")` | Alternative way to create a complaint from one line of text |
| Class (`@classmethod`) | `Complaint.category_options()` | Gives the allowed categories as text for prompts and errors |
| Static (`@staticmethod`) | `Complaint.suggest_priority()` | Suggests a starting priority from the category |
| Static (`@staticmethod`) | `Complaint.overdue_limit()` | Gives the number of days allowed for each priority |
| Static (`@staticmethod`) | `Complaint.normalize_category()` and `Complaint.normalize_status()` | Check a category or status typed in any capitalisation |

## Digital Public Goods (DPG) Alignment

| DPG Principle | How this project meets it |
|---------------|---------------------------|
| **Open-source** | The full source code is public on GitHub under the MIT licence, so anyone can use, study, modify and share it. |
| **Inclusive and accessible design** | Plain-language prompts, a numbered menu, and clear error messages that say how to fix a mistake. Input is accepted in any capitalisation. It runs on any low-spec computer, needs no internet connection and has no cost. Anyone can submit a complaint without creating an account. |
| **Privacy-respecting** | Complaints are anonymous. Only a category, a general area (district or ward), a description and a status history are stored. There are no names, phone numbers, addresses or ID numbers, and the prompt reminds users not to type personal details. A citizen tracks a complaint using the reference ID only. Data is kept in memory only and is not sent anywhere. A complaint can be removed at any time. |
| **Modular and reusable** | `Complaint` and `ComplaintRegistry` are separate, self-contained classes. They can be imported into other projects, for example a permit tracker or a feedback system, without changing the code. The start block means importing the file does not run the menu. |

## Sample Output

```
1. Submit complaint  2. Update status  3. Show all  4. Track one
5. Overdue complaints  6. Category summary  7. Remove complaint  8. Exit
Choose: 1
Do not include names, phone numbers or other personal details.
Category,area,description (categories: Water, Electricity, Roads, Health, Education, Waste, Other):
water,Kissy,No water from the community tap for three days
Complaint received. Your reference ID is CMP001.

Choose: 2
Complaint ID: cmp001
New status: In review, Resolved, Rejected
Status: in review
Short note (optional): Sent to water team
Updated. CMP001 is now: In review.

Choose: 4
Complaint ID: CMP001
ID: CMP001 | Water | Kissy | Priority: High | Status: In review | Open: 0 day(s)
    Issue: No water from the community tap for three days
    - 2026-10-18: Submitted (Complaint received)
    - 2026-10-18: In review (Sent to water team)
```

## Limitations and Future Improvements

- Complaints are lost when the program closes (kept in memory for privacy). A future version could add optional local storage.
- Anyone who has the program can update a status. A future version could add a staff login.
- Priorities and overdue limits are general values. Each office could set its own.
- Add a graphical interface and local-language support (e.g. Krio).

## Author
Ibrahim Kai Bangura

## Licence

Released under the [MIT Licence](LICENSE).
