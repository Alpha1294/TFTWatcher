from flask import Blueprint, render_template, flash, request, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from riotwatcher import TftWatcher, ApiError


views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        note = request.form.get("note")

        if len(note) < 1:
            flash("Note is too short!", category="error")

        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note Added!", category="succes")
    return render_template("home.html", user=current_user)


@views.route("/delete-note", methods=["POST"])
def delete_note():
    note = json.loads(request.data)
    noteId = note["noteId"]
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


@views.route("/edit_note/<id>", methods=["GET", "POST"])
@login_required
def edit_note(id):
    note = Note.query.get(id)

    if request.method == "POST":
        note.data = request.form["note"]
        db.session.commit()

        return redirect(url_for("views.home"))

    return render_template("edit_note.html", user=current_user, note=note)


@views.route("/tft", methods=["GET", "POST"])
def tft():
    summoner = request.form.get("summoner")
    my_region = "euw1"
    tft_watcher = TftWatcher("RGAPI-363c863e-2e71-4992-85e9-6742897145ea")
    summoner = request.form.get("summoner")
    summoner_name = ""
    summoner_info = ""
    match_by_id = {}
    participantes = []
    units = []

    try:
        summoner_name = tft_watcher.summoner.by_name(my_region, summoner)
        summoner_info = tft_watcher.league.by_summoner(my_region, summoner_name["id"])
        puuid = summoner_name["puuid"]
        match_history_ids = tft_watcher.match.by_puuid(my_region, puuid, 1)
        last_match = match_history_ids[0]

        match_by_id = tft_watcher.match.by_id(my_region, last_match)
        units = match_by_id["info"]["participants"][0]["units"]

    except ApiError as err:
        if err.response.status_code == 404:
            flash(
                "You crazy or what,thats not a valid summoners name", category="error"
            )
        elif err.response.status_code != 404:
            summoner_name = tft_watcher.summoner.by_name(my_region, summoner)
            summoner_info = tft_watcher.league.by_summoner(
                my_region, summoner_name["id"]
            )
    if request.method == "POST":
        print("soy el post method loco")

    return render_template(
        "tft.html",
        user=current_user,
        summoner=summoner,
        summoner_info=summoner_info,
        match_by_id=match_by_id,
    )
