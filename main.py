import customtkinter
import requests

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("740x500")
app.title("Currency exchanger")
currencyframe = customtkinter.CTkFrame(app, fg_color= 'transparent')
currencyframe2 = customtkinter.CTkFrame(app, fg_color= 'transparent')

response = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/EUR/')
# response2 = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/usd/')
data = response.json()
# data2 = response2.json()
liczba = data['rates'][0]['mid']
# liczba2 = data2['rates'][0]['mid']

# x = input()

# x = float(x)

# a = x*liczba
# b = round(a/liczba2, 2)
# print(b)

Currency = ['PLN', 'EUR', 'USD', 'GBP', 'CHF', 'JPY', 'CZK', 'CNY', 'HUF']

def ExchangeCurrency():
    sum = float(total.get())
    curr = ChooseCurrency.get()
    curr2 = ChooseCurrency2.get()

    if curr != 'PLN':
        api = f'http://api.nbp.pl/api/exchangerates/rates/a/{curr}'
        response = requests.get(api)
        data = response.json()
        liczba = data['rates'][0]['mid']
        sum = sum*liczba

    if curr2 != 'PLN':
        api2 = f'http://api.nbp.pl/api/exchangerates/rates/a/{curr2}'
        response2 = requests.get(api2)
        data2 = response2.json()
        liczba2 = data2['rates'][0]['mid']
        final = round(sum/liczba2, 2)
    else:
        final = round(sum, 2)
    

    exchanged.configure(text=final)
    

def ChangeCurrenct():
    curr = ChooseCurrency.get()
    curr2 = ChooseCurrency2.get()
    ChooseCurrency.set(curr2)
    ChooseCurrency2.set(curr)

font=customtkinter.CTkFont(family='Open Sans', size=14, weight='bold')
font2=customtkinter.CTkFont(family='Open Sans', size=14)

total = customtkinter.CTkEntry(currencyframe, font=font2, width=60, height=35)
total.pack(side = 'top')

ChooseCurrency = customtkinter.CTkOptionMenu(currencyframe, width=80, values=Currency)
ChooseCurrency.set('PLN')
ChooseCurrency.pack(pady=5)

currencyframe.place(anchor='w', relx = 0.30,rely=0.45)

enter = customtkinter.CTkButton(app, width=50, height=40, text="Przelicz", font=font, command=ExchangeCurrency)
enter.pack(pady=180)

exchanged = customtkinter.CTkLabel(currencyframe2, width=50, height=40, text="", font=font)
exchanged.pack()

ChooseCurrency2 = customtkinter.CTkOptionMenu(currencyframe2, width=80, values=Currency)
ChooseCurrency2.pack(pady=5)
ChooseCurrency2.set('EUR')

currencyframe2.place(anchor='w', relx = 0.60, rely=0.447)

change = customtkinter.CTkButton(app, text = '<>', width=40, height=30, font=font, command=ChangeCurrenct)
change.place(anchor='n', relx = 0.5, rely=0.48)

app.mainloop()