master = getpass.getuser() or "Ayon"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def speak(audio):
    gui.speak(audio)
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning" + master)
    elif 12 <= hour < 18:
        speak("Good afternoon" + master)
    else:
        speak("Good evening" + master)

    speak("I am Finder, please tell me how I can help you")



def textCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        txt_name.value = ("Listening")
        
        speak("listening")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        question = r.recognize_google(audio, language='en-in')
    # question = r.recognize_google(audio, language='en-in')
        print(f"User said: {question}\n")

    except Exception as e:
        # print(e)
        print("Say that again, please")
        speak("please say that again")
        return "none"
    return question


def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)


def get_operator_fn(op):
    return {
        '+': operator.add,
        '-': operator.sub,
        'x': operator.mul,
        '/': operator.__truediv__,
        'Mod': operator.mod,
        'mod': operator.mod,
        '^': operator.xor,
    }[op]


def eval_binary_expr(op1, oper, op2):
    op1, op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)


def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]


def get_weather_report(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=c71d5fdb1e7a7497705053202f40ac17&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"


def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


'''def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False'''


def oddeven(num):
    if num % 2 == 0:
        print("even")
        speak("The number is even")
        speak("The number is even")
    elif num > 0:
        print("The number is odd")
        speak("The number is odd")


def play_on_youtube(video):
    kit.playonyt(video)


def search_on_google(query):
    kit.search(query)


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']


def get_latest_news():
    news_headlines = []
    res = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey=4c0c2a2bd3d84e318ef8f4dc23e2793a&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]


wish()

