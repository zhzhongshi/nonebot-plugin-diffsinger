import librosa


def process_notes(preps, phone_dict):
    notes = []
    for prep in preps:
        if prep[2] in phone_dict:
            notes.append({"key": prep[0], "duration": prep[1],
                         "slur": False, "phonemes": phone_dict[prep[2]]})
        else:
            if prep[2] in ["AP", "SP"]:
                notes.append(
                    {
                        "key": prep[0],
                        "duration": prep[1],
                        "slur": False,
                        "phonemes": [prep[2]]
                    }
                )
            elif prep[2] == "+":
                notes.append(
                    {"key": prep[0], "duration": prep[1], "slur": True})
            else:
                notes.append(
                    {
                        "key": prep[0],
                        "duration": prep[1],
                        "slur": False,
                        "phonemes": [prep[2]]
                    }
                )
    req = {"notes": notes}
    return req


def bpm2dur(bpm=120, input=[]):
    preps = []
    for note in input:
        dur_bar = 60*4/bpm
        dur = (note[1]/16)*dur_bar
        preps.append([note[0], dur, note[2]])
    return preps


def get_f0(input_notes, f0_timestep=0.005):
    midi_note = []
    for note in input_notes['notes']:
        midi_note.append(note['key'])
    note_dur = []
    for noted in input_notes['notes']:
        note_dur.append(noted['duration'])
    f0 = []
    for i in range(len(note_dur)):
        notes = []
        for _ in range(int(note_dur[i]/f0_timestep)):
            if midi_note[i] == 0:
                f0.append(296.0)
            else:
                notes.append(midi_note[i])
        f0.extend(librosa.midi_to_hz(notes).tolist())
    return f0
