"""Forms for playlist app."""

from wtforms import SelectField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Optional, Length


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField("Playlist Name", validators=[InputRequired(), Length(min=1, max=20)],)
    description = StringField("Description", validators=[Optional(),Length(min=1, max=50)],)

    # Add the necessary code to use this form


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField("Title Name", validators=[InputRequired()],)
    artist = StringField("Artist Name", validators=[Optional()],)

    # Add the necessary code to use this form


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add')
