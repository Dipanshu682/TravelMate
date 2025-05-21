from trips.forms import TripPreferenceForm, CommentForm


def test_trip_preference_form_valid_data():
    form = TripPreferenceForm(data={"destination": "Paris", "date": "2024-12-25"})
    assert form.is_valid()


def test_trip_preference_form_no_data():
    form = TripPreferenceForm(data={})
    assert not form.is_valid()


def test_comment_form_valid_data():
    form = CommentForm(data={"text": "Great trip!"})
    assert form.is_valid()


def test_comment_form_no_data():
    form = CommentForm(data={})
    assert not form.is_valid()
