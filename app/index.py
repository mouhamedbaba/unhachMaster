from flask import  request, render_template

import string
import bcrypt

from lib.generate_combo import generate_password_combinations
from lib.db import *
from app.app import app



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        hashed_password = request.form['hashed_password']
        if check_in_db(hashed_password):
            db_data = get_db_data()  # Obtenir les données de la base de données
            print(db_data)
            password="Pas de mot de passe trouvable"
            for row in db_data['data']:
                print(row['hash'])
                print(row['password'])
                if row['hash'] == hashed_password :
                    password = row['password']
            return render_template('result.html', password_found=True, password=password, db_data=db_data['data'])
        else:
            digit_number = int(request.form['digit_number'])
            have_special_char = request.form['have_special_char'].lower() == "oui"
            range_caracters_min = int(request.form['range_caracters_min'])
            range_caracters_max = int(request.form['range_caracters_max'])

            total_combinations = sum(len(string.printable) ** length for length in range(range_caracters_min, range_caracters_max + 1))

            for length in range(range_caracters_min, range_caracters_max + 1):
                for password in generate_password_combinations(length, length, digit_number > 0, have_special_char):
                    print("Password:", password, end='\r', flush=True)
                    if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                        insert_into_db(hashed_password, password)
                        db_data = get_db_data()  # Obtenir les données de la base de données
                        return render_template('result.html', password_found=True, password=password, db_data=db_data['data'])
            return render_template('result.html', password_found=False)
    return render_template('index.html')