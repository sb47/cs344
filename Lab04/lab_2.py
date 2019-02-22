'''
This module implements part 2 of lab 4

@author: Sean Brouwer
@version February 22, 2018

4.2:
  a:   i: The number of entries has doubled to now be 16
      ii: The probabilities add up to 1 as they should.
          That is one of Komogorov's Axioms
     iii: Other values could be used (light rain, mist,
          etc.) but they would make the distribution much
          more complex.
      iv: Yes, as each of the original probabilities was
          split in half, indicating the chance of rain
          is always 50%, regardless of other values.
  b: P(toothache|rain) = P(toothache^rain)/P(rain)
                       = (0.054+0.006+0.008+0.032)/(0.054+
                                0.006+0.036+0.004+0.008+
                                0.032+0.072+0.288)
                       = 0.2
     Computed result:  False: 0.8, True: 0.2
'''

from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch', 'Rain'])
T, F = True, False
P[T, T, T, T] = 0.054; P[T, T, F, T] = 0.006
P[T, T, T, F] = 0.054; P[T, T, F, F] = 0.006
P[F, T, T, T] = 0.036; P[F, T, F, T] = 0.004
P[F, T, T, F] = 0.036; P[F, T, F, F] = 0.004
P[T, F, T, T] = 0.008; P[T, F, F, T] = 0.032
P[T, F, T, F] = 0.008; P[T, F, F, F] = 0.032
P[F, F, T, T] = 0.072; P[F, F, F, T] = 0.288
P[F, F, T, F] = 0.072; P[F, F, F, F] = 0.288

# Compute P(Toothache|Rain=T)  (see the text, page 493).
PC = enumerate_joint_ask('Toothache', {'Rain': T}, P)
print(PC.show_approx())