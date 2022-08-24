from flask import Blueprint, render_template,url_for,redirect
from myproject import db 
from myproject.models import Owner
from myproject.owners.forms import AddOwner

owners_blueprint = Blueprint('owners', __name__,
                                template_folder = 'templates/owners')
                                
                                
@owners_blueprint.route('/add', methods = ['GET', 'POST'])                          
def add():
    
    form = AddOwner()
    
    if form.validate_on_submit():
        
        name = form.name.data
        puppy_id = form.puppy_id.data
        
        new_owner = Owner(name, puppy_id)
        
        db.session.add(new_owner)
        db.session.commit()
        
        return redirect(url_for('puppies.list'))
    
    return render_template('add_owner.html', form = form)