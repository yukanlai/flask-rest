from flask import abort, flash, redirect, render_template, url_for

from . import admin
from forms import AnimalForm
from .. import db
from ..models import Animal

# Animal Views

@admin.route('/animals', methods=['GET', 'POST'])
def list_animals():
    """
    List all animals
    """

    animals = Animal.query.all()

    return render_template('admin/animals/animals.html',
                           animals=animals, title="Animals")

@admin.route('/animals/add', methods=['GET', 'POST'])
def add_animal():
    """
    Add an animal to the database
    """

    add_animal = True

    form = AnimalForm()
    if form.validate_on_submit():
        animal = Animal(animal_id=form.animal_id.data,
                                sex=form.sex.data,
                                age=form.age.data)
        try:
            # add animal to the database
            db.session.add(animal)
            db.session.commit()
            flash('You have successfully added a new animal.')
        except Exception as e:
            # in case animal id already exists
            flash('Error: animal id already exists.')

        # redirect to animals page
        return redirect(url_for('admin.list_animals'))

    # load animal template
    return render_template('admin/animals/animal.html', action="Add",
                           add_animal=add_animal, form=form,
                           title="Add Animal")

@admin.route('/animals/edit/<int:id>', methods=['GET', 'POST'])
def edit_animal(id):
    """
    Edit an animal
    """

    add_animal = False

    animal = Animal.query.get_or_404(id)
    form = AnimalForm(obj=animal)
    if form.validate_on_submit():
        animal.animal_id = form.animal_id.data
        animal.sex = form.sex.data
        animal.age = form.age.data

        db.session.commit()
        flash('You have successfully edited the animal.')

        # redirect to the animals page
        return redirect(url_for('admin.list_animals'))

    form.animal_id.data = animal.animal_id
    form.sex.data = animal.sex
    form.age.data = animal.age

    return render_template('admin/animals/animal.html', action="Edit",
                           add_animal=add_animal, form=form,
                           animal=animal, title="Edit Animal")

@admin.route('/animals/delete/<int:id>', methods=['GET', 'POST'])
def delete_animal(id):
    """
    Delete an animal from the database
    """

    animal = Animal.query.get_or_404(id)
    db.session.delete(animal)
    db.session.commit()
    flash('You have successfully deleted the animal.')

    # redirect to the animals page
    return redirect(url_for('admin.list_animals'))

    return render_template(title="Delete Animal")