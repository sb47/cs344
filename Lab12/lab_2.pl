% Part a:
    % Exercise 2.1:
        % 1: bread = bread will unify, as they are the same constant
        % 2: 'Bread' will not unify with bread as prolog is case sensitive
        % 8: if X were to be 'bread', then this expression would unify
        % 9: if X were 'sausage' and Y were 'bread', this expression would unify
        % 14: the variables would require two values each to unify, which is not possible
    % Exercise 2.2:
        % 1: This query fails as 'house_elf' is a classification, not a constant.
        % 2: This query fails as 'harry' is not defined
        % 3: This query fails for the same reason as #1
        % 4: This query succeeds via modus ponens
        % 5: This query also succeeds via modus ponens
% Part b:
    % Inference in propositional logic uses unification because unification is the method by which
    % the true/falseness of a statement is evaluated. Wherever an equal or inequal sign appears,
    % unification is being used.
% Part c:
    % Prolog inferencing does use resolution because resolution is a viable method to determine
    % the validity of a statement.