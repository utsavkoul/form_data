# # This is a sample Python script.
# from datetime import datetime
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# from flask import Flask, render_template, request
# from datetime import *; from dateutil.relativedelta import *
# import calendar
# from formapp.database import Personal_details, add_form_data, get_data
#
# app = Flask(__name__, template_folder='templates')
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'GET':
#         pass
#         data = get_data()
#         # return render_template('index.html', data=data, detail_msg='Details', first_name='', last_name='',email='', dob='', days='', months='', years='', percentage='', aadhar_no='')data = get_data()
#         return render_template('index.html', data=[], detail_msg='Details', first_name='', last_name='',email='', dob='', days='', months='', years='', percentage='', aadhar_no='')
#     if request.method == 'POST':
#         first_name = request.form['first_name']
#         last_name = request.form['last_name']
#         email = request.form['email']
#         dob = str(request.form['dob'])
#         marks = request.form['marks']
#         outof = request.form['outof']
#         aadhar_no = request.form['aadhar_no']
#
#         dob_year = datetime.strptime(dob, "%Y-%m-%d")
#         present = datetime.now()
#         percentage = (float(marks) / float(outof)) * 100
#         if dob_year <= datetime.now():
#         # days = present.day - dob_year.day
#         # months = present.month - dob_year.month
#         # years = present.year - dob_year.year
#             total_time = relativedelta(present, dob_year)
#             print(total_time)
#             age = total_time.years
#             personal_details = Personal_details(first_name, last_name, email, dob, age, total_time.days,
#                                                 total_time.months, total_time.years, marks, outof, percentage, aadhar_no)
#
#             add_form_data(personal_details)
#         else:
#             raise Exception("Date selected is greater than current date")
#
#         print(first_name, last_name, email, dob, total_time, total_time.days, total_time.months, total_time.years, marks, outof, percentage, aadhar_no)
#
#
#         all_data = get_data()
#         return render_template('index.html', detail_msg='Details', all_data=all_data, first_name=first_name, last_name=last_name,email=email, dob=dob, age=age, days=total_time.days, months=total_time.months, years=total_time.years, percentage=percentage, aadhar_no=aadhar_no)
#
#
# @app.route('/form', methods=['POST'])
# def form():
#     data = get_data()
#     return render_template('index.html', data=data, detail_msg='Details', first_name='', last_name='', email='', dob='',
#                            days='', months='', years='', percentage='', aadhar_no='')
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     app.run(debug=True)
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
