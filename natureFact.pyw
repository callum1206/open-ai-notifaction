import openai
from win11toast import toast
from datetime import datetime
import tkinter as tk

openai.api_key = "PUT YOUR API KEY HERE"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Tell a random fact about nature in less than 20 words"}
  ]
)

response = completion.choices[0].message.content
name = 'PUT YOUR NAME HERE'

if int(datetime.now().strftime('%H')) < 12:
  greet = f'Good Morning {name}'
elif int(datetime.now().strftime('%H')) < 17:
  greet = f'Good afternoon {name}'
else:
  greet = f'Good Evening {name}'


xml = """
<toast launch="action=openThread&amp;threadId=92187">

    <visual>
        <binding template="ToastGeneric">
            <text hint-maxLines="1">{}</text>
            <text>{}</text>
            <image placement="appLogoOverride" hint-crop="circle" src="https://i.pinimg.com/originals/7d/26/a6/7d26a662ac1efc82ef189d093494c3a2.jpg"/>
            <image placement="hero" src="https://secretcompass.com/wp-content/uploads/2018/01/Jungle-Rot.jpg"/>
        </binding>
    </visual>

</toast>""".format(greet, response)


toast(xml=xml)
