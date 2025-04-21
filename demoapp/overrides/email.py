import frappe

def get_sender_details():
    return "Custom Sender", "noreply@example.com"

def send(self, sender, recipient, msg):    
    frappe.logger().info(f"Custom Email Hook: Sending email to {recipient} from {sender}")
    self.update_status("Sending")
    try:
        frappe.sendmail(
            recipients=recipient,
            sender=sender,
            subject=self.subject,
            message=msg
        )
        self.update_status("Sent")
        frappe.logger().info("Email sent successfully!")

    except Exception as e:
        self.update_status("Error")
        frappe.logger().error(f"Failed to send email: {str(e)}")