while True:
    question = textCommand().lower()
    if 'wikipedia' in question:
        speak("Searching Wikipedia...")
        question = question.replace("wikipedia", "")
        results = wikipedia.summary(question, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in question:
        webbrowser.open("youtube.com")
    

    elif 'open google' in question:
        webbrowser.open("google.com")

    elif 'your name' in question:
        speak("FINDER")
        print(speak)

    elif "what can you do for me" in question or "what can you do" in question:
        speak(
            "I can help you in searching google, youtube and tell you jokes and many more")
        print(speak)

    elif "hi" in question or "hello" in question or "hai" in question:
        speak("Hello how are you, I hope your loved once are safe and healthy")

    elif 'volume up' in question or 'sound up' in question or 'increase sound' in question or 'increase volume' in question:
        pyautogui.press("volumeup")

    elif 'volume down' in question or 'sound down' in question or 'decrease sound' in question or 'decrease volume' in question:
        pyautogui.press('volumedown')

    elif 'volume mute' in question or 'mute' in question:
        pyautogui.press('volumemute')

    elif 'alarm' in question:
        speak("tell me the time to set alarm for you. for example you can say , set alarm to 7:30 am ")
        tt = textCommand()
        tt = tt.replace("set alarm to", "") or ("set alarm at", "") or ("set alarm for", "")
        tt = tt.replace(".", "")
        tt = tt.upper()
        import alarm
        speak(("Alarm set to"), (tt))
        alarm.alarm(tt)
    elif 'time' in question:
        hour = str(int(datetime.datetime.now().hour))
        min = str(int(datetime.datetime.now().minute))
        time = (hour+"hours"+min+"minutes")
        speak(time)
    elif "send whatsapp message" in question:
        speak('To what number should I send the message? Please enter in the console: ')
        number = input("Enter the number: ")
        speak("What is the message?")
        message = textCommand().lower()
        send_whatsapp_message(number, message)
        speak("I've sent the message.")
    elif 'date' in question:
        date = str(int(datetime.datetime.now().day))
        mon = str(datetime.datetime.now().month)
        year = str(int(datetime.datetime.now().year))
        speak(date)
        speak(mon)
        speak(year)
    elif 'calculate' in question:
        speak("what should i calculate")
        calc = textCommand().lower()
        print(eval_binary_expr(*(calc.split())))
        speak("The answer is ")
        speak(eval_binary_expr(*(calc.split())))
    elif 'news' in question:
        speak(f"I'm reading out the latest news headlines,")
        speak(get_latest_news())
        speak("For your convenience, I am printing it on the screen.")
        print(*get_latest_news(), sep='\n')

    elif 'open word' in question:
        os.chdir(r'C:/Users/ayond/OneDrive/Desktop')
        os.startfile("New Microsoft Word Document.docx")

    elif 'open powerpoint' in question:
        os.chdir(
            r'C:/Users/ayond/OneDrive/Desktop')
        os.startfile("New Microsoft PowerPoint Presentation.pptx")

    elif 'open excel' in question:
        os.chdir(
            r'C:/Users/ayond/OneDrive/Desktop')
        os.startfile("New Microsoft Excel Worksheet.xlsx")

    elif 'play music' in question or "play songs" in question:
        music_dir = 'C:/Users/ayond/OneDrive/Desktop/music'
        # music_dir = ''  # Music directory of your system # Linux
        songs = os.listdir(music_dir)
        print(songs)
        count = 0
        # Iterate directory
        for path in os.listdir(music_dir):
            # check if current path is a file
            if os.path.isfile(os.path.join(music_dir, path)):
                count += 1
        n = random.randint(0, (count - 1))
        print("Playing Music...")
        # Finder surprise you a random music
        os.startfile(os.path.join(music_dir, songs[n]))

    elif 'your name' in question:
        speak("My name is Finder")
        print(speak)

    elif 'open google' in question:
        webbrowser.open("google.com")

    elif 'tomorrow' in question:
        date = str(int(datetime.datetime.now().day) + 1)
        speak(date)

    elif 'is this a leap year' in question:
        year = int(datetime.datetime.now().year)
        l = year % 4
        if l == 0:
            print("Leap-Year")
            speak("Yes this is a leap year")
        else:
            print("Not a Leap-Year")
            speak("No this is not a leap year")

    elif 'open instagram' in question:
        webbrowser.open('instagram.com')

    elif 'odd or even' in question:
        print("Please say the number which you want to check odd or even")
        speak("Please say the number which you want to check odd or even")
        a = textCommand().lower()
        num = int(a)
        oddeven(num)

    elif 'bmi score' in question or "bmi calculator" in question:
        speak('what is your height in centimeter')
        a1 = int(textCommand().lower())
        speak('what is your weight in kilogram')
        a2 = int(textCommand().lower())
        a3 = a1/100
        height = float(a3)
        weight = float(a2)
        bmi = round(weight/(height^2))
        if bmi < 18.5:
            speak("underweight eat a little more you're bmi is=", bmi)
            print("underweight eat a little more you're bmi is =", bmi)
        elif bmi < 25.0:
            speak("normal weight you are perfect you're bmi is = ", bmi)
            print("normal weight you are perfect you're bmi is = ", bmi)
        elif bmi < 30.0:
            speak("overweight you should start thinking for gym you're bmi is=", bmi)
            print("overweight you should start thinking for gym you're bmi is = ", bmi)
        elif bmi < 35.0:
            speak("overweight you should start dieting you're bmi is=", bmi)
            print("overweight you should start dieting you're bmi is = ", bmi)
        elif bmi > 35.0:
            speak("you Should start work out from now you are overweight you're bmi is=", bmi)
            print("you Should start work out from now you are overweight you're bmi is = ", bmi)

    elif "email" in question:
        speak("Who is the recipient? ")
        recipient = textCommand()
        if "me" in recipient:
            try:
                speak("What should I say? ")
                content = textCommand()
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.login("Your_Username", "Your_Password")
                server.sendmail("Your_Username", "Recipient_Username", content)
                server.close()
                speak("Email sent!")
            except Exception:
                speak("Sorry! I am unable to send your message at this moment!")

    elif 'who are you' in question:
        print("I am Finder. An AI Featured Desktop Assistant")
        speak("I am Finder. An AI Featured Desktop Assistant")
    elif 'how are you' in question:
        print("I am well, How are you")
        speak("I am well, How are you")

    elif 'i am well' in question:
        print("Have a nice day")
        speak("Have a nice day")

    elif 'i am not well' in question or "not good" in question or "not well" in question or "bad" in question:
        print("Sorry about that, may you recover soon")
        speak("Sorry about that, may you recover soon")

    elif 'quit' in question or 'bye' in question or 'exit' in question:
        print("Quitting...")
        speak("good bye, i hope i was helpful thank you")
        exit()

    elif 'joke' in question:
        speak(f"Hope you like this one")
        joke = get_random_joke()
        speak(joke)
        speak("For your convenience, I am printing it on the screen.")
        print(joke)
    elif 'youtube' in question:
        speak('What do you want to play on Youtube,?')
        video = textCommand().lower()
        play_on_youtube(video)
    elif "advice" in question:
        speak(f"Here is an advice for you,")
        advice = get_random_advice()
        speak(advice)
        speak("For your convenience, I am printing it on the screen.")
        print(advice)
    elif 'search on google' in question:
        speak('What do you want to search on Google,?')
        query = textCommand().lower()
        search_on_google(question)
    elif 'weather' in question:
        ip_address = find_my_ip()
        city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
        speak(f"Getting weather report for your city {city}")
        weather, temperature, feels_like = get_weather_report(city)
        speak(
            f"The current temperature is {temperature}, but it feels like {feels_like}")
        speak(f"Also, the weather report talks about {weather}")
        speak("For your convenience, I am printing it on the screen.")
        print(
            f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
        page.update()