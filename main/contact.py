from flask.ext import wtf
import flask
import auth
import model
from main import app

class ContactUpdateForm(wtf.Form):
  name = wtf.StringField('Name', [wtf.validators.required()])
  email = wtf.StringField('Email', [wtf.validators.optional(), wtf.validators.email()])
  phone = wtf.StringField('Phone', [wtf.validators.optional()])
  address = wtf.TextAreaField('Address', [wtf.validators.optional()])
  
@app.route('/contact/create/', methods=['GET', 'POST'])
@auth.login_required
def contact_create():
  form = ContactUpdateForm()
  if form.validate_on_submit():
    contact_db = model.Contact(
        user_key=auth.current_user_key(),
        name=form.name.data,
        email=form.email.data,
        phone=form.phone.data,
        address=form.address.data,
      )
    contact_db.put()
    return flask.redirect(flask.url_for('welcome'))
  return flask.render_template(
      'contact_create.html',
      html_class='contact-create',
      title='Create Contact',
      form=form,
    )
