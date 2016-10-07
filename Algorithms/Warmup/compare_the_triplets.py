# -*- coding : utf-8 -*-

# Challenge : https://www.hackerrank.com/challenges/compare-the-triplets

alice_scores = [float(score) for score in input().strip().split(' ')]
bob_scores   = [float(score) for score in input().strip().split(' ')]

total_alice = 0
total_bob   = 0

# for index,value in enumerate(alice_scores):
    
#     if value > bob_scores[index]:
#         total_alice += 1
#     if value < bob_scores[index]:
#         total_bob += 1        

for alice , bob in zip(alice_scores,bob_scores):
	if alice > bob:
		total_alice += 1
	if bob > alice:
		total_bob += 1
		
print(total_alice,total_bob)