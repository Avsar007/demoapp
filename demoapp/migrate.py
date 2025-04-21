import frappe
from frappe.utils.backups import scheduled_backup

def before_migrate():
    print("Before Migrate: Taking database backup...") 
    try:
        scheduled_backup(ignore_files=True) 
        print("Database backup completed successfully.")
    except Exception as e:
        print(f"Backup Failed: {e}")

def after_migrate():
    print("After Migrate: Running custom post-migration tasks...")
    try:
        # frappe.db.set_value("User", {"enabled": 1}, "last_login", frappe.utils.now())
        frappe.clear_cache()
        print("Migration completed successfully!")
    except Exception as e:
        print(f"Error in after_migrate: {e}")