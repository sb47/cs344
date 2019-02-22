'''
This module implements the flipping of two coins and determines the probability
of specific results.

@author: Sean Brouwer
@version February 22, 2018

4.1:
  b: P(Cavity|Catch) = P(Cavity^Catch)/P(Catch)
                     = (0.108+0.072)/(0.108+0.072+0.016+0.144)
                     = 0.529
     Program result: False: 0.471, True: 0.529
  c: This program shows the expected result, that regardless of
     the previous throw, each toss will have a 50-50 chance of heads
'''

# Probability of getting heads for each individual toss is 1/2
p_heads1 = 0.5
p_heads2 = 0.5

# Use conditional probability to compute the result
p_heads2_given_heads1 = (p_heads1*p_heads2)/p_heads1
print("P(Coin2=heads | Coin1=heads) = " + str(p_heads2_given_heads1))
