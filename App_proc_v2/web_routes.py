from flask import Flask, request, render_template, url_for, redirect
import reach_db

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("layout.html")


@app.route("/mentors")
def mentors_and_schools_page():
    webpage_data = reach_db.select_mentors_by_school
    return render_template("mentors.html", data=webpage_data)


@app.route("/all-school")
def all_school_page():
    webpage_data = reach_db.select_all_schools
    return render_template("all-school.html", data=webpage_data)


@app.route("/mentors-by-country")
def mentors_by_country():
    webpage_data = reach_db.mentors_by_country
    return render_template("mentors-by-country.html", data=webpage_data)


@app.route("/contacts")
def contacts_page():
    webpage_data = reach_db.contacts_by_school
    return render_template("contacts.html", data=webpage_data)


@app.route("/applicants")
def applicants_page():
    webpage_data = reach_db.applicants_with_creaton_dates
    return render_template("applicants.html", data=webpage_data)


@app.route("/applicants-and-mentors")
def applicants_and_mentors_page():
    webpage_data = reach_db.applicants_and_their_mentors
    return render_template("applicants-and-mentors.html", data=webpage_data)


@app.route("/search-in-database", methods=["POST"])
def search_in_mentors_db():
    given_name = request.form['name']
    database_name = request.form['database']
    mentor_data = None
    applicant_data = None
    if database_name == "mentors":
        mentor_data = reach_db.database_custom_select_query(database_name, given_name)
    elif database_name == "applicants":
        applicant_data = reach_db.database_custom_select_query(database_name, given_name)

    return render_template("layout.html", mentor_data=mentor_data, applicant_data=applicant_data)


if __name__ == '__main__':
    app.run(debug=True)