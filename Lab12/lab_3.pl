% Witch Sketch Program
witch(X):- burn(X).
burn(X):- wood(X).
wood(X):- floats(X).
floats(X):- weigh_duck(X).
weigh_duck(woman).
?- witch(woman).
