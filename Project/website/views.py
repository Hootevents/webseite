# Hier kommen die Pfade rein, zu denen ein Nutzer navigieren kann, die nichts mit anmeldung zu tun haben
# Mit der render_tempplate function werden die html templates zu einer webseite geformt
from flask import Blueprint, render_template, request, flash, jsonify
from . import db
from .models import Note
import json

from flask_login import login_required, current_user
# Wir erstellen einen Blueprint, damit wir hier unsere URLs definieren können und den tatsächlichen Inhalt von anderen Dateien beziehen können
views = Blueprint('views', __name__)

# Der Pfad eines Blueprints wird so definiert:


@views.route('/', methods=['GET', 'POST'])
def home():
    # Hier könnte man nun einfach html zurückgeben
    # return "<h1>Test</h1>" - Auf der Webseite steht "Test"

    return render_template("home.html", user=current_user)
