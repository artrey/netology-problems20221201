def note_factory():
    def inner():
        return baker.make('Note', make_m2m=True)

    return inner


def test_api(note_factory):
    #
    note = note_factory(m2m)

    #
    response = api_client.get(f'/notes/?is_private=true')
    data = response.json()

    #
    assert data['id'] == note.id
    assert data['text'] == note.text
