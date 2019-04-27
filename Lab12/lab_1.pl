% Part a:
    % Exercise 1.4:
        killer(butch).
        married(mia, marsellus).
        dead(zed).
        kill(marsellus, X):- footmassage(X, mia). % kill shows that marsellus will kill X,
                                                  % footmassage shows x gives massage to mia
        loves(mia, X):- good_dancer(X). % mia loves x if x is good dancer
        eats(jules, X):- nutritious(X); tasty(X). % jules eats x if x is nutritious or tasty
    % Exercise 1.5:
        % 1: wizard(ron)        Responds: yes, as provided in declarations
        % 2: witch(ron)         Responds: no, as witch not defined in declarations
        % 3: wizard(hermione)   Responds: no, as hermione does not exist
        % 4: witch(hermione)    Responds: no, as hermione does not exist
        % 5: wizard(harry)      Responds: yes, as harry is quiddichPlayer and hasWand, which together imply wizard
        % 6: wizard(Y)          Responds: ron, harry, as those are known to be wizards
        % 7: witch(Y)           Responds: NULL, as witch is not defined
% Part b:
    % Prolog does use modus ponens, as in the example below:
    listens2Music(mia).
    playsAirGuitar(mia):- listens2Music(mia).
    ?- playsAirGuitar(mia).
% Part c:
    % Horn clauses are representationally powerful because they can represent using variables, whereas
    % propositional logic does not support variable use
% Part d:
    % Prolog uses "?-" to distinguish an ASK statement. All statements that do not begin with that
    % syntax are TELL statements.