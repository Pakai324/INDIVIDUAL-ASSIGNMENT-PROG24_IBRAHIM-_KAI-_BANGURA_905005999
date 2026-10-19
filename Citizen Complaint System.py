
# Citizen Complaint System

from datetime import date


# ---------------------------------------------------------------- Class 1
class Complaint:
    """One citizen complaint and its status history (Task 1: attributes + methods)."""

    CATEGORIES = ("Water", "Electricity", "Roads", "Health", "Education", "Waste", "Other")
    STATUSES = ("Submitted", "In review", "Resolved", "Rejected")
    PRIORITIES = ("High", "Medium", "Low")
    CLOSED = ("Resolved", "Rejected")
    _counter = 0  # class attribute used to generate unique reference IDs

    def __init__(self, category, area, description):
        category = self.normalize_category(category)
        area = area.strip()
        description = description.strip()
        if not area:
            raise ValueError("Area cannot be empty (use a district or ward name).")
        if len(description) < 10:
            raise ValueError("Description must be at least 10 characters.")
        Complaint._counter += 1
        self.complaint_id = f"CMP{Complaint._counter:03d}"
        self.category = category
        self.area = area                      # general area only, no street address
        self.description = description
        self.priority = self.suggest_priority(category)
        # tuple of (date, status, note) tuples; it always holds the first entry
        self.status_log = ((date.today().isoformat(), "Submitted", "Complaint received"),)

    # ---- instance methods (Task 3)
    def update_status(self, new_status, note=""):
        """Add a status change as an immutable tuple: (date, status, note).
        Tuples cannot be changed, so a new tuple of entries is built."""
        new_status = self.normalize_status(new_status)
        if self.is_closed():
            raise ValueError("This complaint is already closed.")
        if new_status == "Submitted":
            raise ValueError("Choose one of: In review, Resolved, Rejected.")
        if new_status == self.current_status():
            raise ValueError(f"The complaint is already '{new_status}'.")
        new_entry = (date.today().isoformat(), new_status, note.strip())
        self.status_log = self.status_log + (new_entry,)

    def update_record(self, area=None, description=None, priority=None):
        if self.is_closed():
            raise ValueError("A closed complaint cannot be edited.")
        if area:
            self.area = area.strip()
        if description:
            if len(description.strip()) < 10:
                raise ValueError("Description must be at least 10 characters.")
            self.description = description.strip()
        if priority:
            priority = priority.strip().title()
            if priority not in Complaint.PRIORITIES:
                raise ValueError("Priority must be one of: " + ", ".join(Complaint.PRIORITIES) + ".")
            self.priority = priority

    def current_status(self):
        return self.status_log[-1][1]

    def is_closed(self):
        return self.current_status() in Complaint.CLOSED

    def days_open(self):
        """Days from submission until closed, or until today if still open."""
        start = date.fromisoformat(self.status_log[0][0])
        end = date.fromisoformat(self.status_log[-1][0]) if self.is_closed() else date.today()
        return (end - start).days

    def is_overdue(self):
        return (not self.is_closed()
                and self.days_open() > self.overdue_limit(self.priority))

    def display_info(self):
        flag = "  ** OVERDUE **" if self.is_overdue() else ""
        print(f"ID: {self.complaint_id} | {self.category} | {self.area} | "
              f"Priority: {self.priority} | Status: {self.current_status()} | "
              f"Open: {self.days_open()} day(s){flag}")
        print(f"    Issue: {self.description}")
        for entry_date, status, note in self.status_log:
            print(f"    - {entry_date}: {status}" + (f" ({note})" if note else ""))

    # ---- class methods (Task 3)
    @classmethod
    def from_string(cls, text):
        """Create a Complaint from 'category,area,description'.
        e.g. 'Water, Kissy, No water in the community tap for three days'.
        Only the first two commas split the text, so the description may contain commas."""
        parts = text.split(",", 2)
        if len(parts) != 3:
            raise ValueError("Use the format: category,area,description")
        return cls(parts[0], parts[1], parts[2])

    @classmethod
    def category_options(cls):
        """Allowed categories as text, for prompts and error messages."""
        return ", ".join(cls.CATEGORIES)

    # ---- static methods (Task 3)
    @staticmethod
    def suggest_priority(category):
        """General starting priority by category; staff can change it later."""
        if category in ("Water", "Health"):
            return "High"
        if category in ("Electricity", "Roads"):
            return "Medium"
        return "Low"

    @staticmethod
    def overdue_limit(priority):
        """Days a complaint may stay open before it is flagged as overdue."""
        return {"High": 7, "Medium": 14}.get(priority, 30)

    @staticmethod
    def normalize_category(category):
        """Check a category (any capitalisation) and return the standard form."""
        clean = category.strip().title()
        if clean not in Complaint.CATEGORIES:
            raise ValueError("Category must be one of: " + ", ".join(Complaint.CATEGORIES) + ".")
        return clean

    @staticmethod
    def normalize_status(status):
        """Check a status (any capitalisation) and return the standard form."""
        clean = status.strip().capitalize()
        if clean not in Complaint.STATUSES:
            raise ValueError("Status must be one of: " + ", ".join(Complaint.STATUSES) + ".")
        return clean


