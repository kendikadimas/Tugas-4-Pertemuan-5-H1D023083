% DATABASE
:- dynamic feature_pos/1.
:- dynamic feature_neg/1.

genre("Action").
genre("Adventure").
genre("Strategy").
genre("RPG").
genre("Simulation").

feature(fast_paced, "Action").
feature(competitive, "Action").
feature(exploration, "Adventure").
feature(puzzle_solving, "Adventure").
feature(planning, "Strategy").
feature(resource_management, "Strategy").
feature(character_progression, "RPG").
feature(story_driven, "RPG").
feature(realistic, "Simulation").
feature(detail_oriented, "Simulation").

question(fast_paced, "Apakah Anda suka game dengan tempo cepat?").
question(competitive, "Apakah Anda suka bermain game yang kompetitif?").
question(exploration, "Apakah Anda suka game dengan elemen eksplorasi?").
question(puzzle_solving, "Apakah Anda suka game yang melibatkan pemecahan teka-teki?").
question(planning, "Apakah Anda suka membuat rencana atau strategi dalam game?").
question(resource_management, "Apakah Anda suka mengelola sumber daya dalam game?").
question(character_progression, "Apakah Anda suka pengembangan karakter dalam game?").
question(story_driven, "Apakah Anda suka game dengan cerita yang mendalam?").
question(realistic, "Apakah Anda suka game dengan elemen realistis?").
question(detail_oriented, "Apakah Anda suka memperhatikan detail kecil dalam game?").
