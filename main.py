from flask import Flask, request

app = Flask(__name__)

# შეტყობინებების სია მეხსიერებაში
messages = []

@app.route("/")
def home():
    # მთავარი გვერდის სტრუქტურა და ფორმა
    html = """
    <title>Whale Chat</title>
    <body style="font-family: Arial, sans-serif; margin: 30px; background: #f0f2f5;">
        <h1>🐳 Whale Chat (პირადი)</h1>
        
        <form action="/send" method="post" style="margin-bottom: 20px;">
            <input name="msg" placeholder="ჩაწერეთ სათქმელი..." required style="padding: 8px; width: 250px;">
            <button style="padding: 8px 15px; background: #0084ff; color: white; border: none; border-radius: 4px; cursor: pointer;">გაგზავნა</button>
        </form>
        
        <div style="background: white; padding: 15px; border-radius: 8px; max-width: 400px; border: 1px solid #ccc;">
    """

    # თუ სია ცარიელია, გამოაჩენს მინიშნებას
    if not messages:
        html += "<p style='color: gray; font-style: italic;'>ჩაწერილი შეტყობინებები არ არის...</p>"

    # შეტყობინებების სათითაოდ გამოტანა სიიდან
    for m in messages:
        html += f"<p style='margin: 5px 0; padding: 6px 10px; background: #e4e6eb; border-radius: 10px; width: fit-content; word-break: break-word;'>{m}</p>"

    html += """
        </div>
    </body>
    """
    return html

@app.route("/send", methods=["POST"])
def send():
    user_text = request.form["msg"]
    
    # ვამატებთ მხოლოდ თქვენს ჩაწერილ ტექსტს
    messages.append(user_text)
    
    # ვაბრუნებთ განახლებულ მთავარ გვერდს
    return home()

if __name__ == '__main__':
    app.run()
