% Part a:
    % Exercise 3.2:
        in(katarina, olga).
        in(olga, natasha).
        in(natasha, irina).
        in(X, Z):- in(X, Y), in(Y, Z).
        ?- in(katarina, natasha).   % True
        ?- in(olga, katarina).      % False

    % Exercise 4.5:
        tran(eins, one).
        tran(zwei, two).
        tran(drei, three).
        tran(vier, four).
        tran(fuenf, five).
        tran(sechs, six).
        tran(sieben, seven).
        tran(acht, eight).
        tran(neun, nine).
        listtran([], []).       % Make sure it works for empty case
        % Evlauate head and then compute the rest of the list recursively
        listtran([HG|TG], [HE|TE]):- tran(HG, HE), listtran(TG, TE).
        ?- listtran([eins, neun, zwei], X).
        ?- listtran(X, [one, seven, six, two]).

% Part b:
    % Prolog is capable of performing modus ponens, although it does not
    % have a specific function to do so. Modus ponens can be implemented
    % in the following manner:
    fail(student):- duetomorrow(project).
    duetomorrow(project).
    ?- fail(student).   % True
