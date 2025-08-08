from flask import Flask, render_template, request, url_for, redirect
from PasswordCheckerPhase3.backend.passwordCheckerPhase3 import passwordChecker

app = Flask(__name__, template_folder='frontend/templates', static_folder='frontend/static')


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/check', methods=['GET','POST'])
def check_password():
    if request.method == 'POST':
        password = request.form.get('password')
        result = passwordChecker(password)

        strength_message = {
            "Verry Strong": "Your password is very strong. Excellent choice!",
            "Strong": "Your password is strong. Good job!",
            "Medium": "Your password is medium. Consider making it stronger.",
            "Weak": "Your password is weak. Please consider improving it.",
            "Very Weak": "Your password is very weak. It needs significant improvement."
        }

        return render_template('results.html', strength_message=strength_message[result['strength']],
                               is_pwned=result['pwned'])

@app.route('/help')
def help():
    return render_template('help.html')


if __name__ == '__main__':
    app.run(debug=True)
