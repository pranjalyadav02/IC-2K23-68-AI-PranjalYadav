crop_requirement(tomato, 40, 65).
crop_requirement(rice, 60, 85).
crop_requirement(wheat, 35, 60).

classify_soil(M, dry) :-
    M < 30, !.
classify_soil(M, moderate) :-
    M >= 30,
    M < 60, !.
classify_soil(_, wet).

classify_temp(T, high) :-
    T >= 35, !.
classify_temp(T, moderate) :-
    T >= 25,
    T < 35, !.
classify_temp(_, low).

classify_humid(H, low) :-
    H < 40, !.
classify_humid(H, normal) :-
    H =< 70, !.
classify_humid(_, high).

evaluate(Crop, M, _, _, _, no_irrigation_required, none,
         'Soil moisture is already sufficient or wet; excessive irrigation prevented.') :-
    crop_requirement(Crop, _, MaxSafe),
    M >= MaxSafe, !.

evaluate(Crop, M, _, _, _, no_irrigation_required, none,
         'Soil moisture already meets the required threshold for this crop.') :-
    crop_requirement(Crop, MinM, _),
    M >= MinM, !.

evaluate(_, M, _, _, yes, irrigation_required_reduced, low,
         'Soil is critically dry (<15%), applying reduced irrigation despite expected rain.') :-
    M < 15, !.

evaluate(_, _, _, _, yes, no_irrigation_postponed, none,
         'Irrigation postponed to conserve water because rainfall is expected.') :- !.

evaluate(_, M, T, H, no, irrigation_required, high,
         'Soil moisture is low, the temperature is high, and rainfall is not expected.') :-
    M < 30,
    T >= 35,
    H < 40, !.

evaluate(Crop, M, _, _, no, irrigation_required, high,
         'Large soil moisture deficit for the crop with no rainfall expected.') :-
    crop_requirement(Crop, MinM, _),
    Deficit is MinM - M,
    Deficit >= 25, !.

evaluate(Crop, M, _, _, no, irrigation_required, medium,
         'Moderate moisture deficit or warm/dry air with no rainfall expected.') :-
    crop_requirement(Crop, MinM, _),
    Deficit is MinM - M,
    Deficit >= 10, !.

evaluate(_, _, T, _, no, irrigation_required, medium,
         'Moisture below crop threshold combined with high temperature.') :-
    T >= 35, !.

evaluate(_, _, _, H, no, irrigation_required, medium,
         'Moisture below crop threshold combined with low humidity.') :-
    H < 40, !.

evaluate(_, _, _, _, no, irrigation_required, low,
         'Slight soil moisture deficit under mild weather conditions.') :- !.

display_result(Crop, SoilC, TempC, HumidC, Rain, Dec, Lvl, Reason) :-
    nl,
    format('SMART IRRIGATION SYSTEM~n~n', []),
    format('Crop: ~w~n', [Crop]),
    format('Soil Condition: ~w~n', [SoilC]),
    format('Temperature: ~w~n', [TempC]),
    format('Humidity: ~w~n', [HumidC]),
    format('Rainfall Expected: ~w~n~n', [Rain]),
    format('Recommendation: ~w~n', [Dec]),
    format('Suggested Level: ~w~n~n', [Lvl]),
    format('Reason: ~w~n', [Reason]).

read_integer(Prompt, Value) :-
    write(Prompt),
    read_line_to_string(user_input, Line),
    number_string(Value, Line).

read_atom(Prompt, Value) :-
    write(Prompt),
    read_line_to_string(user_input, Line),
    atom_string(Value, Line).

run :-
    writeln('--- SMART IRRIGATION INPUT ---'),
    read_atom('Enter Crop (tomato / rice / wheat): ', Crop),
    crop_requirement(Crop, _, _),
    read_integer('Enter Soil Moisture (%): ', M),
    read_integer('Enter Temperature (C): ', T),
    read_integer('Enter Humidity (%): ', H),
    read_atom('Rainfall Expected? (yes / no): ', Rain),
    classify_soil(M, SoilC),
    classify_temp(T, TempC),
    classify_humid(H, HumidC),
    evaluate(Crop, M, T, H, Rain, Dec, Lvl, Reason),
    display_result(Crop, SoilC, TempC, HumidC, Rain, Dec, Lvl, Reason), !.

run :-
    nl,
    writeln('Error: Invalid crop name. Please enter tomato, rice, or wheat.').
