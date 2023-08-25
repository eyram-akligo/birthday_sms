import datetime
from azure.communication.sms import SmsClient
from staff_info import birthdays


connection_string = "endpoint=https://vra-comm-demo.africa.communication.azure.com/;accesskey=ZbmpC" \
                    "+faessFTozix5OW8IXj4oOLORCRlFUi14JVDASWDY6YZCVknQOvLknvKegPjr0/RJUBy0BLSqV0jtouSA== "
sender_phone_number = "+12564101734"


def send_birthday_sms(receiver, name):
    """Connecting to azure communication services and sending message"""
    sms_client = SmsClient.from_connection_string(connection_string)
    message = f"Happy Birthday, {name.title()}!!\nEnjoy your day."
    sms_client.send(sender_phone_number, receiver, message)


today = datetime.date.today()
for employee in birthdays:
    name = employee['name']
    contact_number = employee['phone_number']
    date_of_birth = employee['d_o_b']
    birth_date = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d")
    if birth_date.month == today.month and birth_date.day == today.day:
        send_birthday_sms(contact_number, name)
        print(f"SMS sent to {name.title()} for their birthday.")
