from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash

from .forms import *

# added this import
from .reservations import *


#@app.route("/", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def user_options():
    
    form = UserOptionForm()
    if request.method == 'POST' and form.validate_on_submit():
        option = request.form['option']

        if option == "1":
            return redirect('/admin')
        else:
            return redirect("/reservations")
    
    return render_template("options.html", form=form, template="form-template")

@app.route("/admin", methods=['GET', 'POST'])
def admin():

    form = AdminLoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            # get admin username and password to validate credentials
            username = request.form['username']
            password = request.form['password']

            logins = get_login_dict()

            if username in logins:
                if password == logins[username]:
                    # LOGIN SUCCESSFUL
                    err = None
                    sales = get_sales()
                    chart = generate_seating_chart()
                    
                else:
                    err = "ERROR: Invalid username or password."
                    sales = None
                    chart = None
            else:
                err = "ERROR: Invalid username or password"
                sales = None
                chart = None
            return render_template("admin.html", form=form, template="form-template", err=err, sales=sales, chart=chart)

    return render_template("admin.html", form=form, template="form-template")
    


@app.route("/reservations", methods=['GET', 'POST'])
def reservations():

    form = ReservationForm()
    chart = generate_seating_chart()
    if request.method == 'POST':
        if form.validate_on_submit():
            firstname = request.form['first_name']
            lastname = request.form['last_name']
            row = request.form['row']
            seat = request.form['seat']


            if chart[int(row)-1][int(seat)-1] == 'X':
                err = "ERROR! Row: " + row + " Seat: " + seat + " is already assigned. Choose again."
                confirmation = None
            else: 
                err = None

                e_ticket = make_eticket(firstname)
                make_reservation(firstname, str(int(row) - 1), str(int(seat) - 1), e_ticket)
                confirmation = "Congratulations " + firstname + "! Row: " + row + " Seat: " + seat + " is now reserved for you. Enjoy the trip! Your e-ticket number is: " + e_ticket

                chart = generate_seating_chart()
            
            return render_template("reservations.html", form=form, template="form-template", err=err, chart=chart, confirmation=confirmation)

    return render_template("reservations.html", form=form, template="form-template", chart=chart)