# ---------------------------------------------------------------- Class 2
class ComplaintRegistry:
    """Stores many Complaint objects in a dictionary keyed by reference ID
    (Task 2: one data structure + add/display functions)."""

    def __init__(self, office_name):
        self.office_name = office_name
        self.complaints = {}  # {complaint_id: Complaint}

    def add_complaint(self, complaint):
        self.complaints[complaint.complaint_id] = complaint
        print(f"Complaint received. Your reference ID is {complaint.complaint_id}.")

    def find(self, complaint_id):
        return self.complaints.get(complaint_id.strip().upper())

    def display_all(self):
        print(f"\n=== {self.office_name}: {len(self.complaints)} complaint(s) ===")
        if not self.complaints:
            print("No complaints yet.")
        for complaint in self.complaints.values():
            complaint.display_info()

    def remove_complaint(self, complaint_id):
        """Delete a complaint (for example when it was sent by mistake)."""
        removed = self.complaints.pop(complaint_id.strip().upper(), None)
        if removed is None:
            print("Complaint not found.")
            return False
        print(f"Complaint {removed.complaint_id} removed.")
        return True

    def display_overdue(self):
        """Show open complaints that have waited longer than their limit."""
        print(f"\n=== Overdue complaints: {self.office_name} ===")
        found = 0
        for complaint in self.complaints.values():
            if complaint.is_overdue():
                found += 1
                print(f"{complaint.complaint_id} | {complaint.category} | {complaint.area} | "
                      f"{complaint.priority} priority | open {complaint.days_open()} days")
        if found == 0:
            print("No overdue complaints.")
        return found

    def category_summary(self):
        """Count the complaints in each category (uses the categories tuple)."""
        print(f"\n=== Category summary: {self.office_name} ===")
        for category in Complaint.CATEGORIES:
            total = sum(1 for c in self.complaints.values() if c.category == category)
            print(f"{category}: {total}")


# ---------------------------------------------------------------- Demo / menu
def demo(registry):
    """Optional sample data. Not run by default; call demo(registry) to load it."""
    c1 = Complaint("Water", "Kissy", "No water from the community tap for three days")
    c2 = Complaint.from_string("Roads, Wellington, Large pothole near the market")  # class method
    registry.add_complaint(c1)
    registry.add_complaint(c2)
    c1.update_status("In review", "Sent to water team")    # instance method
    c2.update_record(priority="High")
    registry.display_all()


def menu(registry):
    while True:
        print("\n1. Submit complaint  2. Update status  3. Show all  4. Track one")
        print("5. Overdue complaints  6. Category summary  7. Remove complaint  8. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            try:
                print("Do not include names, phone numbers or other personal details.")
                text = input(f"Category,area,description (categories: {Complaint.category_options()}):\n")
                registry.add_complaint(Complaint.from_string(text))
            except ValueError as error:
                print(f"Error: {error}")
        elif choice == "2":
            complaint = registry.find(input("Complaint ID: "))
            if complaint:
                try:
                    print("New status: " + ", ".join(Complaint.STATUSES[1:]))
                    status = input("Status: ")
                    note = input("Short note (optional): ")
                    complaint.update_status(status, note)
                    print(f"Updated. {complaint.complaint_id} is now: {complaint.current_status()}.")
                except ValueError as error:
                    print(f"Error: {error}")
            else:
                print("Complaint not found.")
        elif choice == "3":
            registry.display_all()
        elif choice == "4":
            complaint = registry.find(input("Complaint ID: "))
            if complaint:
                complaint.display_info()
            else:
                print("Complaint not found.")
        elif choice == "5":
            registry.display_overdue()
        elif choice == "6":
            registry.category_summary()
        elif choice == "7":
            registry.remove_complaint(input("Complaint ID to remove: "))
        elif choice == "8":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    registry = ComplaintRegistry("District Complaints Office")
    menu(registry)  # starts empty; use demo(registry) for sample data
