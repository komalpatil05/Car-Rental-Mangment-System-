import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

def send_booking_email(customer_email, customer_name, car_name, booking_date):
    my_mail = "urbandrive05@gmail.com"
    passcode = "jjcf cwas dvqj yncq"   # Gmail App Password

    subject = "Car Rental Booking Confirmation"
    message = f"""
Dear {customer_name},

Your UrbanDrive booking has been confirmed successfully!

Booking Details:
Car Name     : {car_name}
Booking Date : {booking_date}

Thank you for choosing UrbanDrive Service.
If you have any questions, feel free to contact us.

Best Regards,
UrbanDrive Team
"""

    msg = MIMEMultipart()
    msg['From'] = my_mail
    msg['To'] = customer_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain', 'utf-8'))

    try:
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=my_mail, password=passcode)

        connection.sendmail(
            from_addr=my_mail,
            to_addrs=customer_email,
            msg=msg.as_string()
        )

        print("✅ Booking confirmation email sent successfully!")

    except Exception as e:
        print("❌ Email sending failed:", e)

    finally:
        connection.close()


def send_payment_success_email(customer_email, customer_name, car_name, pickup_date, return_date, total_amount):
    logging.info(f"Attempting to send payment success email to {customer_email}")

    my_mail = "urbandrive05@gmail.com"
    passcode = "jjcf cwas dvqj yncq"   # Gmail App Password

    subject = "Car Rental Payment Confirmation"
    message = f"""
Dear {customer_name},

Your payment has been processed successfully! 🎉

Booking Details:
Car Name      : {car_name}
Pickup Date   : {pickup_date}
Return Date   : {return_date}
Total Amount  : ₹{total_amount}

Thank you for choosing UrbanDrive Service.
Your booking is now confirmed and ready.

Best Regards,
UrbanDrive Team
"""

    msg = MIMEMultipart()
    msg['From'] = my_mail
    msg['To'] = customer_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain', 'utf-8'))

    try:
        logging.info("Connecting to SMTP server")
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        logging.info("Logging in to Gmail")
        connection.login(user=my_mail, password=passcode)
        logging.info(f"Sending email to {customer_email}")
        connection.sendmail(
            from_addr=my_mail,
            to_addrs=customer_email,
            msg=msg.as_string()
        )

        print("✅ Payment confirmation email sent successfully!")
        logging.info("Email sent successfully")

    except Exception as e:
        print("❌ Email sending failed:", e)
        logging.error(f"Email sending failed: {e}")

    finally:
        try:
            connection.close()
            logging.info("SMTP connection closed")
        except:
            pass